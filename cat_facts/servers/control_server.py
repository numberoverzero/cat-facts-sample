from bottle import route, static_file, run, template
from cat_facts import config, util

pics = list(util.load_file_config({}, 'static/sources'))
pic_hits = {pic:0 for pic in pics}
host_hits = {}

@route('/add_host/<host>')
def add_host(host):
	if host in host_hits:
		return
	host_hits[host] = 0

@route('/add_hit/<host>/<pic>')
def add_hit(host, pic):
	host_hits[host] += 1
	pic_hits[pic] += 1

@route('/dashboard')
def dashboard():
	pass

@route('/dashboard/reset')
def dashboard_reset():
	for host in host_hits:
		util.load_url(host + '/reset')
		host_hits[host] = 0
	for pic in pic_hits:
		pic_hits[pic] = 0

run(host=config['HOST'], port=config['PORT'], reloader=True)
