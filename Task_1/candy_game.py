# 1. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.

# a) Добавьте игру против бота

# b) Подумайте как наделить бота 'интеллектом'

import random

# Функция для многопользовательской игры
def multiplayer_game(num_players, candies):

    first_player = random.randint(1, num_players)
    print(f"\n\033[94mВсего {candies} на столе\033[0m")
    print(f"\nИгрок {first_player} ходит первым.")

    while candies > 0:
        move = input(
            f"\nИгрок {first_player}, сколько конфет вы хотите взять? ")
        if not move.isnumeric() or int(move) <= 0:
            print("Неверный ввод, пожалуйста, введите число!")
            continue
        move = int(move)

        if move > 28:
            print(f"\nВы не можете взять больше 28 конфет, пожалуйста, попробуйте снова!")
            continue

        elif move > candies:
            print(
                f"\nВы не можете взять больше {candies} конфет, пожалуйста, попробуйте снова!")
            continue

        candies -= move
        print(f"\033[94mНа столе осталось {candies} конфет\033[0m")

        first_player = first_player % num_players+1

    if candies == 0:
        print(f"\033[91mИгрок {first_player-1} выиграл!")

# Функция для игры с ботом с легким уровнем сложности
def play_bot_simple(candies):

    players = random.randint(1, 2)
    print(f"\n\033[94mВсего {candies} на столе\033[0m")

    if players == 1:
        print("\n\033[93mТы ходишь первым\033[0m")
    else:
        print("\n\033[93mБот ходит первым\033[0m")

    while candies > 0:
        if players == 1:
            move = input("\nСколько конфет ты хочешь взять?")
            if not move.isnumeric() or int(move) <= 0:
                print("Неверный ввод, пожалуйста, введите число!")
                continue
            move = int(move)

            if move > 28:
                print(
                    f"\nВы не можете взять больше 28 конфет, пожалуйста, попробуйте снова!")
                continue

            elif move > candies:
                print(
                    f"\nВы не можете взять больше {candies} конфет, пожалуйста, попробуйте снова!")
                continue

            candies -= move
            print(f"\033[94mНа столе осталось {candies} конфет\033[0m")

            if candies == 0:
                break
            players = 2

        else:
            bot_move = random.randint(1, 28)
            bot_move = min(bot_move, candies)
            print(f"\nБот взял {bot_move} конфет.")

            candies -= bot_move
            print(f"\033[94mНа столе осталось {candies} конфет\033[0m")

            if candies == 0:
                break
            players = 1

    if players == 1:
        print("\033[91mТы выиграл!")
    else:
        print("\033[91mБот выиграл!")

# Функция для игры с ботом со сложным уровнем сложности
def play_bot_complex(candies):

    players = random.randint(1, 2)
    print(f"\n\033[94mВсего {candies} на столе\033[0m")

    if players == 1:
        print("\n\033[93mТы ходишь первым\033[0m")
    else:
        print("\n\033[93mБот ходит первым\033[0m")

    while candies > 0:
        if players == 1:
            move = input("\nСколько конфет ты хочешь взять?")
            if not move.isnumeric() or int(move) <= 0:
                print("Неверный ввод, пожалуйста, введите число!")
                continue
            move = int(move)

            if move > 28:
                print(
                    f"\nВы не можете взять больше 28 конфет, пожалуйста, попробуйте снова!")
                continue

            elif move > candies:
                print(
                    f"\nВы не можете взять больше {candies} конфет, пожалуйста, попробуйте снова!")
                continue

            candies -= move
            print(f"\033[94mНа столе осталось {candies} конфет\033[0m")

            if candies == 0:
                break
            players = 2

        else:
            bot_move = candies % 29 if candies % 29 != 0 else random.randint(
                1, 28)
            print(f"\nБот взял {bot_move} конфет.")
            candies -= bot_move
            print(f"\033[94mНа столе осталось {candies} конфет\033[0m")

            if candies == 0:
                break
            players = 1

    if players == 1:
        print("\033[91mТы выиграл!")
    else:
        print("\033[91mБот выиграл!")

# Основной код
candies = random.randint(50, 200)

game_mode = input(
    "\nВы хотите играть против других игроков или бота, где p(player) - игрок(и), b(bot) - bot?: (p/b): ")
while game_mode.lower() != "p" and game_mode.lower() != "b":
    print("\nНеверный ввод, пожалуйста, введите 'p', чтобы играть с другими игроками, или 'b', чтобы играть с ботом!")
    game_mode = input(
        "Вы хотите играть против других игроков или бота, где p(player) - игрок(и), b(bot) - bot?: (p/b): ")

if game_mode.lower() == "p":
    num_players = input("Сколько игроков будет играть?: ")
    while not num_players.isnumeric() or int(num_players) <= 0:
        print("Неверный ввод, пожалуйста, повторите заново!")
        num_players = input("Сколько игроков будет играть?: ")
    multiplayer_game(int(num_players), candies)
else:
    difficulty_level = input(
        "Пожалуйста, выберите уровень сложности s(simple) - простой, c(complex) - сложный: (s/c): ")
    while difficulty_level.lower() != "s" and difficulty_level.lower() != "c":
        print("Неверный ввод, пожалуйста, повторите заново!")
        difficulty_level = input(
            "Пожалуйста, выберите уровень сложности s(simple) - простой, c(complex) - сложный: (s/c): ")
    if difficulty_level.lower() == "s":
        play_bot_simple(candies)
    elif difficulty_level.lower() == "c":
        play_bot_complex(candies)
