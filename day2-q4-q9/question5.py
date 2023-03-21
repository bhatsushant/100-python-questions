'''
Q5. Define a class which has at least two methods:

getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''

class StringClass:
    def __init__(self):
        self.user_input = ""
    def getString(self):
        self.user_input = input("Please enter your input: ")
    def printString(self):
        print(self.user_input.upper())

my_class = StringClass()
my_class.getString()
my_class.printString()