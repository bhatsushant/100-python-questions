'''
Q19. You are required to write a program to sort the (name, age, score) tuples by ascending order where name is string, age and score are numbers. The tuples are input by console. The sort criteria is:

1: Sort based on name
2: Then sort based on age
3: Then sort by score
The priority is that name > age > score.

If the following tuples are given as input to the program:

Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:

[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
'''

# Method 1
print("Please provide a sequence of tuples:")
input_list = []
while True:
    try:
        user_input = input()
        if not user_input:
            break
    except KeyboardInterrupt:
        break
    input_list.append(user_input)
result = sorted([tuple(str(i).split(",")) for i in input_list], key= lambda a: (a[0], a[1], a[2]))
print(result)


# Method 2
print("Please provide a sequence of tuples:")
input_list = []
while True:
    try:
        user_input = input().split(",")
        if not user_input[0]:
            break
    except KeyboardInterrupt:
        break
    input_list.append(tuple(user_input))
result = sorted(input_list, key = lambda a: (a[0], a[1], a[2]))
print(result)