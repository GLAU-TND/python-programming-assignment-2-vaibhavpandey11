# SOLUTION OF PROBLEM NO.2
list_n = input().split(" ")
for i in range(0, len(list_n)):
    for j in range(0, len(list_n)-1):
        if len(list_n[j]) == len(list_n[j + 1]):  # if two numbers have equal number of digits
            list_n[j], list_n[j+1] = str(max(int(list_n[j]), int(list_n[j+1]))), str(min(int(list_n[j]), int(list_n[j+1])))
        elif len(list_n[j]) > len(list_n[j + 1]):  # if first number has greater number of digits than the second one
            for k in range(0, len(list_n[j + 1])):
                if int(list_n[j][k]) <= int(list_n[j + 1][k]):
                    list_n[j], list_n[j + 1] = list_n[j + 1], list_n[j]
                    break
        elif len(list_n[j]) < len(list_n[j + 1]):  # if first number has lesser number of digits than the second one
            for k in range(0, len(list_n[j])):
                if int(list_n[j][k]) <= int(list_n[j + 1][k]):
                    list_n[j], list_n[j + 1] = list_n[j + 1], list_n[j]
                    break
print(''.join(list_n))
