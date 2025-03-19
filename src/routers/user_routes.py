from flask import Blueprint
from handlers.controllers.user_controller import UserController
from services_layer.auth.auth import AuthService
from startup.loggings import logger
from handlers.middlewares.authentication import auth_required

user_blueprint = Blueprint("user", __name__)
user_controller = UserController()

user_blueprint.route("/register", methods=['POST'])(user_controller.register)
user_blueprint.route("login", methods=['POST'])(user_controller.login)
user_blueprint.route("/profile", methods=['GET'])(auth_required(user_controller.get_profile))