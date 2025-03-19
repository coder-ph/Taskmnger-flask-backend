from startup.loggings import logger
from repositories.user_repository import UserRepository
from services_layer.utilities.hash import Hash
from services_layer.auth.auth import AuthService
from  error.apiErrors import InvalidAccessError

class UserService:
    @staticmethod
    def register_user(data):
        try:
            if not data.get("email") or not data.get("password"):
                raise ValueError ("Email and password is required")
            data['password'] = Hash.hash_password(data["password"])
            user = UserRepository.create_user(data)
            logger.info(f"user registered: {user.enail}")
            return user
        except Exception as e:
            logger.error(f"Failed to register user: {e}")
            raise e
        
    @staticmethod
    def login_user(data):
        try:
            if not data.get("email") or not data.get("password"):
                raise ValueError ("Email and password are required")
            user = UserRepository.get_user_by_email(data['email'])
            if not user:
                raise InvalidAccessError("email not found")
            if not Hash.verify_password(user.password, data['password']):
                raise InvalidAccessError ("Incorrect password")
            token = AuthService.generate_token(user.id)
            logger.info(f'user logged in : {user.email}')
            return token
        except Exception as e:
            logger.error(f"Login failed {e}")
            raise e
        
    @staticmethod
    def get_user_profile(user_id):
        try:
            user = UserRepository.get_user_by_id(user_id)
            if not user:
                raise ValueError ("user not found")
            return user
        except Exception as e:
            logger.error(f"failed to fetch user profile: {e}")
            raise e