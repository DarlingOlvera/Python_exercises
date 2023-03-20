"""
In this assignment you will write a Python program somewhat
similar to http://www.py4e.com/code3/geojson.py. The program 
will prompt for a location, contact a web service and retrieve 
JSON for the web service and parse that data, and retrieve the 
first place_id from the JSON. A place ID is a textual identifier 
that uniquely identifies a place as within Google Maps.

Author: Darling Olvera Piña
"""

import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_key = 42
serviceurl ='http://py4e-data.dr-chuck.net/json?'
address = input('Enter Universitie: ')

params = dict()
params['address'] = address
params['key'] = api_key
url = serviceurl + urllib.parse.urlencode(params)

uhand = urllib.request.urlopen(url,context=ctx)
data = uhand.read().decode()
print('Retrieved', len(data),'characters')
try:
    info = json.loads(data)
except:
    info = None

if not info or 'status' not in info or info['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    quit()
#print(json.dumps(info,indent=4))

print('Place id: ',info['results'][0]['place_id'])