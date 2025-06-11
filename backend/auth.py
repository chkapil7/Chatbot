from fastapi import APIRouter, Depends, Request
from fastapi.responses import RedirectResponse
from starlette.config import Config
from authlib.integrations.starlette_client import OAuth
from database import users_collection
from bson import ObjectId

router = APIRouter(prefix="/auth", tags=["Auth"])

config = Config(".env")  # or directly use environment variables
oauth = OAuth(config)

# Google OAuth configuration
oauth.register(
    name='google',
    client_id="67124208014-9dvbd7d1i2bej8bote3kd93q3u3epp94.apps.googleusercontent.com",
    client_secret="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",
    access_token_url='https://oauth2.googleapis.com/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    client_kwargs={'scope': 'openid email profile'},
    redirect_uri="http://localhost:8000/api/auth/callback"
)

@router.get("/login")
async def login_with_google(request: Request):
    redirect_uri = oauth.google.redirect_uri
    return await oauth.google.authorize_redirect(request, redirect_uri)

@router.get("/callback")
async def auth_callback(request: Request):
    token = await oauth.google.authorize_access_token(request)
    user_info = await oauth.google.parse_id_token(request, token)
    
    # Save user to DB if not exists
    existing_user = await users_collection.find_one({"email": user_info['email']})
    if not existing_user:
        await users_collection.insert_one({
            "email": user_info['email'],
            "name": user_info['name'],
            "picture": user_info['picture']
        })
    
    return {"message": "Login successful", "user": user_info}
