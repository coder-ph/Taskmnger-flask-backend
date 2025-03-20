
    
from src.Models.task import Task
from src.seeding.user_seed import seed_users
from src.Models.user import User
from src.services_layer.utilities.hash import Hash
from src.database import db
from datetime import datetime, timedelta

def seed_tasks():
    student = User.query.filter_by(email="student@example.com").first()
    teacher = User.query.filter_by(email="teacher@example.com").first()
    admin = User.query.filter_by(email="admin@example.com").first()
    
    if not student or not teacher or not admin:
        print(" ERROR: One or more users do not exist! Seeding users first...")
        seed_users()
        
        student = User.query.filter_by(email="student@example.com").first()
        teacher = User.query.filter_by(email="teacher@example.com").first()
        admin = User.query.filter_by(email="admin@example.com").first()

        if not student or not teacher or not admin:
            print(" SEVERE ERROR: Users could not be seeded. Exiting...")
            return  

    print(" Users exist. Seeding tasks...")
    
    tasks = [
        {
            "title": "Complete homework",
            "description": "Finish math and science homework",
            "due_date": datetime.utcnow() + timedelta(days=2),
            "status": "Pending",
            "user_id": student.id
        },
        {
            "title": "Prepare lesson plan",
            "description": "Create lesson plan for next week",
            "due_date": datetime.utcnow() + timedelta(days=5),
            "status": "Pending",
            "user_id": teacher.id
        },
        {
            "title": "Review reports",
            "description": "Review monthly performance reports",
            "due_date": datetime.utcnow() + timedelta(days=1),
            "status": "Pending",
            "user_id": admin.id
        }
    ]
    
    for task_data in tasks:
        if not Task.query.filter_by(title=task_data["title"]).first():
            task = Task(**task_data)
            db.session.add(task)
    db.session.commit()