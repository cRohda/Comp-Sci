import func as f
from time import sleep
import webbrowser as w
import sys
import AI

f.clearconsole()
print('Welcome to python Tic Tac Toe (Version 0.0.1 Alpha)! A final project for Computer Programming by Cormac Rohda!\n'
      'To start please tell me ', end='')

while True:
    spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9 = ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
    players = input('how many players are playing today? (1/2): ')

    f.clearconsole()
    print('1 | 2 | 3\n'
          '--|---|--\n'
          '4 | 5 | 6\n'
          '--|---|--\n'
          '7 | 8 | 9\n')
    pause = input('Here is the layout of the board. REMEMBER THE SPACE NUMBERS! Press Enter to continue:')

    rounds = 1
    winner = False

    if players == '1':
        print('You selected: ONE PLAYER')

        while rounds < 10:
            f.clearconsole()
            print(f.boardupdate(spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9))

            if rounds % 2 == 0:
                player = 'O'
                print('Computers turn\nThinking...')
                sleep(1)
                spot = AI.aiattack(spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9)
                if spot == 10:
                    spot = AI.aidefend(spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9)
                    if spot == 10:
                        spot = AI.random(spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9)

            elif rounds % 2 != 0:
                player = 'X'
                print(f"Player {player}'s turn")
                spot = f.turn(spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9)

            else:
                print(f'ERROR IN ROUND NUMBER {rounds}')
                break

            if spot == 1:
                spot1 = player
            elif spot == 2:
                spot2 = player
            elif spot == 3:
                spot3 = player
            elif spot == 4:
                spot4 = player
            elif spot == 5:
                spot5 = player
            elif spot == 6:
                spot6 = player
            elif spot == 7:
                spot7 = player
            elif spot == 8:
                spot8 = player
            elif spot == 9:
                spot9 = player

            f.clearconsole()
            if rounds % 2 == 0:
                print(f'Computer chose spot: {spot}\n')
            rounds += 1

            if rounds >= 5:
                f.boardupdate(spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9)
                rounds = f.wintest(spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9, rounds)
                if rounds == 11:
                    winner = True
                    break

        if not winner:
            print('GAME OVER!\nThe Game was a tie')
        while True:
            again = input('Would you like to play again? (Y/N): ')
            f.clearconsole()
            if again.lower() == 'y':
                break
            else:
                sys.exit('Thank you for playing!')

    elif players == '2':
        print('You selected: TWO PLAYERS')

        while rounds < 10:
            if rounds % 2 == 0:
                player = 'O'
            elif rounds % 2 != 0:
                player = 'X'
            else:
                print(f'ERROR IN ROUND NUMBER {rounds}')
                break

            rounds += 1

            f.clearconsole()
            print(f.boardupdate(spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9))
            print(f"Player {player}'s turn")
            spot = f.turn(spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9)

            if spot == 1:
                spot1 = player
            elif spot == 2:
                spot2 = player
            elif spot == 3:
                spot3 = player
            elif spot == 4:
                spot4 = player
            elif spot == 5:
                spot5 = player
            elif spot == 6:
                spot6 = player
            elif spot == 7:
                spot7 = player
            elif spot == 8:
                spot8 = player
            elif spot == 9:
                spot9 = player

            f.clearconsole()

            if rounds >= 5:
                f.boardupdate(spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9)
                rounds = f.wintest(spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9, rounds)
                if rounds == 11:
                    winner = True
                    break

        if not winner:
            print('GAME OVER!\nThe Game was a tie')
        while True:
            again = input('Would you like to play again? (Y/N): ')
            f.clearconsole()
            if again.lower() == 'y':
                break
            else:
                sys.exit('Thank you for playing!')

    elif players == '0':
        print('You selected: ZERO PLAYERS')

        while rounds < 10:
            f.clearconsole()
            print(f.boardupdate(spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9))

            if rounds % 2 == 0:
                player = 'O'
                print('Computers turn\nThinking...')
                sleep(1)
                spot = AI.aiattack(spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9)
                if spot == 10:
                    spot = AI.aidefend(spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9)
                    if spot == 10:
                        spot = AI.random(spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9)

            elif rounds % 2 != 0:
                player = 'X'
                print('Computers turn\nThinking...')
                sleep(1)
                spot = AI.aiattack(spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9)
                if spot == 10:
                    spot = AI.aidefend(spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9)
                    if spot == 10:
                        spot = AI.random(spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9)

            else:
                print(f'ERROR IN ROUND NUMBER {rounds}')
                break

            if spot == 1:
                spot1 = player
            elif spot == 2:
                spot2 = player
            elif spot == 3:
                spot3 = player
            elif spot == 4:
                spot4 = player
            elif spot == 5:
                spot5 = player
            elif spot == 6:
                spot6 = player
            elif spot == 7:
                spot7 = player
            elif spot == 8:
                spot8 = player
            elif spot == 9:
                spot9 = player

            f.clearconsole()
            print(f'Computer chose spot: {spot}\n')
            rounds += 1

            if rounds >= 5:
                f.boardupdate(spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9)
                rounds = f.wintest(spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9, rounds)
                if rounds == 11:
                    winner = True
                    break

        if not winner:
            print('GAME OVER!\nThe Game was a tie')
        while True:
            again = input('Would you like to play again? (Y/N): ')
            f.clearconsole()
            if again.lower() == 'y':
                break
            else:
                sys.exit('Thank you for playing!')

    elif players.lower() == 'rick':
        url = 'https://ponjo.club/reflux'
        w.open(url)

    else:
        print('I did not recognize that input, please try again.')
        sleep(.5)
