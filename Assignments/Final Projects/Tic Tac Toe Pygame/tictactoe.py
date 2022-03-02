import pygame
import sys
import time
from pygame.locals import *

# Variables to be used
height = 700
width = 700
turn = 'x'
winner = None
tie = None
white = (255, 255, 255)
black = (0, 0, 0)

# Sets board as 3 rows of the 3
board = [[None] * 3, [None] * 3, [None] * 3]

# Initialize pygame
pygame.init()

# Set display and game speeds
frames = 30
clock = pygame.time.Clock()
display = pygame.display.set_mode((width, height + 100), 0, 32)
pygame.display.set_caption("Pygame TicTacToe by Cormac")

# import sprites
outline = pygame.image.load("title.png")
x_sprite = pygame.image.load("X.png")
o_sprite = pygame.image.load("O.png")

# resize sprites
outline = pygame.transform.scale(outline, (width, height + 100))
x_sprite = pygame.transform.scale(x_sprite, (80, 80))
o_sprite = pygame.transform.scale(o_sprite, (80, 80))


def window_init():
    display.blit(outline, (0, 0))

    pygame.display.update()
    time.sleep(3)
    display.fill(white)

    pygame.draw.line(display, black, (width / 3, 0), (width / 3, height), 7)
    pygame.draw.line(display, black, (width / 3 * 2, 0), (width / 3 * 2, height), 7)

    pygame.draw.line(display, black, (0, height / 3), (width, height / 3), 7)
    pygame.draw.line(display, black, (0, height / 3 * 2), (width, height / 3 * 2), 7)
    tie_check()


def tie_check():
    global tie

    if winner is None:
        message = f"{turn.upper()}'s turn"
    else:
        message = f"{winner.upper()} won!"
    if tie:
        message = "Game ended in a tie"

    font = pygame.font.Font(None, 30)

    text = font.render(message, True, white)

    display.fill(black, (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width / 2, 500 - 50))
    display.blit(text, text_rect)
    pygame.display.update()


def win_test():
    global board, winner, tie

    for row in range(0, 3):
        if (board[row][0] == board[row][1] == board[row][2]) and (board[row][0] is not None):
            winner = board[row][0]
            pygame.draw.line(display, (250, 0, 0),
                             (0, (row + 1) * height / 3 - height / 6),
                             (width, (row + 1) * height / 3 - height / 6),
                             4)
            break

    for col in range(0, 3):
        if (board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None):
            winner = board[0][col]
            pygame.draw.line(display, (250, 0, 0), ((col + 1) * width / 3 - width / 6, 0),
                             ((col + 1) * width / 3 - width / 6, height), 4)
            break

    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
        winner = board[0][0]
        pygame.draw.line(display, (250, 70, 70), (50, 50), (350, 350), 4)

    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
        winner = board[0][2]
        pygame.draw.line(display, (250, 70, 70), (350, 50), (50, 350), 4)

    if all([all(row) for row in board]) and winner is None:
        tie = True
    tie_check()


def drawturn(row, col):
    global board, turn

    if row == 1:
        pos_x = 30

    if row == 2:
        pos_x = width / 3 + 30

    if row == 3:
        pos_x = width / 3 * 2 + 30

    if col == 1:
        pos_y = 30

    if col == 2:
        pos_y = height / 3 + 30

    if col == 3:
        pos_y = height / 3 * 2 + 30

    board[row-1][col-1] = turn

    if turn == 'x':

        display.blit(x_sprite, (pos_y, pos_x))
        turn = 'o'

    else:
        display.blit(o_sprite, (pos_y, pos_x))
        turn = 'x'

    pygame.display.update()


def click():

    x, y = pygame.mouse.get_pos()

    if x < width / 3:
        col = 1

    elif x < width / 3 * 2:
        col = 2

    elif x < width:
        col = 3

    else:
        col = None

    if y < height / 3:
        row = 1

    elif y < height / 3 * 2:
        row = 2

    elif y < height:
        row = 3

    else:
        row = None

    if row and col and board[row - 1][col - 1] is None:
        global turn
        drawturn(row, col)
        win_test()


def reset():
    global board, winner, turn, tie
    time.sleep(3)
    turn = 'x'
    tie = False
    window_init()
    winner = None
    board = [[None]*3, [None]*3, [None]*3]


window_init()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            click()
            if winner or tie:
                reset()
    pygame.display.update()
    clock.tick(frames)
