# Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом

import random

field = [" " for x in range(9)]

# Функция создания игрового поля
def playing_field():
    print("\033[94m+---+---+---+")
    for i in range(3):
        for j in range(3):
            if field[i*3+j] == "X":
                print("\033[94m| \033[33mX\033[0m ", end="")
            elif field[i*3+j] == "O":
                print("\033[94m| \033[37mO\033[0m ", end="")
            else:
                print("\033[94m|   ", end="")
        print("\033[94m|")
        print("\033[94m+---+---+---+\033[0m")


# Функция проверки выигрышной позиции
def check_win():
    win_condition = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_condition:
        if field[each[0]] == field[each[1]] == field[each[2]] != " ":
            return field[each[0]]
    return None

# Функция самой игры
def main():
    counter = 0
    win = None
    first_player = random.choice(["X", "O"])
    print("Перый игрок - это: {}".format(first_player))
    while not win:
        playing_field()
        if counter % 2 == 0 and first_player == "X" or counter % 2 == 1 and first_player == "O":
            player = "X"
        else:
            player = "O"
        choice = input("{} ходит, выбери от 1 до 9: ".format(player))
        if not choice.isnumeric() or int(choice) not in range(1,10):
            print("Неверный ввод, пожалуйста, выберите число от 1 до 9!")
            continue
        choice = int(choice)
        if field[choice - 1] == " ":
            field[choice - 1] = player
            counter += 1
        else:
            print("Это клетка занята, повторите попытку")
            continue
        win = check_win()
        if counter >= 9:
            print("\033[91mНичья")
            break
    if win:
        playing_field()
        print("\033[91m{} выиграл!".format(win))


main()
