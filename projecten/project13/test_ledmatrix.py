# 8x8 LED matrix gebaseerd op de MAX7219 controller
from machine import Pin, SPI
from max7219 import Matrix8x8
import time

ON = True
OFF = False
LED_ROWS = 8
LED_COLS = 8

# initialisatie hardware SPI bus
# SPI    Master     Slave
# PIN    ESP8266    MAX7219
# -------------------------
# SCK    D5 (14)    SCK
# MOSI   D7 (13)    DIN
# MISO   D6 (12)    ---
# CS     D8 (15)    CS
# polarity=1 -> idle state of SCK
# phase=0 -> data op stijgende flank SCK
# phase=1 -> data op dalende flank SCK
spi = SPI(1, baudrate=20000000, polarity=0, phase=0)
cs = Pin(15, Pin.OUT)

# initialisatie 8x8 LED matrix
matrix = Matrix8x8(spi, cs)
matrix.init()

# helderheid (0-15)
matrix.brightness(15)

# matrix blanko
matrix.fill(OFF)
matrix.show()

# wandelende pixel
for p in range(LED_ROWS * LED_COLS):
    x = p // LED_COLS
    y = p % LED_COLS
    print("x:{} - y:{}".format(x, y))
    matrix.pixel(x, y, ON)
    matrix.show()
    time.sleep_ms(500)
    matrix.pixel(x, y, OFF)
    matrix.show()
