"""
Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times 
they appear in the file. After the dictionary is produced, the program reads through the dictionary using a 
maximum loop to find the most prolific committer.

Author: Darling Olvera Piña
"""



name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

count = dict()

for line in handle:
    if 'From' not in line:
        continue
    elif 'From:' in line:
        continue
    w = line.split()
    count[w[1]] = count.get(w[1],0) + 1

max_count = None
max_email = None

for email, value in count.items():
    if max_count is None or value > max_count:
        max_email = email
        max_count = value

print(max_email, max_count)

