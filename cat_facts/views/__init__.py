import datetime
now = datetime.datetime.now

import random
from bottle import static_file, template, redirect
from cat_facts import app, util, facts, pics

import socket
hits = 0
hostname = socket.gethostname()

start_time = now()

@app.route('/')
def index():
    redirect('/facts')

@app.route('/facts')
def cat_facts():
    global hits
    hits += 1
    fact = random.choice(facts)
    pic = random.choice(pics)
    title = 'Cat Facts'
    data = {
        'title': title,
        'cat_src': pic,
        'fact': fact,
        'host': hostname,
        'hits': hits
    }
    return template('facts', **data)

@app.route('/stats')
def stats():
    uptime = str(now() - start_time)
    title = 'Server Stats'
    data = {
        'title': title,
        'hits': hits,
        'host': hostname,
        'uptime': uptime
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
