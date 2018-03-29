def find_short(s):
    words = s.split()
    word = list()
    for i in words:
        x = len(i)
        word.append(x)
    return min(word)
     # l: shortest word length


print(find_short("bitcoin take over the world maybe who knows perhaps"))
