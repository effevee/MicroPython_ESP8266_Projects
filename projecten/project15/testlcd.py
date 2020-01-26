import hd44780

# Initialisatie LCM1602C 16x2 karakter display
# Pins: RS - ES - DB4 - DB5 - DB6 - DB7
# GPIO: 13 - 14 -  2  -  0  -  4  -  5
pins = [13, 14, 2, 0, 4, 5]
lcd = hd44780.HD44780_LCD(pins, 16, 2)

# lcd initialiseren
lcd.lcd_init()

# tekst op display zetten
lcd.lcd_string("HD44780 LCD", 1, 0)
lcd.lcd_string("met MicroPython", 2, 0)
