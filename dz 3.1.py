n1 = int(input())
n2 = int(input())
dia = input()
if dia == '+' :
    print(n1 + n2)
elif dia == '-' :
    print(n1 - n2)
elif dia == '*' :
    print(n1 * n2)
elif dia == '/' :
    if  n2 == 0:
        print("0 не може бути дільником")
    else:
        print(n1 / n2)


