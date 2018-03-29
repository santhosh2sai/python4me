fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    l = line.rstrip().split()
    for i in l:
        if i in lst:
            continue
        else:
            lst.append(a)
lst.sort()
print(lst)
