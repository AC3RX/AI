import chess
import chess.engine
import math

# Emoji Representation of Chess Pieces
PIECE_EMOJIS = {
    chess.PAWN: "♙",
    chess.KNIGHT: "♞",
    chess.BISHOP: "♝",
    chess.ROOK: "♜",
    chess.QUEEN: "♛",
    chess.KING: "♚",
    "white": "⚪",
    "black": "⚫"
}

# Evaluation weights (no changes to this)
PIECE_VALUES = {
    chess.PAWN: 100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 20000
}

def evaluate_board(board):
    """
    A basic evaluation function using material count.
    Add positional bonuses for advanced versions.
    """
    if board.is_checkmate():
        if board.turn:
            return -math.inf  # Black wins
        else:
            return math.inf   # White wins
    if board.is_stalemate() or board.is_insufficient_material():
        return 0  # Draw

    score = 0
    for piece_type in PIECE_VALUES:
        score += len(board.pieces(piece_type, chess.WHITE)) * PIECE_VALUES[piece_type]
        score -= len(board.pieces(piece_type, chess.BLACK)) * PIECE_VALUES[piece_type]
    return score

def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board), None

    best_move = None
    if maximizing_player:
        max_eval = -math.inf
        for move in board.legal_moves:
            board.push(move)
            eval, _ = minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = math.inf
        for move in board.legal_moves:
            board.push(move)
            eval, _ = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

def find_best_move(board, depth=3):
    """
    Finds the best move using minimax algorithm with alpha-beta pruning.
    """
    _, move = minimax(board, depth, -math.inf, math.inf, board.turn)
    return move

def print_board(board):
    """
    Prints the chessboard with emojis instead of standard letters.
    The pieces are spaced out for better readability.
    """
    board_str = str(board)
    board_lines = board_str.splitlines()
    emoji_board = []
    
    for line in board_lines:
        emoji_line = ''
        for char in line:
            if char == 'p': emoji_line += PIECE_EMOJIS[chess.PAWN].lower() + "  "
            elif char == 'P': emoji_line += PIECE_EMOJIS[chess.PAWN] + "  "
            elif char == 'n': emoji_line += PIECE_EMOJIS[chess.KNIGHT].lower() + "  "
            elif char == 'N': emoji_line += PIECE_EMOJIS[chess.KNIGHT] + "  "
            elif char == 'b': emoji_line += PIECE_EMOJIS[chess.BISHOP].lower() + "  "
            elif char == 'B': emoji_line += PIECE_EMOJIS[chess.BISHOP] + "  "
            elif char == 'r': emoji_line += PIECE_EMOJIS[chess.ROOK].lower() + "  "
            elif char == 'R': emoji_line += PIECE_EMOJIS[chess.ROOK] + "  "
            elif char == 'q': emoji_line += PIECE_EMOJIS[chess.QUEEN].lower() + "  "
            elif char == 'Q': emoji_line += PIECE_EMOJIS[chess.QUEEN] + "  "
            elif char == 'k': emoji_line += PIECE_EMOJIS[chess.KING].lower() + "  "
            elif char == 'K': emoji_line += PIECE_EMOJIS[chess.KING] + "  "
            elif char == '.': emoji_line += "⬛  "  # Empty square
            
        emoji_board.append(emoji_line.strip())
    
    return "\n".join(emoji_board)

# Play a game against the bot
def play_vs_bot():
    board = chess.Board()
    while not board.is_game_over():
        print("\nCurrent Board:")
        print(print_board(board))  # Print the board with emojis
        
        if board.turn:
            # Human (White)
            user_move = input("Your move (e.g., e2e4): ")
            try:
                move = chess.Move.from_uci(user_move)
                if move in board.legal_moves:
                    board.push(move)
                else:
                    print("Illegal move.")
            except:
                print("Invalid move format.")
        else:
            # Bot (Black)
            print("Bot thinking...")
            move = find_best_move(board, depth=3)
            if move:
                print(f"Bot plays: {move}")
                board.push(move)
            else:
                print("Bot resigns.")
                break

    print("\nGame Over!")
    print("Final Board:")
    print(print_board(board))
    print(f"Result: {board.result()}")

if __name__ == "__main__":
    play_vs_bot()
