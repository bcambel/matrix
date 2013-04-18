from app import matrix, DB
import os,sys
# from app import initialize,



if __name__ == "__main__":
	# initialize()
	current_dir = os.path.dirname(os.path.abspath(__file__))

	from web import views
	from web import api
	from web import admin
	DB.create_all()
	if True:
		from werkzeug import SharedDataMiddleware
		print current_dir
		file_hosted_at = os.path.join(current_dir, 'web' , 'static')
		print file_hosted_at

		matrix.wsgi_app = SharedDataMiddleware(matrix.wsgi_app, {
			'/static': file_hosted_at
		})
	matrix.run(debug=True,port=5555)
