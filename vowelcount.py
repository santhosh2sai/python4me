#vowel count
s='azcbobobegghakl'
count = 0
vowels = "aeiou"
for letter in s:
    if letter in vowels:
        count += 1
print(count)
