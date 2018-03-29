# split Strings
def solution(s):
    i = len(s)
    #print(i)
    x  = i%2
    if x == 0:
        return split_half(s)
    else:
        str = s + '_'
        return split_half(str)

def split_half(s):
    i = len(s)//2
    l = []
    j = 2
    first_half = s[0:i]
    second_half = s[i:]
    print(first_half,second_half)
    if len(first_half) > j and len(second_half) > j:
        solution(first_half)
        solution(second_half)
    else:
        l.append(first_half)
        l.append(second_half)
    return l
print(solution('abcdadcb'))
print(solution('abcde'))
