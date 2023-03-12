"""Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below."""

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

d =dict()

for line in handle:
    if 'From' not in line:
        continue
    elif 'From:' in line:
        continue
    tmp = line.split()
    h = tmp[5].split(':')
    d[h[0]] = d.get(h[0],0) + 1

tmp = list()
for k,v in d.items():
    tmp.append((k,v))

tmp = sorted(tmp)

for k,v in tmp:
    print(k,v)
