from flask import Flask
from therum.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_socketio import SocketIO, emit

db = SQLAlchemy()
migrate = Migrate()
socket = SocketIO()


def Therum(config_class=Config):

    app = Flask(__name__, template_folder="../ui/templates/", static_folder="../ui/static/")
    app.config.from_object(config_class)
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['DEBUG'] = True
   
    db.init_app(app)
    migrate.init_app(app, db) 
    
    from therum.views import bp as main_bp
    app.register_blueprint(main_bp)

    socket.init_app(app,cors_allowed_origins="*", async_mode='eventlet')
    
    return app
