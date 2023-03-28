# Q34. Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.

# Method 1 - using traditional for loop
def squarelist_1(n):
    square = []
    for i in range(1, n+1):
        square.append(i ** 2)
    return square[:5]

print(squarelist_1(20))

# Method 1 - using list comprehension
def squarelist_2(n):
    square = [i ** 2 for i in range(1, n+1)]
    return square[:5]

print(squarelist_2(40))