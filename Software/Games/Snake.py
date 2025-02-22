#
# *****     Snake     *****
#
# gespielt wird mit den Buttons
#
# Adaptiert von Frank Hellmann 2023
# für das Attraktor MicroPython Demo Board
#
# Original source code from
# https://github.com/YouMakeTech/PicoRetroGamingSystem
# https://github.com/Twan37/PicoSnake

# Bibliotheken laden
from machine import Pin, PWM, I2C, Timer
import ssd1306
import time
import random

# global variables
SCREEN_WIDTH = 128
SCREEN_HEIGHT = 64

SEGMENT_WIDTH = 8
SEGMENT_PIXELS = int(SCREEN_HEIGHT/SEGMENT_WIDTH)
SEGMENTS_HIGH = int(SCREEN_HEIGHT/SEGMENT_WIDTH)
SEGMENTS_WIDE = int(SCREEN_WIDTH/SEGMENT_WIDTH)
VALID_RANGE = [[int(i /SEGMENTS_HIGH), i % SEGMENTS_HIGH] for i in range(SEGMENTS_WIDE * SEGMENTS_HIGH -1)]

game_timer = Timer()
player = None
food = None

# Initialiere Pins
speaker = PWM(Pin(10))
i2c = I2C(0, sda=Pin(20), scl=Pin(21))
oled = ssd1306.SSD1306_I2C(SCREEN_WIDTH, SCREEN_HEIGHT, i2c)
oled.fill(0)

# Buttons
up = Pin(11, Pin.IN, Pin.PULL_DOWN)
down = Pin(14, Pin.IN, Pin.PULL_DOWN)
left = Pin(12, Pin.IN, Pin.PULL_DOWN)
right = Pin(13, Pin.IN, Pin.PULL_DOWN)
button1 = Pin(15, Pin.IN, Pin.PULL_DOWN)

# Game code
class Snake:
    up = 0
    down = 1
    left = 2
    right = 3
    
    def __init__(self, x=int(SEGMENTS_WIDE/2), y=int(SEGMENTS_HIGH/2) + 1):
        self.segments = [[x, y]]
        self.x = x
        self.y = y
        self.dir = random.randint(0,3)
        self.state = True
        
    def reset(self, x=int(SEGMENTS_WIDE/2), y=int(SEGMENTS_HIGH/2) + 1):
        self.segments = [[x, y]]
        self.x = x
        self.y = y
        self.dir = random.randint(0,3)
        self.state = True
        
    def move(self):
        new_x = self.x
        new_y = self.y
        
        if self.dir == Snake.up:
            new_y -= 1
        elif self.dir == Snake.down:
            new_y += 1
        elif self.dir == Snake.left:
            new_x -= 1
        elif self.dir == Snake.right:
            new_x += 1
        
        for i, _ in enumerate(self.segments):
            if i != len(self.segments) - 1:
                self.segments[i][0] = self.segments[i+1][0]
                self.segments[i][1] = self.segments[i+1][1]
        
        if self._check_crash(new_x, new_y):
            # Oh no, we killed the snake :C
            if self.state == True:
                # play an ugly sound
                speaker.freq(200)
                speaker.duty_u16(2000)
                time.sleep(0.5)
                speaker.duty_u16(0)
            self.state = False
        
        self.x = new_x
        self.y = new_y
        
        self.segments[-1][0] = self.x
        self.segments[-1][1] = self.y
        
    def eat(self):
        oled.fill_rect(self.x * SEGMENT_PIXELS, self.y * SEGMENT_PIXELS, SEGMENT_PIXELS, SEGMENT_PIXELS, 0)
        oled.rect(self.x * SEGMENT_PIXELS, self.y * SEGMENT_PIXELS, SEGMENT_PIXELS, SEGMENT_PIXELS, 1)
        self.segments.append([self.x, self.y])
        # Make a sound
        speaker.freq(1000)
        speaker.duty_u16(2000)
        time.sleep(0.100)
        speaker.duty_u16(0)
        
    def change_dir(self, dir):
        if  dir == Snake.down and self.dir == Snake.up:
            return False
        
        elif dir == Snake.up and self.dir == Snake.down:
            return False
        
        elif dir == Snake.right and self.dir == Snake.left:
            return False
        
        elif dir == Snake.left and self.dir == Snake.right:
            return False
        
        self.dir = dir
        
    def _check_crash(self, new_x, new_y):
        if new_y >= SEGMENTS_HIGH or new_y < 0 or new_x >= SEGMENTS_WIDE or new_x < 0 or [new_x, new_y] in self.segments:
            return True
        else:
            return False
    
    def draw(self):
        oled.rect(self.segments[-1][0] * SEGMENT_PIXELS, self.segments[-1][1] * SEGMENT_PIXELS, SEGMENT_PIXELS, SEGMENT_PIXELS, 1)

def update_game(timer):
    global food
    global player
    
    # Remove the previous tail of the snake (more effecient than clearing the entire screen and redrawing everything)
    oled.fill_rect(player.segments[0][0] * SEGMENT_PIXELS, player.segments[0][1] * SEGMENT_PIXELS, SEGMENT_PIXELS, SEGMENT_PIXELS, 0)
    
    # Move the snake
    player.move()
    
    if player.state == True:
        # Our snake is still alive and moving
        if food[0] == player.x and food[1] == player.y:
            # Our snake reached the food
            player.eat()
            food = random.choice([coord for coord in VALID_RANGE if coord not in player.segments])
            oled.fill_rect(food[0] * SEGMENT_PIXELS , food[1] * SEGMENT_PIXELS, SEGMENT_PIXELS, SEGMENT_PIXELS, 1)
        
        player.draw()
        
    # Show the new frame
    oled.rect(0,0,SCREEN_WIDTH,SCREEN_HEIGHT,1)
    oled.show()

def pico_snake_main():
    global player
    global food
    
    player = Snake()
    food = random.choice([coord for coord in VALID_RANGE if coord not in player.segments])
    oled.fill_rect(food[0] * SEGMENT_PIXELS , food[1] * SEGMENT_PIXELS, SEGMENT_PIXELS, SEGMENT_PIXELS, 1)
    
    # Playing around with this cool timer.
    game_timer.init(freq=5, mode=Timer.PERIODIC, callback=update_game)
    
    while True:
        if player.state == True:
            # If the snake is alive
            if up.value() == 1:
                    player.change_dir(Snake.up)
                    
            elif right.value() == 1:
                    player.change_dir(Snake.right)
                    
            elif left.value() == 1:
                    player.change_dir(Snake.left)
                    
            elif down.value() == 1:
                    player.change_dir(Snake.down)
        
        else:
            # The snake is dead
            
            # disable the timer
            game_timer.deinit()
            
            # display Game Over
            oled.fill(0)
            oled.text("Game Over!" , int(SCREEN_WIDTH/2) - int(len("Game Over!")/2 * 8), int(SCREEN_HEIGHT/2) - 8)
            oled.text("Snake length:" + str(len(player.segments)) , int(SCREEN_WIDTH/2) - int(len("Snake length:" + str(len(player.segments))) /2 * 8), int(SCREEN_HEIGHT/2) + 16)
            oled.show()
            
            # wait for a button
            while button1.value()==0:
                time.sleep(0.01)
            
            # exit the loop and restart the game
            oled.fill(0)
            break
                
while True:
    pico_snake_main()