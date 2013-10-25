import bottle
from cat_facts import app
bottle.run(app, host=app.config['HOST'], port=app.config['PORT'], reloader=app.config['DEBUG'])
