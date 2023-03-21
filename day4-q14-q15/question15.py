'''
Q15. Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

Suppose the following input is supplied to the program:

9
Then, the output should be:

11106
'''

# Method 1: using a list. A little longer and tedious solution
# try:
formula = []
a = input("Please enter a digit: ")
i = 1
while i < 5:
    formula.append(i*a)
    i += 1
formula = [int(i) for i in formula]
print(sum(formula))
# except ValueError:
    # a = input("The value does not seem to be numeric. Please enter a digit: ")
    # pass

# print('9'+'9')

# Method 2: using a temporary string
a = input("Please enter a digit: ")
total, temp = 0, str()
for i in range(4):
    temp += a           # concatinating 'a' to 'temp'
    total += int(temp)     # converting 'temp' to int and adding to total
print(total)