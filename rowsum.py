def row_sum_odd_numbers(n):
    if(n is 1):
        return 1
    elif(n is 2):
        return n**3
    else:
        #i = n + 1
        return n**3
print(row_sum_odd_numbers(13))
print(row_sum_odd_numbers(19))
print(row_sum_odd_numbers(41))
