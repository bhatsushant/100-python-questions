'''
Q11. Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.

Example:

0100,0011,1010,1001
Then the output should be:

1010
'''

# Method 1: using for loop and bin() function
user_input = input("Please enter your binary sequence: ").split(',')
values = []
result = []
for i in user_input:
    values.append(int(i, 2))
div = [i for i in values if i%5 == 0]
for i in div:
    result.append(bin(i)[2:])
print(','.join(result))


# Method 2: Shorter way
user_input = input("Please enter your binary sequence: ").split(',')
result = [i for i in user_input if int(i,2)%5 == 0]
print(','.join(result))