# Q33. Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

def squarelist_1(n):
    square = []
    for i in range(1, n+1):
        square.append(i ** 2)
    return square

print(squarelist_1(20))

def squarelist_2(n):
    square = [i ** 2 for i in range(0, n+1)]
    return square

print(squarelist_2(40))