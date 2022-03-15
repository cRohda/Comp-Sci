from random import randint


def ai(board):
    # AI attack spot
    # test for win in top left
    if (board[0][1] and board[0][2] == 'o') and (board[0][0] is None):
        spot = 1
    elif (board[1][0] and board[2][0] == 'o') and (board[0][0] is None):
        spot = 1
    elif (board[1][1] and board[2][2] == 'o') and (board[0][0] is None):
        spot = 1

    # test for win in top center
    elif (board[0][0] and board[0][2] == 'o') and (board[0][1] is None):
        spot = 2
    elif (board[1][1] and board[2][1] == 'o') and (board[0][1] is None):
        spot = 2

    # test for win in top right
    elif (board[0][0] and board[0][1] == 'o') and (board[0][2] is None):
        spot = 3
    elif (board[1][2] and board[2][2] == 'o') and (board[0][2] is None):
        spot = 3
    elif (board[2][0] and board[1][1] == 'o') and (board[0][2] is None):
        spot = 3

    # test for win in left center
    elif (board[1][1] and board[1][2] == 'o') and (board[1][0] is None):
        spot = 4
    elif (board[0][0] and board[2][0] == 'o') and (board[1][0] is None):
        spot = 4

    # test for win in center
    elif (board[0][0] and board[2][2] == 'o') and (board[1][1] is None):
        spot = 5
    elif (board[0][2] and board[2][0] == 'o') and (board[1][1] is None):
        spot = 5
    elif (board[1][0] and board[1][2] == 'o') and (board[1][1] is None):
        spot = 5
    elif (board[0][1] and board[2][1] == 'o') and (board[1][1] is None):
        spot = 5

    # test for win in right center
    elif (board[1][0] and board[1][1] == 'o') and (board[1][2] is None):
        spot = 6
    elif (board[0][2] and board[2][2] == 'o') and (board[1][2] is None):
        spot = 6

    # test for win in bottom right
    elif (board[0][0] and board[1][0] == 'o') and (board[2][0] is None):
        spot = 7
    elif (board[0][2] and board[1][1] == 'o') and (board[2][0] is None):
        spot = 7
    elif (board[2][1] and board[2][2] == 'o') and (board[2][0] is None):
        spot = 7

    # test for win in bottom center
    elif (board[0][1] and board[1][1] == 'o') and (board[2][1] is None):
        spot = 8
    elif (board[2][0] and board[2][2] == 'o') and (board[2][1] is None):
        spot = 8

    # test for win in bottom right
    elif (board[2][0] and board[2][1] == 'o') and (board[2][2] is None):
        spot = 9
    elif (board[0][0] and board[1][1] == 'o') and (board[2][2] is None):
        spot = 9
    elif (board[0][2] and board[1][2] == 'o') and (board[2][2] is None):
        spot = 9

    # AI Defend spot
    # test for win in top left
    if (board[0][1] and board[0][2] == 'x') and (board[0][0] is None):
        spot = 1
    elif (board[1][0] and board[2][0] == 'x') and (board[0][0] is None):
        spot = 1
    elif (board[1][1] and board[2][2] == 'x') and (board[0][0] is None):
        spot = 1

    # test for win in top center
    elif (board[0][0] and board[0][2] == 'x') and (board[0][1] is None):
        spot = 2
    elif (board[1][1] and board[2][1] == 'x') and (board[0][1] is None):
        spot = 2

    # test for win in top right
    elif (board[0][0] and board[0][1] == 'x') and (board[0][2] is None):
        spot = 3
    elif (board[1][2] and board[2][2] == 'x') and (board[0][2] is None):
        spot = 3
    elif (board[2][0] and board[1][1] == 'x') and (board[0][2] is None):
        spot = 3

    # test for win in left center
    elif (board[1][1] and board[1][2] == 'x') and (board[1][0] is None):
        spot = 4
    elif (board[0][0] and board[2][0] == 'x') and (board[1][0] is None):
        spot = 4

    # test for win in center
    elif (board[0][0] and board[2][2] == 'x') and (board[1][1] is None):
        spot = 5
    elif (board[0][2] and board[2][0] == 'x') and (board[1][1] is None):
        spot = 5
    elif (board[1][0] and board[1][2] == 'x') and (board[1][1] is None):
        spot = 5
    elif (board[0][1] and board[2][1] == 'x') and (board[1][1] is None):
        spot = 5

    # test for win in right center
    elif (board[1][0] and board[1][1] == 'x') and (board[1][2] is None):
        spot = 6
    elif (board[0][2] and board[2][2] == 'x') and (board[1][2] is None):
        spot = 6

    # test for win in bottom right
    elif (board[0][0] and board[1][0] == 'x') and (board[2][0] is None):
        spot = 7
    elif (board[0][2] and board[1][1] == 'x') and (board[2][0] is None):
        spot = 7
    elif (board[2][1] and board[2][2] == 'x') and (board[2][0] is None):
        spot = 7

    # test for win in bottom center
    elif (board[0][1] and board[1][1] == 'x') and (board[2][1] is None):
        spot = 8
    elif (board[2][0] and board[2][2] == 'x') and (board[2][1] is None):
        spot = 8

    # test for win in bottom right
    elif (board[2][0] and board[2][1] == 'x') and (board[2][2] is None):
        spot = 9
    elif (board[0][0] and board[1][1] == 'x') and (board[2][2] is None):
        spot = 9
    elif (board[0][2] and board[1][2] == 'x') and (board[2][2] is None):
        spot = 9

    # random spot
    else:
        spot = randint(1, 9)

    return spot
