import random
from bottle import route, static_file, run, template
from multihost_example import config, util

import socket
fact_page_loads = 0
hostname = socket.gethostname()
facts = util.load_file('facts').split('\n')
pics = list(util.load_file_config({}, 'static/sources'))
layout = util.load_file('layout')

@route('/ping')
def ping():
    return 'HEALTHY'

@route('/static/<filename>')
def static(filename):
    return static_file(filename, root=util.abs_path('static'))

@route('/fact')
def fact():
    global fact_page_loads
    fact_page_loads += 1
    fact = random.choice(facts)
    src = '/static/' + random.choice(pics) + '.jpg'
    return template(layout, src=src, fact=fact, host=hostname, hits=fact_page_loads)

@route('/hits')
def hits():
    return fact_page_loads

run(host=config['HOST'], port=config['PORT'], reloader=True)