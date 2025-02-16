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

# Analog/Digital Wandler ADC0 GPIO 26 initialisieren
# an ADC 0 hängt das einstellbare Potentiometer RV1
# initialize analog/digital converter on ADC0 GPIO 26
# where the RV1 potentiometer is connected to
potentiometer = machine.ADC(26)

# Endlosschleife ADC0 auslesen und damit LED PWM Helligkeit einstellen
# endless loop reading the potentiometer value and adjusting the LED brightness via PWM
while True:
    pwm.duty_u16(potentiometer.read_u16())
    sleep(0.005)
