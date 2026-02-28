from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

from models import (
    BrandRequest, ContentRequest, SentimentRequest,
    ColorRequest, ChatRequest, LogoRequest, SummarizeRequest,
    CompetitorRequest, BrandVoiceRequest
)
from ai_services import (
    generate_brand_names, generate_marketing_content,
    analyze_sentiment, get_color_palette, chat_with_ai,
    generate_logo_image, transcribe_voice, summarize_text,
    analyze_competitors, generate_brand_voice
)
from auth import LoginRequest, LoginResponse, verify_login, make_token, validate_token

app = FastAPI(title="BizForge API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

BASE_DIR      = Path(__file__).parent.parent
frontend_path = BASE_DIR / "frontend"
static_path   = frontend_path / "static"
logos_path    = static_path / "generated_logos"

app.mount("/static", StaticFiles(directory=str(static_path)), name="static")


# ── ENDPOINTS ──────────────────────────────────────────────

@app.post("/api/login", response_model=LoginResponse)
async def login(request: LoginRequest):
    """
    Authenticate user with username and password.
    Returns session token + user info on success.
    Returns 401 with error message on failure.
    """
    user = verify_login(request.username, request.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password. Please try again."
        )
    token = make_token(user["id"], user["username"])
    return LoginResponse(
        success=True,
        token=token,
        user_id=user["id"],
        username=user["username"],
        full_name=user["full_name"],
        role=user["role"],
        avatar=user["avatar"],
        theme_color=user["theme_color"],
        message=f"Welcome back, {user['full_name']}!"
    )

@app.post("/api/logout")
async def logout():
    """
    Logout endpoint. Frontend clears localStorage.
    Returns success message.
    """
    return {"success": True, "message": "Logged out successfully"}

@app.get("/api/verify-session")
async def verify_session(token: str = ""):
    """
    Verify if a session token is still valid.
    Called by pages on load to check authentication.
    """
    if not token:
        raise HTTPException(status_code=401, detail="No token provided")
    user = validate_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid or expired session")
    return {
        "success": True,
        "user_id": user["id"],
        "username": user["username"],
        "full_name": user["full_name"],
        "role": user["role"],
        "avatar": user["avatar"],
        "theme_color": user["theme_color"]
    }

@app.post("/api/generate-brand")
async def ep_brand(request: BrandRequest):
    try:
        r = await generate_brand_names(
            request.industry, request.keywords, request.tone, request.language)
        return {"success": True, "data": r}
    except Exception as e:
        raise HTTPException(500, str(e))

@app.post("/api/generate-content")
async def ep_content(request: ContentRequest):
    try:
        r = await generate_marketing_content(
            request.brand_description, request.tone,
            request.content_type, request.language)
        return {"success": True, "data": r}
    except Exception as e:
        raise HTTPException(500, str(e))

@app.post("/api/analyze-sentiment")
async def ep_sentiment(request: SentimentRequest):
    try:
        r = await analyze_sentiment(request.text, request.brand_tone)
        return {"success": True, "data": r}
    except Exception as e:
        raise HTTPException(500, str(e))

@app.post("/api/get-colors")
async def ep_colors(request: ColorRequest):
    try:
        r = await get_color_palette(request.tone, request.industry)
        return {"success": True, "data": r}
    except Exception as e:
        raise HTTPException(500, str(e))

@app.post("/api/chat")
async def ep_chat(request: ChatRequest):
    try:
        r = await chat_with_ai(request.message)
        return {"success": True, "data": {"content": r}}
    except Exception as e:
        raise HTTPException(500, str(e))

@app.post("/api/generate-logo")
async def ep_logo(request: LogoRequest):
    try:
        r = await generate_logo_image(
            request.brand_name, request.industry, request.keywords)
        return {"success": True, "data": r}
    except Exception as e:
        raise HTTPException(500, str(e))

@app.post("/api/transcribe-voice")
async def ep_voice(audio_file: UploadFile = File(...)):
    try:
        content = await audio_file.read()
        r = await transcribe_voice(content)
        return {"success": True, "text": r}
    except Exception as e:
        raise HTTPException(400, f"Transcription failed: {str(e)}")

@app.post("/api/summarize")
async def ep_summarize(request: SummarizeRequest):
    try:
        r = await summarize_text(request.text)
        return {"success": True, "data": r}
    except Exception as e:
        raise HTTPException(500, str(e))

@app.post("/api/competitor-analysis")
async def ep_competitor(request: CompetitorRequest):
    try:
        r = await analyze_competitors(
            request.brand_name, request.industry, 
            request.target_audience, request.unique_value)
        return {"success": True, "data": r}
    except Exception as e:
        raise HTTPException(500, str(e))

@app.post("/api/brand-voice")
async def ep_brand_voice(request: BrandVoiceRequest):
    try:
        r = await generate_brand_voice(
            request.brand_name, request.industry, 
            request.values, request.audience, request.tone)
        return {"success": True, "data": r}
    except Exception as e:
        raise HTTPException(500, str(e))

# ── FRONTEND SERVING ───────────────────────────────────────

@app.get("/login")
async def login_page():
    return FileResponse(frontend_path / "login.html")

@app.get("/")
async def root():
    return FileResponse(frontend_path / "index.html")

@app.get("/health")
async def health():
    from ai_services import granite_model, groq_client
    return {
        "status": "healthy",
        "ibm_granite": "loaded" if granite_model else "groq_fallback",
        "groq": "connected" if groq_client else "missing_key",
        "sdxl": "via_huggingface"
    }

@app.get("/{page}.html")
async def serve_html(page: str):
    p = frontend_path / f"{page}.html"
    return FileResponse(p if p.exists() else frontend_path / "index.html")

@app.get("/{path:path}")
async def catch_all(path: str):
    p = frontend_path / path
    return FileResponse(p if p.exists() else frontend_path / "index.html")

@app.on_event("startup")
async def startup():
    logos_path.mkdir(parents=True, exist_ok=True)
    print("\n" + "="*55)
    print("🚀 BizForge Backend Running!")
    print("🌐 http://localhost:8000")
    print("="*55 + "\n")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
