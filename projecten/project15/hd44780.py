# Eenvoudige klasse voor een HD44780 gebaseerde LCD in 4-bit mode
# Deze displays hebben een 8-bit databus maar kunnen ook in 4-bit mode
# werken (de 4 lage bits DB0-DB3 worden dan niet gebruikt)
# Aansluitingen LCD :
# 1 : GND
# 2 : VDD (5V)
# 3 : VO (Contrast 0-5V)
# 4 : RS (Register select : low = Command - high = Data)
# 5 : RW (Read/Write : low = Write - high = Read)
# 6 : ES (Enable of Strobe)
# 7 : DB0 (Data Bit 0 - niet gebruikt in 4-bit mode)
# 8 : DB1 (Data Bit 1 - niet gebruikt in 4-bit mode)
# 9 : DB2 (Data Bit 2 - niet gebruikt in 4-bit mode)
# 10: DB3 (Data Bit 3 - niet gebruikt in 4-bit mode)
# 11: DB4 (Data Bit 4)
# 12: DB5 (Data Bit 5)
# 13: DB6 (Data Bit 6)
# 14: DB7 (Data Bit 7)
# 15: BL1 (Backlight 5V)
# 16: BL2 (Backlight GND)

import machine
import time

# gebruikte pinnen
PIN_RS = None
PIN_ES = None
PIN_D4 = None
PIN_D5 = None
PIN_D6 = None
PIN_D7 = None

pins = [PIN_RS, PIN_ES, PIN_D4, PIN_D5, PIN_D6, PIN_D7]

# dimensies LCD
LCD_COLS = 16   # LCM1602 = 16 - LCM2004 = 20
LCD_ROWS = 2    # LCM1602 = 2  - LCM2004 = 4

# LCD Register select
LCD_CHR = True
LCD_CMD = False

# LCD timings
E_PULSE = 0.005
E_DELAY = 0.001


class HD44780_LCD:

    def __init__(self, pins=[13, 14, 2, 0, 4, 5],
                 cols=LCD_COLS, rows=LCD_ROWS):
        self.pins = pins
        self.pin_rs = machine.Pin(self.pins[0], machine.Pin.OUT)
        self.pin_es = machine.Pin(self.pins[1], machine.Pin.OUT)
        self.pin_d4 = machine.Pin(self.pins[2], machine.Pin.OUT)
        self.pin_d5 = machine.Pin(self.pins[3], machine.Pin.OUT)
        self.pin_d6 = machine.Pin(self.pins[4], machine.Pin.OUT)
        self.pin_d7 = machine.Pin(self.pins[5], machine.Pin.OUT)
        self.cols = cols
        self.rows = rows

    def lcd_init(self):
        self.lcd_byte(0x33, LCD_CMD)    # 110011 Initialise
        self.lcd_byte(0x32, LCD_CMD)    # 110010 Initialise
        self.lcd_byte(0x0C, LCD_CMD)    # 000110 Cursor move direction
        self.lcd_byte(0x01, LCD_CMD)    # 001100 Display On, Cursor Off, Blink Off
        self.lcd_byte(0x28, LCD_CMD)    # 101000 Data length, number of lines, font size
        self.lcd_byte(0x06, LCD_CMD)    # 000001 Clear display
        time.sleep(E_DELAY)

    def lcd_byte(self, bits, mode):
        self.bits = bits
        self.mode = mode
        # Register select
        self.pin_rs.value(self.mode)
        # High bits
        self.pin_d4.low()
        self.pin_d5.low()
        self.pin_d6.low()
        self.pin_d7.low()
        if self.bits & 0x10 == 0x10:
            self.pin_d4.high()
        if self.bits & 0x20 == 0x20:
            self.pin_d5.high()
        if self.bits & 0x40 == 0x40:
            self.pin_d6.high()
        if self.bits & 0x80 == 0x80:
            self.pin_d7.high()
        # Toggle Enable
        self.lcd_toggle_enable()
        # Low bits
        self.pin_d4.low()
        self.pin_d5.low()
        self.pin_d6.low()
        self.pin_d7.low()
        if self.bits & 0x01 == 0x01:
            self.pin_d4.high()
        if self.bits & 0x02 == 0x02:
            self.pin_d5.high()
        if self.bits & 0x04 == 0x04:
            self.pin_d6.high()
        if self.bits & 0x08 == 0x08:
            self.pin_d7.high()
        # Toggle Enable
        self.lcd_toggle_enable()

    def lcd_toggle_enable(self):
        time.sleep(E_DELAY)
        self.pin_es.high()
        time.sleep(E_PULSE)
        self.pin_es.low()
        time.sleep(E_DELAY)

    def lcd_string(self, string, row=1, col=0):
        self.string = string
        # controle positie
        if row > self.rows:
            row = self.rows
        if col > self.cols:
            col = self.cols
        # adres in buffer
        if row == 1:
            self.lcd_byte(0x80 + col, LCD_CMD)
        elif row == 2:
            self.lcd_byte(0xC0 + col, LCD_CMD)
        elif row == 3:
            self.lcd_byte(0x94 + col, LCD_CMD)
        elif row == 4:
            self.lcd_byte(0xD4 + col, LCD_CMD)
        # Druk string af
        for i in range(len(self.string)):
            if i <= self.cols:
                self.lcd_byte(ord(self.string[i]), LCD_CHR)
        # Vul rest van lijn met spaties
        for i in range(self.cols - len(self.string)):
            self.lcd_byte(32, LCD_CHR)
