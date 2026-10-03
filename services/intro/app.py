"""Study intro. Sign-in stays here. The questionnaire opens in a new tab with only an ID."""

import hashlib
import hmac
import json
import os
import secrets
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode

import httpx
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

ROOT = Path(__file__).resolve().parent
DATA = Path(os.environ.get("DATA_DIR", "/data"))
PUBLIC_URL = os.environ.get(
    "PUBLIC_URL",
    "https://intro-think-21.apps.ocp.7hrxw.sandbox880.opentlc.com",
).rstrip("/")
QUESTIONNAIRE_URL = os.environ.get(
    "QUESTIONNAIRE_URL",
    "https://questionnaire-think-21.apps.ocp.7hrxw.sandbox880.opentlc.com",
).rstrip("/")
SESSION_SECRET = os.environ.get("SESSION_SECRET", "dev-only-change-me")
CONSENT_VERSION = "gm965-intro-1"
LANGS = {"en", "ru", "he"}

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", "")
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", "")
LINKEDIN_CLIENT_ID = os.environ.get("LINKEDIN_CLIENT_ID", "")
LINKEDIN_CLIENT_SECRET = os.environ.get("LINKEDIN_CLIENT_SECRET", "")

app = FastAPI(title="think21-intro")


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sign(value: str) -> str:
    digest = hmac.new(SESSION_SECRET.encode(), value.encode(), hashlib.sha256).hexdigest()
    return f"{value}.{digest}"


def unsign(value: str) -> str | None:
    if not value or "." not in value:
        return None
    raw, digest = value.rsplit(".", 1)
    expected = hmac.new(SESSION_SECRET.encode(), raw.encode(), hashlib.sha256).hexdigest()
    if not hmac.compare_digest(digest, expected):
        return None
    return raw


def account_key(provider: str, subject: str) -> str:
    digest = hashlib.sha256(f"{provider}:{subject}".encode()).hexdigest()[:24]
    return f"{provider}-{digest}"


def account_path(key: str) -> Path:
    return DATA / "accounts" / f"{key}.json"


def load_account(key: str) -> dict | None:
    path = account_path(key)
    if not path.is_file():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def save_account(account: dict) -> None:
    path = account_path(account["key"])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(account, ensure_ascii=False, indent=2), encoding="utf-8")


def new_participant_id() -> str:
    folder = DATA / "accounts"
    for _ in range(20):
        participant_id = f"P{secrets.randbelow(90000000) + 10000000}"
        used = False
        if folder.exists():
            for path in folder.glob("*.json"):
                if json.loads(path.read_text(encoding="utf-8")).get("participantId") == participant_id:
                    used = True
                    break
        if not used:
            return participant_id
    raise HTTPException(status_code=500, detail="could not allocate an id")


def current_account(request: Request) -> dict | None:
    key = unsign(request.cookies.get("t21", ""))
    if not key:
        return None
    return load_account(key)


def public_account(account: dict) -> dict:
    return {
        "provider": account["provider"],
        "name": account.get("name") or "",
        "email": account.get("email") or "",
        "participantId": account.get("participantId") or "",
        "lang": account.get("lang") or "en",
        "consentAt": account.get("consentAt") or "",
    }


def set_cookie(response: RedirectResponse, name: str, value: str, max_age: int) -> None:
    response.set_cookie(
        name,
        sign(value),
        max_age=max_age,
        httponly=True,
        secure=True,
        samesite="lax",
        path="/",
    )


@app.on_event("startup")
def startup() -> None:
    (DATA / "accounts").mkdir(parents=True, exist_ok=True)


@app.get("/health")
def health() -> dict:
    return {"ok": True}


@app.get("/api/config")
def config() -> dict:
    return {
        "google": bool(GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET),
        "linkedin": bool(LINKEDIN_CLIENT_ID and LINKEDIN_CLIENT_SECRET),
        "questionnaireUrl": QUESTIONNAIRE_URL,
        "consentVersion": CONSENT_VERSION,
    }


@app.get("/api/me")
def me(request: Request) -> dict:
    account = current_account(request)
    if not account:
        raise HTTPException(status_code=401, detail="signed out")
    return public_account(account)


@app.post("/api/consent")
async def consent(request: Request) -> dict:
    account = current_account(request)
    if not account:
        raise HTTPException(status_code=401, detail="signed out")
    body = await request.json()
    if not body.get("accepted"):
        raise HTTPException(status_code=400, detail="consent is required")
    lang = body.get("lang") or account.get("lang") or "en"
    if lang not in LANGS:
        raise HTTPException(status_code=400, detail="lang must be en, ru, or he")
    if not account.get("participantId"):
        account["participantId"] = new_participant_id()
    account["lang"] = lang
    account["consentAt"] = account.get("consentAt") or now()
    account["consentVersion"] = CONSENT_VERSION
    save_account(account)
    return public_account(account)


@app.post("/api/logout")
def logout() -> RedirectResponse:
    response = RedirectResponse("/", status_code=303)
    response.delete_cookie("t21", path="/")
    return response


def start_oauth(provider: str) -> RedirectResponse:
    state = secrets.token_urlsafe(24)
    if provider == "google":
        if not (GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET):
            return RedirectResponse("/?auth=unconfigured", status_code=303)
        url = "https://accounts.google.com/o/oauth2/v2/auth?" + urlencode({
            "client_id": GOOGLE_CLIENT_ID,
            "redirect_uri": PUBLIC_URL + "/auth/google/callback",
            "response_type": "code",
            "scope": "openid email profile",
            "state": state,
            "prompt": "select_account",
        })
    else:
        if not (LINKEDIN_CLIENT_ID and LINKEDIN_CLIENT_SECRET):
            return RedirectResponse("/?auth=unconfigured", status_code=303)
        url = "https://www.linkedin.com/oauth/v2/authorization?" + urlencode({
            "response_type": "code",
            "client_id": LINKEDIN_CLIENT_ID,
            "redirect_uri": PUBLIC_URL + "/auth/linkedin/callback",
            "state": state,
            "scope": "openid profile email",
        })
    response = RedirectResponse(url, status_code=303)
    set_cookie(response, "oauth_state", state, 600)
    return response


@app.get("/auth/google")
def google_start() -> RedirectResponse:
    return start_oauth("google")


@app.get("/auth/linkedin")
def linkedin_start() -> RedirectResponse:
    return start_oauth("linkedin")


async def finish_oauth(request: Request, provider: str) -> RedirectResponse:
    state = unsign(request.cookies.get("oauth_state", ""))
    if not state or state != request.query_params.get("state") or request.query_params.get("error"):
        return RedirectResponse("/?auth=failed", status_code=303)
    code = request.query_params.get("code", "")
    try:
        profile = await exchange(provider, code)
    except httpx.HTTPError:
        return RedirectResponse("/?auth=failed", status_code=303)
    key = account_key(provider, profile["subject"])
    account = load_account(key) or {
        "key": key,
        "provider": provider,
        "subject": profile["subject"],
        "created": now(),
        "participantId": "",
        "consentAt": "",
        "lang": "en",
    }
    account["name"] = profile.get("name") or account.get("name") or ""
    account["email"] = profile.get("email") or account.get("email") or ""
    save_account(account)
    response = RedirectResponse("/", status_code=303)
    set_cookie(response, "t21", key, 60 * 60 * 24 * 30)
    response.delete_cookie("oauth_state", path="/")
    return response


async def exchange(provider: str, code: str) -> dict:
    async with httpx.AsyncClient(timeout=30) as client:
        if provider == "google":
            token = await client.post(
                "https://oauth2.googleapis.com/token",
                data={
                    "code": code,
                    "client_id": GOOGLE_CLIENT_ID,
                    "client_secret": GOOGLE_CLIENT_SECRET,
                    "redirect_uri": PUBLIC_URL + "/auth/google/callback",
                    "grant_type": "authorization_code",
                },
            )
            token.raise_for_status()
            access = token.json()["access_token"]
            info = await client.get(
                "https://www.googleapis.com/oauth2/v3/userinfo",
                headers={"Authorization": f"Bearer {access}"},
            )
            info.raise_for_status()
            body = info.json()
            return {"subject": body["sub"], "name": body.get("name", ""), "email": body.get("email", "")}
        token = await client.post(
            "https://www.linkedin.com/oauth/v2/accessToken",
            data={
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": PUBLIC_URL + "/auth/linkedin/callback",
                "client_id": LINKEDIN_CLIENT_ID,
                "client_secret": LINKEDIN_CLIENT_SECRET,
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        token.raise_for_status()
        access = token.json()["access_token"]
        info = await client.get(
            "https://api.linkedin.com/v2/userinfo",
            headers={"Authorization": f"Bearer {access}"},
        )
        info.raise_for_status()
        body = info.json()
        return {"subject": body["sub"], "name": body.get("name", ""), "email": body.get("email", "")}


@app.get("/auth/google/callback")
async def google_callback(request: Request) -> RedirectResponse:
    return await finish_oauth(request, "google")


@app.get("/auth/linkedin/callback")
async def linkedin_callback(request: Request) -> RedirectResponse:
    return await finish_oauth(request, "linkedin")


@app.get("/auth/setup", response_class=HTMLResponse)
def setup() -> str:
    return (
        "<!DOCTYPE html><meta charset='utf-8'><title>Sign-in setup</title>"
        f"<p>LinkedIn redirect URI<br>{PUBLIC_URL}/auth/linkedin/callback</p>"
        f"<p>Google redirect URI<br>{PUBLIC_URL}/auth/google/callback</p>"
    )


app.mount("/", StaticFiles(directory=ROOT / "static", html=True), name="static")
