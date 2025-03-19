from repositories.task_repository import  TaskRepository

class TaskService:
    @staticmethod
    def get_all_tasks():
        try:
            return TaskRepository.get_all_tasks()
        except Exception as e:
            raise e
    
    @staticmethod
    def create_task(data):
        if not data.get('title'):
            raise ValueError ('Title is required')
        try:
            return TaskRepository.create_task(data)
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