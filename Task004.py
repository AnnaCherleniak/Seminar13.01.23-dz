#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
with open('task13-4.txt', 'r', encoding='utf-8') as file:
    data = file.read()
res_dict ={}
count = 1
for i in range(len(data)):
    if i == len(data) - 1:
        if data[i] == data[i-1]:
            j = data[i]
            res_dict[j] = count
        else:
            j = data[i]
            res_dict[j] = 1
    else:
        if data[i] == data[i+1]:
            count += 1
        else:
            j = data[i]
            res_dict[j] = count
            count = 1
with open('res.txt', 'a', encoding='utf-8') as file:
    file.write('\n')
    for i, j in res_dict.items():
        file.write(str(j))
        file.write(i)
some_list = ''
for i in res_dict.keys():
    count = int(res_dict[i])
    while count > 0:
        some_list += i
        count -= 1
with open('res.txt', 'a', encoding='utf-8') as file:
    file.write('\n')
    file.write(some_list)