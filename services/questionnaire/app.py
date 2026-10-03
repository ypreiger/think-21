"""Questionnaire UI and API. Wix opens this site in a new tab. No Wix API."""

import json
import os
import re
import secrets
from datetime import datetime, timezone
from pathlib import Path

import httpx
from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from format_text import format_transcript

ROOT = Path(__file__).resolve().parent
DATA = Path(os.environ.get("DATA_DIR", "/data"))
SPEECH_URL = os.environ.get("SPEECH_URL", "http://speech:8080").rstrip("/")
ID_RE = re.compile(r"^P[0-9]{6,12}$")
LANGS = {"en", "ru", "he"}

app = FastAPI(title="think21-questionnaire")
INSTRUMENT = json.loads((ROOT / "instrument.json").read_text(encoding="utf-8"))
QUESTIONS = {
    question["id"]: question
    for section in INSTRUMENT["sections"]
    for question in section["questions"]
}


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def session_path(participant_id: str) -> Path:
    return DATA / "sessions" / f"{participant_id}.json"


def submission_path(participant_id: str, day: str) -> Path:
    return DATA / "submissions" / f"GM965_{participant_id}_{day}.json"


def load_session(participant_id: str) -> dict:
    path = session_path(participant_id)
    if not path.is_file():
        raise HTTPException(status_code=404, detail="session not found")
    return json.loads(path.read_text(encoding="utf-8"))


def save_session(session: dict) -> None:
    path = session_path(session["id"])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(session, ensure_ascii=False, indent=2), encoding="utf-8")


def new_id() -> str:
    for _ in range(20):
        participant_id = f"P{secrets.randbelow(90000000) + 10000000}"
        if not session_path(participant_id).exists():
            return participant_id
    raise HTTPException(status_code=500, detail="could not allocate an id")


def blank_session(participant_id: str, lang: str, interviewer: bool) -> dict:
    return {
        "id": participant_id,
        "lang": lang,
        "interviewer": interviewer,
        "status": "draft",
        "step": 0,
        "created": now(),
        "updated": now(),
        "answers": {},
    }


def question_visible(session: dict, question: dict) -> bool:
    if question.get("interviewer") and not session.get("interviewer"):
        return False
    condition = question.get("showIf")
    if not condition:
        return True
    answer = session.get("answers", {}).get(condition["question"]) or {}
    if answer.get("skipped"):
        return False
    return condition["includes"] in (answer.get("choice") or [])


def visible_questions(session: dict) -> list[dict]:
    questions = []
    for section in INSTRUMENT["sections"]:
        if section.get("interviewer") and not session.get("interviewer"):
            continue
        for question in section["questions"]:
            if question_visible(session, question):
                questions.append(question)
    return questions


def answer_ok(question: dict, answer: dict | None) -> bool:
    if not answer or answer.get("skipped"):
        return True
    kind = question["type"]
    if kind == "text":
        return bool((answer.get("text") or "").strip())
    if kind == "single":
        choice = answer.get("choice") or []
        if len(choice) != 1:
            return False
        return other_ok(question, choice[0], answer)
    if kind == "multi":
        choice = answer.get("choice") or []
        if not choice:
            return False
        return all(other_ok(question, item, answer) for item in choice)
    return False


def other_ok(question: dict, option_id: str, answer: dict) -> bool:
    option = next((item for item in question.get("options", []) if item["id"] == option_id), None)
    if option is None:
        return False
    if option.get("other"):
        return bool((answer.get("other") or "").strip())
    return True


@app.on_event("startup")
def startup() -> None:
    (DATA / "sessions").mkdir(parents=True, exist_ok=True)
    (DATA / "submissions").mkdir(parents=True, exist_ok=True)


@app.get("/health")
def health() -> dict:
    return {"ok": True}


@app.get("/api/instrument")
def instrument() -> dict:
    return INSTRUMENT


@app.post("/api/sessions")
def create_session(body: dict) -> dict:
    lang = body.get("lang") or "en"
    if lang not in LANGS:
        raise HTTPException(status_code=400, detail="lang must be en, ru, or he")
    requested = (body.get("id") or "").strip()
    interviewer = bool(body.get("interviewer"))
    if requested:
        if not ID_RE.match(requested):
            raise HTTPException(status_code=400, detail="id must look like P00000000")
        path = session_path(requested)
        if path.is_file():
            session = json.loads(path.read_text(encoding="utf-8"))
            if session.get("status") == "draft" and session.get("lang") != lang:
                session["lang"] = lang
                session["updated"] = now()
                save_session(session)
            return session
        participant_id = requested
    else:
        participant_id = new_id()
    session = blank_session(participant_id, lang, interviewer)
    save_session(session)
    return session


@app.get("/api/sessions/{participant_id}")
def get_session(participant_id: str) -> dict:
    if not ID_RE.match(participant_id):
        raise HTTPException(status_code=400, detail="bad id")
    return load_session(participant_id)


@app.put("/api/sessions/{participant_id}")
def update_session(participant_id: str, body: dict) -> dict:
    session = load_session(participant_id)
    if session["status"] != "draft":
        raise HTTPException(status_code=409, detail="session is locked")
    lang = body.get("lang", session["lang"])
    if lang not in LANGS:
        raise HTTPException(status_code=400, detail="lang must be en, ru, or he")
    answers = body.get("answers", session["answers"])
    if not isinstance(answers, dict):
        raise HTTPException(status_code=400, detail="answers must be an object")
    known = set(QUESTIONS)
    clean = {}
    for key, value in answers.items():
        if key not in known or not isinstance(value, dict):
            continue
        clean[key] = {
            "text": str(value.get("text") or "")[:8000],
            "choice": [str(item) for item in (value.get("choice") or [])][:12],
            "other": str(value.get("other") or "")[:2000],
            "skipped": bool(value.get("skipped")),
        }
    session["lang"] = lang
    session["answers"] = clean
    if "step" in body:
        try:
            session["step"] = max(0, int(body.get("step") or 0))
        except (TypeError, ValueError):
            pass
    session["updated"] = now()
    save_session(session)
    return session


@app.post("/api/sessions/{participant_id}/transcribe")
async def transcribe(
    participant_id: str,
    file: UploadFile = File(...),
    language: str = Form("en"),
) -> dict:
    session = load_session(participant_id)
    if session["status"] != "draft":
        raise HTTPException(status_code=409, detail="session is locked")
    if language not in LANGS:
        language = session["lang"]
    data = await file.read()
    if not data:
        raise HTTPException(status_code=400, detail="empty audio")
    try:
        async with httpx.AsyncClient(timeout=180) as client:
            response = await client.post(
                f"{SPEECH_URL}/v1/transcribe",
                files={"file": (file.filename or "answer.wav", data, file.content_type or "audio/wav")},
                data={"language": language},
            )
    except httpx.HTTPError as exc:
        raise HTTPException(status_code=502, detail="speech service unavailable") from exc
    if response.status_code == 503:
        raise HTTPException(status_code=503, detail="speech model is still loading")
    if response.status_code >= 400:
        raise HTTPException(status_code=502, detail="speech service rejected the audio")
    payload = response.json()
    return {
        "text": payload.get("text", ""),
        "language": language,
        "segments": payload.get("segments") or [],
    }


@app.post("/api/format")
async def format_answer(body: dict) -> dict:
    language = body.get("language") or "en"
    if language not in LANGS:
        language = "en"
    text = str(body.get("text") or "")[:8000]
    segments = body.get("segments") if isinstance(body.get("segments"), list) else None
    return {"text": format_transcript(text, language, segments)}


@app.post("/api/sessions/{participant_id}/submit")
def submit(participant_id: str) -> dict:
    session = load_session(participant_id)
    if session["status"] == "submitted":
        return {"id": session["id"], "file": session.get("file"), "status": "submitted"}
    visible = visible_questions(session)
    missing = [
        question["id"]
        for question in visible
        if not answer_ok(question, session["answers"].get(question["id"]))
    ]
    if missing:
        raise HTTPException(status_code=400, detail={"missing": missing})
    day = datetime.now(timezone.utc).strftime("%Y%m%d")
    visible_ids = {question["id"] for question in visible}
    record = {
        "participantId": session["id"],
        "instrument": INSTRUMENT["id"],
        "language": session["lang"],
        "submitted": now(),
        "answers": {
            key: value
            for key, value in session["answers"].items()
            if key in visible_ids
        },
    }
    path = submission_path(session["id"], day)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
    session["status"] = "submitted"
    session["updated"] = record["submitted"]
    session["file"] = path.name
    save_session(session)
    return {"id": session["id"], "file": path.name, "status": "submitted"}


@app.get("/api/sessions/{participant_id}/file")
def download(participant_id: str):
    session = load_session(participant_id)
    name = session.get("file")
    if not name:
        raise HTTPException(status_code=404, detail="no file")
    path = DATA / "submissions" / name
    if not path.is_file():
        raise HTTPException(status_code=404, detail="file missing")
    return FileResponse(path, filename=name, media_type="application/json")


app.mount("/", StaticFiles(directory=ROOT / "static", html=True), name="static")
