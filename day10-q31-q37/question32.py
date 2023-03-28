# Q32. Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.

# Method 1 - using traditional for loop
def squaredict_1(n):
    square = dict()
    for i in range(1, n+1):
        square[i] = i ** 2
    return square.keys()

print(squaredict_1(20))

# Method 2 - using dictionary comprehension
def squaredict_2(n):
    square = {i:i ** 2 for i in range(0, n+1)}
    return square.keys()

print(squaredict_2(40))