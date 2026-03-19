from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

from auth import LoginRequest, LoginResponse, verify_login, make_token, validate_token

app = FastAPI(title="BizForge API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

@app.get("/")
async def root():
    return {"message": "BizForge backend is running"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.post("/api/login", response_model=LoginResponse)
async def login(request: LoginRequest):
    user = verify_login(request.username, request.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

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
    return {"success": True}

@app.get("/api/verify-session")
async def verify_session(token: str = ""):
    if not token:
        raise HTTPException(status_code=401, detail="No token")

    user = validate_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid session")

    return {"success": True}

@app.post("/api/generate-brand")
async def generate_brand_placeholder():
    raise HTTPException(status_code=503, detail="AI disabled")

@app.post("/api/generate-content")
async def generate_content_placeholder():
    raise HTTPException(status_code=503, detail="AI disabled")

@app.post("/api/analyze-sentiment")
async def analyze_sentiment_placeholder():
    raise HTTPException(status_code=503, detail="AI disabled")

@app.post("/api/get-colors")
async def get_colors_placeholder():
    raise HTTPException(status_code=503, detail="AI disabled")

@app.post("/api/chat")
async def chat_placeholder():
    raise HTTPException(status_code=503, detail="AI disabled")

@app.post("/api/generate-logo")
async def generate_logo_placeholder():
    raise HTTPException(status_code=503, detail="AI disabled")

@app.post("/api/transcribe-voice")
async def transcribe_voice_placeholder():
    raise HTTPException(status_code=503, detail="AI disabled")

@app.post("/api/summarize")
async def summarize_placeholder():
    raise HTTPException(status_code=503, detail="AI disabled")

@app.post("/api/competitor-analysis")
async def competitor_placeholder():
    raise HTTPException(status_code=503, detail="AI disabled")

@app.post("/api/brand-voice")
async def brand_voice_placeholder():
    raise HTTPException(status_code=503, detail="AI disabled")

if __name__ == "__main__":
    import os
    import uvicorn

    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)