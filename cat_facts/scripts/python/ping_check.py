import os
import sys
from cat_facts import config, util

os.environ['no_proxy'] = '127.0.0.1,localhost'
url = 'http://{host}:{port}/ping'.format(host=config['HOST'], port=config['PORT'])
status = util.load_url(url)
if status == 'HEALTHY':
    msg = "Server is up."
    exit = 0
else:
    msg = 'Server failed ping check!'
    exit = msg
print msg
sys.exit(exit)
