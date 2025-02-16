# Bibliotheken laden
# import libs
import machine
import utime

# Analog/Digital Wandler ADC0 GPIO 26 initialisieren
# an ADC 0 hängt das einstellbare Potentiometer RV1
# initialize analog/digital converter on ADC0 GPIO 26
# where the RV1 potentiometer is connected to
potentiometer = machine.ADC(26)

# Endlosschleife Poti auslesen und Wert anzeigen
# endless loop reading and displaying the potentiometer value
while True:
    print("Poti: " + str(potentiometer.read_u16()))
    utime.sleep(1)
