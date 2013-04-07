from app import DB as db

members = db.Table('members',
		db.Column('team_id',db.Integer,db.ForeignKey('team.id')),
		db.Column('user_id',db.Integer,db.ForeignKey('user.id'))
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    teams = db.relationship('Team', secondary=members,backref=db.backref('team',lazy='dynamic'))

    def __init__(self):
    	pass
        #self.username = username
        # self.email = email

    def __repr__(self):
        return self.username



class UserAccount(db.Model):
	id = db.Column(db.Integer, primary_key=True)

class Team(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80),unique=True)
	#members = db.relationship('User', secondary=members, backref=db.backref('user',lazy='dynamic'))

	def __repr__(self):
		return self.name if self.name is not None and len(self.name) > 0 else "Untitled"

