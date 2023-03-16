'''
Q10. Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

Suppose the following input is supplied to the program:

hello world and practice makes perfect and hello world again
Then, the output should be:

again and hello makes perfect practice world
'''

# Method 1: Using dictionary
user_input = sorted(list(dict.fromkeys(input("Please enter a sentence: ").split())))
print(" ".join(user_input))


# Method 2: Using set
user_input = " ".join(sorted(list(set(input("Please enter a sentence: ").split()))))
print(user_input)