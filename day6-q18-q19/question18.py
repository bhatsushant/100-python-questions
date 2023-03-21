'''
Q18. A website requires the users to input username and password to register. Write a program to check the validity of password input by users.

Following are the criteria for checking the password:

At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 6
Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.

Example

If the following passwords are given as input to the program:

ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:

ABd1234@1
'''

# Method 1: using traditional for loop
def isLow(string):
    for i in string:
        if 'a' <= i and i <= 'z':
            return True
    return False

def isUp(string):
    for i in string:
        if 'A' <= i and i <= 'Z':
            return True
    return False

def isNum(string):
    for i in string:
        if '0' <= i and i <= '9':
            return True
    return False

def isSpecial(string):
    for i in string:
        if i == '$' or i == '#' or i == '@':
            return True
    return False

def checkLength(string):
    if len(string) >= 6 and len(string) <= 12:
        return True
    return False

user_input = input("Please provide a sequence of comma separated paswords: ").split(",")
result = []
for i in user_input:
    if checkLength(i) and isLow(i) and isUp(user_input) and isNum(i) and isSpecial(i):
        result.append(i)
print(','.join(result))


# Method 2: using filter() method and a counter
def validate(string):
    count = (len(string) >= 6 and len(string) <= 12)
    for i in string:
        if i.isupper():
            count += 1
            break
    for i in string:
        if i.islower():
            count += 1
            break
    for i in string:
        if i.isnumeric():
            count += 1
            break
    for i in string:
        if i == '@' or i == '#' or i == '$':
            count += 1
            break
    return count == 5

user_input = input("Please provide a sequence of comma separated paswords: ").split(",")
result = filter(validate, user_input)
print(",".join(result))
