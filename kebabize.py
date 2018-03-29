def kebabize(string):
    output = ''
    for i in string:
        if i.isalpha():
            if i.isupper():
                output += '-' + i.lower()
            else:
                output += i
    if len(output)>0:
        return output if output[0] != '-' else output[1:]
    else:
        return ''
print(kebabize('myCamelCasedString'))
print(kebabize('myCamelHas3Humps'))
print(kebabize('SOS'))
