import os
import sys
import urllib2
from multihost_example import config

#os.environ['no_proxy'] = 'localhost'
ADDRESS = 'http://{ADDRESS}:{PORT}'.format(**config)
exit = 'Server failed ping check!'
try:
	response = urllib2.urlopen(ADDRESS + '/ping')
	html = response.read()
	if html == 'HEALTHY':
		exit = 0
except urllib2.URLError:
	pass
sys.exit(exit)