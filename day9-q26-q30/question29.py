# Q29. Define a function that can accept two strings as input and concatenate them and then print it in console.

a, b = input("Please provide two comma separated strings: ").split(',')

def str_to_int(x, y):
    print(x + y)

print(str_to_int(a,b))