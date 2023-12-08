#! /usr/bin/env python y
"""cette ligne permet de rendre le script exécutable directement depuis la ligne de commande sans avoir à spécifier l'interpréteur Python à utiliser, et elle utilise l'interpréteur Python trouvé dans le chemin d'accès, facilitant ainsi la portabilité du script sur différents systèmes.
"""
import random

# Roll function
def roll():
    return random.randint(1, 6)

# Number of players input
while True:
    players_input = input("Enter the number of players (2-4): ")
    if players_input.isdigit():
        players = int(players_input)
        if 2 <= players <= 4:
            break
        else:
            print("The number of players should be between 2 and 4.")
    else:
        print("Invalid input. Please try again.")
print("Number of players:", players)

max_score = 50
players_score = [0] * players  # Create a list containing the score of each player

while max(players_score) < max_score:
    for player_idx in range(players):
        print("\nPlayer", player_idx + 1, "'s turn has just started!\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y/n)? ").lower()
            if should_roll != "y":
                break

            value = roll()

            if value == 1:
                current_score = 0
                print("You rolled a 1! Turn over.")
                print("Your score is:", current_score)
                break
            else:
                current_score += value
                print("You rolled a:", value)
                print("Your score is:", current_score)

        players_score[player_idx] += current_score
        print("Your total score is:", players_score[player_idx])

    # Determine the winning player
    max_score = max(players_score)
    winning_index = players_score.index(max_score)
    print("The winning player is Player", winning_index + 1, "with a score of:", max_score)

