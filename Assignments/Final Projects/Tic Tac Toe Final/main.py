import func as f
from time import sleep
import webbrowser as w

spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9 = ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '

print('Welcome to python Tic Tac Toe (Version 0.0.1 Alpha)! A final project for Computer Programming by Cormac Rohda!\n'
      'To start please tell me ', end='')

while True:
    players = input('how many players are playing today? (1/2): ')

    f.fewlines()
    print('1 | 2 | 3\n'
          '--|---|--\n'
          '4 | 5 | 6\n'
          '--|---|--\n'
          '7 | 8 | 9\n')
    pause = input('Here is the layout of the board. REMEMBER THE SPACE NUMBERS! Press Enter to continue:')

    if players == '1':
        print('You selected: ONE PLAYER')

    elif players == '2':
        print('You selected: TWO PLAYERS')

        for rounds in range(1, 10):
            if rounds % 2 == 0:
                player = 'O'
            elif rounds % 2 != 0:
                player = 'X'
            else:
                print(f'ERROR IN ROUND NUMBER {rounds}')
                break

            f.clearconsole()
            f.boardupdate(spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9)
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

            if rounds >= 5:
                print('tested for win')
                f.wintest(spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9)
            f.clearconsole()

    elif players == '0':
        print('You selected: ZERO PLAYERS')

    elif players.lower() == 'rick':
        url = 'https://ponjo.club/reflux'
        w.open(url)

    else:
        print('I did not recognize that input, please try again.')
        sleep(.5)
