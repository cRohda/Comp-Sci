import func as f
from time import sleep
import webbrowser as w

spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9 = ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '

print('Welcome to python Tic Tac Toe (Version 0.0.1 Alpha)! A final project for Computer Programming by Cormac Rohda!\n'
      'To start please tell me ', end='')

while True:
    players = input('how many players are playing today? (1/2): ')

    f.boardupdate(spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9)

    if players == '1':
        print('You selected: ONE PLAYER')

    elif players == '2':
        print('You selected: TWO PLAYERS')
        f.fewlines()
        for rounds in range (1, 10):
            pass
    elif players == '0':
        print('You selected: ZERO PLAYERS')

    elif players.lower() == 'rick':
        url = 'https://ponjo.club/reflux'
        w.open(url)

    else:
        print('I did not recognize that input, please try again.')
        sleep(.5)
