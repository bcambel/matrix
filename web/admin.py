
from app import matrix,DB as db, admin
from models.user import User, Team,	UserAccount
from models.application import Service, Application, Version, Environment, CodeBase, Component, Feature, Datapoint, Datacollection
from models.news import News
from flask.ext.admin.contrib.sqlamodel import ModelView


admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Application, db.session, category='Application'))
admin.add_view(ModelView(Version, db.session, category='Application'))
admin.add_view(ModelView(Feature, db.session, category='Application'))
admin.add_view(ModelView(Environment, db.session, category='Application'))
admin.add_view(ModelView(Datapoint, db.session, category='Application'))
admin.add_view(ModelView(Team, db.session))
admin.add_view(ModelView(News, db.session))
admin.add_view(ModelView(Datacollection, db.session))
admin.add_view(ModelView(Service, db.session))