#
#      MicroPython Demo Board
#        Hardware Test Code
#           Version 1.1
#
#    by Frank Hellmann, 06.2024
#

# Bibliotheken laden
# import libs
from machine import Pin, I2C, SPI, PWM
from utime import sleep
from neopixel import NeoPixel
from ssd1306 import SSD1306_I2C
from bmp280_spi import BMP280SPI

print("MicroPython Demoboard Test")

# Schalte onboard LED auf Pi Pico Modul ein
# turn on onboard LED on Pi Pico module
onboard_led = Pin("LED", Pin.OUT)
onboard_led.on() 
print("Pi Pico Module: OK")

# GPIO Pins als Eingänge mit Pull_Down initalisieren
# initialize GPIO Pins as inputs with Pull_Down enabled
button_up     = Pin(11, Pin.IN, Pin.PULL_DOWN)
button_left   = Pin(12, Pin.IN, Pin.PULL_DOWN)
button_right  = Pin(13, Pin.IN, Pin.PULL_DOWN)
button_down   = Pin(14, Pin.IN, Pin.PULL_DOWN)
button_center = Pin(15, Pin.IN, Pin.PULL_DOWN)

## NEOPIXEL TEST
# NeoPixel/WS2812 LED Streifen mit GPIO 28 initialisieren
# initialize NeoPixel/WS2812 LED strip on GPIO 28 to show status
pixels = NeoPixel(Pin(28, Pin.OUT), 5)
pixels.fill((30,30,30))
pixels.write()
print("Neopixel: OK")

## OLED TEST
# OLED Display am I2C Bus initialisieren
# initialize OLED Display on I2C Bus
try:
    i2c = I2C(0, sda=Pin(20), scl=Pin(21))
    oled = SSD1306_I2C(128, 64, i2c)
    # OLED Display löschen und Text anzeigen
    # clear OLED display and show text
    oled.fill(0)
    oled.text("Attraktor e.V.", 10, 0)
    oled.text("PWM Testing", 10, 32)
    oled.show()
    print("OLED Display: OK")
except:
    pixels.fill((30,0,30))
    pixels.write()
    print("OLED Display: failed")
    while True:
        sleep(1)

## PWM LED Test
pwm = PWM(Pin(22))
pwm.freq(4000)
pwm.duty_u16(8000)

## Buzzer Test
buzzer = PWM(Pin(10))
buzzer.freq(1000)
buzzer.duty_u16(1000)
sleep(0.3)
print("Buzzer: OK")

## ADC Tests
potentiometer = machine.ADC(26)
ldr = machine.ADC(27)

## OLED Display löschen und Text anzeigen
oled.fill(0)
oled.text("Attraktor e.V.", 10, 0)
oled.text("SPI Testing", 10, 32)
oled.show()

## SPI BPM280 Test
try:
    spi = SPI(0, sck=Pin(18), mosi=Pin(19), miso=Pin(16), polarity=1, phase=1)
    spi_cs = Pin(17, Pin.OUT, value=1)
    bmp280_spi = BMP280SPI(spi, spi_cs)
    # Die BMP280 Chip ID Auslesen. Sollte 0x58 sein
    print("BMP280 Chip ID (0x58): "+bmp280_spi.chip_id)
    readout = bmp280_spi.measurements
    print(f"Temperature: {readout['t']} °C, pressure: {readout['p']} hPa.")
    pixels.fill((10,10,30))
    pixels.write()
    print("BMP280: OK\n")
except:
    pixels.fill((30,0,0))
    pixels.write()
    print("BMP280: failed\n")

# Test Loop for Keys and Temp
while True:
    oled.fill(0)
    oled.text("Attraktor e.V.", 10, 0)
    
    # Wenn BMP280 Sensor gefunden wurde, die Messwerte anzeigen
    # If we found the BMP280 sensor display the measurements
    if bmp280_spi.chip_id == "0x58":
        readout = bmp280_spi.measurements
        oled.text(f"{readout['t']:.1f}C {readout['p']:.1f}hPa", 2,12)
    else:
        oled.text("No BPM280 Sensor", 2,12)   
    
    # ADC Werte anzeigen 0-1023
    oled.text("LDR "+str(int(ldr.read_u16()/64)), 2, 24)
    oled.text("PT  "+str(int(potentiometer.read_u16()/64)), 2, 36)

    # LED per PWM setzen
    pwm.duty_u16(potentiometer.read_u16())
    
    # Buttons
    if button_up.value() == 1:
        print("Up Button is Pressed")
        oled.fill_rect(90,24,8,8,1)
    else:
        oled.rect(90,24,8,8,1)
    if button_left.value() == 1:
        print("Left Button is Pressed")
        oled.fill_rect(80,34,8,8,1)
    else:
        oled.rect(80,34,8,8,1)
    if button_right.value() == 1:
        print("Right Button is Pressed")
        oled.fill_rect(100,34,8,8,1)
    else:
        oled.rect(100,34,8,8,1)
    if button_down.value() == 1:
        print("Down Button is Pressed")
        oled.fill_rect(90,44,8,8,1)
    else:
        oled.rect(90,44,8,8,1)
    if button_center.value() == 1:
        print("Center Button is Pressed")
        oled.fill_rect(90,34,8,8,1)
        buzzer.duty_u16(1000)
    else:
        oled.rect(90,34,8,8,1)
        buzzer.duty_u16(0)

    oled.show()
    sleep(0.1)
