import json
from pathlib import Path
from fastapi import HTTPException
from pydantic import BaseModel

USERS_FILE = Path(__file__).parent / "users.json"

class LoginRequest(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    success: bool
    token: str = ""
    user_id: str = ""
    username: str = ""
    full_name: str = ""
    role: str = ""
    avatar: str = ""
    theme_color: str = ""
    message: str = ""

def load_users() -> list:
    try:
        with open(USERS_FILE, "r") as f:
            data = json.load(f)
            return data.get("users", [])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Cannot load users: {e}")

def verify_login(username: str, password: str) -> dict | None:
    """
    Check if username + password match any user in users.json.
    Returns user dict if valid, None if invalid.
    Username check is case-insensitive.
    """
    users = load_users()
    for user in users:
        if (user["username"].lower() == username.lower().strip()
                and user["password"] == password):
            return user
    return None

def make_token(user_id: str, username: str) -> str:
    """
    Create a simple session token.
    Format: bizforge_{user_id}_{username}_{timestamp_hash}
    This is NOT cryptographically secure — it's for demo purposes only.
    For production use: implement JWT with python-jose.
    """
    import time, hashlib
    ts = str(int(time.time()))
    raw = f"{user_id}:{username}:{ts}:bizforge_secret_2025"
    token_hash = hashlib.sha256(raw.encode()).hexdigest()[:16]
    return f"bizforge_{user_id}_{token_hash}"

def validate_token(token: str) -> dict | None:
    """
    Validate a session token by checking its prefix and user_id.
    Returns user dict if valid, None if invalid.
    """
    if not token or not token.startswith("bizforge_"):
        return None
    try:
        parts = token.split("_")
        # format: bizforge_user_001_<hash>
        user_id = parts[1] + "_" + parts[2]  # reconstruct user_001
        users = load_users()
        for user in users:
            if user["id"] == user_id:
                return user
        return None
    except Exception:
        return None
