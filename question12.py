'''
Q12. Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line.
'''

number_list = []
for i in range(1000, 3001):
    digits = [int(i) for i in str(i)]
    divisible = all(i%2 == 0 for i in digits)
    if divisible:
        number = int(''.join([str(i) for i in digits]))
        number_list.append(number)
print(','.join([str(i) for i in number_list]))