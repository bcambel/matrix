# Reset Db
from app import matrix, DB
from models.application import *
from models.user import *



DB.drop_all()
DB.create_all()

app = Application()
app.name='Matrix'
app.slug='matrix'
app.repository='https://github.com/spil-bahadir/matrix'

DB.session.add(app)
DB.session.commit()

versions = ['v0.1.0','v0.1.1','v.0.2.0','v0.3.0', 'v1.0.0']

for idx, ver in enumerate(versions):
	version = Version(name=ver,active=(True if idx==len(versions)-1 else False),application_id=app.id)
	DB.session.add(version)

features = ['User login','User register', 'Email subscription', 'Documentation' ]

for fname in features:
	feat = Feature(name=fname, application_id=app.id)
	DB.session.add(feat)

env = Environment(name="STG", application_id=app.id)

dpoint = Datapoint(name='User login successfull',slug='login_success',application_id=app.id)

components = ['Requests','HTTPie', 'Django', 'Flask']
for comp in components:
	component = Component(name=comp)
	DB.session.add(component)

services = ['MYSQL', 'REDIS', 'HA-Proxy', 'Github']
for srv in services:
	serv = Service(name=srv, location=srv+'-cluster-001')
	DB.session.add(serv)



DB.session.add(env)
DB.session.add(dpoint)

DB.session.commit()