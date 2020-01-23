from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import firebase_admin
from firebase_admin import credentials
from google.cloud import firestore
from firebase_admin import firestore, initialize_app

# pg_user = os.getenv('PG_USER', 'postgres')
# pg_host = os.getenv('PG_HOST', 'localhost')
# pg_port = os.getenv('PG_PORT', '5432')
# pg_database = os.getenv('PG_DATABASE', 'postgres')
# pg_password = os.getenv('PG_PASSWORD', 'postgres_password')
cred = credentials.Certificate('webapp/account/key.json')
default_app = initialize_app(cred)
db = firestore.client()
# db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # app.config['SQLALCHEMY_DATABASE_URI'] \
    #     = 'postgresql://' + pg_user + ':' + pg_password + '@' + pg_host + ':' + pg_port + '/' + pg_database
    app.config['SECRET_KEY'] = 'super secret key'
    app.config['DEBUG'] = True
    app.config['ENVIRONMENT'] = 'development'
    # db.init_app(app)

    with app.app_context():
        # Imports
        from . import routes
        #db.create_all()




        return app
