import random

choices = ['rock', 'paper', 'scissors']
player_history = {'rock': 0, 'paper': 0, 'scissors': 0}

def beats(move):
    return {
        'rock': 'paper',
        'paper': 'scissors',
        'scissors': 'rock'
    }[move]

def ai_move():
    if sum(player_history.values()) == 0:
        return random.choice(choices)
    predicted_move = max(player_history, key=player_history.get)
    return beats(predicted_move)

while True:
    player = input("Enter your move (rock, paper, scissors or quit): ").lower()
    
    if player == 'quit':
        print("Thanks for playing!")
        break
    if player not in choices:
        print("Invalid move. Try again.")
        continue

    player_history[player] += 1
    ai = ai_move()
    
    print(f"You played {player}, AI played {ai}.")

    if player == ai:
        print("It's a tie!")
    elif beats(player) == ai:
        print("You lose!")
    else:
        print("You win!")

    print("-" * 30)
