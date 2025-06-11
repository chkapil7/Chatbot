from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests
import os
import requests as external_requests

# Load environment variables
load_dotenv()

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
MONGO_URI = os.getenv("MONGO_URI")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# App initialization
app = FastAPI()

# CORS setup for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB setup
client = AsyncIOMotorClient(MONGO_URI)
db = client.chatbot_db
users_collection = db.users

# Auth dependency
auth_scheme = HTTPBearer()

def verify_jwt(token: str):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# ========== ROUTES ==========

@app.get("/")
def home():
    return {"status": "Backend running"}

@app.post("/auth/callback")
async def google_callback(request: Request):
    data = await request.json()
    id_token_str = data.get("credential")

    if not id_token_str:
        raise HTTPException(status_code=400, detail="Missing ID token")

    try:
        idinfo = id_token.verify_oauth2_token(
            id_token_str,
            google_requests.Request(),
            GOOGLE_CLIENT_ID
        )
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid ID token")

    user = {
        "email": idinfo["email"],
        "name": idinfo.get("name"),
        "picture": idinfo.get("picture"),
    }

    # Save or update user in database
    await users_collection.update_one(
        {"email": user["email"]},
        {"$set": user},
        upsert=True
    )

    # Generate custom JWT
    token = jwt.encode(user, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return {"token": token}

@app.post("/chat")
async def chat(request: Request, credentials: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    token = credentials.credentials
    user = verify_jwt(token)

    data = await request.json()
    prompt = data.get("prompt")

    if not prompt:
        raise HTTPException(status_code=400, detail="Prompt is required")

    # Gemini (PaLM) API call
    gemini_url = "https://generativelanguage.googleapis.com/v1beta2/models/chat-bison-001:generateMessage"
    headers = {"Content-Type": "application/json"}
    payload = {
        "prompt": {"text": prompt},
        "temperature": 0.7,
    }

    response = external_requests.post(
        f"{gemini_url}?key={GEMINI_API_KEY}",
        json=payload,
        headers=headers
    )

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Gemini API error")

    gemini_reply = response.json()["candidates"][0]["content"]["parts"][0]["text"]

    return {"response": gemini_reply}
