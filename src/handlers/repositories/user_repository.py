from sqlalchemy.exc import SQLAlchemyError
from src.startup.loggings import logger
from src.Models.user import User
from src.database import db

class UserRepository:
    @staticmethod
    def create_user(data):
        try:
            if not data.get("email") or not data.get("password"):
                raise ValueError ("Email and password required")
            user = User(**data)
            db.session.add(user)
            db.session.commit()
            logger.info(f"User created: {user.email}")
            return user
        except SQLAlchemyError as e:
            db.session.rollback()
            logger.error(f"failed to create user: {e}")
            raise e
        
    @staticmethod
    def get_user_by_email(email):
        try:
            user  = User.query.filter_by(email=email).first()
            if not user:
                raise ValueError ("Invalid email")
            logger.info(f"user found: {email}")
            return user
        
        except SQLAlchemyError as e:
            logger.error(f"Failed to fetch user by email: {e}")
            raise e
        
    @staticmethod
    def get_user_by_id(user_id):
        try:
            user = User.query.get(user_id)
            if not user:
                raise ValueError ("user not found")
            return user
        except SQLAlchemyError as e:
            logger.error(f'Error while fetching user by id: {e}')
            raise e

