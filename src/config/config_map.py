import os
from dotenv import load_dotenv

load_dotenv()
class Config:
    SQLALCHEMY_DATABASE_URI=os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY")
    JWT_COOKIE_SECURE = True
    JWT_COOKIE_HTTPONLY = True
    
    print("Loaded DATABASE URI:", SQLALCHEMY_DATABASE_URI) 