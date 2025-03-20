from flask import jsonify, request
from src.handlers.services.task_service import TaskService
from src.handlers.middlewares.authentication import auth_required

class TaskController:
    @auth_required
    def get_tasks(self):
        tasks = TaskService.get_all_tasks()
        return jsonify (tasks)
    
    @auth_required
    def create_task(self):
        data = request.get_json()
        task = TaskService.create_task(data)
        return jsonify(task), 201
    
    @auth_required
    def update_task(self, task_id):
        data = request.get_json()
        task = TaskService.update_task(task_id, data)
        return jsonify(task)
    
    @auth_required
    def delete_task(self, task_id):
        TaskService.delete_task(task_id)
        return " ", 204
    
    @auth_required
    def task_as_complete(self, task_id):
        task = TaskService.mark_task_complete(task_id)
        return jsonify(task)
        