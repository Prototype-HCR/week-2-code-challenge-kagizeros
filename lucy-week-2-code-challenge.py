import board
import time
from digitalio import DigitalInOut, Direction, Pull
import neopixel

# create a neopixel object
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
pixels.brightness = 0.1
# create a color as a tuple value
red = 0xff0000
green = 0x00ff00
blue = 0x0000ff
# pixels[9] = ac_orange
# pixels[1] = 0x0000ff
time.sleep(5)


# declare a digitial input
button_a = DigitalInOut(board.BUTTON_A)
button_a.switch_to_input(pull=Pull.DOWN)

button_b = DigitalInOut(board.BUTTON_B)
button_b.switch_to_input(pull=Pull.DOWN)


# A variable to track the LED led state
led_state_A = True
led_state_B = True


while True:
    # gather all input values from sensors
    # print the value of our button_a object
    button_a_read = button_a.value
    print("button a read is:", button_a_read)
    button_b_read = button_b.value
    print("button a read is:", button_b_read)

    # set variables based on the value of your inputs
    if button_a_read == True:
        led_state_A = True
    else:
        led_state_A = False
    if button_b_read == True:
        led_state_B = True
    else:
        led_state_B = False

    if led_state_A & led_state_B == True:
        pixels.fill(green)
    elif led_state_A == True:
        pixels.fill(red)
    elif led_state_B == True:
        pixels.fill(blue)
    else:
        pixels.fill(0)
        # turn the neopixels off

    # set outputs based on the value of my variables

