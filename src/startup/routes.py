from src.routers.task_routes import task_blueprint
from src.routers.user_routes import user_blueprint

def register_routes(app):
    try:
        app.register_blueprint(task_blueprint, url_prefix="/api")
        app.register_blueprint(user_blueprint, url_prefix="/api")
    except Exception as e:
        raise e