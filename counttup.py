fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
lst = list()
hours = dict()
count = 0
for line in fh:
    line = line.rstrip()
    words=line.split()
    if  len(words) < 3  or words[0] != 'From' :
            continue
    else:
        x= words[5]
        lst.append(x[0:2])
        count = count + 1
for hrs in lst:
    hours[hrs] = hours.get(hrs,0) + 1
tmp = list()
for k,v in hours.items():
    newtup = (k,v)
    tmp.append(newtup)
tmp = sorted(tmp)
for k,v in tmp:
    print(k,v)
#print(sorted( (k,v) for k,v in hours.items()))
