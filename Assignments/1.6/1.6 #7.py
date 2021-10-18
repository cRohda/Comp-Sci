from random import randint  # imports randint for choosing a random integer

round_number = 0  # sets round number to 0 to keep track of round number
player_1_score = 0  # sets player 1 score to 0 to keep track of player 1s score
player_2_score = 0  # sets player 2 score to 0 to keep track of player 2s score

while(True):  # Loop will repeat until it is broken with break
    round_number += 1  # Add 1 to the round number
    print("")
    print("Starting round #" + str(round_number) + "...")
    print("───────────────")
    player_1_input = input("Player 1, press enter to roll the dice. ")
    print("───────────────")
    # Creating two dice and rolling them three times (each roll is 2 dice). Records the value of the rolls
    roll1, roll2, roll3 = randint(2, 12), randint(2, 12), randint(2, 12)
    if roll1 == round_number:  # check if the first roll is the round number
        player_1_score = player_1_score + roll1  # adds the points the player 1's score
    if roll2 == round_number:  # check if the second roll is the round number
        player_1_score = player_1_score + roll2  # adds the points the player 1's score
    if roll3 == round_number:  # check if the third roll is the round number
        player_1_score = player_1_score + roll3  # adds the points the player 1's score
    print("Your total score is now " + str(player_1_score) + ".")
    print("───────────────")
    player_2_input = input("Player 2, press enter to roll the dice. ")
    print("───────────────")
    # Creating two dice and rolling them three times (each roll is 2 dice). Records the value of the rolls
    p2roll1, p2roll2, p2roll3 = randint(2, 12), randint(2, 12), randint(2, 12)
    if p2roll1 == round_number:  # check if the first roll is the round number
        player_2_score = player_2_score + p2roll1  # adds the points the player 2's score
    if p2roll2 == round_number:  # check if the second roll is the round number
        player_2_score = player_2_score + p2roll2  # adds the points the player 1's score
    if p2roll3 == round_number:  # check if the third roll is the round number
        player_2_score = player_2_score + p2roll3  # adds the points the player 1's score
    print("Your total score is now " + str(player_2_score) + ".")
    print("───────────────")
    if round_number == 12:  # Checking for final round
        if player_1_score > player_2_score:  # If P1 has a higher score than P2
            print("")
            print("Player 1 has won the game with a total of " + str(player_1_score) + " points!")  # Print that P1 wins
            break  # End the loop
        elif player_2_score > player_1_score:  # If P2 has a higher score than P1
            print("")
            print("Player 2 has won the game with a total of " + str(player_2_score) + " points!")  # Print that P2 wins
            break  # End the loop
        else:  # if neither have more
            print("")
            print("The game was a draw.")
            break
