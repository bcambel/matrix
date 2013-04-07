from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.admin import Admin
from flask.ext.restless import APIManager
from flask.ext.login import LoginManager
import os,sys

matrix = None
DB = None
api = None
api = None


parentdir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,parentdir)

matrix = Flask(__name__)
matrix.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/matrix.db'
matrix.secret_key = 'A0Zr98j/3yX R~XaHH!Sw3f22vjekel3tjmN]LWX/,?2RT'

login_manager = LoginManager()
login_manager.setup_app(matrix)

admin = Admin(matrix, name='Matrix Admin')
DB = SQLAlchemy(matrix)
manager = APIManager(matrix, flask_sqlalchemy_db=DB)