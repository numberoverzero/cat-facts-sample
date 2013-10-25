from cat_facts import util
util.set_root(__file__)

import bottle
app = bottle.Bottle()
config = util.load_file_config(app.config, '.config')

pics = util.list_files('static')
config['pics'] = sorted(pics)

import views
