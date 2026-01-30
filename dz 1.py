number = int(input())
one = (number % 10)*10000
two = ((number % 100) // 10)*1000
three = ((number % 1000) // 100)*100
four = ((number // 1000) % 10) * 10
five = number // 10000
print(one + two + three + four + five)


