import math


def print_board(board):
    for row in board:
        print(" ".join(row))
    print()


def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != '-':
            return row[0]

    # Check columns
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '-':
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '-':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '-':
        return board[0][2]

    return None
def get_empty_cells(board):
    cells = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '-':
                cells.append((i, j))
    return cells


def minimax(board, depth, is_maximizing):
    scores = {
        'X': 1,
        'O': -1,
        'Tie': 0
    }

    winner = check_winner(board)
    if winner:
        return scores[winner]

    empty_cells = get_empty_cells(board)

    if len(empty_cells) == 0:
        return scores['Tie']

    if is_maximizing:
        best_score = -math.inf
        for cell in empty_cells:
            board[cell[0]][cell[1]] = 'X'
            score = minimax(board, depth + 1, False)
            board[cell[0]][cell[1]] = '-'
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for cell in empty_cells:
            board[cell[0]][cell[1]] = 'O'
            score = minimax(board, depth + 1, True)
            board[cell[0]][cell[1]] = '-'
            best_score = min(score, best_score)
        return best_score


def get_best_move(board):
    best_score = -math.inf
    best_move = None
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '-':
                board[i][j] = 'X'
                score = minimax(board, 0, False)
                board[i][j] = '-'
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move


def play_game():
    board = [['-' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    while True:
        print_board(board)

        if current_player == 'X':
            row, col = get_best_move(board)
            board[row][col] = 'X'
        else:
            while True:
                try:
                    row = int(input("Enter row (0, 1, or 2): "))
                    col = int(input("Enter column (0, 1, or 2): "))
                    if board[row][col] == '-':
                        board[row][col] = 'O'
                        break
                    else:
                        print("That cell is already taken. Try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == 'Tie':
                print("It's a tie!")
            else:
                print(f"{winner} wins!")
            break

        current_player = 'X' if current_player == 'O' else 'O'

    if __name__=="__main__":
        print("Welcome to Tic Toc Toe!")
    play_game()
