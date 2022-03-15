import pygame as pg
from time import sleep
from pygame.locals import *
import sys
import AI

# Variables
HEIGHT = 700
WIDTH = 700
turn = 'x'
winner = False
tie = False
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
running = True
players = 0


# sets board
board = [[None] * 3, [None] * 3, [None] * 3]

# Init pygame
pg.init()

FPS = 30
clock = pg.time.Clock()
canvas = pg.display.set_mode((WIDTH, HEIGHT + 100), 0, 32)
pg.display.set_caption("Pygame TicTacToe")

# sprites
menu = pg.image.load("title.png")
x_sprite = pg.image.load("X.png")
o_sprite = pg.image.load("O.png")

# resize sprite
menu = pg.transform.scale(menu, (WIDTH, HEIGHT + 100))
x_sprite = pg.transform.scale(x_sprite, (100, 100))
o_sprite = pg.transform.scale(o_sprite, (100, 100))


# loads the meny screen
def menu_screen():
    canvas.fill(WHITE)
    canvas.blit(menu, (0, 0))
    pg.display.update()


# gets player choice from menu screen
def num_players_choice():

    x, y = pg.mouse.get_pos()

    if x > WIDTH / 2:
        return 2
    elif x < WIDTH / 2:
        return 1


def game_start():
    # Draw board
    canvas.fill(WHITE)
    pg.draw.line(canvas, BLACK, (WIDTH / 3, 0), (WIDTH / 3, HEIGHT), 7)
    pg.draw.line(canvas, BLACK, (WIDTH / 3 * 2, 0), (WIDTH / 3 * 2, HEIGHT), 7)
    pg.draw.line(canvas, BLACK, (0, HEIGHT / 3), (WIDTH, HEIGHT / 3), 7)
    pg.draw.line(canvas, BLACK, (0, HEIGHT / 3 * 2), (WIDTH, HEIGHT / 3 * 2), 7)
    message_status()


def message_status():
    global tie
    message = 'Welcome to Tic Tac Toe!'

    if tie:
        message = "The game is a tie"
    if winner is False:
        message = f"{turn.upper()}'s turn"
    elif winner == 'x' or 'o':
        message = f"{winner.upper()} won the game!"

    font = pg.font.Font(None, 30)
    text = font.render(message, True, WHITE)

    canvas.fill(BLACK, (WIDTH / 2 - 150, HEIGHT, 300, 50))
    text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT + 25))
    canvas.blit(text, text_rect)
    pg.display.update()


def is_winner():
    global board, winner, tie

    # Test for wins in rows
    for row in range(0, 3):
        if (board[row][0] == board[row][1] == board[row][2]) and (board[row][0] is not None):
            winner = board[row][0]
            pg.draw.line(canvas, RED,
                         (0, (row + 1) * HEIGHT / 3 - HEIGHT / 6),
                         (WIDTH, (row + 1) * HEIGHT / 3 - HEIGHT / 6),
                         4)
            break

    for col in range(0, 3):
        if (board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None):
            winner = board[0][col]
            pg.draw.line(canvas, RED,
                         ((col + 1) * WIDTH / 3 - WIDTH / 6, 0),
                         ((col + 1) * WIDTH / 3 - WIDTH / 6, HEIGHT),
                         4)
            break

    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
        winner = board[0][0]
        pg.draw.line(canvas, (250, 70, 70), (50, 50), (600, 600), 4)

    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
        winner = board[0][2]
        pg.draw.line(canvas, (250, 70, 70), (650, 50), (50, 600), 4)

    if all([all(row) for row in board]) and winner is None:
        tie = True
    message_status()


def mark_turn(row, col):
    global board, turn
    posx, posy = 0, 0

    # pick coords based off of spot
    if row == 1:
        posx = 70
    if row == 2:
        posx = WIDTH / 3 + 70
    if row == 3:
        posx = WIDTH / 3 * 2 + 70

    if col == 1:
        posy = 70
    if col == 2:
        posy = HEIGHT / 3 + 70
    if col == 3:
        posy = HEIGHT / 3 * 2 + 70

    # Set move on virtual board
    board[row-1][col-1] = turn

    # Draw sprite on screen
    # Add scrible noise?
    if turn == 'x':
        canvas.blit(x_sprite, (posy, posx))
        turn = 'o'
    else:
        canvas.blit(o_sprite, (posy, posx))
        turn = 'x'

    pg.display.update()


def game_click():
    x, y = pg.mouse.get_pos()

    if x < WIDTH / 3:
        col = 1
    elif x < WIDTH / 3 * 2:
        col = 2
    elif x < WIDTH:
        col = 3
    else:
        col = None

    if y < HEIGHT / 3:
        row = 1
    elif y < HEIGHT / 3 * 2:
        row = 2
    elif y < HEIGHT:
        row = 3
    else:
        row = None

    if row and col and board[row - 1][col - 1] is None:
        global turn
        mark_turn(row, col)
        is_winner()


# way too long function for AI. starts with finding a spot it can win, then a spot it can stop player win, then random
def computer_move(game):
    while True:
        spot = AI.ai(game)
        if spot == 1 and (board[0][0] is None):
            row, col = 1, 1
            break
        elif spot == 2 and (board[0][1] is None):
            row, col = 1, 2
            break
        elif spot == 3 and (board[0][2] is None):
            row, col = 1, 3
            break
        elif spot == 4 and (board[1][0] is None):
            row, col = 2, 1
            break
        elif spot == 5 and (board[1][1] is None):
            row, col = 2, 2
            break
        elif spot == 6 and (board[1][2] is None):
            row, col = 2, 3
            break
        elif spot == 7 and (board[2][0] is None):
            row, col = 3, 1
            break
        elif spot == 8 and (board[2][1] is None):
            row, col = 3, 2
            break
        elif spot == 9 and (board[2][2] is None):
            row, col = 3, 3
            break
        else:
            pass

    mark_turn(row, col)
    is_winner()


def reset():
    global board, winner, turn, tie, players
    sleep(3)
    turn = 'x'
    tie = False
    winner = False
    board = [[None] * 3, [None] * 3, [None] * 3]
    players = 0
    menu_screen()


menu_screen()

# Game loop
while running:
    # Menu loop
    while players == 0:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                players = num_players_choice()
                game_start()

    # 2 Player loop
    if players == 2:
        while True:
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    game_click()
                    if winner or tie:
                        reset()
                        break
            break

    # Single Player loop
    if players == 1:
        while True:
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    game_click()
                    if winner or tie:
                        reset()
                        break
                    sleep(1)
                    computer_move(board)
                    if winner or tie:
                        reset()
                        break
            break

    pg.display.update()
    clock.tick(FPS)
