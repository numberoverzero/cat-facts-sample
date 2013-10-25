import bottle
from cat_facts import app

app.config['MODE'] = 'WEBSITE'
bottle.run(app, host=app.config['HOST'], port=app.config['PORT'], reloader=app.config['DEBUG'])
