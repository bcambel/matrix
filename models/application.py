from app import matrix, DB as db

class Application(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))
	slug = db.Column(db.String(80), unique=True)
	repository = db.Column(db.String(200))
	environments = db.relationship('Environment', backref='application',lazy='dynamic')
	features = db.relationship('Feature', backref='application',lazy='dynamic')
	data_points = db.relationship('Datapoint', backref='application',lazy='dynamic')
	versions = db.relationship("Version", backref='application',lazy='dynamic')
	#active_version = db.Column(db.Integer, db.ForeignKey('version.id'))

	def __repr__(self):
		return self.name


class Version(db.Model):
	"""Application Versions"""
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))
	active = db.Column(db.Boolean)
	application_id = db.Column(db.Integer, db.ForeignKey('application.id'))

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


class Datapoint(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	slug = db.Column(db.String(100), unique=True)
	application_id = db.Column(db.Integer, db.ForeignKey('application.id'))


class Datacollection(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	ts = db.Column(db.DateTime)
	app_id = db.Column(db.Integer, db.ForeignKey('application.id'))
	env_id = db.Column(db.Integer, db.ForeignKey('environment.id'))	
	point = db.Column(db.String(100))
	data = db.Column(db.Text)

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


class Service(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	location = db.Column(db.String(100))

