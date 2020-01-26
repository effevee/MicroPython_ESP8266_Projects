from dcmotor import HBridge
import time

# pinnen HBridge L293
IN1 = 12        # pin D6
IN2 = 13        # pin D7
ENA = 14        # pin D5

# motorpinnen initialiseren
motor = HBridge([IN1, IN2], ENA)

# motor voorwaarts versnellen tot maximum
snelheid = 0
while snelheid < 100:
    print("F {} %".format(snelheid))
    motor.vooruit(snelheid)
    time.sleep_ms(250)
    snelheid+=1

# motor voorwaarts vertragen tot minimum
while snelheid > 0:
    print("F {} %".format(snelheid))
    motor.vooruit(snelheid)
    time.sleep_ms(250)
    snelheid-=1

# motor achterwaarts versnellen tot maximum
snelheid = 0
while snelheid < 100:
    print("B {} %".format(snelheid))
    motor.achteruit(snelheid)
    time.sleep_ms(250)
    snelheid+=1

# motor achterwaarts vertragen tot minimum
while snelheid > 0:
    print("B {} %".format(snelheid))
    motor.achteruit(snelheid)
    time.sleep_ms(250)
    snelheid-=1

# motor stoppen
motor.stoppen()   