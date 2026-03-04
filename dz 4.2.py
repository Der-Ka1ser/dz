example = [4,0,6,2,0,8,5,9]
if not example:
    result = 0
else:
    result = sum(example[::2]) * example[-1]
print(result)