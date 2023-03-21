# Q30. Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.

def maxstr(a, b):
    if len(a) > len(b):
        print(a)
    elif len(a) == len(b):
        print(a)
        print(b)
    else:
        print(b)

print(maxstr('sush','sush'))
print(maxstr('sush','sushant'))
print(maxstr('sushi','bhat'))