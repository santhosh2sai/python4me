import re
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "regex.txt"
x =[]
flattened_list= []
sum1 = 0
fh = open(fname)
for line in fh:
    line.rstrip()

    x.append(re.findall('[0-9]+',line))
for i in x:
    for y in i:
        flattened_list.append(y)
for i in flattened_list:
    num = int(i)
    sum1 = sum1 + num
print(sum1)
