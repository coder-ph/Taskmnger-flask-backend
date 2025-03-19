from routers.task_routes import task_blueprint
from routers.user_routes import user_routes

def register_routes(app):
    try:
        app.register_blueprint(task_blueprint, url_prefix="/api")
        app.register_blueprint(user_routes, url_prefix="/api")
    except Exception as e:
        raise e