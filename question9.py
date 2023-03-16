'''
Q9. Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

Suppose the following input is supplied to the program:

Hello world
Practice makes perfect
Then, the output should be:

HELLO WORLD
PRACTICE MAKES PERFECT
'''

# Method 1: Exit when line is empty
print("Please enter your input. Press Ctrl + C to run program after providing input: \n")
user_input = []
while True:
        line = input()
        if not line:
                break
        user_input.append(line)
str = ",".join(user_input)
result = str.replace(",", "\n")
print(result.upper())

# # Method 2: Exit when user specifically exits the program
print("Please enter your input. Press Ctrl + Z to run program after providing input: \n")
user_input = []
while True:
    try:
        line = input()
    except KeyboardInterrupt:
        break
    user_input.append(line)
str = ",".join(user_input)
result = str.replace(",", "\n")
print(result.upper())
