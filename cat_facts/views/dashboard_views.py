from bottle import template
from cat_facts import app, util

pics = app.config['pics']
pic_hits = {pic:0 for pic in pics}
host_hits = {}

@app.route('/add_host/<host>')
def add_host(host):
    if host in host_hits:
        return
    host_hits[host] = 0

@app.route('/add_hit/<host>/<pic>')
def add_hit(host, pic):
    host_hits[host] += 1
    pic_hits[pic] += 1

@app.route('/dashboard')
def dashboard():
    pass

@app.route('/dashboard/reset')
def dashboard_reset():
    for host in host_hits:
        util.load_url(host + '/reset')
        host_hits[host] = 0
    for pic in pic_hits:
        pic_hits[pic] = 0
