import math

board = [' '] * 9
AI = 'O'
HUMAN = 'X'

def print_board():
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("---+---+---")
    print()

def print_positions():
    print("Positions are as follow:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 \n")

def check_winner(player):
    win = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    return any(all(board[i] == player for i in combo) for combo in win)

def is_full():
    return all(cell != ' ' for cell in board)

def minimax(depth, alpha, beta, is_maximizing):
    if check_winner(AI):
        return 10 - depth
    if check_winner(HUMAN):
        return depth - 10
    if is_full():
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = AI
                score = minimax(depth + 1, alpha, beta, False)
                board[i] = ' '
                best = max(best, score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = HUMAN
                score = minimax(depth + 1, alpha, beta, True)
                board[i] = ' '
                best = min(best, score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
        return best

def best_move():
    best_val = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = AI
            val = minimax(0, -math.inf, math.inf, False)
            board[i] = ' '
            if val > best_val:
                best_val = val
                move = i
    return move

# Game loop
print("Welcome to Tic-Tac-Toe with AI")
print("Computer (O) goes first.")
print_positions()
board[best_move()] = AI

while True:
    print_board()
    try:
        user = int(input("Enter your move (1-9): ")) - 1
        if board[user] != ' ':
            print("Invalid move. Cell already taken.")
            continue
    except:
        print("Please enter a valid number (1–9).")
        continue

    board[user] = HUMAN

    if check_winner(HUMAN):
        print_board()
        print("🎉 You win!")
        break

    if is_full():
        print_board()
        print("🤝 Draw!")
        break

    ai = best_move()
    board[ai] = AI

    if check_winner(AI):
        print_board()
        print("💻 AI wins!")
        break

    if is_full():
        print_board()
        print("🤝 Draw!")
        break
