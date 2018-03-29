def kebab(string):
    # your code here
    ans = ''
    for i in string:
        if i.isalpha():
            if i.isupper():
                ans += '-' + i.lower()
            else:
                ans += i
    if len(ans) > 0:
        return ans if ans[0] != '-' else ans[1:]
    else:
        return ''

# Test Cases

print(kebab('myCamelCasedString'))
print(kebab('myCamelHas3Humps'))
print(kebab('SOS'))
