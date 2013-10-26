import bottle
from cat_facts import app
bottle.run(app, server='paste', host=app.config['HOST'], port=app.config['PORT'], reloader=app.config['DEBUG'])
