import random
from bottle import static_file, template
from cat_facts import app, util

import socket
fact_page_loads = 0
hostname = socket.gethostname()
facts = util.load_file('facts').split('\n')
layout = util.load_file('fact_layout')
dashboard_url = app.config['DASHBOARD_ENDPOINT']
pics = app.config['pics']

@app.route('/')
def fact():
    global fact_page_loads
    fact_page_loads += 1
    fact = random.choice(facts)
    pic = random.choice(pics)
    src = resource(pic)
    update_dashboard(pic)
    return template(layout, src=src, fact=fact, host=hostname, hits=fact_page_loads)

@app.route('/ping')
def ping():
    return 'HEALTHY'

@app.route('/static/<filename>')
def static(filename):
    return static_file(filename, root=util.abs_path('static'))

@app.route('/reset')
def reset():
    global fact_page_loads
    fact_page_loads = 0

def update_dashboard(pic):
    if app.config['DEBUG']:
        print "Not updating dashboard, no dashboard endpoint"
        return
    url = dashboard_url + '/add_hit/{host}/{pic}'
    url = url.format(host=app.config['HOST'], pic=pic)
    util.load_url(url)

def resource(name):
    return '/static/' + name
