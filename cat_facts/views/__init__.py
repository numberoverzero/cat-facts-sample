import collections
import random
import socket
from bottle import static_file, template, redirect
from cat_facts import app, util, facts, pics
from datetime import datetime

from gevent.coros import Semaphore
class HitCounter(object):
    
    def __init__(self):
        self.value = 0
        self.lock = Semaphore(1)
    
    def __str__(self):
        return str(self.value)

    def increment(self):
        try:
            self.lock.acquire()
            self.value += 1
        finally:
            self.lock.release()

hostname = socket.gethostname()
start_time = datetime.now()
hits = HitCounter()

@app.route('/')
def index():
    redirect('/facts')

@app.route('/facts')
def cat_facts():
    hits.increment()
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
    uptime = str(datetime.now() - start_time)
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
    return static_file(filename, root=util.abs_path('static/img'))

@app.route('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root=util.abs_path('static/css'))
