#views.py
from app import matrix,DB as db, api, manager, admin
from models.user import User
from models.application import Application, Environment, CodeBase, Component, Feature
# from flask.ext.restful import restful
from flask import jsonify
from flask.ext.admin.contrib.sqlamodel import ModelView

@matrix.route("/")
def index():
	return "Hello World!"

@matrix.route("/login")
def login():
	return "Login page"


@matrix.route("/logout")
def logout():
	return "Logout page"

@matrix.route("/users")
def users():
	return "Users list"


manager.create_api(User, methods=['GET', 'POST', 'DELETE'])
manager.create_api(Application, methods=['GET', 'POST', 'DELETE'])
manager.create_api(Feature, methods=['GET', 'POST', 'DELETE'])
manager.create_api(Environment, methods=['GET', 'POST', 'DELETE'])
manager.create_api(Component, methods=['GET', 'POST', 'DELETE'])
manager.create_api(CodeBase, methods=['GET', 'POST', 'DELETE'])

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Application, db.session))