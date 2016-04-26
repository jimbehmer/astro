#get TLE from celestrak url
#Jim Behmer on 25 April 2016

#import modules
from lxml import html
import requests

def get_tle(noradid):
	url = 'https://celestrak.com/cgi-bin/TLE.pl?CATNR=' + str(noradid)
	sat = requests.get(url)
	tle_html = html.fromstring(sat.content)
	tle = tle_html.xpath('/html/body/pre/text()')[0]
	
	return tle
