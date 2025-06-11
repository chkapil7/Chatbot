from fastapi import APIRouter, Depends, HTTPException, Request
from jose import jwt, JWTError
from config import JWT_SECRET, JWT_ALGORITHM
from models import ChatRequest
from database import chats_collection
import httpx

router = APIRouter()

async def get_current_user(request: Request):
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(status_code=401, detail="Missing token")
    try:
        user = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@router.post("/chat")
async def chat(req: ChatRequest, user: dict = Depends(get_current_user)):
    if req.model == "gemini":
        answer = await call_gemini(req.query)
    elif req.model == "ollama":
        answer = await call_ollama(req.query)
    else:
        raise HTTPException(status_code=400, detail="Invalid model")

    await chats_collection.insert_one({
        "email": user["email"],
        "query": req.query,
        "response": answer,
        "model": req.model
    })

    return {"answer": answer}

async def call_gemini(prompt):
    # Replace with actual Gemini API call
    return f"[Gemini] You said: {prompt}"

async def call_ollama(prompt):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://localhost:11434/api/generate",
            json={"model": "llama3", "prompt": prompt}
        )
        data = response.json()
        return data.get("response", "No response from Ollama.")
