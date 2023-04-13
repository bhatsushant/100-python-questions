# Q37. Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).

# Method 1 - using a traditional for loop
def printTuple_1():
    myList = []
    for i in range(1, 21):
        myList.append(i ** 2)
    return tuple(myList)

print(printTuple_1());

# Method 2 - using list comprehension
def printTuple_2():
    return tuple([ i** 2 for i in range(1,21)])

print(printTuple_2());