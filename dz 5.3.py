import string
s = input()
words = s.split()
example = []
for i in words:
    new_word = ""
    for c in i:
        if c not in string.punctuation:
            new_word += c
    example.append(new_word.capitalize())
result = "#" + "".join(example)
result = result[ :140]
print(result)