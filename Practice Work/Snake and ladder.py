import random
import sys

def dice():
    return random.randint(1,6)

player1 = input("Enter the player-1: ")
player2 = input("Enter the player-2: ")

player1_score = 0
player2_score = 0

winning_point = 100

snakes = {99:23, 81:17, 72:64, 67:14, 56:32, 48:12, 34:3, 25:19, 16:9}
ladders = {7:19, 18:77, 23:85, 31:44, 45:71, 54:63, 61:94, 78:88, 89:93}

while player1_score < winning_point and player2_score < winning_point:
    # Player 1 turn
    player1_turn = dice()
    player1_score += player1_turn
    if player1_score in snakes:
        player1_score = snakes[player1_score]
        print(f"\n{player1}'s turn:\nDice: {player1_turn}\n---Snake bite---\nBoard position: {player1_score}")
    elif player1_score in ladders:
        player1_score = ladders[player1_score]
        print(f"\n{player1}'s turn:\nDice: {player1_turn}\n*****Ladder*****\nBoard position: {player1_score}")
    else:
        print(f"\n{player1}'s turn:\nDice: {player1_turn}\nBoard position: {player1_score}")

    if player1_score >= winning_point:
        break

    # Player 2 turn
    player2_turn = dice()
    player2_score += player2_turn
    if player2_score in snakes:
        player2_score = snakes[player2_score]
        print(f"\n{player2}'s turn:\nDice: {player2_turn}\n---Snake bite---\nBoard position: {player2_score}")
    elif player2_score in ladders:
        player2_score = ladders[player2_score]
        print(f"\n{player2}'s turn:\nDice: {player2_turn}\n*****Ladder*****\nBoard position: {player2_score}")
    else:
        print(f"\n{player2}'s turn:\nDice: {player2_turn}\nBoard position: {player2_score}")

else:
    if player1_score > player2_score:
        print(f"\n\n{player1} Win the game!!!!!!")
    elif player1_score == player2_score:
        print(f"\n\nTie!!!!!!")
    else:
        print(f"\n\n{player2} Win the game!!!!!!")