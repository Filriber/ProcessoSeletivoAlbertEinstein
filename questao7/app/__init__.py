from flask import Flask
from app.routes import login_blueprint
from app.limiter import limiter

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config")
    limiter.init_app(app)
    app.register_blueprint(login_blueprint)

    return app
