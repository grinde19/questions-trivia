from flask import Flask
from database import db, ma
from .config import Config
from .routes.question_routes import bp as question_bp
from .routes.answer_routes import bp as answer_bp
from .routes.level_routes import bp as level_bp
from .routes.trivia_routes import bp as trivia_bp
from .routes.user_routes import bp as user_bp
from .routes.role_routes import bp as role_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)
    
    with app.app_context():
        db.create_all()

    app.register_blueprint(question_bp)
    app.register_blueprint(answer_bp)
    app.register_blueprint(level_bp)
    app.register_blueprint(trivia_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(role_bp)

    return app
