lst = [1,4,56,21,23,7,9]
if len(lst) == 0:
    result = [[], []]
else:
    mid = (len(lst) + 1) // 2
    first = lst[:mid]
    second = lst[mid:]
    result = [first, second]
print(result)