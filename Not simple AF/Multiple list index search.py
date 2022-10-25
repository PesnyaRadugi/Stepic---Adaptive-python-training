# Напишите программу, которая принимает на вход список чисел и число, после чего выводит все позиции, на которых это число встречается в переданном списке.

# Позиции в списке нумеруются с нуля.
# Если число x не найдено в списке, нужно вывести строку "None" (без кавычек, с большой буквы).


# First solution
# Used string for result, instead of list, cause of course compiler's conditions

# def find_id(x, n):
#     id = ''
#     for i in range(len(x)):
#         if x[i] == n:
#             id += str(i) + " "

#     if len(id) > 0:
#         return id
#     else:
#         return 'None'

# print(find_id(list(map(int,input().split())), int(input())))

# Second Solution

x = input().split()
n = input()

if not n in x:
    print("None")
else:
    for i in range(len(x)):
        if x[i] == n:
            print(i)