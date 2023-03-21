'''
Q14. Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

Suppose the following input is supplied to the program:

Hello world!
Then, the output should be:

UPPER CASE 1
LOWER CASE 9
'''

# Method 1: using upper(), lower() and isalnum() functions
user_input = input("Please enter a sentence: ").split()
user_string = ','.join(user_input)
upper_case = [i for i in user_string if i == i.upper() and i.isalnum()]
lower_case = [i for i in user_string if i == i.lower() and i.isalnum()]
print(f"UPPER CASE {len(upper_case)}")
print(f"LOWER CASE {len(lower_case)}")

# Method 2: using isupper() and islower() methods
user_input = input("Please enter a sentence: ")
upper, lower = 0,0
for i in user_input:
    upper += i.isupper()
    lower += i.islower()
print("UPPER CASE {} \nLOWER CASE {}".format(upper, lower))