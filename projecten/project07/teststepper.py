from machine import Pin
from stepper import FullCycleOYPB, Stepper
import time

# initialisatie pinnen
pins = [ 14, 12, 13, 15]
in1 = Pin(14, Pin.OUT)     # pin D5
in2 = Pin(12, Pin.OUT)     # pin D6
in3 = Pin(13, Pin.OUT)     # pin D7
in4 = Pin(15, Pin.OUT)     # pin D8

# initialisatie stappenmotor
c = FullCycleOYPB(pins)
c.Build()
s = Stepper(0.008,c)

# lus draaien wijzer- en tegenwijzerzin
richting = [ True, False ]
for r in richting:
    s.setCW(r)
    for k in range(20000):
        res = s.nextPin()
        pin = res[0]
        if pin == "org":
            in1.value(res[1])
        elif pin == "yel":
            in2.value(res[1])
        elif pin == "pik":
            in3.value(res[1])
        elif pin == "blu":
            in4.value(res[1])
        time.sleep(0.0001)