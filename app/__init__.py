from flask import Flask
from flask_migrate import Migrate
from .database import db, ma
from .config import Config
from .routes.user_answer_routes import bp as user_answer_bp
from .routes.question_routes import bp as question_bp
from .routes.answer_routes import bp as answer_bp
from .routes.level_routes import bp as level_bp
from .routes.trivia_routes import bp as trivia_bp
from .routes.user_routes import bp as user_bp
from .routes.role_routes import bp as role_bp


migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Importar los modelos para que las migraciones los detecten
    from app import models
        

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    
    app.register_blueprint(user_answer_bp)
    app.register_blueprint(question_bp)
    app.register_blueprint(answer_bp)
    app.register_blueprint(level_bp)
    app.register_blueprint(trivia_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(role_bp)

    # Ruta de prueba
    @app.route('/')
    def index():
        return {'message': 'API Flask funcionando correctamente!', 'status': 'success'}
    

    return app
