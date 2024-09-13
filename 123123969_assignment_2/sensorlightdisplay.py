from adafruit_circuitplayground import cp
import time

class SensorLightDisplay:

    __lights_off = [0, 0, 0]

    def __init__(self, brightness): 
        cp.pixels.brightness = brightness
        self.__pixels_count = len(cp.pixels)
        cp.pixels.auto_write = False

    def light(self, acceleration, colour):
        cp.pixels.fill(SensorLightDisplay.__lights_off)
        x = acceleration[0]
        y = acceleration[1]
        if x < -3 and x < y:
            for i in range(6, 9):
                cp.pixels[i] = colour
        elif x > 3 and x > y:
            for i in range(1, 4):
                cp.pixels[i] = colour
        elif y > 3 and y > x:
            for i in range(4, 6):
                cp.pixels[i] = colour
        elif y < -3 and y < x:
            for i in range(-1, 1):
                cp.pixels[i % self.__pixels_count] = colour
        cp.pixels.show()

    def control_feedback_y(self, acceleration_y):
        cp.pixels.fill(SensorLightDisplay.__lights_off)
        limit = 9.81
        colour_range = 255
        if acceleration_y < 0:
           abs_y = (-1) * acceleration_y
        else:
            abs_y = acceleration_y
        if abs_y <= limit:
            blue = (colour_range * abs_y / limit)
            cp.pixels.fill([0, 0, blue])
        cp.pixels.show()
