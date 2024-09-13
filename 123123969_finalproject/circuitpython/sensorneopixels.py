from adafruit_circuitplayground import cp
import time

class LightDisplay:

    __lights_off = [0, 0, 0]

    def __init__(self, brightness):
        cp.pixels.brightness = brightness
        self.__pixels_count = len(cp.pixels)
        cp.pixels.auto_write = False

    def light_scale(self, blue, side):
        cp.pixels.fill(SensorLightDisplay.__lights_off)
        colour_range = 255
        if side == 0:
            pass  
        else:
            i = 0
            while blue > 0:
                if blue > colour_range:
                    shade = colour_range
                else:
                    shade = blue
                if side == 1:
                    cp.pixels[7-i] = shade
                    cp.pixels[7+i] = shade
                elif side == 2:
                    cp.pixels[2-i] = shade
                    cp.pixels[2+i] = shade
                elif side == 3:
                    cp.pixels[4-i] = shade
                    cp.pixels[5+i] = shade
                elif side == 4:
                    cp.pixels[9-i] = shade
                    cp.pixels[0+i] = shade
                i += 1
                blue -= colour_range
        cp.pixels.show()
            

class SensorLightDisplay(LightDisplay):
    def __init__(self, brightness):
        super().__init__(brightness)

    def advanced_control_feedback(self, acceleration):
        limit = 9.81
        blue_total = 255 * 2 # colour range of pixel * 2 levels of pixels 
        x = acceleration[0]
        y = acceleration[1]
        if y < 0:
           flipped_y = (-1) * y
        else:
            flipped_y = y
        if x < 0:
           flipped_x = (-1) * x
        else:
            flipped_x = x
       
        if flipped_y <= limit and flipped_x <= limit:
            if x < -3 and x < y:
                blue = int((flipped_x-3) * blue_total / (limit-3))
                self.light_scale(blue, 1)

            elif x > 3 and x > y:
                blue = int((flipped_x-3) * blue_total / (limit-3))
                self.light_scale(blue, 2)
            
            elif y > 3 and y > x:
                blue = int((flipped_y-3) * blue_total / (limit-3))
                self.light_scale(blue, 3)
                
            elif y < -3 and y < x:
                blue = int((flipped_y-3) * blue_total / (limit-3))
                self.light_scale(blue, 4)
            else:
                self.light_scale(0, 0)
