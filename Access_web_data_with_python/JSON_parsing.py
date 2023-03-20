"""Similar exercise as the one with xml

    Author: Darling Olvera Piña
"""

import urllib.request, urllib.parse, urllib.error
import json
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')


uhand = urllib.request.urlopen(url,context=ctx)

numbers = list()

data = uhand.read().decode()
print('Retrieved', len(data), 'characters')

info = json.loads(data)

for item in info['comments']:
    #print('Count',item['count'])
    numbers.append(int(item['count']))

print('Sum',sum(numbers))


#imprime el objeto json
#print(json.dumps(info, indent=4))

