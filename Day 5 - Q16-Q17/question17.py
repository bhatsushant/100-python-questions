'''
Q17. Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:

"
D 100
W 200
"

- D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:

"
D 300
D 300
W 200
D 100
"

Then, the output should be:

500
'''

# Method 1
print("Please enter your input. Press Ctrl + C to run program after providing input: \n")
transaction = []
total = 0
while True:
    try:
        user_input = input()
        if not user_input:
            break
    except KeyboardInterrupt:
        break
    transaction.append(user_input)
for i in transaction:
    amount = int("".join([str(int(j)) for j in i.split() if j.isdigit()]))
    if 'd' in i or 'D' in i:
        total += amount
    elif 'w' in i or 'W' in i:
        total -= amount
    else:
        total += 0
print(total)


# Method 2: using the map() function
print("Please enter your input. Press Ctrl + C to run program after providing input: \n")
total = 0
while True:
    try:
        user_input = input().split()
        if not user_input:
            break
    except KeyboardInterrupt:
        break
    transaction, amount = map(str, user_input)

    if 'd' in transaction or 'D' in transaction:
        total += int(amount)
    elif 'w' in transaction or 'W' in transaction:
        total -= int(amount)
    else:
        total += 0
print(total)
