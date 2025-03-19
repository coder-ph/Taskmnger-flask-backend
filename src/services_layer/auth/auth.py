import jwt
from datetime import datetime, timedelta
from config.config import Config

class AuthService:
    @staticmethod
    def generate_token(user_id, role):
        payload = {
            "user_id": user_id,
            "role": role,
            "exp": datetime.utcnow() + timedelta(hours=1)
        }
        return jwt.encode(payload, Config.SECRET_KEY, algorithm=["HS256"])
    
    @staticmethod
    def verify_token(token):
        try:
            payload = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
            return payload["user_id"]
        except jwt.ExpiredSignatureError:
            raise ValueError ("Token has expired")
        except jwt.InvalidTokenError:
            raise ValueError ("Invalid Token")
        except Exception as e:
            raise e