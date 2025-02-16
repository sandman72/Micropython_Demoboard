# Bibliotheken laden
import machine
import utime

# Analog/Digital Wandler ADC1 GPIO 27 initialisieren
# an ADC 1 hängt der lichtempfindliche Widerstand LDR1
# initialize analog/digital converter on ADC1 GPIO 27
# where the light dependend resistor LDR1 is connected to
ldr = machine.ADC(27)

# Endlosschleife LDR auslesen und Wert anzeigen
# endless loop reading and displaying the LDR value
while True:
    print("LDR: " + str(ldr.read_u16()))
    utime.sleep(1)
