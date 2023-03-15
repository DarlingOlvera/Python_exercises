"""
 In this assignment you will write a Python program that expands on
 http://www.py4e.com/code3/urllinks.py. The program will use urllib 
 to read the HTML from the data files below, extract the href= values 
 from the anchor tags, scan for a tag that is in a particular position 
 relative to the first name in the list, follow that link and repeat 
 the process a number of times and report the last name you find.

 Author: Darling Olvera Piña
"""

import urllib.error, urllib.parse, urllib.request
from bs4 import BeautifulSoup

url =input('Enter -')
times = int(input('times:'))
position = int(input('position:'))
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')
new_url=''
#retrieving all span tags
tags = soup('a')

for t in range(times-1):
    
    new_url = tags[position-1].get('href',None)
    html = urllib.request.urlopen(new_url).read()
    soup = BeautifulSoup(html,'html.parser')
    tags = soup('a')
    print('Name: ',tags[position-1].contents[0])

    

