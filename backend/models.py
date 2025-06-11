from pydantic import BaseModel

class ChatRequest(BaseModel):
    query: str
    model: str  # 'gemini' or 'ollama'

class User(BaseModel):
    email: str
    name: str
    picture: str

class ChatHistory(BaseModel):
    user_id: str
    query: str
    response: str
    model: str
