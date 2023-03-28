# Q31. Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.

# Method 1 - using traditional for loop
def printdict_1(n):
    square = {}
    for i in range(1,n+1):
        square[i] = i ** 2
    
    return square

print(printdict_1(20))

# Method 2 - using dictionary comprehension

def printdict_2(n):
    square = {i: i** 2 for i in range(1, n+1)}
    return square

print(printdict_2(40))