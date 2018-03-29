name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)
lst=list()
names=dict()
count = None
largekey = None
for line in fh:
    line = line.rstrip()
    words=line.split()
    if  len(words) < 3  or words[0] != 'From' :
            continue
    else:
        lst.append(words[1])

for name in lst:
    names[name] = names.get(name,0) + 1
for k,v in names.items():
    if count is None or v > count:
        largekey = k
        count =v
print(largekey ,count)
#print(names)
