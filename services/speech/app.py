"""Speech-to-text. Transcribes in the requested language and returns text only."""

import asyncio
import os
import tempfile
from pathlib import Path

from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from faster_whisper import WhisperModel

MODEL_NAME = os.environ.get("WHISPER_MODEL", "medium")
COMPUTE = os.environ.get("WHISPER_COMPUTE", "int8")
DEVICE = os.environ.get("WHISPER_DEVICE", "cpu")
BEAM = int(os.environ.get("WHISPER_BEAM", "1"))
MAX_BYTES = int(os.environ.get("MAX_AUDIO_BYTES", str(8 * 1024 * 1024)))

LANGS = {"en": "en", "ru": "ru", "he": "he"}

app = FastAPI(title="think21-speech")
model: WhisperModel | None = None
ready = False
lock = asyncio.Lock()


def load_model() -> WhisperModel:
    return WhisperModel(MODEL_NAME, device=DEVICE, compute_type=COMPUTE)


@app.on_event("startup")
async def startup() -> None:
    async def _load() -> None:
        global model, ready
        model = await asyncio.to_thread(load_model)
        ready = True

    asyncio.create_task(_load())


@app.get("/live")
def live() -> dict:
    return {"ok": True}


@app.get("/health")
def health() -> dict:
    if not ready or model is None:
        raise HTTPException(status_code=503, detail="model loading")
    return {"ok": True, "model": MODEL_NAME, "device": DEVICE, "compute": COMPUTE}


def transcribe_file(path: str, language: str) -> dict:
    assert model is not None
    segments, _info = model.transcribe(
        path,
        language=language,
        task="transcribe",
        beam_size=BEAM,
        vad_filter=False,
        condition_on_previous_text=False,
    )
    pieces = []
    for segment in segments:
        piece = segment.text.strip()
        if piece:
            pieces.append({"text": piece, "start": round(segment.start, 2), "end": round(segment.end, 2)})
    return {
        "text": " ".join(item["text"] for item in pieces).strip(),
        "segments": pieces,
    }


@app.post("/v1/transcribe")
async def transcribe(
    file: UploadFile = File(...),
    language: str = Form("en"),
) -> dict:
    if language not in LANGS:
        raise HTTPException(status_code=400, detail="language must be en, ru, or he")
    if not ready or model is None:
        raise HTTPException(status_code=503, detail="model loading")
    data = await file.read()
    if not data:
        raise HTTPException(status_code=400, detail="empty audio")
    if len(data) > MAX_BYTES:
        raise HTTPException(status_code=413, detail="audio larger than 8MB")

    suffix = Path(file.filename or "audio.wav").suffix or ".wav"
    if suffix.lower() not in {".wav", ".webm", ".mp3", ".m4a", ".ogg", ".flac"}:
        suffix = ".wav"

    fd, path = tempfile.mkstemp(suffix=suffix, dir="/tmp")
    try:
        os.write(fd, data)
        os.close(fd)
        fd = -1
        async with lock:
            result = await asyncio.to_thread(transcribe_file, path, LANGS[language])
    finally:
        if fd >= 0:
            os.close(fd)
        try:
            os.remove(path)
        except OSError:
            pass
    return {"text": result["text"], "language": language, "segments": result["segments"]}
