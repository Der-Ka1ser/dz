number = int(input())
1000<= number <= 9999
one = number // 1000
two = (number % 1000) // 100
three = (number % 100) // 10
four = number % 10
print(one)
print(two)
print(three)
print(four)