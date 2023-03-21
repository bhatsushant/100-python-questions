'''
Q22. Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.

Suppose the following input is supplied to the program:

New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:

2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
'''

user_input = input("Please provide a sentence to calculate frequency:\n").split()
words = dict(sorted([[i,0] for i in user_input]))

for i in user_input:
    if i in words:
        words[i] += 1
result = str(words)
print(result)

