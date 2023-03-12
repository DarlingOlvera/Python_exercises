"""In this assignment you will read through and parse a file with text and numbers. 
You will extract all the numbers in the file and compute the sum of the numbers.
The basic outline of this problem is to read the file, look for integers using the re.findall(), 
looking for a regular expression of '[0-9]+' 
and then converting the extracted strings to integers and summing up the integers.

Author: Darling Olvera Piña
"""
import re

fname = input('Enter the file name:')
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)

for line in fh:
    line.rstrip()
    num = re.findall('[0-9]+',line)
print(num)