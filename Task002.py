#Создайте программу для игры с конфетами человек против человека.

#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

#a) 2 игрока
import random
num = 2021
player = random.randint(0, 2)
while num > 0:
    if player == 0:
        n = int(input('Игрок А, возьмите конфеты от 1 до 28 шт: '))
        if 0< n <= 28:
            num -= n
            if num == 0:
                print('Поздравляю! Игрок А, Вы выйграли и забираете все 2021 конфету!!!')
            else:
                player = 1
                print(f'Остаток конфет: {num}')
        else:
            print('Выедите правильное количество конфет')
    else:
        n = int(input('Игрок В, возьмите конфеты от 1 до 28 шт: '))
        if 0< n <= 28:
            num -= n
            if num == 0:
                print('Поздравляю! Игрок B, Вы выйграли и забираете все 2021 конфету!!!')
            else:
                player = 0
                print(f'Остаток конфет: {num}')
        else:
            print('Выедите правильное количество конфет')

#b) Подумайте как сделать бота с ""интеллектом""
import random
num = 202
player = random.randint(0, 2)
while num > 0:
    if player == 0:
        t = int(num/29)
        n = num - (29 * t)
        if n == 0:
            n = 28
        print(f'Бот, берет {n} шт')
        num -= n
        if num == 0:
            print('Поздравляю!Бот, Вы выйграли и забираете все 2021 конфету!!!')
        else:
            player = 1
            print(f'Остаток конфет: {num}')
    else:
        n = int(input('Игрок Игрок, возьмите конфеты от 1 до 28 шт: '))
        if 0< n <= 28:
            num -= n
            if num == 0:
                print('Поздравляю! Игрок, Вы выйграли и забираете все 2021 конфету!!!')
            else:
                player = 0
                print(f'Остаток конфет: {num}')
        else:
            print('Выедите правильное количество конфет')