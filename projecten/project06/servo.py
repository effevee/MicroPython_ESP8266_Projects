from machine import Pin, PWM
import time

# servo motor sturing zit op pin D5 (GPIO14)
PinNum = 14
# posities servo
links = 40
midden = 77
rechts = 110

# initialisatie servo
servo = PWM(Pin(PinNum), freq=50, duty=midden)

for t in range(10):
    # links
    servo.duty(links)
    time.sleep(1)
    # midden
    servo.duty(midden)
    time.sleep(1)
    # rechts
    servo.duty(rechts)
    time.sleep(1)
    # midden
    servo.duty(midden)
    time.sleep(1)
   
# pwm resetten
servo.duty(midden)
servo.deinit()    