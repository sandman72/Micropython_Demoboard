# Bibliotheken laden
# import libs 
from machine import Pin, PWM
from time import sleep

# Blaue LED an GPIO22 mit PWM initialisieren
# initialize GPIO22 as PWM output for blue LED
pwm = PWM(Pin(22))

# PWM Frequenz (Hz) einstellen
# set PWM frequency (Hz)
pwm.freq(4000)

# Endlosschleife LED Helligkeit hoch/runterfahren
# endless loop fading LED brightness up and down
while True:
  # Helligkeit hoch fahren
  # fade up brightness
  for duty_cycle in range(0, 65536, 129):
    pwm.duty_u16(duty_cycle)
    sleep(0.005)
    
  # Helligkeit runter fahren
  # fade down brightness
  for duty_cycle in range(65536, 0, -129):
    pwm.duty_u16(duty_cycle)
    sleep(0.005)
