# Напишите программу, которая принимает на вход список целых чисел и выводит на экран значения, которые повторяются в нём более одного раза.

# Для решения задачи может пригодиться метод sort списка.

def duplicates(lst):
    lst.sort()
    lst_res = []
    for i in range(len(lst)):
        if len(lst) == 1:
            return lst_res
        elif lst[i] == lst[i - 1]:
            if lst[i] not in lst_res:
                lst_res.append(lst[i])
    return lst_res

print(' '.join(duplicates(input().split())))