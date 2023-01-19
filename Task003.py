#Создайте программу для игры в ""Крестики-нолики"".
game = [['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']]
rows = 3
colomns = 3
def Print(array, rows):
    for i in range(rows):
        print(*array[i])
#Print(game, rows)
player = 0
for i in range(rows * colomns):
    temp = input().split()
    j = int(temp[0]) - 1
    k = int(temp[1]) - 1
    if player == 0:
        game[j][k] = 'x'   
        Print(game, rows)
        player = 1
    else:
        game[j][k] = '0'   
        Print(game, rows)
        player = 0

