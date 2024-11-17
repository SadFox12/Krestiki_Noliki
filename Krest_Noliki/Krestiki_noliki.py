import random


# Инициализация игрового поля
def print_board(board):
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("--+---+--")


# Проверка на победителя
def check_winner(board, player):
    # Проверка строк, столбцов и диагоналей
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # строки
            return True
        if all([board[j][i] == player for j in range(3)]):  # столбцы
            return True
    if all([board[i][i] == player for i in range(3)]):  # диагональ 1
        return True
    if all([board[i][2 - i] == player for i in range(3)]):  # диагональ 2
        return True
    return False


# Проверка на ничью
def is_draw(board):
    return all(cell != " " for row in board for cell in row)


# Алгоритм Минимакс
def minimax(board, depth, is_maximizing, alpha, beta):
    # Символы игроков
    human = "X"
    computer = "O"

    # Базовые условия: проверка победителя
    if check_winner(board, human):
        return -10 + depth
    if check_winner(board, computer):
        return 10 - depth
    if is_draw(board):
        return 0

    # Для игрока-компьютера (максимизация)
    if is_maximizing:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = computer
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    # Для игрока-человека (минимизация)
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = human
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval


# Выбор хода ИИ
def best_move(board):
    best_val = float('-inf')
    move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"  # Символ компьютера
                move_val = minimax(board, 0, False, float('-inf'), float('inf'))
                board[i][j] = " "
                if move_val > best_val:
                    best_val = move_val
                    move = (i, j)

    return move


# Основная логика игры
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print_board(board)
    while True:
        # Ход игрока
        row, col = map(int, input("Введите строку и столбец (0-2) для X: ").split())
        if board[row][col] != " ":
            print("Ячейка занята, попробуйте снова.")
            continue
        board[row][col] = "X"

        if check_winner(board, "X"):
            print_board(board)
            print("Вы победили!")
            break
        if is_draw(board):
            print_board(board)
            print("Ничья!")
            break

        # Ход ИИ
        print("Ход ИИ:")
        move = best_move(board)
        board[move[0]][move[1]] = "O"
        print_board(board)

        if check_winner(board, "O"):
            print("Компьютер победил!")
            break
        if is_draw(board):
            print("Ничья!")
            break


# Запуск игры
if __name__ == "__main__":
    play_game()
