from machine import Pin, PWM
import time

# piezo speaker zit op pin D5 (GPIO14)
PinNum = 14

# constanten
tempo = 5
tones = {
    'c': 262,
    'd': 294,
    'e': 330,
    'f': 349,
    'g': 392,
    'a': 440,
    'b': 494,
    'C': 523,
    ' ': 0,
}
melody = 'cdefgabC'
rhythm = [8, 8, 8, 8, 8, 8, 8, 8]

# initialisatie beeper
beeper = PWM(Pin(14, Pin.OUT), freq=440, duty=512)

# speel melodie
for tone, length in zip(melody, rhythm):
    beeper.freq(tones[tone])
    time.sleep(tempo/length)

# reset beeper
beeper.deinit()