# Classic Rock Paper scissors game
# Single player
import random

def play():
    player = input("Type s for scissors, r for rock or p for paper: ")
    player = player.lower()
    if player == "r" or player == "p" or player == "s":
        computer = random.choice(["r","p","s"])
        if computer == player:
            return "Draw! \nPlay Again..."
        if ((computer == "r" and player == "p") or  (computer == "p" and player == "s") or  (computer == "s" and player == "r")):
            return "Congratulations! You Won.."
        return "Sorry, You Lose. Better luck next time."
    else:
        print("Invalid input. Follow the instruction")
        return play()

print(play())
