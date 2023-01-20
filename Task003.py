#Создайте программу для игры в ""Крестики-нолики"".
def Print(array, rows):
    for i in range(rows):
        print(*array[i])
def Final(array, rows):
    if ((array[0][0] == array[0][1] == array[0][2] == 'x')
        or (array[0][0] == array[0][1] == array[0][2] == '0')
        or (array[1][0] == array[1][1] == array[1][2] == 'x')
        or (array[1][0] == array[1][1] == array[1][2] == '0')
        or (array[2][0] == array[2][1] == array[2][2] == 'x')
        or (array[2][0] == array[2][1] == array[2][2] == '0')
        or (array[0][0] == array[1][0] == array[2][0] == 'x')
        or (array[0][0] == array[1][0] == array[2][0] == '0')
        or (array[0][1] == array[1][1] == array[2][1] == 'x')
        or (array[0][1] == array[1][1] == array[2][1] == '0')
        or (array[0][2] == array[1][2] == array[2][2] == 'x')
        or (array[0][2] == array[1][2] == array[2][2] == '0')
        or (array[0][0] == array[1][1] == array[2][2] == 'x')
        or (array[0][0] == array[1][1] == array[2][2] == '0')):
        return '1'

game = [['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']]
rows = len(game[0])
columns = rows
player = 0
for i in range(rows * columns):
    temp = input('Введите номер ячейки: ').split()
    j = int(temp[0])
    k = int(temp[1])
    if 0 <= j < rows and 0 <= k < columns:
        if game[j][k] == '0' or game[j][k] == 'x':
            print('введите другой номер ячейки, эта ячейка ужа заполнена')
            i += 1
        else:
            if player == 0:
                game[j][k] = 'x'   
                Print(game, rows)
                if Final(game, rows) == '1':
                    print('Поздравлюя! Игрок номер 1, Вы выйграл!!!')
                    break
                player = 1

            else:
                game[j][k] = '0'   
                Print(game, rows)
                if Final(game, rows) == '1':
                    print('Поздравлюя! Игрок номер 2, Вы выйграл!!!')
                    break
                player = 0
    else:
        i += 1
