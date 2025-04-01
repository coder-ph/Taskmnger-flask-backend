import jwt
from datetime import datetime, timedelta
from src.config.config import Config
from src.services_layer.utilities.redis_client import cache_data, get_cached_data

class AuthService:
    @staticmethod
    def generate_token(user_id, role):
        payload = {
            "user_id": user_id,
            "role": role,
            "exp": datetime.utcnow() + timedelta(hours=1)
        }
        token = jwt.encode(payload, Config.SECRET_KEY, algorithm="HS256")
        cache_data(f"token_{user_id}", role)
        return token
    
    @staticmethod
    def verify_token(token):
        try:
            payload = jwt.decode(token, Config.SECRET_KEY, algorithms="HS256")
            cache_role = get_cached_data(f"token_{payload['user_id']}")
            
            if cache_role:
                return payload["user_id"], cache_role.decode('utf-8')
            return payload["user_id"], payload['role']
        except jwt.ExpiredSignatureError:
            raise ValueError ("Token has expired")
        except jwt.InvalidTokenError:
            raise ValueError ("Invalid Token")
        except Exception as e:
            raise e