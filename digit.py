#Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p we want to find a positive integer k, if it exists, such as the sum of the digits of n taken to the successive powers of p is equal to k * n. In other words:

#Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

#If it is the case we will return k, if not return -1.


num = 89
p = 1
d_squared = 0
for d in str(num):
    x =int(d)**p
    d_squared = d_squared + x
    p = p+1
if(d_squared%num is 0):
    print(d_squared//num)
else:
    print("-1")
