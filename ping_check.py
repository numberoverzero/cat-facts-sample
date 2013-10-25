import os
import sys
from multihost_example import config, util

url = 'http://{ADDRESS}:{PORT}/ping'.format(**config)
status = util.load_url(url)
if status == 'HEALTHY':
	exit = 0
else:
	exit = 'Server failed ping check!'
sys.exit(exit)