from flask import Blueprint, request,render_template, redirect, abort
from models.application import Application

index_bp = Blueprint('index', __name__)

@index_bp.route("/")
@index_bp.route("/index")
def index():
	return render_template("index.html")


@index_bp.route("/applications/<int:id>")
def application_details(id):
	app = Application.query.get(id)
	return render_template("application.html", app=app)

@index_bp.route("/applications")
def applications():
	applications = Application.query.all()
	return render_template("applications.html",applications=applications)