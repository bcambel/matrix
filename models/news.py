from app import matrix, DB as db

class News(db.Model):
	id = db.Column(db.Integer, primary_key=True)

	content = db.Column(db.Text())