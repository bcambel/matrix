
from app import matrix,DB as db, manager
from models.user import User, Team,	UserAccount
from models.application import Application, Environment, CodeBase, Component, Feature
from models.news import News


manager.create_api(User, methods=['GET', 'POST', 'DELETE'])
manager.create_api(Team	, methods=['GET', 'POST', 'DELETE'])
manager.create_api(Application, methods=['GET', 'POST', 'DELETE'])
manager.create_api(Feature, methods=['GET', 'POST', 'DELETE'])
manager.create_api(Environment, methods=['GET', 'POST', 'DELETE'])
manager.create_api(Component, methods=['GET', 'POST', 'DELETE'])
manager.create_api(CodeBase, methods=['GET', 'POST', 'DELETE'])
manager.create_api(News, methods=['GET', 'POST', 'DELETE'])