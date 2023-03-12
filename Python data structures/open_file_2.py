# Use the file name mbox-short.txt as the file name
#fname = input("Enter file name: ")
fh = open('mbox-short.txt')
n_lines = 0
value = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    n_lines = n_lines + 1
    lx = line[line.find('0'):]
    value = value + float(lx)
    #print(lx)
average = value / n_lines
print("Average spam confidence: ",average)
