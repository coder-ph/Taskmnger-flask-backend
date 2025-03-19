from routers.task_routes import task_blueprint

def register_routes(app):
    try:
        app.register_blueprint(task_blueprint, url_prefix="/api")
    except Exception as e:
        raise e