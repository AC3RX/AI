import math


PLAYER = "X"  
AI = "O"      
EMPTY = " "    


def print_board(board):
    print("\n---------")
    for i, row in enumerate(board):
        print("|", " | ".join(row), "|")  
        print("---------")
    print("\n")
    print("Positions (1-9) to select: ")
    print("1 | 2 | 3")
    print("4 | 5 | 6")
    print("7 | 8 | 9")


def is_game_over(board):
   
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return True
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return True
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return True
    
  
    if all(board[row][col] != EMPTY for row in range(3) for col in range(3)):
        return "Draw"
    
    return False 


def get_possible_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == EMPTY]


def minimax(board, depth, maximizing_player):
   
    result = is_game_over(board)
    if result == "Draw":
        return 0
    if result == True:
        return -1 if maximizing_player else 1

    if maximizing_player:  
        best_score = -math.inf
        best_move = None
        for move in get_possible_moves(board):
            r, c = move
            board[r][c] = AI
            score = minimax(board, depth + 1, False)
            board[r][c] = EMPTY
            if score > best_score:
                best_score = score
                best_move = move
        if depth == 0:
            return best_move  
        return best_score

    else:  
        best_score = math.inf
        for move in get_possible_moves(board):
            r, c = move
            board[r][c] = PLAYER
            score = minimax(board, depth + 1, True)
            board[r][c] = EMPTY
            if score < best_score:
                best_score = score
        return best_score


def ai_move(board):
    return minimax(board, 0, True) 


def number_to_position(number):
    return (number - 1) // 3, (number - 1) % 3


def play_game():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    
    while True:
        print_board(board)

       
        print("Your move (X):")
        try:
            choice = int(input("Enter a number (1-9) to place your X: "))
            if choice < 1 or choice > 9:
                print("Invalid input! Please select a number between 1 and 9.")
                continue
            row, col = number_to_position(choice)
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER
            else:
                print("That spot is already taken! Try again.")
                continue
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        if is_game_over(board):
            print_board(board)
            print("Game Over! You win!" if is_game_over(board) == 1 else "Game Over! It's a draw!")
            break

        s
        print("AI's move (O):")
        move = ai_move(board)
        board[move[0]][move[1]] = AI

        if is_game_over(board):
            print_board(board)
            print("Game Over! AI wins!" if is_game_over(board) == -1 else "Game Over! It's a draw!")
            break

if __name__ == "__main__":
    play_game()
    