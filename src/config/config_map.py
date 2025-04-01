import os
from dotenv import load_dotenv

load_dotenv()
class Config:
    SQLALCHEMY_DATABASE_URI=os.getenv("DATABASE_URL", "sqlite:///test.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY")
    JWT_COOKIE_SECURE = True
    JWT_COOKIE_HTTPONLY = True
    REDIS_URL= os.getenv("REDIS_URL","redis://redis:6379/0" )
    
    print("Loaded DATABASE URI:", SQLALCHEMY_DATABASE_URI) 