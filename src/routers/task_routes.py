from flask import Blueprint
from  handlers.controllers.task_controller import TaskController

task_blueprint = Blueprint('task', __name__)
task_controller = TaskController()

task_blueprint.route("/tasks", methods=['GET'])(task_controller.get_tasks)
task_blueprint.route("/tasks", methods=['POST'])(task_controller.create_task)
task_blueprint.route("/tasks/<int:task_id>", methods = ['PUT'])(task_controller.update_task)
task_blueprint.route("/tasks/<int:task_id>", methods=['DELETE'])(task_controller.delete_task)
task_blueprint.route("/tasks/<int:task_id>/complete", methods=['PATCH'])(task_controller.task_as_complete)