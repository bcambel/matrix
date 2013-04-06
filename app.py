from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.admin import Admin

import os,sys
parentdir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,parentdir)

matrix = Flask(__name__)
matrix.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

admin = Admin(matrix, name='Matrix Admin')
DB = SQLAlchemy(matrix)