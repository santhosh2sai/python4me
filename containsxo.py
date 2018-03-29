#Check to see if a string has the same amount of 'x's and 'o's. The method must
#return a boolean and be case insensitive. The string can contain any char.

#XO("ooxx") => true
#XO("xooxx") => false
#XO("ooxXm") => true
#XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
#XO("zzoo") => false

#Program
def xo(s):
    co = 0
    xo = 0
    for i in s:
        if(i is 'o' or i is 'O' ):
            co = co + 1
        elif(i is 'x' or i is 'X'):
            xo = xo + 1
    print('count of o & x is',co,xo)
    if(xo is co):
        print('True')
    else:
        print('False')
#xo('XxOO')
xo('xo(XXXodhXopoQXoXoXoXXoXCoNomofLXGJooXSXoXobErXAXkoXoo)')
xo('xxxoo')

# another solution
#def xo(s):
#    s = s.lower()
#    return s.count('x') == s.count('o')
#
