#Correct the mistakes of the character recognition software
def correct(string):
    replacement = {"0": "O","5": "S","1": "I"}
    return "".join([replacement.get(c,c) for c in string ])
print(correct("L0ND0N"))
