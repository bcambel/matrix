#views.py
from app import matrix,DB
from models.user import User

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
	#return "<br />".join([repr(u) for u in User.query.all()])
