# SOLUTION OF PROBLEM NO.2
list_n = input().split(" ")
number = ""  # contains all numbers in jumbled form
for i in list_n: number += i  # numbers simply concatenated
list_n = list(number)  # list of digits
list_n.sort(reverse=True)
number = ""  # contains the largest number possible
for i in list_n: number += i  # sorted digits simply concatenated
print(number)
