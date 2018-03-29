#Multiples of 3 or 5
def solution(n):
    sum = 0
    for i in range(1,n):
        #print(i)
        j = i%3
        k= i%5
        if(j is 0 or k is 0):
            sum = sum + i
    print(sum)
solution(10)
