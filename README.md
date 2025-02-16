# MicroPython DemoBoard
This repo contains all necessary files for our MicroPython Hardware Workshop at the Attraktor e.V. Makerspace in Hamburg, Germany: <a href="https://wiki.attraktor.org/Micropython_Kurs_2023"> Attraktor MicroPython Workshop </a>

<img width="640px" src="./Hardware/MicroPython_DemoBoard_V1.1_3D.jpg" alt="DemoBoard 3D" />

You can find the documentation in the Docs directory:

<a href="./Docs/MicroPython_Demoboard_V1.1_EN.pdf"> MicroPython Demoboard EN Doc (pdf) </a>
<a href="./Docs/MicroPython_Demoboard_V1.1_DE.pdf"> MicroPython Demoboard DE Doc (pdf) </a>

### Hardware:
The demoboard works with a Raspberry Pi Pico WH plugged into the pinheaders and connects it to various sensors, buttons, LEDs and an OLED display.

Gerber files to get your own boards produced can be found under the releases tab on the right and in the hardware directory.

You can find an interactive BOM (Bill of Material) here: <a href="https://raw.githack.com/sandman72/micropython_demoboard/main/Hardware/KiCAD_DemoBoard_V1.1/MicroPython_DemoBoard_V1.1_iBOM.html" traget="_blank"> iBOM </a>

<img width="640px" src="./Hardware/KiCAD_DemoBoard_V1.1/MicroPython_DemoBoard_V1.1_Schematic.jpg" alt="DemoBoard Schematic" />
<img width="640px" src="./Hardware/KiCAD_DemoBoard_V1.1/MicroPython_DemoBoard_V1.1.jpg" alt="DemoBoard PCB" />

BEWARE: Due to the infamous Errata E7 bug I recommend to stick to the Rasperry Pi Pico RP2040 boards and not use the Pi Pico 2 RP2350 based ones.

### Firmware:
Included in the firmware directory is a board test file and the invaders game as self contained UF2 files.

Simply enter the bootsel mode (hold down the bootsel button, while plugging the Pi Pico in) and copy one for the firmwares over.

### Software:
The software folder contains some demo scripts to try out the different sensors, buttons, buzzer, LEDs and display.

Included are some games like space invaders, flappy bird, snake and pong as well.

Also you'll find the test scripts there.
