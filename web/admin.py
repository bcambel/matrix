
from app import matrix,DB as db, admin
from models.user import User, Team,	UserAccount
from models.application import Application, Environment, CodeBase, Component, Feature
from models.news import News
from flask.ext.admin.contrib.sqlamodel import ModelView


admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Application, db.session, category='Application'))
admin.add_view(ModelView(Feature, db.session, category='Application'))
admin.add_view(ModelView(Environment, db.session, category='Application'))
admin.add_view(ModelView(Team, db.session))
admin.add_view(ModelView(News, db.session))