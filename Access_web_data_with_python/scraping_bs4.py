"""
 Scraping Numbers from HTML using BeautifulSoup In this assignment you
 will write a Python program similar to http://www.py4e.com/code3/urllink2.py. 
 The program will use urllib to read the HTML from the data files below, 
 and parse the data, extracting numbers and compute the sum of the numbers in the file.
 
 Author: Darling Olvera Piña
 
"""


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#test_url = 'http://py4e-data.dr-chuck.net/comments_42.html'
url =input('Enter -')
html = urllib.request.urlopen(url,context=ctx).read()
soup = BeautifulSoup(html,'html.parser')

numbers = list()
#retrieving all span tags
tags = soup('span')
for tag in tags:
    numbers.append(int(tag.contents[0]))

print('Sum: ',sum(numbers))

 