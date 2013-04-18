from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.admin import Admin
from flask.ext.restless import APIManager
from flask.ext.login import LoginManager
from simplekv.memory import DictStore
from flaskext.kvsession import KVSessionExtension

import os,sys

matrix = None
DB = None
api = None
api = None


parentdir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,parentdir)
path = os.path.dirname(os.path.abspath(__file__))
print path
	
tmpl_dir = os.path.join( path, 'web/templates')
matrix = Flask(__name__,template_folder=tmpl_dir)
matrix.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/matrixx.db'
matrix.secret_key = 'A0Zr98j/3yX R~XaHH!Sw3f22vjekel3tjmN]LWX/,?2RT'

login_manager = LoginManager()
login_manager.setup_app(matrix)

store = DictStore()

KVSessionExtension(store, matrix)

login_manager = LoginManager()
login_manager.login_view = "/login"
login_manager.session_protection = "strong"
login_manager.init_app(matrix)

admin = Admin(matrix, name='Matrix Admin')
DB = SQLAlchemy(matrix)
manager = APIManager(matrix, flask_sqlalchemy_db=DB)

import lib.ghub 

from web.controllers.index import index_bp
matrix.register_blueprint(index_bp)