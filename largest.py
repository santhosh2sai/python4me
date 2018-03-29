
lst = []
while True:
    num = input("Enter a number: ")
    if num == 'done' :
        break
    try:
        n = int(num)
    except:
        print('Invalid Input')
        continue
    lst.append(n)

l =max(lst)
s =min(lst)
print("Maximum",l)
print("Minimun",s)
