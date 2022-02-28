import random as r


def aidefend(a: str, b: str, c: str, d: str, e: str, f: str, g: str, h: str, i: str) -> int:

    if b == 'X' and c == 'X' and a == ' ':
        return 1
    elif d == 'X' and g == 'X' and a == ' ':
        return 1
    elif e == 'X' and i == 'X' and a == ' ':
        return 1

    elif a == 'X' and c == 'X' and b == ' ':
        return 2
    elif e == 'X' and h == 'X' and b == ' ':
        return 2

    elif a == 'X' and b == 'X' and c == ' ':
        return 3
    elif f == 'X' and i == 'X' and c == ' ':
        return 3
    elif g == 'X' and e == 'X' and c == ' ':
        return 3

    elif a == 'X' and g == 'X' and d == ' ':
        return 4
    elif e == 'X' and f == 'X' and d == ' ':
        return 4

    elif a == 'X' and i == 'X' and e == ' ':
        return 5
    elif b == 'X' and h == 'X' and e == ' ':
        return 5
    elif d == 'X' and f == 'X' and e == ' ':
        return 5
    elif g == 'X' and c == 'X' and e == ' ':
        return 5

    elif d == 'X' and e == 'X' and f == ' ':
        return 6
    elif c == 'X' and i == 'X' and f == ' ':
        return 6

    elif a == 'X' and d == 'X' and g == ' ':
        return 7
    elif c == 'X' and e == 'X' and g == ' ':
        return 7
    elif h == 'X' and i == 'X' and g == ' ':
        return 7

    elif b == 'X' and e == 'X' and h == ' ':
        return 8
    elif g == 'X' and i == 'X' and h == ' ':
        return 8

    elif a == 'X' and e == 'X' and i == ' ':
        return 9
    elif g == 'X' and h == 'X' and i == ' ':
        return 9
    elif c == 'X' and f == 'X' and i == ' ':
        return 9

    else:
        return 10


def aiattack(a: str, b: str, c: str, d: str, e: str, f: str, g: str, h: str, i: str) -> int:

    if b == 'O' and c == 'O' and a == ' ':
        return 1
    elif d == 'O' and g == 'O' and a == ' ':
        return 1
    elif e == 'O' and i == 'O' and a == ' ':
        return 1

    elif a == 'O' and c == 'O' and b == ' ':
        return 2
    elif e == 'O' and h == 'O' and b == ' ':
        return 2

    elif a == 'O' and b == 'O' and c == ' ':
        return 3
    elif f == 'O' and i == 'O' and c == ' ':
        return 3
    elif g == 'O' and e == 'O' and c == ' ':
        return 3

    elif a == 'O' and g == 'O' and d == ' ':
        return 4
    elif e == 'O' and f == 'O' and d == ' ':
        return 4

    elif a == 'O' and i == 'O' and e == ' ':
        return 5
    elif b == 'O' and h == 'O' and e == ' ':
        return 5
    elif d == 'O' and f == 'O' and e == ' ':
        return 5
    elif g == 'O' and c == 'O' and e == ' ':
        return 5

    elif d == 'O' and e == 'O' and f == ' ':
        return 6
    elif c == 'O' and i == 'O' and f == ' ':
        return 6

    elif a == 'O' and d == 'O' and g == ' ':
        return 7
    elif c == 'O' and e == 'O' and g == ' ':
        return 7
    elif h == 'O' and i == 'O' and g == ' ':
        return 7

    elif b == 'O' and e == 'O' and h == ' ':
        return 8
    elif g == 'O' and i == 'O' and h == ' ':
        return 8

    elif a == 'O' and e == 'O' and i == ' ':
        return 9
    elif g == 'O' and h == 'O' and i == ' ':
        return 9
    elif c == 'O' and f == 'O' and i == ' ':
        return 9

    else:
        return 10


def random(a: str, b: str, c: str, d: str, e: str, f: str, g: str, h: str, i: str) -> int:
    while True:

        spot = r.randint(1, 9)

        if spot == 1 and a == ' ':
            return 1
        elif spot == 2 and b == ' ':
            return 2
        elif spot == 3 and c == ' ':
            return 3
        elif spot == 4 and d == ' ':
            return 4
        elif spot == 5 and e == ' ':
            return 5
        elif spot == 6 and f == ' ':
            return 6
        elif spot == 7 and g == ' ':
            return 7
        elif spot == 8 and h == ' ':
            return 8
        elif spot == 9 and i == ' ':
            return 9
        else:
            pass
