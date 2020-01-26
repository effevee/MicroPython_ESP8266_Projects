import ssd1306
from machine import I2C, Pin

# OLED
OLED_WIDTH  = 64
OLED_HEIGHT = 48

# I2C initialiseren
scl = Pin(5)            # pin D1
sda = Pin(4)            # pin D2
i2c = I2C(-1, scl, sda)

# OLED initialiseren
oled = ssd1306.SSD1306_I2C(OLED_WIDTH, OLED_HEIGHT, i2c)

# tekst plaatsen
oled.fill(0)
oled.text("Hello", 0, 0)
oled.text("World", 0, 10)
oled.pixel(20, 20, 1)
oled.show()