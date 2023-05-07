import random
# Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. 
# Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8

def Task1():
    print("задача 1:")
    numbers = [random.randint(1, 10) for _ in range(10)]
    print("Исходный список: ", numbers)
    numbers = list(filter(lambda x:x > 5, numbers))
    print("Элементы больше 5: ", numbers)
Task1()

# Задача 2. Дан список случайных чисел. 
# Создайте список, в который попадают числа, описывающие случайную возрастающую последовательность. 
# Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [2, 7] или [4, 6, 7] и т.д.

def Task2():
    print("\nЗадача 2:")
    numbers = [random.randint(1, 20) for _ in range(20)]
    print("Исходный список: ", numbers)
    max_num = max(numbers)
    accending_list = list()
    for num in numbers:
        if not accending_list and num != max_num or accending_list and num > accending_list[-1]:
            accending_list.append(num)
    print("восходящая последовательность: ", accending_list)
Task2()

# Задача 3. Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают
# Список уникальных элементов
# [1, 4, 2, 3, 6, 7]

def Task3():
    print("\nЗадача 3:")
    numbers = [random.randint(1, 10) for _ in range(20)]
    counts = {}
    print("Исходный список: ", numbers)
    for num in numbers:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1
    total_matches = sum(filter(lambda x: x > 1, counts.values()))
    numbers_set = set(numbers)
    print(f"В исходной последовательности элеменов совпадает: {total_matches}.\nУникальные элементы: {numbers_set}")
Task3()

# Задача 4*. (Необязательная). Создайте игру в крестики-нолики.
print("\nЗадача 4:")
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_valid_move(board, row, col):
    return board[row][col] == " "

def check_winner(board, symbol):
    for row in board:
        if all([s == symbol for s in row]):
            return True
    for col in range(3):
        if all([board[row][col] == symbol for row in range(3)]):
            return True
    if all([board[i][i] == symbol for i in range(3)]) or all([board[i][2 - i] == symbol for i in range(3)]):
        return True
    return False

def make_move(board, row, col, symbol):
    board[row][col] = symbol

def game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        try:
            row, col = map(int, input(f"Игрок {player}, сделайте ход (ряд, столбец): ").split())
        except ValueError:
            print("Неверный ввод. Введите ряд и столбец, разделенные пробелом.")
            continue
        if not (0 <= row < 3 and 0 <= col < 3) or not is_valid_move(board, row, col):
            print("Неверный ход. Попробуйте ещё раз.")
            continue

        make_move(board, row, col, player)

        if check_winner(board, player):
            print_board(board)
            print(f"Игрок {player} выиграл!")
            break

        if all([not is_valid_move(board, row, col) for row in range(3) for col in range(3)]):
            print_board(board)
            print("Ничья!")
            break

        player = "O" if player == "X" else "X"

game()
