import random
from bottle import route, static_file, run, template
from multihost_example import config, util

import socket
hostname = socket.gethostname()

@route('/hello/<name>')
def index(name='World'):
    return template('<b>Hello {{name}}</b>! (sent from my {{hostname}})',
        name=name, hostname=hostname)

@route('/ping')
def ping():
    return 'HEALTHY'

facts = util.load_file('facts')
facts = facts.split('\n')

pics = list(util.load_file_config({}, 'static/sources'))

@route('/static/<filename>')
def server_static(filename):
    print "Trying to serve {}".format(filename)
    return static_file(filename, root=util.abs_path('static'))

@route('/random')
def random_fact():
    fact = random.choice(facts)
    img = random.choice(pics) + '.jpg'
    src = '/static/' + img
    layout = '<img src="{{src}}"></img><h1>Fact</h1>\n<p>{{fact}}</p>\n<p><h3>Brought to you by</h3>\n<p>{{host}}</p>'
    return template(layout, src=src, fact=fact, host=hostname)

run(host=config['HOST'], port=config['PORT'], reloader=True)