def boardupdate(a: str, b: str, c: str, d: str, e: str, f: str, g: str, h: str, i: str) -> None:
    board = f'{a} | {b} | {c}\n' \
            f'--|---|--\n' \
            f'{d} | {e} | {f}\n' \
            f'--|---|--\n' \
            f'{g} | {h} | {i}'
    print(board)


def clearconsole():
    print('\n' * 150)


def fewlines():
    print('\n' * 5)


def wintest(a: str, b: str, c: str, d: str, e: str, f: str, g: str, h: str, i: str) -> None:
    if a == b and a == c and a != ' ':
        fewlines()
        print(f'GAME OVER!\nThe Winner is {a}')
    elif d == e and d == f and d != ' ':
        fewlines()
        print(f'GAME OVER!\nThe Winner is {d}')
    elif g == h and g == i and g != ' ':
        fewlines()
        print(f'GAME OVER!\nThe Winner is {g}')
    elif a == d and a == g and a != ' ':
        fewlines()
        print(f'GAME OVER!\nThe Winner is {a}')
    elif b == e and b == h and b != ' ':
        fewlines()
        print(f'GAME OVER!\nThe Winner is {b}')
    elif c == f and c == i and c != ' ':
        fewlines()
        print(f'GAME OVER!\nThe Winner is {c}')
    elif a == e and a == i and a != ' ':
        fewlines()
        print(f'GAME OVER!\nThe Winner is {a}')
    elif c == e and c == g and c != ' ':
        fewlines()
        print(f'GAME OVER!\nThe Winner is {c}')
    else:
        pass


def turn(a: str, b: str, c: str, d: str, e: str, f: str, g: str, h: str, i: str):
    while True:
        choice = int(input('Where would you like to go?: '))

        if choice == 1 and a != '1':
            print('That spot is occupied, please choose another\n')
        elif choice == 2 and b != '2':
            print('That spot is occupied, please choose another\n')
        elif choice == 3 and c != '3':
            print('That spot is occupied, please choose another\n')
        elif choice == 4 and d != '4':
            print('That spot is occupied, please choose another\n')
        elif choice == 5 and e != '5':
            print('That spot is occupied, please choose another\n')
        elif choice == 6 and f != '6':
            print('That spot is occupied, please choose another\n')
        elif choice == 7 and g != '7':
            print('That spot is occupied, please choose another\n')
        elif choice == 8 and h != '8':
            print('That spot is occupied, please choose another\n')
        elif choice == 9 and i != '9':
            print('That spot is occupied, please choose another\n')
        elif choice > 9:
            print('That spot does not exist, please choose another')
        elif choice < 1:
            print('That spot does not exist, please choose another')
        else:
            return choice
