# Q26. Define a function which can compute the sum of two numbers.

# Method 1
def sum_of_n(a,b):
    return a + b

print(sum_of_n(4,4))

# Method 2 - using lambda function
sum_of_n = lambda a,b: a + b
print(sum_of_n(2,2))