'''
Q8. Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

Suppose the following input is supplied to the program:

without,hello,bag,world
Then, the output should be:

bag,hello,without,world
'''

# Method 1: Using the sorted() function
user_input = input("Please enter a sequence: ").split(',')
print(",".join(sorted(user_input)))

# Method 2: Using the list.sort() function
user_input = input("Please enter a sequence: ").split(',')
user_input.sort()
print(",".join(user_input))