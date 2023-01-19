#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
with open('task13-1.txt', 'r', encoding='utf-8') as file:
    text_list = file.read().split()
some_list = 'абв'
for e in some_list:
    text_list = list(filter(lambda word: e not in word, text_list))
print(text_list)
with open('res.txt', 'a', encoding='utf-8') as file:
    file.write('\n')
    file.write(str(*text_list))