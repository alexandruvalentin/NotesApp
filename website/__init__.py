from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'asodjaosijdas oasjdas'

    # Adjust the database path to be relative to this file
    db_path = path.join(path.dirname(__file__), DB_NAME)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    with app.app_context():
        db.create_all()
        print("Created tables!")

    return app
