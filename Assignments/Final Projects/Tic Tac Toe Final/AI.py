def aicheck(a: str, b: str, c: str, d: str, e: str, f: str, g: str, h: str, i: str) -> int:

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
