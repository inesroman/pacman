import pygame
import random 

class Food:

    # Constructor of Food class:
    def __init__(self, width, height, colour):
        # initialisation of private class variables:
        self.__height = height    # height of the food item 
        self.__width = width      # width of the food item 
        self.__colour = colour    # colour of the food item
        self.__y = 0              # y-coordinate of the food
        self.__x = 0              # x-coordinate of the food

    # Returns string representation of the ghost.
    def __str__(self):
        return "Food: colour = " + str(self.__colour) + ", x = " + str(self.__x) + ", y = " + str(self.__y)
    
    # Method that draws the food on the pygame display.
    def draw(self, display):
        pygame.draw.rect(display, self.__colour, [self.__x, self.__y, self.__width, self.__height])

    # Returns the y-coordinate of the food.
    def get_y(self):
        return self.__y
    
    # Returns the y-coordinate of the food.
    def get_x(self):
        return self.__x
    
    # Returns the height of the food.
    def get_height(self):
        return self.__height

    # Returns the width of the food.
    def get_width(self):
        return self.__width

    # Method that randomly relocates the food within the display boundaries.
    def relocate(self, display_width, display_height):
        self.__x = random.randint(0, display_width - self.__width)
        self.__y = random.randint(0, display_height - self.__height)

    # Method that randomly assigns new values to the height and the width of the food
    def change_size(self, lower_limit, upper_limit):
        self.__height = random.randint(lower_limit, upper_limit)
        self.__width = random.randint(lower_limit, upper_limit)
