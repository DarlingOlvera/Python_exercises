fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    for w in line.split():
        if w not in lst:
            lst.append(w)
        continue
lst.sort()
print(lst)

    





    


