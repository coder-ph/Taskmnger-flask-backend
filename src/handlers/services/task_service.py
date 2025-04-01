from src.handlers.repositories.task_repository import  TaskRepository
from src.services_layer.utilities.redis_client import cache_data, get_cached_data, invalidate_cache
import json 

class TaskService:
    @staticmethod
    def get_all_tasks():
        try:
            return TaskRepository.get_all_tasks()
        except Exception as e:
            raise e
    
    @staticmethod
    def get_task_id(user_id: int):
        cache_key = f"user_{user_id}:tasks"
        cache_tasks = get_cached_data(cache_key)
        if cache_tasks:
            return json.loads(cache_tasks.decode('utf-8'))
        
        tasks = TaskRepository.get_task_by_id(user_id)
        cache_data(cache_key, json.dumps([task.to_dict() for task in tasks]))
        return tasks
    
    @staticmethod
    def create_task(data):
        if not data.get('title'):
            raise ValueError ('Title is required')
        try:
        
            task = TaskRepository.create_task(data)
            invalidate_cache(f"user_{data['user_id']}: tasks")
            return task
        except Exception as e:
            raise e
        
    @staticmethod
    def update_task(task_id, data):
        if not data:
            raise ValueError ('Empty payload')
        
        try:
            TaskRepository.update_task(task_id, data)
        except Exception as e:
            raise e
        
    @staticmethod
    def delete_task(task_id):
        try:
            TaskRepository.delete_task(task_id)
            return True
        except Exception as e:
            raise e
        
    @staticmethod
    def mark_task_complete(task_id):
        try:
            task = TaskRepository.get_task_by_id(task_id)
            if task.status == "completed":
                raise ValueError("Task already completed")
            return TaskRepository.mark_task_complete(task_id)
        except Exception as e:
            raise e