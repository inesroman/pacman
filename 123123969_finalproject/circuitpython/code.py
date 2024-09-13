from adafruit_circuitplayground import cp
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from sensorneopixels import SensorLightDisplay
import time
import usb_hid


sld = SensorLightDisplay(0.1)
kbd = Keyboard(usb_hid.devices)

while True:
    x = cp.acceleration[0]
    y = cp.acceleration[1]
    if x < -3 and x < y:
        kbd.press(Keycode.LEFT_ARROW)
        kbd.release(Keycode.UP_ARROW)
        kbd.release(Keycode.RIGHT_ARROW)
        kbd.release(Keycode.DOWN_ARROW)
    elif x > 3 and x > y:
        kbd.release(Keycode.LEFT_ARROW)
        kbd.release(Keycode.UP_ARROW)
        kbd.press(Keycode.RIGHT_ARROW)
        kbd.release(Keycode.DOWN_ARROW)
    elif y > 3 and y > x:
        kbd.release(Keycode.LEFT_ARROW)
        kbd.press(Keycode.UP_ARROW)
        kbd.release(Keycode.RIGHT_ARROW)
        kbd.release(Keycode.DOWN_ARROW)
    elif y < -3 and y < x:
        kbd.release(Keycode.LEFT_ARROW)
        kbd.release(Keycode.UP_ARROW)
        kbd.release(Keycode.RIGHT_ARROW)
        kbd.press(Keycode.DOWN_ARROW)
    else:
        kbd.release(Keycode.LEFT_ARROW)
        kbd.release(Keycode.UP_ARROW)
        kbd.release(Keycode.RIGHT_ARROW)
        kbd.release(Keycode.DOWN_ARROW)

    sld.advanced_control_feedback(cp.acceleration)

    time.sleep(0.1)
