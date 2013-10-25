import random
from bottle import static_file, template
from cat_facts import app, util

import socket
hits = 0
hostname = socket.gethostname()
facts = util.load_file('facts').split('\n')
pics = app.config['pics']

@app.route('/')
def fact():
    global hits
    hits += 1
    fact = random.choice(facts)
    pic = random.choice(pics)
    cat_src = image(pic)
    nav = [
        ('Cat Facts', '/'),
        ('Hits', '/hits'),
    ]
    current_nav = 'Cat Facts'
    title = 'Cat Facts'
    data = {
        'nav': nav,
        'current_nav': current_nav,
        'title': title,
        'cat_src': cat_src,
        'fact': fact,
        'host': hostname,
        'hits': hits
    }
    return template('fact', **data)

@app.route('/hits')
def page_hits():
    nav = [
        ('Cat Facts', '/'),
        ('Hits', '/hits')
    ]
    current_nav = 'Hits'
    title = 'Cat Facts - Server Hits'
    data = {
        'nav': nav,
        'current_nav': current_nav,
        'title': title,
        'hits': hits
    }
    return template('hits', **data)

@app.route('/ping')
def ping():
    return 'HEALTHY'

@app.route('/static/<filename>')
def static(filename):
    print "Serving filename: "+filename
    return static_file(filename, root=util.abs_path('static'))

@app.route('/static/img/<filename>')
def static(filename):
    print "Serving filename: "+filename
    return static_file(filename, root=util.abs_path('static/img'))

def image(name):
    return '/static/img/' + name
