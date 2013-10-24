import random
import util
from bottle import route, run, template
from multihost_example import config
util.set_root(__file__)

import socket
hostname = socket.gethostname()

@route('/hello/<name>')
def index(name='World'):
    return template('<b>Hello {{name}}</b>! (sent from my from {{hostname}})',
        name=name, hostname=hostname)

@route('/ping')
def ping():
    return 'HEALTHY'


facts = util.load_file('facts')
facts = facts.split('\n')

@route('/random')
def random_fact():
    fact = random.choice(facts)
    layout = '<h1>Fact</h1>\n<p>{{fact}}</p>\n<p><h3>Brought to you by</h3>\n<p>{{host}}</p>'
    return template(layout, fact=fact, host=hostname)

run(host=config['HOST'], port=config['PORT'], reloader=True)