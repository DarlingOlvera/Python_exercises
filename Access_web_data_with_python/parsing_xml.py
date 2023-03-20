"""
In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. 
The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract 
the comment counts from the XML data, compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your testing 
and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_1769248.xml (Sum ends with 88)

Author: Darling Olvera Piña
"""




import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')

uhand = urllib.request.urlopen(url,context=ctx)

numbers = list()

data = uhand.read()
#print(data.decode())
tree = ET.fromstring(data)

"""To make the code a little simpler, you can use an XPath selector string to look 
through the entire tree of XML for any tag named 'count' with the following line of code:"""
counts = tree.findall('.//count')

for c in counts:
    numbers.append(int(c.text))

print('Count: ', len(counts))
print('Sum: ',sum(numbers))