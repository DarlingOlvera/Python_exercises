
fname = input("Enter file name: ")

try:
    fhand = open(fname)
except:
    print('Cannot open file', fname)
    quit()

for line in fhand:
   line = line.upper()
   line = line.rstrip()
   print(line)
