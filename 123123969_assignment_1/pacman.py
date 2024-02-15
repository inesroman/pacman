import pygame

class Pacman:

    # Constructor of Pacman class
    def __init__(self, x, y, speed_x, speed_y):
        # initialisation of private class variables:
        self.__colour = [255, 255, 0]  # Yellow color for Pacman
        self.__radius = 10             # Radius of Pacman
        self.__x = x                   # initial x-coordinate
        self.__y = y                   # initial y-coordinate
        self.__speed_x = speed_x       # horizontal speed  
        self.__speed_y = speed_y       # vertical speed

    # Returns string representation of Pacman.
    def __str__(self):
        return "Pacman: colour = yellow, x = " + str(self.__x) + ", y = " + str(self.__y)
    
    # Method that draws Pacman on the pygame display.
    def draw(self, display):
        pygame.draw.circle(display, self.__colour, [self.__x, self.__y], self.__radius)

    # Move Pacman downwards on the display.
    def move_down(self, display_height):
        self.__y = self.__y + self.__speed_y
        if self.__y > display_height + self.__radius:
            self.__y = - self.__radius

    # Move Pacman upwards on the display.
    def move_up(self, display_height):
        self.__y = self.__y - self.__speed_y
        if self.__y < - self.__radius:
            self.__y = display_height + self.__radius

    # Move Pacman leftwards on the display.
    def move_left(self, display_width):
        self.__x = self.__x - self.__speed_x
        if self.__x < - self.__radius:
            self.__x = display_width + self.__radius

    # Move Pacman rightwards on the display.
    def move_right(self, display_width):
        self.__x = self.__x + self.__speed_x
        if self.__x > display_width + self.__radius:
            self.__x = - self.__radius

    # Returns the y-coordinate of Pacman.
    def get_y(self):
        return self.__y
    
    # Returns the x-coordinate of Pacman.
    def get_x(self):
        return self.__x
    
    # Returns the radius of Pacman.
    def get_size(self):
        return self.__radius
    