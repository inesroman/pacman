from adafruit_circuitplayground import cp
from lightdisplay import LightDisplay
from sensorlightdisplay import SensorLightDisplay
import time

orange = [255, 63, 0]
cyan = [0, 165, 255]
yellow = [255, 165, 0]
pink = [255, 63, 63]
magenta = [255, 0, 255]

# -------------    VARIABLE TEST   -------------------
# The different values of the TEST variable will
# execute the methods of the classes LightDisplay and
# SensorLightDisplay:
# - TEST = 0    half_pattern        LightDisplay
# - TEST = 1    snake               LightDisplay
# - TEST = 2    light               LightDisplay
# - TEST = 3    random_light        LightDisplay
# - TEST = 4    light               SensorLightDisplay
# - TEST = 5    control_feedback_y  SensorLightDisplay
# -----------------------------------------------------
TEST = 1

ld = LightDisplay(0.1)
sld = SensorLightDisplay(0.1)

while True:
    if TEST == 0:
        ld.half_pattern(orange)
    if TEST == 1:
        for i in range(6):
            ld.snake(i, cyan, 0.3)
    if TEST == 2:
        for i in range(4):
            ld.light(i, yellow)
            time.sleep(0.3)
    if TEST == 3:
        ld.random_light(magenta, 0.3)
    if TEST == 4:
        sld.light(cp.acceleration, pink)
    if TEST == 5:
        sld.control_feedback_y(cp.acceleration[1])

    time.sleep(0.1)


