import random
import sys

"""
The main of the program is to make a simple rock, paper and scissors game
"""
print("LAUNCHING GAME......")
print("Rock, Paper, Scissors")

# Tally the number of wins, losses and drawed games
wins = 0
losses = 0
draws = 0

# Main loop that runs the game
while True:
    print(f"{wins} Wins, {losses} Losses, {draws} Draws")
    # This inner loop controls the user input
    while True:
        print("Enter 'q' to quit game....")
        player_move = input("Enter your move: r - Rock\np - Paper\ns - Scissors")
        if player_move == 'q':
            print("Quitting Game....")
            sys.exit()  # Allows user to quit program
        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break  # Breaks the user of the input loop
        else:
            print("Invalid Move! Enter r for Rock, p for Paper and s for "
                  "Scissors.")

    # Displays the what the player chooses
    if player_move == 'r':
        print("Rock versus....")
    elif player_move == 'p':
        print("Paper versus....")
    elif player_move == 's':
        print("Scissors versus....")

    # Set up the computer's move
    random_number = random.randint(1, 3)
    if random_number == 1:
        computer_move = 'r'
        print("Rock")
    elif random_number == 2:
        computer_move = 'p'
        print("Paper")
    elif random_number == 3:
        computer_move = 's'
        print("Scissors")

    # Display and record the wins, losses, and draws
    if player_move == computer_move:
        print('This round is a tie!')
        draws += 1
    elif player_move == 'r' and computer_move == 'p':
        print("Paper wraps Rock :( You lost this round!")
        losses += 1
    elif player_move == 'r' and computer_move == 's':
        print("Rock breaks Scissors:) You win this round!")
        wins += 1
    elif player_move == 'p' and computer_move == 'r':
        print("Paper wraps Rock :) You win this round")
        wins += 1
    elif player_move == 'p' and computer_move == 's':
        print("Scissors cuts Paper :( You lose this round!")
        losses += 1
    elif player_move == 's' and computer_move == 'r':
        print("Rock breaks Scissors :( You lose this round!")
        losses += 1
    elif player_move == 's' and computer_move == 'p':
        print("Scissors cuts Paper :) You win this round!")
        wins += 1
