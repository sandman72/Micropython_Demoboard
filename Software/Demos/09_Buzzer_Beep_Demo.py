# Bibliotheken laden
# import libs
from machine import Pin, PWM
from utime import sleep

# Buzzer an GPIO 10 mit PWM initialisieren
# initialize Buzzer on GPIO 10 with PWM
buzzer = PWM(Pin(10))

# Frequenz (Hz) einstellen
# set PWM frequency (Hz)
frequency = 1000
buzzer.freq(frequency)

# Buzzer einschalten für 0.3 Sekunden
# turn Buzzer on for 0.3 seconds 
buzzer.duty_u16(1000)
sleep(0.3)

# Ausschalten Buzzer
# turn off Buzzer
buzzer.duty_u16(0)
