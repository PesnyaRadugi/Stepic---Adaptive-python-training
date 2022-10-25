# Напишите программу, которая проверяет, являются ли два введённых слова анаграммами.
# Программа должна вывести True в случае, если введённые слова являются анаграммами, и False в остальных случаях.


# First solution

# def is_anagramm(str1, str2):
#     list1 = list(str1)
#     list2 = list(str2)
    
#     list1.sort()
#     list2.sort()
    
#     if len(list1) == len(list2):
#         for i in range(len(list1)):
#             if list1[i] == list2[i]:
#                 pass
#             else:
#                 return False
#         return True
#     else:
#         return False
    
# print(is_anagramm(str(input().lower()), str(input().lower())))


# Second Solution
print(sorted(input().lower())==sorted(input().lower()))