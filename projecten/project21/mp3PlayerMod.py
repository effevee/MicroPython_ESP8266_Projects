from machine import UART

class mp3Player:
    br = 9600
    TxPin = 1
    ser = None
    values = bytearray([0,0,0,0,0,0,0,0,0,0])
    
    @classmethod
    def start(cls):
        try:
            cls.ser = UART(cls.TxPin, cls.br)
            return True
        except Exception as e:
            print("problem connecting mp3player")
            print(e)
            return False

    @classmethod
    def command(cls):
        check = 0
        for j in range(2,8):
            check+=cls.values[j]
        check8 = check&0xFF
        check8Invert = 0xFF-check8
        cls.values[8] = check8Invert
        cls.ser.write(cls.values)

    @classmethod
    def play(cls):
        cls.values=bytearray([0X7E, 0xFF, 0x06, 0X0D, 00, 00, 00, 0xFE, 0xee, 0XEF])
        cls.command()

    @classmethod
    def playTrack(cls, track):
        try:
            cls.values = bytearray([0X7E, 0xFF, 0x06, 0X03, 00, 00, 00, 0xFE, 0xee, 0XEF])
            cls.values[5] = 0xFF&(track>>8)
            cls.values[6] = track&0xFF
            cls.command()
            return True
        except:
            return False

    @classmethod
    def pause(cls):
        cls.values = bytearray([0x7E, 0xFF, 0x06, 0x0E, 0x00, 0x00, 0x00, 0xFE, 0xED, 0xEF])
        cls.command()

    @classmethod
    def stop(cls):
        cls.values = bytearray([0x7E, 0xFF, 0x06, 0x16, 0x00, 0x00, 0x00, 0xFE, 0xED, 0xEF])
        cls.command()

    @classmethod
    def next(cls):
        cls.values = bytearray([0x7E, 0xFF, 0x06, 0x01, 0x00, 0x00, 0x00, 0xFE, 0xFA, 0xEF])
        cls.command()

    @classmethod
    def prev(cls):
        cls.values = bytearray([0x7E, 0xFF, 0x06, 0x02, 0x00, 0x00, 0x00, 0xFE, 0xF9, 0xEF])
        cls.command()

    @classmethod
    def volumeStepDown(cls):
        cls.values = bytearray([0x7E, 0xFF, 0x06, 0x05, 0x00, 0x00, 0x00, 0xFE, 0xED, 0xEF])
        cls.command()

    @classmethod
    def volumeStepUp(cls):
        cls.values = bytearray([0x7E, 0xFF, 0x06, 0x04, 0x00, 0x00, 0x00, 0xFE, 0xED, 0xEF])
        cls.command()
    
    @classmethod
    def setVolume(cls, volume):
        try:
            cls.values = bytearray([0x7E, 0xFF, 0x06, 0x06, 0x00, 0x00, 0x00, 0xFE, 0x00, 0xEF])
            cls.values[5] = 0xFF&(volume>>8)
            cls.values[6] = volume&0xFF
            cls.command()
            return True
        except:
            return False
 