import keyword
import builtins

x = input()

if x[0].isdigit():
    print(False)
elif not x.islower():
    print(False)
elif x.count("_") > 1:
    print(False)
elif not x.isidentifier():
    print(False)
elif x in dir(builtins) or keyword.iskeyword(x):
    print(False)
else:
    print(True)