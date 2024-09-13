from adafruit_circuitplayground import cp
import time
import random

class LightDisplay:

    __lights_off = [0, 0, 0]

    def __init__(self, brightness):
        cp.pixels.brightness = brightness
        self.__pixels_count = len(cp.pixels)
        cp.pixels.auto_write = False

    def half_pattern(self, colour):
        cp.pixels.fill(LightDisplay.__lights_off)
        for i in range(self.__pixels_count//2):
            cp.pixels[i] = colour
            cp.pixels[self.__pixels_count-i-1] = colour
            cp.pixels.show()
            time.sleep(0.2)

    def light(self, side, colour):
        cp.pixels.fill(LightDisplay.__lights_off)
        if side == 0:
            for i in range(1, 4):
                cp.pixels[i] = colour
        elif side == 1:
            for i in range(6, 9):
                cp.pixels[i] = colour
        elif side == 2:
            for i in range(4, 6):
                cp.pixels[i] = colour
        elif side == 3:
            for i in range(-1, 1):
                cp.pixels[i % self.__pixels_count] = colour
        cp.pixels.show()

    def random_light(self, colour, sec_interval):
        cp.pixels.fill(LightDisplay.__lights_off)
        pixel = random.randint(0, 9)
        for i in range(5):
            cp.pixels[pixel] = colour
            cp.pixels.show()
            time.sleep(sec_interval)
            cp.pixels[pixel] = LightDisplay.__lights_off
            cp.pixels.show()
            time.sleep(sec_interval)

    def snake(self, snake_size, colour, interval):
        if snake_size > 1 and snake_size <= self.__pixels_count // 2:
            for i in range(self.__pixels_count-snake_size+1):
                cp.pixels.fill(LightDisplay.__lights_off)
                for j in range(i, i + snake_size):
                    cp.pixels[j] = colour
                cp.pixels.show()
                time.sleep(interval)

