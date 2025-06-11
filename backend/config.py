from starlette.config import Config

config = Config(".env")

GOOGLE_CLIENT_ID = config("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = config("GOOGLE_CLIENT_SECRET")
REDIRECT_URI = config("REDIRECT_URI")
JWT_SECRET = config("JWT_SECRET")
JWT_ALGORITHM = config("JWT_ALGORITHM", default="HS256")
MONGO_URI = config("MONGO_URI")
