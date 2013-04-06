from app import matrix, DB

from web import views

if __name__ == "__main__":
	DB.create_all()
	matrix.run(debug=True,port=5555)
