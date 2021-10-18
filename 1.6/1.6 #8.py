from random import randint
from time import sleep  # Imports for, Random, Delay (rolling dice), and exit (ending code on demand)
from sys import exit
firstTotal = 0
secondTotal = 0  # Variable setting scores to 0
thirdTotal = 0

print('Each player will roll for the order')
input('\nPlayer 1, press enter to roll for your spot')
P1pos = randint(3,18)
print(f'Player 1 Rolled a {P1pos}')
input('\nPlayer 2, press enter to roll for your spot')   # Rolls to determine position
P2pos = randint(3,18)
print(f'Player 2 Rolled a {P2pos}')
input('\nPlayer 3, press enter to roll for your spot')
P3pos = randint(3,18)
print(f'Player 3 Rolled a {P3pos}')

sleep(0.1)
tie = 1

while tie == 1:
    if P1pos == P2pos:
        print('\nThere is a tie, P1 and P2 roll again.')
        input('\nPlayer 1, press enter to roll for your spot')
        P1pos = randint(3, 18)
        print(f'Player 1 Rolled a {P1pos}')
        input('\nPlayer 2, press enter to roll for your spot')
        P2pos = randint(3, 18)
        print(f'Player 2 Rolled a {P2pos}')
        break
    elif P2pos == P3pos:
        print('\nThere is a tie, P2 and P3 roll again.')
        input('\nPlayer 2, press enter to roll for your spot')
        P2pos = randint(3, 18)
        print(f'Player 2 Rolled a {P2pos}')
        input('\nPlayer 3, press enter to roll for your spot')
        P3pos = randint(3, 18)
        print(f'Player 3 Rolled a {P3pos}')
        break
    elif P3pos == P1pos:                                   # Determining if there is a tie and rolling again if there is
        print('\nThere is a tie, P1 and P3 roll again.')
        input('\nPlayer 1, press enter to roll for your spot')
        P1pos = randint(3, 18)
        print(f'Player 1 Rolled a {P1pos}')
        input('\nPlayer 3, press enter to roll for your spot')
        P3pos = randint(3, 18)
        print(f'Player 3 Rolled a {P3pos}')
        break
    elif P1pos == P2pos and P1pos == P3pos:
        print('\nThere is a tie, everyone roll again')
        input('\nPlayer 1, press enter to roll for your spot')
        P1pos = randint(3, 18)
        print(f'Player 1 Rolled a {P1pos}')
        input('\nPlayer 2, press enter to roll for your spot')
        P2pos = randint(3, 18)
        print(f'Player 2 Rolled a {P2pos}')
        input('\nPlayer 3, press enter to roll for your spot')
        P3pos = randint(3, 18)
        print(f'Player 3 Rolled a {P3pos}')
        break
    else:
        tie = 0

if P1pos > P2pos and P1pos > P3pos:
    first = 'P1'
    if P2pos > P3pos:
        second = 'P2'
        third = 'P3'
    elif P3pos > P2pos:
        second = 'P3'
        third = 'P2'
    else:
        exit('Positioning Error Crash')
elif P2pos > P3pos and P2pos > P1pos:       # Making the order
    first = 'P2'
    if P1pos > P3pos:
        second = 'P1'
        third = 'P3'
    elif P3pos > P1pos:
        second = 'P3'
        third = 'P1'
    else:
        exit('Positioning Error Crash')
elif P3pos > P1pos and P3pos > P2pos:
    first = 'P3'
    if P1pos > P2pos:
        second = 'P1'
        third = 'P3'
    elif P2pos > P1pos:
        second = 'P2'
        third = 'P1'
    else:
        exit('Positioning Error Crash')
else:
    exit('Positioning Error Crash')

print('\nThe game will now begin\n')

Round = 0

while Round < 6:    # Loop for 6 rounds
    Round += 1
    roundScore = 0
    input(f'{first} press enter to roll your 5 die')
    die1, die2, die3, die4, die5, = randint(1,6), randint(1,6), randint(1,6), randint(1,6), randint(1,6)
    print('Rolling...')
    sleep(1)                  # Rolling the 5 dice and getting score, repeats 3 times in the loop, once for each player.
    print(f'{first} rolled a {die1}, {die2}, {die3}, {die4}, {die5}.')  # Because print statements are slightly
    if die1 == 6 or die2 == 6 or die3 == 6 or die4 == 6 or die5 == 6:   # Different for each player
        print('Congratulations! You rolled your ship!')
        if die1 == 5 or die2 == 5 or die3 == 5 or die4 == 5 or die5 == 5:
            print('Congratulations! You rolled your captain!')
            if die1 == 4 or die2 == 4 or die3 == 4 or die4 == 4 or die5 == 4:
                print('Congratulations! You rolled your crew!')
                roundScore = die1 + die2 + die3 + die4 + die5 - 6 - 5 - 4
                yn1 = input(f'Your current score is {roundScore}, would you like to re-roll? (y/n): ')
                if yn1.lower() == 'y':
                    die1, die2 = randint(1,6), randint(1,6)
                    print('Rolling...')
                    sleep(1)
                    print(f'{first} rolled a {die1}, {die2}.')
                    roundScore = die1 + die2
                    yn1 = input(f'Your new score is {roundScore}, would you like to re-roll? (y/n): ')
                    if yn1 == 'y':
                        die1, die2 = randint(1,6), randint(1,6)
                        print('Rolling...')
                        sleep(1)
                        print(f'{first} rolled a {die1}, {die2}.')
                        roundScore = die1 + die2            # Calculating the score for the player on this round
                        print(f'Your score for this round is: {roundScore}')
                    else:
                        pass
                else:
                    pass
            else:
                input(f'{first} press enter to roll your 3 remaining die')
                die1, die2, die3 = randint(1, 6), randint(1, 6), randint(1, 6)
                print('Rolling...')
                sleep(1)
                print(f'{first} rolled a {die1}, {die2}, {die3}, {die4}.')
                if die1 == 4 or die2 == 4 or die3 == 4:
                    print('Congratulations! You rolled your crew!')
                    roundScore = die1 + die2 + die3 - 4
                    yn1 = input(f'Your score is {roundScore}, would you like to re-roll? (y/n): ')
                    if yn1 == 'y':
                        die1, die2 = randint(1,6), randint(1,6)
                        print('Rolling...')
                        sleep(1)
                        print(f'{first} rolled a {die1}, {die2}.')
                        roundScore = die1 + die2
                        print(f'Your score for this round is: {roundScore}')
                    else:
                        pass
                else:
                    input(f'{first} press enter to roll your 3 remaining die')
                    die1, die2, die3 = randint(1, 6), randint(1, 6), randint(1, 6)
                    print('Rolling...')
                    sleep(1)
                    print(f'{first} rolled a {die1}, {die2}, {die3}.')
                    if die1 == 4 or die2 == 4 or die3 == 4:
                        roundScore = die1 + die2 + die3 - 4
                        print(f'Your score for the round was: {roundScore}')
                    else:
                        print('You did not score any points this round')
        else:
            input(f'{first} press enter to roll your 4 remaining die')
            die1, die2, die3, die4 = randint(1,6), randint(1,6), randint(1,6), randint(1,6)
            print('Rolling...')
            sleep(1)
            print(f'{first} rolled a {die1}, {die2}, {die3}, {die4}.')
            if die1 == 5 or die2 == 5 or die3 == 5 or die4 == 5:
                print('Congratulations, You rolled your captain')
                if die1 == 4 or die2 == 4 or die3 == 4 or die4 == 4:
                    print('Congratulations, You rolled your crew!')
                    roundScore = die1 + die2 + die3 + die4 - 5 - 4
                    yn1 = input(f'Your score for this round is {roundScore}, would you like to re-roll? (y/n):')
                    if yn1 == 'y':
                        die1, die2 = randint(1,6), randint(1,6)
                        print('Rolling...')
                        sleep(1)
                        print(f'{first} rolled a {die1}, {die2}.')
                        roundScore = die1 + die2
                        print(f'Your total for this round is: {roundScore}')
                    else:
                        pass
                else:
                    input('You Rolled you Captain! But not your crew, you have one roll remaining\n'
                          'Press enter to roll again')
                    die1, die2, die3 = randint(1,6), randint(1,6), randint(1,6)
                    print('Rolling...')
                    sleep(1)
                    print(f'{first} rolled a {die1}, {die2}, {die3}.')
                    if die1 == 4 or die2 == 4 or die3 == 4:
                        print('You rolled your crew!')
                        roundScore = die1 + die2 + die3 - 4
                        print(f'Your score for this round is: {roundScore}')
                    else:
                        print('You scored no points this round')
            else:
                input('You have one roll remaining, press enter to roll')
                die1, die2, die3, die4 = randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)
                print(f'You rolled a {die1}, {die2}, {die3}, {die4}')
                if die1 == 5 or die2 == 5 or die3 == 5 or die4 == 5:
                    print('Rolling...')
                    sleep(1)
                    print(f'{first} rolled a {die1}, {die2}, {die3}, {die4}.')
                    if die1 == 4 or die2 == 4 or die3 == 4 or die4 == 4:
                        print(f'Your score for the round is: {roundScore}')
                    else:
                        print('You scored no points this round')
                else:
                    print('You scored no points this round')  # Utter disappointment for the player

    else:
        print('You did not successfully roll your ship')
        input(f'{first} press enter to roll your 5 die')
        die1, die2, die3, die4, die5, = randint(1,6), randint(1,6), randint(1,6), randint(1,6), randint(1,6)
        print('Rolling...')
        sleep(1)
        print(f'{first} rolled a {die1}, {die2}, {die3}, {die4}, {die5}.')
        if die1 == 6 or die2 == 6 or die3 == 6 or die4 == 6 or die5 == 6:
            print('Congratulations, You rolled your ship!')
            if die1 == 5 or die2 == 5 or die3 == 5 or die4 == 5 or die5 == 5:
                print('Congratulations, You rolled your captain')
                if die1 == 4 or die2 == 4 or die3 == 4 or die4 == 4 or die5 == 4:
                    print('Congratulations, You rolled your crew!')
                    roundScore = die1 + die2 + die3 + die4 + die5 - 6 - 5 - 4
                    yn1 = input(f'Your score is {roundScore}, would you like to roll again? (y/n): ')
                    if yn1 == 'y':
                        die1, die2 = randint(1,6), randint(1,6)
                        print('Rolling...')
                        sleep(1)
                        print(f'{first} rolled a {die1}, {die2}.')
                        roundScore = die1 + die2
                        print(f'Your score for the round is {roundScore}')
                    else:
                        pass
                else:
                    input('Press enter to roll your 3 remaining die')
                    die1, die2, die3 = randint(1,6), randint(1,6), randint(1,6)
                    print('Rolling...')
                    sleep(1)
                    print(f'{first} rolled a {die1}, {die2}, {die3}.')
                    if die1 == 4 or die2 == 4 or die3 == 4:
                        roundScore = die1 + die2 + die3 - 4
                        print(f'Congratulations, you rolled your crew. Your score for the round is {roundScore}')
                    else:
                        print('You did not score any points this round')
            else:
                input('Press enter to roll your 4 remaining die')
                die1, die2, die3, die4 = randint(1,6), randint(1,6), randint(1,6), randint(1,6)
                print('Rolling...')
                sleep(1)
                print(f'{first} rolled a {die1}, {die2}, {die3}, {die4}.')
                if die1 == 5 or die2 == 5 or die3 == 5 or die4 == 5:
                    if die1 == 4 or die2 == 4 or die3 == 4 or die4 == 4:
                        roundScore = die1 + die2 + die3 + die4 - 5 - 4
                        print(f'Congratulations you rolled your Captain and Crew,')
                        print(f'your score for the round is {roundScore}')
                    else:
                        print('You scored no points this round')
                else:
                    print('You scored no points this round')
        else:
            input('Press enter to roll your 5 remaining die')
            die1, die2, die3, die4, die5, = randint(1,6), randint(1,6), randint(1,6), randint(1,6), randint(1,6)
            print('Rolling...')
            sleep(1)
            print(f'{first} rolled a {die1}, {die2}, {die3}, {die4}, {die5}.')
            if die1 == 6 or die2 == 6 or die3 == 6 or die4 == 6 or die5 == 6:
                if die1 == 5 or die2 == 5 or die3 == 5 or die4 == 5 or die5 == 5:
                    if die1 == 4 or die2 == 4 or die3 == 4 or die4 == 4 or die5 == 4:
                        roundScore = die1 + die2 + die3 + die4 + die5 - 6 - 5 - 4
                        print('Congratulations, you rolled your ship, captain and crew!')
                        print(f'Your score for the round is {roundScore}')
                    else:
                        print('You scored no points this round')
                else:
                    print('You scored no points this round')
            else:
                print('You scored no points this round')
    firstTotal = firstTotal + roundScore  # Adding the score for the round to the total score
    print(f"{first}'s score is {firstTotal}\n\n\n\n")   # Note first ≠ P1, rather the first player in order

    # Code repeats as above but slightly different to have different player names and printed text, bulk of code
    # is the exact same.
    roundScore = 0
    input(f'{second} press enter to roll your 5 die')
    die1, die2, die3, die4, die5, = randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)
    print('Rolling...')
    sleep(1)
    print(f'{second} rolled a {die1}, {die2}, {die3}, {die4}, {die5}.')
    if die1 == 6 or die2 == 6 or die3 == 6 or die4 == 6 or die5 == 6:
        print('Congratulations! You rolled your ship!')
        if die1 == 5 or die2 == 5 or die3 == 5 or die4 == 5 or die5 == 5:
            print('Congratulations! You rolled your captain!')
            if die1 == 4 or die2 == 4 or die3 == 4 or die4 == 4 or die5 == 4:
                print('Congratulations! You rolled your crew!')
                roundScore = die1 + die2 + die3 + die4 + die5 - 6 - 5 - 4
                yn1 = input(f'Your current score is {roundScore}, would you like to re-roll? (y/n): ')
                if yn1.lower() == 'y':
                    die1, die2 = randint(1, 6), randint(1, 6)
                    print('Rolling...')
                    sleep(1)
                    print(f'{second} rolled a {die1}, {die2}.')
                    roundScore = die1 + die2
                    yn1 = input(f'Your new score is {roundScore}, would you like to re-roll? (y/n): ')
                    if yn1 == 'y':
                        die1, die2 = randint(1, 6), randint(1, 6)
                        print('Rolling...')
                        sleep(1)
                        print(f'{second} rolled a {die1}, {die2}.')
                        roundScore = die1 + die2
                        print(f'Your score for this round is: {roundScore}')
                    else:
                        pass
                else:
                    pass
            else:
                input(f'{second} press enter to roll your 3 remaining die')
                die1, die2, die3 = randint(1, 6), randint(1, 6), randint(1, 6)
                print('Rolling...')
                sleep(1)
                print(f'{second} rolled a {die1}, {die2}, {die3}, {die4}.')
                if die1 == 4 or die2 == 4 or die3 == 4:
                    print('Congratulations! You rolled your crew!')
                    roundScore = die1 + die2 + die3 - 4
                    yn1 = input(f'Your score is {roundScore}, would you like to re-roll? (y/n): ')
                    if yn1 == 'y':
                        die1, die2 = randint(1, 6), randint(1, 6)
                        print('Rolling...')
                        sleep(1)
                        print(f'{second} rolled a {die1}, {die2}.')
                        roundScore = die1 + die2
                        print(f'Your score for this round is: {roundScore}')
                    else:
                        pass
                else:
                    input(f'{second} press enter to roll your 3 remaining die')
                    die1, die2, die3 = randint(1, 6), randint(1, 6), randint(1, 6)
                    print('Rolling...')
                    sleep(1)
                    print(f'{second} rolled a {die1}, {die2}, {die3}.')
                    if die1 == 4 or die2 == 4 or die3 == 4:
                        roundScore = die1 + die2 + die3 - 4
                        print(f'Your score for the round was: {roundScore}')
                    else:
                        print('You did not score any points this round')
        else:
            input(f'{second} press enter to roll your 4 remaining die')
            die1, die2, die3, die4 = randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)
            print('Rolling...')
            sleep(1)
            print(f'{second} rolled a {die1}, {die2}, {die3}, {die4}.')
            if die1 == 5 or die2 == 5 or die3 == 5 or die4 == 5:
                print('Congratulations, You rolled your captain')
                if die1 == 4 or die2 == 4 or die3 == 4 or die4 == 4:
                    print('Congratulations, You rolled your crew!')
                    roundScore = die1 + die2 + die3 + die4 - 5 - 4
                    yn1 = input(f'Your score for this round is {roundScore}, would you like to re-roll? (y/n):')
                    if yn1 == 'y':
                        die1, die2 = randint(1, 6), randint(1, 6)
                        print('Rolling...')
                        sleep(1)
                        print(f'{second} rolled a {die1}, {die2}.')
                        roundScore = die1 + die2
                        print(f'Your total for this round is: {roundScore}')
                    else:
                        pass
                else:
                    input('You Rolled you Captain! But not your crew, you have one roll remaining\n'
                          'Press enter to roll again')
                    die1, die2, die3 = randint(1, 6), randint(1, 6), randint(1, 6)
                    print('Rolling...')
                    sleep(1)
                    print(f'{second} rolled a {die1}, {die2}, {die3}.')
                    if die1 == 4 or die2 == 4 or die3 == 4:
                        print('You rolled your crew!')
                        roundScore = die1 + die2 + die3 - 4
                        print(f'Your score for this round is: {roundScore}')
                    else:
                        print('You scored no points this round')
            else:
                input('You have one roll remaining, press enter to roll')
                die1, die2, die3, die4 = randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)
                print(f'You rolled a {die1}, {die2}, {die3}, {die4}')
                if die1 == 5 or die2 == 5 or die3 == 5 or die4 == 5:
                    print('Rolling...')
                    sleep(1)
                    print(f'{second} rolled a {die1}, {die2}, {die3}, {die4}.')
                    if die1 == 4 or die2 == 4 or die3 == 4 or die4 == 4:
                        print(f'Your score for the round is: {roundScore}')
                    else:
                        print('You scored no points this round')
                else:
                    print('You scored no points this round')

    else:
        print('You did not successfully roll your ship')
        input(f'{second} press enter to roll your 5 die')
        die1, die2, die3, die4, die5, = randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)
        print('Rolling...')
        sleep(1)
        print(f'{second} rolled a {die1}, {die2}, {die3}, {die4}, {die5}.')
        if die1 == 6 or die2 == 6 or die3 == 6 or die4 == 6 or die5 == 6:
            print('Congratulations, You rolled your ship!')
            if die1 == 5 or die2 == 5 or die3 == 5 or die4 == 5 or die5 == 5:
                print('Congratulations, You rolled your captain')
                if die1 == 4 or die2 == 4 or die3 == 4 or die4 == 4 or die5 == 4:
                    print('Congratulations, You rolled your crew!')
                    roundScore = die1 + die2 + die3 + die4 + die5 - 6 - 5 - 4
                    yn1 = input(f'Your score is {roundScore}, would you like to roll again? (y/n): ')
                    if yn1 == 'y':
                        die1, die2 = randint(1, 6), randint(1, 6)
                        print('Rolling...')
                        sleep(1)
                        print(f'{second} rolled a {die1}, {die2}.')
                        roundScore = die1 + die2
                        print(f'Your score for the round is {roundScore}')
                    else:
                        pass
                else:
                    input('Press enter to roll your 3 remaining die')
                    die1, die2, die3 = randint(1, 6), randint(1, 6), randint(1, 6)
                    print('Rolling...')
                    sleep(1)
                    print(f'{second} rolled a {die1}, {die2}, {die3}.')
                    if die1 == 4 or die2 == 4 or die3 == 4:
                        roundScore = die1 + die2 + die3 - 4
                        print(f'Congratulations, you rolled your crew. Your score for the round is {roundScore}')
                    else:
                        print('You did not score any points this round')
            else:
                input('Press enter to roll your 4 remaining die')
                die1, die2, die3, die4 = randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)
                print('Rolling...')
                sleep(1)
                print(f'{second} rolled a {die1}, {die2}, {die3}, {die4}.')
                if die1 == 5 or die2 == 5 or die3 == 5 or die4 == 5:
                    if die1 == 4 or die2 == 4 or die3 == 4 or die4 == 4:
                        roundScore = die1 + die2 + die3 + die4 - 5 - 4
                        print(f'Congratulations you rolled your Captain and Crew,')
                        print(f'your score for the round is {roundScore}')
                    else:
                        print('You scored no points this round')
                else:
                    print('You scored no points this round')
        else:
            input('Press enter to roll your 5 remaining die')
            die1, die2, die3, die4, die5, = randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)
            print('Rolling...')
            sleep(1)
            print(f'{second} rolled a {die1}, {die2}, {die3}, {die4}, {die5}.')
            if die1 == 6 or die2 == 6 or die3 == 6 or die4 == 6 or die5 == 6:
                if die1 == 5 or die2 == 5 or die3 == 5 or die4 == 5 or die5 == 5:
                    if die1 == 4 or die2 == 4 or die3 == 4 or die4 == 4 or die5 == 4:
                        roundScore = die1 + die2 + die3 + die4 + die5 - 6 - 5 - 4
                        print('Congratulations, you rolled your ship, captain and crew!')
                        print(f'Your score for the round is {roundScore}')
                    else:
                        print('You scored no points this round')
                else:
                    print('You scored no points this round')
            else:
                print('You scored no points this round')
    secondTotal = secondTotal + roundScore
    print(f"{second}'s score is {secondTotal}\n\n\n\n")

    # Code repeats as above but slightly different to have different player names and printed text, bulk of code
    # is the exact same
    roundScore = 0
    input(f'{third} press enter to roll your 5 die')
    die1, die2, die3, die4, die5, = randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)
    print('Rolling...')
    sleep(1)
    print(f'{third} rolled a {die1}, {die2}, {die3}, {die4}, {die5}.')
    if die1 == 6 or die2 == 6 or die3 == 6 or die4 == 6 or die5 == 6:
        print('Congratulations! You rolled your ship!')
        if die1 == 5 or die2 == 5 or die3 == 5 or die4 == 5 or die5 == 5:
            print('Congratulations! You rolled your captain!')
            if die1 == 4 or die2 == 4 or die3 == 4 or die4 == 4 or die5 == 4:
                print('Congratulations! You rolled your crew!')
                roundScore = die1 + die2 + die3 + die4 + die5 - 6 - 5 - 4
                yn1 = input(f'Your current score is {roundScore}, would you like to re-roll? (y/n): ')
                if yn1.lower() == 'y':
                    die1, die2 = randint(1, 6), randint(1, 6)
                    print('Rolling...')
                    sleep(1)
                    print(f'{third} rolled a {die1}, {die2}.')
                    roundScore = die1 + die2
                    yn1 = input(f'Your new score is {roundScore}, would you like to re-roll? (y/n): ')
                    if yn1 == 'y':
                        die1, die2 = randint(1, 6), randint(1, 6)
                        print('Rolling...')
                        sleep(1)
                        print(f'{third} rolled a {die1}, {die2}.')
                        roundScore = die1 + die2
                        print(f'Your score for this round is: {roundScore}')
                    else:
                        pass
                else:
                    pass
            else:
                input(f'{third} press enter to roll your 3 remaining die')
                die1, die2, die3 = randint(1, 6), randint(1, 6), randint(1, 6)
                print('Rolling...')
                sleep(1)
                print(f'{third} rolled a {die1}, {die2}, {die3}, {die4}.')
                if die1 == 4 or die2 == 4 or die3 == 4:
                    print('Congratulations! You rolled your crew!')
                    roundScore = die1 + die2 + die3 - 4
                    yn1 = input(f'Your score is {roundScore}, would you like to re-roll? (y/n): ')
                    if yn1 == 'y':
                        die1, die2 = randint(1, 6), randint(1, 6)
                        print('Rolling...')
                        sleep(1)
                        print(f'{third} rolled a {die1}, {die2}.')
                        roundScore = die1 + die2
                        print(f'Your score for this round is: {roundScore}')
                    else:
                        pass
                else:
                    input(f'{third} press enter to roll your 3 remaining die')
                    die1, die2, die3 = randint(1, 6), randint(1, 6), randint(1, 6)
                    print('Rolling...')
                    sleep(1)
                    print(f'{third} rolled a {die1}, {die2}, {die3}.')
                    if die1 == 4 or die2 == 4 or die3 == 4:
                        roundScore = die1 + die2 + die3 - 4
                        print(f'Your score for the round was: {roundScore}')
                    else:
                        print('You did not score any points this round')
        else:
            input(f'{third} press enter to roll your 4 remaining die')
            die1, die2, die3, die4 = randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)
            print('Rolling...')
            sleep(1)
            print(f'{third} rolled a {die1}, {die2}, {die3}, {die4}.')
            if die1 == 5 or die2 == 5 or die3 == 5 or die4 == 5:
                print('Congratulations, You rolled your captain')
                if die1 == 4 or die2 == 4 or die3 == 4 or die4 == 4:
                    print('Congratulations, You rolled your crew!')
                    roundScore = die1 + die2 + die3 + die4 - 5 - 4
                    yn1 = input(f'Your score for this round is {roundScore}, would you like to re-roll? (y/n):')
                    if yn1 == 'y':
                        die1, die2 = randint(1, 6), randint(1, 6)
                        print('Rolling...')
                        sleep(1)
                        print(f'{third} rolled a {die1}, {die2}.')
                        roundScore = die1 + die2
                        print(f'Your total for this round is: {roundScore}')
                    else:
                        pass
                else:
                    input('You Rolled you Captain! But not your crew, you have one roll remaining\n'
                          'Press enter to roll again')
                    die1, die2, die3 = randint(1, 6), randint(1, 6), randint(1, 6)
                    print('Rolling...')
                    sleep(1)
                    print(f'{third} rolled a {die1}, {die2}, {die3}.')
                    if die1 == 4 or die2 == 4 or die3 == 4:
                        print('You rolled your crew!')
                        roundScore = die1 + die2 + die3 - 4
                        print(f'Your score for this round is: {roundScore}')
                    else:
                        print('You scored no points this round')
            else:
                input('You have one roll remaining, press enter to roll')
                die1, die2, die3, die4 = randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)
                print(f'You rolled a {die1}, {die2}, {die3}, {die4}')
                if die1 == 5 or die2 == 5 or die3 == 5 or die4 == 5:
                    print('Rolling...')
                    sleep(1)
                    print(f'{third} rolled a {die1}, {die2}, {die3}, {die4}.')
                    if die1 == 4 or die2 == 4 or die3 == 4 or die4 == 4:
                        print(f'Your score for the round is: {roundScore}')
                    else:
                        print('You scored no points this round')
                else:
                    print('You scored no points this round')

    else:
        print('You did not successfully roll your ship')
        input(f'{third} press enter to roll your 5 die')
        die1, die2, die3, die4, die5, = randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)
        print('Rolling...')
        sleep(1)
        print(f'{third} rolled a {die1}, {die2}, {die3}, {die4}, {die5}.')
        if die1 == 6 or die2 == 6 or die3 == 6 or die4 == 6 or die5 == 6:
            print('Congratulations, You rolled your ship!')
            if die1 == 5 or die2 == 5 or die3 == 5 or die4 == 5 or die5 == 5:
                print('Congratulations, You rolled your captain')
                if die1 == 4 or die2 == 4 or die3 == 4 or die4 == 4 or die5 == 4:
                    print('Congratulations, You rolled your crew!')
                    roundScore = die1 + die2 + die3 + die4 + die5 - 6 - 5 - 4
                    yn1 = input(f'Your score is {roundScore}, would you like to roll again? (y/n): ')
                    if yn1 == 'y':
                        die1, die2 = randint(1, 6), randint(1, 6)
                        print('Rolling...')
                        sleep(1)
                        print(f'{third} rolled a {die1}, {die2}.')
                        roundScore = die1 + die2
                        print(f'Your score for the round is {roundScore}')
                    else:
                        pass
                else:
                    input('Press enter to roll your 3 remaining die')
                    die1, die2, die3 = randint(1, 6), randint(1, 6), randint(1, 6)
                    print('Rolling...')
                    sleep(1)
                    print(f'{third} rolled a {die1}, {die2}, {die3}.')
                    if die1 == 4 or die2 == 4 or die3 == 4:
                        roundScore = die1 + die2 + die3 - 4
                        print(f'Congratulations, you rolled your crew. Your score for the round is {roundScore}')
                    else:
                        print('You did not score any points this round')
            else:
                input('Press enter to roll your 4 remaining die')
                die1, die2, die3, die4 = randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)
                print('Rolling...')
                sleep(1)
                print(f'{third} rolled a {die1}, {die2}, {die3}, {die4}.')
                if die1 == 5 or die2 == 5 or die3 == 5 or die4 == 5:
                    if die1 == 4 or die2 == 4 or die3 == 4 or die4 == 4:
                        roundScore = die1 + die2 + die3 + die4 - 5 - 4
                        print(f'Congratulations you rolled your Captain and Crew,')
                        print(f'your score for the round is {roundScore}')
                    else:
                        print('You scored no points this round')
                else:
                    print('You scored no points this round')
        else:
            input('Press enter to roll your 5 remaining die')
            die1, die2, die3, die4, die5, = randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)
            print('Rolling...')
            sleep(1)
            print(f'{third} rolled a {die1}, {die2}, {die3}, {die4}, {die5}.')
            if die1 == 6 or die2 == 6 or die3 == 6 or die4 == 6 or die5 == 6:
                if die1 == 5 or die2 == 5 or die3 == 5 or die4 == 5 or die5 == 5:
                    if die1 == 4 or die2 == 4 or die3 == 4 or die4 == 4 or die5 == 4:
                        roundScore = die1 + die2 + die3 + die4 + die5 - 6 - 5 - 4
                        print('Congratulations, you rolled your ship, captain and crew!')
                        print(f'Your score for the round is {roundScore}')
                    else:
                        print('You scored no points this round')
                else:
                    print('You scored no points this round')
            else:
                print('You scored no points this round')
    thirdTotal = thirdTotal + roundScore
    print(f"{third}'s score is {thirdTotal}\n\n\n\n")

    # Prints the total scores at the end of the round
    print(f'After round {Round} the standing are:\n{first}: {firstTotal}\n{second}: {secondTotal}\n'
          f'{third}: {thirdTotal}\n')

# Determines winner, if there is a tie it goes off of the initial role, so a player who rolled a 10 initially will
# win over a player who rolled a 9 initially in the event of a tie.
print('The game is over! Calculating final results...')
if firstTotal >= secondTotal and firstTotal >= thirdTotal:
    if secondTotal >= thirdTotal:
        print(f'1st: {first} with {firstTotal}pts\n2nd: {second} with {secondTotal}pts\n'
              f'3rd: {third} with {thirdTotal}pts')
    else:
        print(f'1st: {first} with {firstTotal}pts\n2nd: {third} with {thirdTotal}pts\n'
              f'3rd: {second} with {secondTotal}pts')
elif secondTotal >= firstTotal and secondTotal >= thirdTotal:
    if firstTotal >= thirdTotal:
        print(f'1st: {second} with {secondTotal}pts\n2nd: {first} with {firstTotal}pts\n'
              f'3rd: {third} with {thirdTotal}pts')
    else:
        print(f'1st: {second} with {secondTotal}pts\n2nd: {third} with {thirdTotal}pts\n'
              f'3rd: {first} with {firstTotal}pts')
elif thirdTotal >= firstTotal and thirdTotal >= secondTotal:
    if firstTotal >= secondTotal:
        print(f'1st: {third} with {thirdTotal}pts\n2nd: {first} with {firstTotal}pts\n'
              f'3rd: {second} with {secondTotal}pts')
    else:
        print(f'1st: {third} with {thirdTotal}pts\n2nd: {second} with {secondTotal}pts\n'
              f'3rd: {first} with {firstTotal}pts')
else:
    exit('Error')

exit('Thank you for playing Ship, Captain, and Crew. I hope you enjoyed. Have a nice day.')
