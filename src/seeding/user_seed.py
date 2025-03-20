from src.Models.user import User
from src.database import db
from src.services_layer.utilities.hash import Hash

def seed_users():
    users = [
        {
            "email": "student@example.com",
            "password": Hash.hash_password("student123"),
            "role": "student"
        },
        {
            "email": "teacher@example.com",
            "password": Hash.hash_password("teacher123"),
            "role": "teacher"
        },
        {
            "email": "admin@example.com",
            "password": Hash.hash_password("admin123"),
            "role": "admin"
        }
    ]
    
    for user_data in users:
        if not User.query.filter_by(email = user_data['email']).first():
            user = User(**user_data)
            db.session.add(user)
    db.session.commit()