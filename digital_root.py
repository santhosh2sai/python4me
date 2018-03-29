#digital_root
def digital_root(n):
    add = 0
    while(n>0):
        i = n%10
        n = n//10
        add = add + i
    return add
#print(digital_root(16))
print(digital_root(267))
add = digital_root(267)
if(add>10):
    print(digital_root(add))
