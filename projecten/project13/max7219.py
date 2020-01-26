_NOOP = 0x00
_DIGIT0 = 0x01
_DIGIT1 = 0x02
_DIGIT2 = 0x03
_DIGIT3 = 0x04
_DIGIT4 = 0x05
_DIGIT5 = 0x06
_DIGIT6 = 0x07
_DIGIT7 = 0x08
_DECODEMODE = 0x09
_INTENSITY = 0x0A
_SCANLIMIT = 0x0B
_SHUTDOWN = 0x0C
_DISPLAYTEST = 0x0F


class Matrix8x8:
    def __init__(self, spi, cs):
        self.spi = spi
        self.cs = cs
        self.cs.init(cs.OUT, True)
        self.buffer = bytearray(8)
        self.init()

    def _register(self, command, data):
        self.cs.low()
        self.spi.write(bytearray([command, data]))
        self.cs.high()

    def init(self):
        for command, data in (
            (_SHUTDOWN, 0),
            (_DISPLAYTEST, 0),
            (_SCANLIMIT, 7),
            (_DECODEMODE, 0),
            (_SHUTDOWN, 1),
        ):
            self._register(command, data)

    def brightness(self, value):
        if not 0 <= value <= 15:
            raise ValueError("Brightness out of range")
        self._register(_INTENSITY, value)

    def fill(self, color):
        data = 0xff if color else 0x00
        for y in range(8):
            self.buffer[y] = data

    def pixel(self, x, y, color=None):
        if color is None:
            return bool(self.buffer[y] & 1 << x)
        elif color:
            self.buffer[y] |= 1 << x
        else:
            self.buffer[y] &= ~(1 << x)

    def show(self):
        for y in range(8):
            self._register(_DIGIT0 + y, self.buffer[y])
