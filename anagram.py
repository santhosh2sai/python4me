#Anagram
def is_anagram(test, original):
    c = ''.join(sorted(test.lower()))
    d = ''.join(sorted(original.lower()))
    print(c)
    print(d)
    if c == d :
        return True
    else:
        return False
print(is_anagram('Creative', 'Reactive'))
