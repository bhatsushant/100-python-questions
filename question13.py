'''
Q13. Write a program that accepts a sentence and calculate the number of letters and digits.

Suppose the following input is supplied to the program:

hello world! 123
Then, the output should be:

LETTERS 10
DIGITS 3
'''

# Method 1: using traditional for loop
user_input = ' '.join(input("Please enter a sentence with letters and digits: ")).split()
letters = 0
digits = 0
for i in user_input:
    if i.isnumeric():
        digits += 1
    elif i.isalnum():
        letters += 1
print(f"LETTERS {letters}")
print(f"DIGITS {digits}")

# Method 2: using list comprehension
user_input = ' '.join(input("Please enter a sentence with letters and digits: ")).split()
letters = [i for i in user_input if i.isalnum()]
digits = [i for i in user_input if i.isnumeric()]
print(f"LETTERS {len(letters)}")
print(f"DIGITS {len(digits)}")