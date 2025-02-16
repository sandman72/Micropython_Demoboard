#
# *****   Boot Menü für Demo Board   *****
#
# von Frank Hellmann 2023
# für das Attraktor MicroPython Demo Board

# Bibliotheken laden
# import libs
from machine import Pin, PWM, I2C, Timer
import framebuf
import ssd1306
import time

# global variables
SCREEN_WIDTH = 128
SCREEN_HEIGHT = 64

# Initialiere Pins
speaker = PWM(Pin(10))
i2c = I2C(0, sda=Pin(20), scl=Pin(21))
oled = ssd1306.SSD1306_I2C(SCREEN_WIDTH, SCREEN_HEIGHT, i2c)
oled.fill(0)

# Buttons
up    = Pin(11, Pin.IN, Pin.PULL_DOWN)
left  = Pin(12, Pin.IN, Pin.PULL_DOWN)
right = Pin(13, Pin.IN, Pin.PULL_DOWN)
down  = Pin(14, Pin.IN, Pin.PULL_DOWN)
enter = Pin(15, Pin.IN, Pin.PULL_DOWN)

# Load Bitmap Logo and display
with open('lib/attraktor_logo.pbm', 'rb') as f:
    f.readline() # Dummy read Magic number
    f.readline() # Dummy read Creator comment
    #f.readline() # Dummy read Dimensions
    data = bytearray(f.read())
    fbuf = framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)

oled.blit(fbuf, 0, 0)
oled.text("Micropython", 36, 4)
oled.text("Demos", 84, 14)
oled.text("V1.1", 92, 24)
oled.show()

# Wait two seconds
time.sleep(2)

# Display menu
menu = 0
oled.fill(0)
oled.text("MicroPython Demos", 0, 4)
oled.text("Flappy Bird", 12, 14)
oled.text("Pong", 12, 24)
oled.text("Snake", 12, 34)
oled.text("Space Invaders", 12, 44)
oled.text("Board Test", 12, 54)
oled.show()

while True:
    # if down button is pressed move selector
    if down.value() == 1:
        menu=menu+1
        if menu>4:
            menu = 0
        time.sleep_ms(100)

    # if up button is pressed move selector
    if up.value() == 1:
        menu=menu-1
        if menu<0:
            menu = 4
        time.sleep_ms(100)
    
    # if enter or left button is pressed boot into game
    if enter.value() == 1 or right.value() == 1:
        oled.fill(0)
        oled.show()
        if menu == 0:
           exec(open("Games/Flappy_Bird.py").read())
        elif menu == 1:
           exec(open("Games/Pong.py").read())
        elif menu == 2:
           exec(open("Games/Snake.py").read())
        elif menu == 3:
           exec(open("Games/Space_Invaders.py").read())
        elif menu == 4:
           exec(open("Tests/Board_Test.py").read())

    # if left button is pressed boot into REPL
    if left.value() == 1:
        oled.fill(0)
        oled.text("MicroPython", 20, 24)
        oled.text("REPL activ",  24, 34)
        oled.show()
        exit()

    # Draw selector
    oled.fill_rect(0, 14, 11, 63, 0)
    oled.text(">", 2, (menu*10)+14)
    oled.show()
    
    time.sleep_ms(100)