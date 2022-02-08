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

        if choice == 1 and a != ' ':
            print('That spot is occupied, please choose another\n')
        elif choice == 2 and b != ' ':
            print('That spot is occupied, please choose another\n')
        elif choice == 3 and c != ' ':
            print('That spot is occupied, please choose another\n')
        elif choice == 4 and d != ' ':
            print('That spot is occupied, please choose another\n')
        elif choice == 5 and e != ' ':
            print('That spot is occupied, please choose another\n')
        elif choice == 6 and f != ' ':
            print('That spot is occupied, please choose another\n')
        elif choice == 7 and g != ' ':
            print('That spot is occupied, please choose another\n')
        elif choice == 8 and h != ' ':
            print('That spot is occupied, please choose another\n')
        elif choice == 9 and i != ' ':
            print('That spot is occupied, please choose another\n')
        else:
            return choice
