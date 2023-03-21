# Q27. Define a function that can convert a integer into a string and print it in console.

# Method 1
def int_to_str(input):
    print(type(str(input)))
    return str(input)

print(int_to_str(5))

# Method 2 - using lambda function
int_to_str = lambda n: str(n)
print(int_to_str(7))