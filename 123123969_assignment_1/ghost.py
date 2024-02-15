import pygame
import random 

class Ghost:

    # Constructor of Ghost class
    def __init__(self, x, y, colour, speed_x, speed_y):
        # initialisation of private class variables:
        self.__x = x                # initial x-coordinate
        self.__y = y                # initial x-coordinate
        self.__radius = 10          # ghost radius
        self.__colour = colour      # ghost colour
        self.__speed_x = speed_x    # horizontal speed  
        self.__speed_y = speed_y    # vertical speed

    # Returns string representation of the ghost.
    def __str__(self):
        return "Ghost: colour = " + str(self.__colour) + ", x = " + str(self.__x) + ", y = " + str(self.__y)
    
    # Method that draws the ghost on the pygame display.
    def draw(self, display):
        pygame.draw.circle(display, self.__colour, [self.__x, self.__y], self.__radius)

    # Method that moves the ghost upward, downwards, leftwards or rightwards on the display.
    def move(self,direction, display_width=None, display_height=None):
        if direction == "UP":
            self.__y = self.__y - self.__speed_y
            if self.__y < - self.__radius + 1:
                self.__y = - self.__radius + 1
        elif direction == "DOWN":
            self.__y = self.__y + self.__speed_y
            if self.__y > display_height + self.__radius - 1:
                self.__y = display_height + self.__radius - 1
        elif direction == "LEFT":
            self.__x = self.__x - self.__speed_x
            if self.__x < - self.__radius + 1:
                self.__x = - self.__radius + 1
        elif direction == "RIGHT":
            self.__x = self.__x + self.__speed_x
            if self.__x > display_width + self.__radius - 1:
                self.__x = display_width + self.__radius - 1

    # Returns the y-coordinate of the ghost.
    def get_y(self):
        return self.__y
    
    # Returns the x-coordinate of the ghost.
    def get_x(self):
        return self.__x
    
    # Returns the radius of the ghost.
    def get_size(self):
        return self.__radius

    # Method that randomly relocates the ghost within the display boundaries.
    def relocate(self, display_width, display_height):
        self.__x = random.randint(self.__radius, display_width - self.__radius)
        self.__y = random.randint(self.__radius, display_height - self.__radius)
