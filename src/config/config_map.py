import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("secret_key ")
    JWT_COOKIE_SECURE = True
    JWT_COOKIE_HTTPONLY = True