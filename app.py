from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.admin import Admin
from flask.ext.restless import APIManager
import os,sys

matrix = None
DB = None
api = None
api = None

#def initialize():
print "Running"
#global admin, matrix, DB,api

parentdir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,parentdir)

matrix = Flask(__name__)
matrix.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/matrix.db'


admin = Admin(matrix, name='Matrix Admin')
DB = SQLAlchemy(matrix)
manager = APIManager(matrix, flask_sqlalchemy_db=DB)