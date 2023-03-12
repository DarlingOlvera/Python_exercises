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
    fname = "regex_sum_1769244.txt"
fh = open(fname)
numbers = list()

for line in fh:
    line.rstrip()
    
    num = re.findall('[0-9]+', line)
    #ignore the lines that don't have a number
    if len(num) < 1:
        continue
    
    for n in num:
        numbers.append(int(n))
        
print('num of values:',len(numbers))
print('sum:',sum(numbers))

