'''
Q7. Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i _ j.*

Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5

Then, the output of the program should be:

[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
'''

# [
#     [0, 0, 0, 0, 0], i = 0, j = 1 - 4 , i*j
#     [0, 1, 2, 3, 4], i = 1, j = 1 - 4 , i*j
#     [0, 2, 4, 6, 8]  i = 2, j = 1 - 4 , i*j
#  ]

user_input = input("Please enter the value of X,Y: ").split(',')
rows = int(user_input[0])
cols = int(user_input[1])
twoD = [[i*j for i in range(cols)] for j in range(rows)]
print(twoD)
