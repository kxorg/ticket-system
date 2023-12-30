import os

SECRET_KEY = os.getenv("SECRET_KEY", default="secret_key")
ALGORITHM = os.getenv("ALGORITHM", default="HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", default=30)