from gevent import monkey
monkey.patch_all()
import bottle
from cat_facts import app
bottle.run(app, server='gevent', host=app.config['HOST'], port=app.config['PORT'], reloader=app.config['DEBUG'])
