from flask import Flask
from src.config.config import Config
from src.startup.routes import register_routes
from src.database import db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()
    register_routes(app)
    
if __name__ == "__main__":
    app.run(debug=True, port=5555)