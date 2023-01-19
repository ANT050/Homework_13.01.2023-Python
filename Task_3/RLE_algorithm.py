# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc

from pathlib import Path

user_input = input("Введите строку: ")

# Функция сжатия строки
def compress_string(user_input):
    compress = ""
    counter = 1
    for i in range(len(user_input) - 1):
        if user_input[i] == user_input[i + 1]:
            counter += 1
        else:
            compress += str(counter) + user_input[i]
            counter = 1
    compress += str(counter) + user_input[-1]
    return compress

# Функция распаковки строки
def unpacking_string(user_input):
    uncompress = ""
    i = 0
    while i < len(user_input):
        counter = ""
        while i < len(user_input) and user_input[i].isdigit():
            counter += user_input[i]
            i += 1
        counter = int(counter) if counter != "" else 1
        uncompress += user_input[i] * counter
        i += 1
    return uncompress

folder_path = Path.cwd() / "Task_3"
try:
    if user_input == unpacking_string(user_input):
        with open(folder_path / 'unpacking.txt', 'w', encoding='utf-8') as file_1, open(folder_path / 'compress.txt', 'w', encoding='utf-8') as file_2:
            file_1.write(user_input)
            file_2.write(f'{user_input} --> {compress_string(user_input)}')
        print(f'{user_input} --> {compress_string(user_input)}')
    else:
        with open(folder_path / 'compress.txt', 'w', encoding='utf-8') as file_1, open(folder_path / 'unpacking.txt', 'w', encoding='utf-8') as file_2:
            file_1.write(user_input)
            file_2.write(f'{user_input} --> {unpacking_string(user_input)}')
        print(f'{user_input} --> {unpacking_string(user_input)}')
except FileNotFoundError:
    print('Файл или директория не существует')
