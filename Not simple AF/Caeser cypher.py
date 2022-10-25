# Шифр Цезаря заключается в замене каждого символа входной строки на символ, находящийся на несколько позиций левее или правее его в алфавите.

# Для всех символов сдвиг один и тот же. Сдвиг циклический, т.е. если к последнему символу алфавита применить единичный сдвиг, то он заменится на первый символ, и наоборот.

# Напишите программу, которая шифрует текст шифром Цезаря.


# First solution (Didn't work properly)

# def caeser_cypher(offset, string):
#     result = ''
#     alphabet = ' abcdefghijklmnopqrstuvwxyz'
#     for i in string:
#         pos = alphabet.find(i)
#         if i in alphabet:
#             result += alphabet[pos + offset]
#         else:
#             result += i
#     return result

# print('"' + caeser_cypher(int(input()), str(input()).lower()) + '"')

#Second Solution

def caeser_cypher(offset, string):
    abc = ' abcdefghijklmnopqrstuvwxyz'
    res = [abc[(abc.index(i) + offset) % len(abc)] for i in string]
    return res
    
print('Result: "' + ''.join(caeser_cypher(int(input()), input().strip())) + '"')