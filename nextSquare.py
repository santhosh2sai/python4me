def find_next_square(sq):
    #Return the next square if sq is a square, -1 otherwise
    x = sq**0.5
    print(x)
    y = int(x) + 1
    print(y)
    if(x%1 == 0):
        return y**2
    else:
        return -1
print(find_next_square(121))
