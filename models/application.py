from app import matrix, DB as db

class Application(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))
	slug = db.Column(db.String(80), unique=True)
	environments = db.relationship('Environment', backref='application',lazy='dynamic')
	features = db.relationship('Feature', backref='application',lazy='dynamic')

	def __repr__(self):
		return self.name
	
class Feature(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))
	description = db.Column(db.Text())
	application_id = db.Column(db.Integer, db.ForeignKey('application.id'))

	def __repr__(self):
		return self.name

class Environment(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))
	application_id = db.Column(db.Integer, db.ForeignKey('application.id'))

	def __repr__(self):
		return self.name

class CodeBase(db.Model):
	id = db.Column(db.Integer, primary_key=True)

	url = db.Column(db.String(500))

class Component(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	versions = db.relationship('ComponentVersion', backref='component',
                                lazy='dynamic')

	def __repr__(self):
		return self.name

class ComponentVersion(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	version = db.Column(db.String(100))
	component_id = db.Column(db.Integer, db.ForeignKey('component.id'))

	def __repr__(self):
		return self.version