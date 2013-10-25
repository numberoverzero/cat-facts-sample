import random
from bottle import static_file, template, redirect
from cat_facts import app, util, facts, pics

import socket
hits = 0
hostname = socket.gethostname()

@app.route('/')
def index():
    redirect('/facts')

@app.route('/facts')
def cat_facts():
    global hits
    hits += 1
    fact = random.choice(facts)
    pic = random.choice(pics)
    nav = [
        ('Cat Facts', '/facts'),
        ('Stats', '/stats'),
    ]
    current_nav = 'Cat Facts'
    title = 'Cat Facts'
    data = {
        'nav': nav,
        'current_nav': current_nav,
        'title': title,
        'cat_src': pic,
        'fact': fact,
        'host': hostname,
        'hits': hits
    }
    return template('facts', **data)

@app.route('/stats')
def stats():
    nav = [
        ('Cat Facts', '/facts'),
        ('Stats', '/stats')
    ]
    current_nav = 'Stats'
    title = 'Server Stats'
    data = {
        'nav': nav,
        'current_nav': current_nav,
        'title': title,
        'hits': hits,
        'name': hostname
    }
    return template('stats', **data)

@app.route('/ping')
def ping():
    return 'HEALTHY'

@app.route('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    print "Serving image: " + filename
    return static_file(filename, root=util.abs_path('static/img'))

@app.route('/<filename:re:.*\.css>')
def stylesheets(filename):
    print "Serving stylesheet: " + filename
    return static_file(filename, root=util.abs_path('static/css'))
