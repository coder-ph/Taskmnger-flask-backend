from sqlalchemy.exc import SQLAlchemyError
from Models.task import Task
from database import db

class TaskRepository:
    @staticmethod
    def get_all_tasks():
        try:
            return Task.query.all()
        except SQLAlchemyError as e:
            raise e
        
    @staticmethod
    def get_task_by_id(task_id):
        try:
            task = Task.query.get(task_id)
            if not task:
                return None
            return task
        except SQLAlchemyError as e:
            raise e

    @staticmethod
    def create_task(data):
        try:
             task = Task(**data)
             db.session.add(task)
             db.session.commit()
             return task
        except SQLAlchemyError as e:
            raise e

    @staticmethod
    def update_task(task_id, data):
        try:
            task = Task.query.get(task_id)
            if not task:
                return None
            for key, value in data.items():
                setattr(task, key, value)
            db.session.commit()
            return task
        
        except SQLAlchemyError as e:
            raise e
        
    @staticmethod
    def delete_task(task_id):
        try:
            task = Task.query.get(task_id)
            if task:
             db.session.delete(task)
             db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e
            
        task = Task.query.get(task_id)
        if task:
            db.session.delete(task)
            db.session.commit()
        
    @staticmethod
    def mark_task_complete(task_id):
        try:
            task = Task.query.get(task_id)
            if task:
                task.status = "Completed"
                db.session.commit()
            return task
        except SQLAlchemyError as e:
            raise e
            
       
        
        