import random
from bottle import route, static_file, run, template
from multihost_example import config, util

import socket
fact_page_loads = 0
hostname = socket.gethostname()
facts = util.load_file('facts').split('\n')
pics = list(util.load_file_config({}, 'static/sources'))
layout = util.load_file('fact_layout')
dashboard = config['DASHBOARD']


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
    pic = random.choice(pics)
    src = '/static/' + pic + '.jpg'
    update_dashboard(pic)
    return template(layout, src=src, fact=fact, host=hostname, hits=fact_page_loads)

@route('/reset')
def reset():
    global fact_page_loads
    fact_page_loads = 0

def update_dashboard(pic):
    if dashboard == 'DEBUG':
        print "Not updating dashboard, debugging"
        return
    url = dashboard + '/add_hit/{host}/{pic}'
    url = url.format(host=config['HOST'], pic=pic)
    util.load_url(url)


run(host=config['HOST'], port=config['PORT'], reloader=True)