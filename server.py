from app import matrix, DB
# from app import initialize,



if __name__ == "__main__":
	# initialize()

	from web import views

	DB.create_all()
	matrix.run(debug=True,port=5555)
