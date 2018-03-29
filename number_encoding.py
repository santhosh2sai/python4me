def encode(n,i):
    s =''
    while(n >=0):
        j = n%10
        n = n//10
        if((i+j) > 10):
            num = (j + i + 1) - 10
            s = s + str(num)
        else:
            num = j  + i
            s = s + str(num)
    return int(s)
#print(encode(234,5))
print(encode(258,6))
print(encode(0,3))
