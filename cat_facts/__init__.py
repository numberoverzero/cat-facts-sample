from cat_facts import util
util.set_root(__file__)

import bottle
app = bottle.Bottle()

bottle.TEMPLATE_PATH.insert(0, util.abs_path('views'))

config = util.load_file_config(app.config, '.config')

facts = util.load_file('static/facts').split('\n')

import views
