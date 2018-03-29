fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.rstrip().startswith("X-DSPAM-Confidence:") :
        continue
    count = count + 1
    c = float(count)

    value = float(line[20:])
    total = total + value
    t = float(total)
    avg = t/c
print('Average Spam Confidence: ',avg)
