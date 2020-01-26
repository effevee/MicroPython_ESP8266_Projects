from machine import Pin, SPI
import time

# ADC MCP3008 met potentiometer op channel 0 pin (CH0)
# 3 bytes versturen naar DIN van MCP3008:
# 1. b00000001 : start byte
# 2. b1000xxxx : 1=single channel + 000=channel 0
# 3. bxxxxxxxx : don't care byte
DIN = bytearray([1, 128, 0])
# 3 byte antwoord van MCP3008 in DOUT:
# 1. bxxxxxxxx : niet relevant
# 2. bxxxxx0ii : bit 9 en 8 van 10bit antwoord
# 3. biiiiiiii : bit 7 tem bit 0 van 10bit antwoord
DOUT = bytearray(3)

# initialisatie software SPI bus
# SPI    Master     Slave
# PIN    ESP8266    MCP3008
# -------------------------
# SCK    D8 (15)    SCK
# MOSI   D6 (12)    DIN
# MISO   D7 (13)    DOUT
# CS     D5 (14)    CS
# polarity=1 -> idle state of SCK
# phase=0 -> data op stijgende flank SCK
# phase=1 -> data op dalende flank SCK
SCK = Pin(15, Pin.OUT)
MOSI = Pin(12, Pin.OUT)
MISO = Pin(13, Pin.OUT)
CS = Pin(14, Pin.OUT)
spi = SPI(-1, baudrate=100000, polarity=1, phase=0,
          sck=SCK, mosi=MOSI, miso=MISO)

# zet baudrate
spi.init(baudrate=200000)

# oneindige lus
while True:
    # zet Chip Select voor communicatie
    CS.low()
    time.sleep_us(5)
    # zend commando en lees antwoord
    spi.write_readinto(DIN, DOUT)
    # reset Chip Select
    CS.high()
    time.sleep_us(5)
    # converteer 10 LSB uit antwoord en druk af in REPL
    waarde = ((((3 & DOUT[1]) << 8) + DOUT[2]) / 1023) * 3.3
    print("Spanning over potentiometer: {:.1f} V".format(waarde))
    # even wachten
    time.sleep_ms(500)
