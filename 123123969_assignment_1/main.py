import pygame
import os
import random
from pacman import Pacman
from ghost import Ghost
from food import Food

pygame.init()

# - SET UP PARAMETERS FOR DISPLAY WINDOW
DISPLAY_WIDTH = 300
DISPLAY_HEIGHT = 300
DISPLAY_SIZE = [DISPLAY_WIDTH, DISPLAY_HEIGHT]
display = pygame.display.set_mode(DISPLAY_SIZE)
clock = pygame.time.Clock()
# -- display_colour
DISPLAY_COLOUR = [0, 0, 0]

# - SET UP PACMAN
SPEED_PAC_X = 3
SPEED_PAC_Y = 3
move_down = False
move_up = False
move_left = False
move_right = False
# -- instantiate Pacman Class
pac = Pacman(DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 4, SPEED_PAC_X, SPEED_PAC_Y)

# - SET UP GHOST
SPEED_GHOST_X = 2
SPEED_GHOST_Y = 2
GHOST_COLOUR = [255, 0, 255]
# -- instantiate Ghost Class
ghost = Ghost(DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2, GHOST_COLOUR, SPEED_GHOST_X, SPEED_GHOST_Y)

# - SET UP FOOD
FOOD_COLOUR = [255, 255, 255]
FOOD_HEIGHT = 10
FOOD_WIDTH = 10
# -- instantiate Food Class
food = Food(FOOD_WIDTH, FOOD_HEIGHT, FOOD_COLOUR)
# -- set food coordinates before drawing
food.relocate(DISPLAY_WIDTH, DISPLAY_HEIGHT)

# --------------------------------------   GAME LOOP   ---------------------------------------
run_game = True
while run_game:
    
    # - DRAW THE FIGURES
    display.fill(DISPLAY_COLOUR)
    food.draw(display)
    pac.draw(display)
    ghost.draw(display)

    # - PRINT THE STRING REPRESENTATIOS IN THE STANDARD OUTPUT
    # -- cls to clean the termial in Windows
    # -- clear to clean the terminal in Linux
    #os.system('cls')
    os.system('clear')
    print(pac.__str__() + "\n")
    print(ghost.__str__() + "\n")
    print(food.__str__() + "\n")
    
    # - KEYBOARD EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                move_down = True
                move_up = False
                move_left = False
                move_right = False
            if event.key == pygame.K_UP:
                move_up = True
                move_down = False
                move_left = False
                move_right = False
            if event.key == pygame.K_LEFT:
                move_left = True
                move_up = False
                move_down = False
                move_right = False
            if event.key == pygame.K_RIGHT:
                move_right = True
                move_left = False
                move_up = False
                move_down = False               
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                move_down = False
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False

    # - DETERMINE NEXT PACMAN POSITION
    if move_down:
        pac.move_down(DISPLAY_HEIGHT)   
    elif move_up:
        pac.move_up(DISPLAY_HEIGHT)
    elif move_right:
        pac.move_right(DISPLAY_WIDTH)
    elif move_left:
        pac.move_left(DISPLAY_WIDTH)

    # - DETERMINE NEXT GHOST POSITION
    # -- Determine the next y-axis ghost position
    if abs(ghost.get_y() - SPEED_GHOST_Y - pac.get_y()) < abs(ghost.get_y() - pac.get_y()):
        ghost.move("UP", DISPLAY_WIDTH, DISPLAY_HEIGHT)
    elif abs(ghost.get_y() + SPEED_GHOST_Y - pac.get_y()) < abs(ghost.get_y() - pac.get_y()):
        ghost.move("DOWN", DISPLAY_WIDTH, DISPLAY_HEIGHT)
    # -- Determine the next x-axis ghost position
    if abs(ghost.get_x() - SPEED_GHOST_X - pac.get_x()) < abs(ghost.get_x() - pac.get_x()):
        ghost.move("LEFT", DISPLAY_WIDTH, DISPLAY_HEIGHT)
    elif abs(ghost.get_x() + SPEED_GHOST_X - pac.get_x()) < abs(ghost.get_x() - pac.get_x()):
        ghost.move("RIGHT", DISPLAY_WIDTH, DISPLAY_HEIGHT)
    
    clock.tick(45)
    pygame.display.update()
# ------------------------------------   END GAME LOOP   -------------------------------------   
pygame.quit()
quit()
