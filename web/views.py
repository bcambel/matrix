#views.py
from app import matrix,DB as db, api, manager, admin
from models.user import User, Team,	UserAccount
from models.application import Application, Environment, CodeBase, Component, Feature
from models.news import News
from flask import jsonify


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




