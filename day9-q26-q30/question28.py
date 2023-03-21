# Q28. Define a function that can receive two integer numbers in string form and compute their sum and then print it in console.

a, b = input("Please provide two comma separated integers: ").split(',')

def str_to_int(x, y):
    print(int(x) + int(y))

print(str_to_int(a,b))