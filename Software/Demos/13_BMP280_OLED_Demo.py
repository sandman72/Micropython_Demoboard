# Bibliotheken laden
# import libs
from machine import Pin, I2C, SPI
from utime import sleep
from ssd1306 import SSD1306_I2C
from bmp280_spi import BMP280SPI


# OLED an I2C Bus initialisieren
# initialize OLED display on I2C Bus
i2c = I2C(0, sda=Pin(20), scl=Pin(21))
oled = SSD1306_I2C(128, 64, i2c)
oled.fill(0)
oled.show()

# SPI BPM280 an SPI Bus initialisieren
# initialize BPM280 sensor on SPI BUS
spi = SPI(0, sck=Pin(18), mosi=Pin(19), miso=Pin(16), polarity=1, phase=1)
spi_cs = Pin(17, Pin.OUT, value=1)
bmp280_spi = BMP280SPI(spi, spi_cs)

# Endlosschleife zeigt die Messwerte auf OLED display an
# endless loop shows measurements on OLED display
while True:
    oled.fill(0)
    oled.text("Temp & Pressure", 0, 0)
    
    readout = bmp280_spi.measurements
    oled.text(f"Tc: {readout['t']:.2f}C", 2,16)
    oled.text(f"Tf: {(readout['t']*1.8+32):.2f}F", 2,26)
    oled.text(f"Tk: {(readout['t']+273.15):.2f}K", 2,36)
    oled.text(f"Pa: {readout['p']:.2f}hPa", 2,46)
    
    oled.show()
    sleep(0.25)
