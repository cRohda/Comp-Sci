from random import randint


def ai(board):
    # AI attack spot
    # test for win in top left
    if (board[0][1] == 'o' and board[0][2] == 'o') and (board[0][0] is None):
        return 1
    elif (board[1][0] == 'o' and board[2][0] == 'o') and (board[0][0] is None):
        return 1
    elif (board[1][1] == 'o' and board[2][2] == 'o') and (board[0][0] is None):
        return 1

    # test for win in top center
    elif (board[0][0] == 'o' and board[0][2] == 'o') and (board[0][1] is None):
        return 2
    elif (board[1][1] == 'o' and board[2][1] == 'o') and (board[0][1] is None):
        return 2

    # test for win in top right
    elif (board[0][0] == 'o' and board[0][1] == 'o') and (board[0][2] is None):
        return 3
    elif (board[1][2] == 'o' and board[2][2] == 'o') and (board[0][2] is None):
        return 3
    elif (board[2][0] == 'o' and board[1][1] == 'o') and (board[0][2] is None):
        return 3

    # test for win in left center
    elif (board[1][1] == 'o' and board[1][2] == 'o') and (board[1][0] is None):
        return 4
    elif (board[0][0] == 'o' and board[2][0] == 'o') and (board[1][0] is None):
        return 4

    # test for win in center
    elif (board[0][0] == 'o' and board[2][2] == 'o') and (board[1][1] is None):
        return 5
    elif (board[0][2] == 'o' and board[2][0] == 'o') and (board[1][1] is None):
        return 5
    elif (board[1][0] == 'o' and board[1][2] == 'o') and (board[1][1] is None):
        return 5
    elif (board[0][1] == 'o' and board[2][1] == 'o') and (board[1][1] is None):
        return 5

    # test for win in right center
    elif (board[1][0] == 'o' and board[1][1] == 'o') and (board[1][2] is None):
        return 6
    elif (board[0][2] == 'o' and board[2][2] == 'o') and (board[1][2] is None):
        return 6

    # test for win in bottom right
    elif (board[0][0] == 'o' and board[1][0] == 'o') and (board[2][0] is None):
        return 7
    elif (board[0][2] == 'o' and board[1][1] == 'o') and (board[2][0] is None):
        return 7
    elif (board[2][1] == 'o' and board[2][2] == 'o') and (board[2][0] is None):
        return 7

    # test for win in bottom center
    elif (board[0][1] == 'o' and board[1][1] == 'o') and (board[2][1] is None):
        return 8
    elif (board[2][0] == 'o' and board[2][2] == 'o') and (board[2][1] is None):
        return 8

    # test for win in bottom right
    elif (board[2][0] == 'o' and board[2][1] == 'o') and (board[2][2] is None):
        return 9
    elif (board[0][0] == 'o' and board[1][1] == 'o') and (board[2][2] is None):
        return 9
    elif (board[0][2] == 'o' and board[1][2] == 'o') and (board[2][2] is None):
        return 9

    # AI Defend spot
    # test for defend in top left
    elif (board[0][1] == 'x' and board[0][2] == 'x') and (board[0][0] is None):
        return 1
    elif (board[1][0] == 'x' and board[2][0] == 'x') and (board[0][0] is None):
        return 1
    elif (board[1][1] == 'x' and board[2][2] == 'x') and (board[0][0] is None):
        return 1

    # test for defend in top center
    elif (board[0][0] == 'x' and board[0][2] == 'x') and (board[0][1] is None):
        return 2
    elif (board[1][1] == 'x' and board[2][1] == 'x') and (board[0][1] is None):
        return 2

    # test for defend in top right
    elif (board[0][0] == 'x' and board[0][1] == 'x') and (board[0][2] is None):
        return 3
    elif (board[1][2] == 'x' and board[2][2] == 'x') and (board[0][2] is None):
        return 3
    elif (board[2][0] == 'x' and board[1][1] == 'x') and (board[0][2] is None):
        return 3

    # test for defend in left center
    elif (board[1][1] == 'x' and board[1][2] == 'x') and (board[1][0] is None):
        return 4
    elif (board[0][0] == 'x' and board[2][0] == 'x') and (board[1][0] is None):
        return 4

    # test for defend in center
    elif (board[0][0] == 'x' and board[2][2] == 'x') and (board[1][1] is None):
        return 5
    elif (board[0][2] == 'x' and board[2][0] == 'x') and (board[1][1] is None):
        return 5
    elif (board[1][0] == 'x' and board[1][2] == 'x') and (board[1][1] is None):
        return 5
    elif (board[0][1] == 'x' and board[2][1] == 'x') and (board[1][1] is None):
        return 5

    # test for defend in right center
    elif (board[1][0] == 'x' and board[1][1] == 'x') and (board[1][2] is None):
        return 6
    elif (board[0][2] == 'x' and board[2][2] == 'x') and (board[1][2] is None):
        return 6

    # test for defend in bottom right
    elif (board[0][0] == 'x' and board[1][0] == 'x') and (board[2][0] is None):
        return 7
    elif (board[0][2] == 'x' and board[1][1] == 'x') and (board[2][0] is None):
        return 7
    elif (board[2][1] == 'x' and board[2][2] == 'x') and (board[2][0] is None):
        return 7

    # test for defend in bottom center
    elif (board[0][1] == 'x' and board[1][1] == 'x') and (board[2][1] is None):
        return 8
    elif (board[2][0] == 'x' and board[2][2] == 'x') and (board[2][1] is None):
        return 8

    # test for defend in bottom right
    elif (board[2][0] == 'x' and board[2][1] == 'x') and (board[2][2] is None):
        return 9
    elif (board[0][0] == 'x' and board[1][1] == 'x') and (board[2][2] is None):
        return 9
    elif (board[0][2] == 'x' and board[1][2] == 'x') and (board[2][2] is None):
        return 9

    # random spot
    else:
        return randint(1, 9)
