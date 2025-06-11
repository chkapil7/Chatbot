from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI

client = AsyncIOMotorClient(MONGO_URI)
db = client.chatbot
users_collection = db.users
chats_collection = db.chats
