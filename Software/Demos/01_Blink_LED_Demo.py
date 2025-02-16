# Bibliotheken laden
# import libs 
from machine import Pin
import time

# GPIO22 als Ausgang für blaue LED initialisieren
# initialize GPIO22 as output for blue LED
led = Pin(22, Pin.OUT)
    
# Endlosschleife LED blinken lassen
# endless loop blinks LED
while True:
    # LED einschalten
    # turn on LED
    led.on()
    # Warte eine halbe Sekunde
    # Wait half a second
    time.sleep(0.5)

    # LED ausschalten
    # turn off LED
    led.off()
    # Warte eine halbe Sekunde
    # Wait half a second
    time.sleep(0.5)
    