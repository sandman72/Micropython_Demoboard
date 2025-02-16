# Bibliotheken laden
# import libs
from machine import Pin
from neopixel import NeoPixel
from time import sleep_ms

# NeoPixel/WS2812 LED Streifen mit GPIO 28 initialisieren 
# initialize NeoPixel/WS2812 LED Strip on GPIO 28 
neopin = Pin(28, Pin.OUT)

# Anzahl der LEDs
# Number of LEDs
leds = 5

# Max. Helligkeit: 0 bis 255
# Max. Brightness: 0 to 255
brightness = 30

# Geschwindigkeit (Millisekunden)
# Speed in milli seconds
speed = 50

# Initialisierung WS2812/NeoPixel
# initialize WS2812/NeoPixel
pixels = NeoPixel(neopin, leds)

# Endlosschleife LEDs abwechselnd einschalten
# endless loop turning on LEDs
while True:
    for i in range (leds):
        # Nächste LED einschalten  (R,G,B)
        # turn on next LED         (R,G,B)
        pixels[i] = (brightness, brightness, brightness)
        pixels.write()
        # kurz warten
        # short delay
        sleep_ms(speed)
        # LED wieder zurücksetzen
        # reset LED
        pixels[i] = (0, 0, 0)