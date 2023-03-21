'''
Q20. Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Suppose the following input is supplied to the program:

7
Then, the output should be:

0
7
14
'''

class Divisible:
    def by_seven(self, n):
        for i in range(0, n+1):
            if i % 7 == 0:
                yield i

user_input = int(input("Please enter a number: "))
number = Divisible().by_seven(user_input)
for i in number:
    print(i)