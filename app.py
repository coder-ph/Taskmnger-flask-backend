from flask import Flask
from src.config.config_map import Config
from src.startup.routes import register_routes
from src.database import db
from flask_migrate import Migrate
from src.seeding.seed import run_seeding

app = Flask(__name__)
app.config.from_object(Config)
if not app.config["SQLALCHEMY_DATABASE_URI"]:
    raise ValueError("SQLALCHEMY_DATABASE_URI is not set!")
db.init_app(app)
migrate = Migrate(app, db)


with app.app_context():
    db.create_all()
    register_routes(app)
    
    @app.cli.command('seed')
    def seed():
        """"""
        run_seeding()
    
if __name__ == "__main__":
    app.run(host="0.0.0.0")