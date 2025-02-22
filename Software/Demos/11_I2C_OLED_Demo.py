# Bibliotheken laden
# import libs 
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

# I2C Bus initialisieren
# initialize I2C Bus
# GPIO 20 - SDA (Data)
# GPIO 21 - SDC (Clock)
i2c = I2C(0, sda=Pin(20), scl=Pin(21))

# OLED Display ist an diesen Bus angeschlossen
# OLED display is connected to this bus
# Auflösung / Resolution 128x64 Pixel
oled = SSD1306_I2C(128, 64, i2c)

# OLED Display löschen und Text anzeigen
# clear OLED display and show text
oled.fill(0)
oled.rect(0,0,128,64,1)
oled.text("Attraktor e.V.", 10, 16)
oled.text("Hello World!", 16, 40)
oled.show()
