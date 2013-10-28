import collections
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
    global hits; hits += 1
    title = 'Cat Facts'
    data = {
        'title': title,
        'host': hostname,
        'src': random.choice(pics),
        'fact': random.choice(facts),
    }
    return template('facts', **data)

@app.route('/stats')
def stats():
    uptime = str(now() - start_time)
    stats = collections.OrderedDict([
        ['Cat Facts Served', hits],
        ['Uptime', uptime]
    ])
    title = 'Server Stats'
    data = {
        'title': title,
        'host': hostname,
        'stats': stats
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
