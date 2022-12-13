# Importing required libraries 
import pygame, sys, os
import numpy as np
from tkinter import *

# Initializing pygame
pygame.init()

# CONSTANTS
WIDTH = HEIGHT = 800
LINE_WIDTH = 20
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH//BOARD_COLS
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)

CIRCLE_RADIUS = SQUARE_SIZE//3
CIRCLE_WIDTH = 15
O_COLOR = (239,231,200) 

X_WIDTH = 25
SPACE = SQUARE_SIZE//4
X_COLOR = (66,66,66)

WINNER_LINE_WIDTH = 30

# SCREEN
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TIC TAC TOE")
screen.fill(BG_COLOR)
programIcon = pygame.image.load('./media/tictactoe_icon.png')
pygame.display.set_icon(programIcon)

# Board
board = np.zeros((BOARD_ROWS, BOARD_COLS))

# Functions
def draw_lines():
    # Horizontal Lines
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (HEIGHT, SQUARE_SIZE), LINE_WIDTH )
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE*2), (HEIGHT, SQUARE_SIZE*2), LINE_WIDTH )

    # Vertical Lines
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE,0), (SQUARE_SIZE,WIDTH), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE*2,0), (SQUARE_SIZE*2,WIDTH), LINE_WIDTH)

# Draws X's and O's
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 2:
                pygame.draw.circle(screen, O_COLOR, (int(col*SQUARE_SIZE + SQUARE_SIZE/2),int(row*SQUARE_SIZE + SQUARE_SIZE/2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            
            elif board[row][col] == 1:
                pygame.draw.line(screen, X_COLOR, (col*SQUARE_SIZE+SPACE, row*SQUARE_SIZE+SQUARE_SIZE-SPACE), (col*SQUARE_SIZE+SQUARE_SIZE-SPACE, row*SQUARE_SIZE+SPACE), X_WIDTH)
                pygame.draw.line(screen, X_COLOR, (col*SQUARE_SIZE+SPACE, row*SQUARE_SIZE+SPACE), (col*SQUARE_SIZE+SQUARE_SIZE-SPACE, row*SQUARE_SIZE+SQUARE_SIZE-SPACE), X_WIDTH)
                
# Marks a spot on the board
def mark_square(row, col, player):
    board[row][col] = player

# Checks if the spot is available
def available_square(row, col):
    return board[row][col] == 0

# Checks if the board is full
def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True

# Checks if the player won
def check_win(player):
    # vertical win check
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True
    
    # vertical win check
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True

    # diagonals win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_diag1_winning_line(player)
        return True
    
    elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_diag2_winning_line(player)
        return True

    return False


# Winning Animations

def draw_vertical_winning_line(col, player):
    posX = col*SQUARE_SIZE + SQUARE_SIZE//2

    if player == 2:
        color = O_COLOR
    elif player == 1:
        color = X_COLOR

    pygame.draw.line(screen, color, (posX, WINNER_LINE_WIDTH), (posX, HEIGHT-WINNER_LINE_WIDTH), WINNER_LINE_WIDTH)


def draw_horizontal_winning_line(row, player):
    posY = row*SQUARE_SIZE+SQUARE_SIZE//2

    if player == 2:
        color = O_COLOR
    elif player == 1:
        color = X_COLOR

    pygame.draw.line(screen, color, (WINNER_LINE_WIDTH, posY), (WIDTH-WINNER_LINE_WIDTH, posY), WINNER_LINE_WIDTH)

def draw_diag1_winning_line(player):
    if player == 2:
        color = O_COLOR
    elif player == 1:
        color = X_COLOR

    pygame.draw.line(screen, color, (WINNER_LINE_WIDTH, HEIGHT-WINNER_LINE_WIDTH), (WIDTH-WINNER_LINE_WIDTH, WINNER_LINE_WIDTH), WINNER_LINE_WIDTH)
    

def draw_diag2_winning_line(player):
    if player == 2:
        color = O_COLOR
    elif player == 1:
        color = X_COLOR

    pygame.draw.line(screen, color, (WINNER_LINE_WIDTH, WINNER_LINE_WIDTH), (WIDTH-WINNER_LINE_WIDTH, HEIGHT-WINNER_LINE_WIDTH), WINNER_LINE_WIDTH)

# Restarts the game (press 'r' after a game ends)
def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0

# Quits the window (press 'q' after a game ends)
def quit():
    sys.exit()

draw_lines()

player = 1 # X is 1, O is 2
game_over = False

# Mainloop
while True:
    for event in pygame.event.get():
        
        if event.type == pygame.KEYDOWN:
            # If user enters 'r' after ending a game or while playing a game, the game restarts
            if event.key == pygame.K_r:
                restart()
                game_over = False

            # If user enters 'q' after ending a game or while playing a game, they exit the game
            elif event.key == pygame.K_q:
                quit()

        if event.type == pygame.QUIT:
            sys.exit()
    
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0] # for x coordinates
            mouseY = event.pos[1] # for y coordinates

            clicked_row = int(mouseY // SQUARE_SIZE) # To get a result between 0 and 2 so it matches out board
            clicked_col = int(mouseX // SQUARE_SIZE)

            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                if check_win(player):
                    game_over = True

                player = player % 2 + 1
                
                draw_figures()   

    pygame.display.update()