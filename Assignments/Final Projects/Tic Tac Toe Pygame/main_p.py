import pygame as pg
from time import sleep
from pygame.locals import *
import sys
import AI
from pygame import mixer
import random as r

# Variables
HEIGHT = 700
WIDTH = 700
turn = 'x'
winner = False
tie = False
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
FPS = 30
running = True
players = 0
message = 'Welcome to Tic Tac Toe!'
total_turns = 0


# sets board
board = [[None] * 3, [None] * 3, [None] * 3]

songs = ['Song1.wav', 'Song2.wav', 'Song3.wav', 'Song4.wav']

# Init pygame
pg.init()

# Set game clock
clock = pg.time.Clock()

# set the pygame display and title
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


# loads the menu screen
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


# Start the game
def game_start():
    # Draw board
    canvas.fill(WHITE)
    pg.draw.line(canvas, BLACK, (WIDTH / 3, 0), (WIDTH / 3, HEIGHT), 7)
    pg.draw.line(canvas, BLACK, (WIDTH / 3 * 2, 0), (WIDTH / 3 * 2, HEIGHT), 7)
    pg.draw.line(canvas, BLACK, (0, HEIGHT / 3), (WIDTH, HEIGHT / 3), 7)
    pg.draw.line(canvas, BLACK, (0, HEIGHT / 3 * 2), (WIDTH, HEIGHT / 3 * 2), 7)
    message_status()


# Update the status message at the bottom of the game
def message_status():
    global tie, message

    if winner is False:
        message = f"{turn.upper()}'s turn"
    elif winner == 'x' or 'o':
        message = f"{winner.upper()} won the game!"
    if tie:
        message = "The game is a tie"

    font = pg.font.Font(None, 30)
    text = font.render(message, True, WHITE)

    canvas.fill(BLACK, (WIDTH / 2 - 150, HEIGHT, 300, 50))
    text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT + 25))
    canvas.blit(text, text_rect)
    pg.display.update()


# Check if there is a winner
def is_winner():
    global board, winner, tie, message, total_turns

    # Test for wins in rows
    for row in range(0, 3):
        if (board[row][0] == board[row][1] == board[row][2]) and (board[row][0] is not None):
            winner = board[row][0]
            # Draw line showing win
            pg.draw.line(canvas, RED,
                         (0, (row + 1) * HEIGHT / 3 - HEIGHT / 6),
                         (WIDTH, (row + 1) * HEIGHT / 3 - HEIGHT / 6),
                         4)
            break

    # Test for wins in columns
    for col in range(0, 3):
        if (board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None):
            winner = board[0][col]
            # Draw line showing win
            pg.draw.line(canvas, RED,
                         ((col + 1) * WIDTH / 3 - WIDTH / 6, 0),
                         ((col + 1) * WIDTH / 3 - WIDTH / 6, HEIGHT),
                         4)
            break

    # check for diagonal win
    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
        winner = board[0][0]
        # Draw line showing win
        pg.draw.line(canvas, (250, 70, 70), (50, 50), (600, 600), 4)
    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
        winner = board[0][2]
        # Draw line showing win
        pg.draw.line(canvas, (250, 70, 70), (650, 50), (50, 600), 4)

    # If there have been 9 turns and no winner there is a tie
    if total_turns == 9 and winner is False:
        tie = True
    message_status()


# Mark the turns on the display
def mark_turn(row, col):
    global board, turn, total_turns
    posx, posy = 0, 0
    total_turns += 1

    # pick coords to draw sprite based off of spot
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

    # Set move on virtual board (used to determine win/tie)
    board[row-1][col-1] = turn

    if turn == 'x':
        # play noise
        mark_x = mixer.Sound("mark_x.wav")
        mark_x.play()
        # draw sprite
        canvas.blit(x_sprite, (posy, posx))
        # change turn
        turn = 'o'
    else:
        # play noise
        mark_o = mixer.Sound("mark_o.wav")
        mark_o.play()
        # draw sprite
        canvas.blit(o_sprite, (posy, posx))
        # change turn
        turn = 'x'

    # update the display
    pg.display.update()


# determine spot player chooses on click
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

    # Only allow this sel if it is an empty spot
    if row and col and board[row - 1][col - 1] is None:
        global turn

        # mark the turn and check for win
        mark_turn(row, col)
        is_winner()


# Makes computer move, only in single player mode
def computer_move(game):

    # Loops to choose a spot that is not occupied
    while True:
        # determines spot from AI function in different file
        spot = AI.ai(game)

        # get the spot and check to make sure that it is unoccupied
        # set row and col to the spot to mark it
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
        # if the selected spot doesn't work, pass and choose a new spot
        else:
            pass

    # draw the computers' selection on the screen and check for winner
    mark_turn(row, col)
    is_winner()


# reset the game
def reset():
    global board, winner, turn, tie, players, total_turns

    # wait 3 seconds to show there is a winner
    sleep(3)
    turn = 'x'
    tie = False
    winner = False
    board = [[None] * 3, [None] * 3, [None] * 3]
    players = 0
    total_turns = 0

    # go back to the menu screen
    menu_screen()


# function to choose and play a new song
def new_song():
    global songs
    music = r.choice(songs)
    mixer.music.load(music)
    mixer.music.play(-1)


new_song()
# start the game
menu_screen()

# Game loop
while running:
    clock.tick(FPS)
    # Menu loop
    while players == 0:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit('Game quit')
                # Quit on escape key
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pg.quit()
                    sys.exit('Escape key pressed')
            # Run when the user clicks
            elif event.type == MOUSEBUTTONDOWN:
                # set players to the users selection (breaks loop)
                players = num_players_choice()
                game_start()

    # 2 Player loop
    if players == 2:
        while True:
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit('Game quit')
                    # Quit on escape key
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pg.quit()
                        sys.exit('Escape key pressed')
                # Run when user clicks
                elif event.type == MOUSEBUTTONDOWN:
                    game_click()
                    # reset and break loop when game ends
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
                    sys.exit('Game quit')
                # Quit on escape key
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pg.quit()
                        sys.exit('Escape key pressed')
                # when user clicks
                elif event.type == MOUSEBUTTONDOWN:
                    # player selection
                    game_click()
                    # check for winner or tie
                    if winner or tie:
                        reset()
                        break
                    # wait a second
                    sleep(1)
                    # computer selection
                    computer_move(board)
                    # check for winner or tie
                    if winner or tie:
                        reset()
                        break
            break
