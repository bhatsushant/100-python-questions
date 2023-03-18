'''
Q16. Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. >Suppose the following input is supplied to the program:

1,2,3,4,5,6,7,8,9
Then, the output should be:

1,9,25,49,81
'''
# Method 1
user_input = input("Please enter a sequence: ").split(",")
numbers = [(int(i) ** 2) for i in user_input if int(i)%2 != 0]
print(','.join([str(i) for i in numbers]))

# Method 2 
user_input = input("Please enter a sequence: ").split(",")
numbers = [str(pow(int(i),2)) for i in user_input if int(i)%2]
print(",".join(numbers))