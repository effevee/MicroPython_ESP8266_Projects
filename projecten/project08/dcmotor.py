from machine import Pin, PWM


class HBridge:
    """ klasse H-Bridge voor het aansturen van 1 gelijkstroom motor.
    Laat de motor voorwaarts of achterwaarts draaien.
    Gebruikt PWM om de snelheid van de motor te varieren van 0 tot 100%.
    Als geen PWM gebruikt wordt is de maximale snelheid steeds 100% """

    # default pwm frequentie en duty cycle
    PWM_FREQ = 60       # in Hz
    PWM_DUTY = 0        # in %

    # status motor
    (ONBEKEND, STOPPEN, VOORUIT, ACHTERUIT) = (-1, 0, 1, 2)
 
    
    # initialisatie H-Bridge
    def __init__(self, input_pins, pwm_pin=None):
        """:param input_pins: tuple met de 2 stuurpinnen
           :param pwm_pin: PWM pin voor de snelheid (None = geen PWM)"""
        self.snelheid = 0
        self.status = HBridge.ONBEKEND
        # Initialisatie HBridge stuurpinnen
        self.in1 = Pin(input_pins[0], Pin.OUT)
        self.in2 = Pin(input_pins[1], Pin.OUT)
        # Initialisatie PWM Enable pin voor snelheidscontrole
        # zonder PWM moet de Enable pin van de L293D hoog staan
        self.met_pwm = (pwm_pin is not None)
        if self.met_pwm:
            self.ena = PWM(Pin(pwm_pin, Pin.OUT))
            self.ena.freq(self.PWM_FREQ)
            self.ena.duty(self.pwm_waarde(self.PWM_DUTY))
        # Alles stoppen
        self.stoppen()

    def pwm_waarde(self, snelheid):
        # omzetten snelheid in % naar PWM waarde (0-1023)
        return int(snelheid / 100.0 * 1023.0)
        
    def zet_snelheid(self, snelheid):
        if not(0 <= snelheid <= 100):
            raise ValueError('Ongeldige snelheid')
        if self.met_pwm:                # snelheid met PWM
            self.ena.duty(self.pwm_waarde(snelheid))
            self.snelheid = snelheid
        else:                           # zonder PWM
            if snelheid == 0:
                self.snelheid = 0
            else:
                self.snelheid = 100
            if self.snelheid == 0 and self.status != HBridge.STOPPEN:
                self.stoppen()          # motor stoppen

    def stoppen(self):
        self.in1.low()                  # in1 laag
        self.in2.low()                  # in2 laag
        self.status = HBridge.STOPPEN   # Deze 2 lijnen ...
        self.zet_snelheid(0)            # niet omkeren

    def vooruit(self, snelheid=100):
        # HBridge herinstellen
        if self.status != HBridge.VOORUIT:
            self.stoppen()
            self.in1.low()              # in1 laag
            self.in2.high()             # in2 hoog
            self.status = HBridge.VOORUIT
        # snelheid instellen
        self.zet_snelheid(snelheid)

    def achteruit(self, snelheid=100):
        # HBridge herinstellen
        if self.status != HBridge.ACHTERUIT:
            self.stoppen()
            self.in1.high()             # in1 hoog
            self.in2.low()              # in2 laag
            self.status = HBridge.ACHTERUIT
        # snelheid instellen
        self.zet_snelheid(snelheid)


class DualHBridge():
    """ klasse Dual H-Bridge voor het aansturen van 2 gelijkstroom motoren.
    Laat de motoren voorwaarts of achterwaarts draaien.
    Gebruikt PWM om de snelheid van de motoren te varieren van 0 tot 100%.
    Als geen PWM gebruikt wordt is de maximale snelheid steeds 100% """

    def __init__(self, mot1_pins, mot1_pwm, mot2_pins, mot2_pwm, afwijking=0):
        """:param mot1_pins: tuple met de 2 stuurpinnen voor motor 1
           :param mot1_pwm: PWM pin voor snelheid van motor 1 (None=geen PWM)
           :param mot2_pins: tuple met de 2 stuurpinnen voor motor 2
           :param mot2_pwm: PWM pin voor snelheid van motor 2 (None=geen PWM)
           :param afwijking: +3 om motor 1 te versnellen bij vooruit rijden
                             -3 om motor 1 te vertragen bij vooruit rijden"""
        if (afwijking != 0) and ((mot1_pwm is None) or (mot2_pwm is None)):
            raise ValueError('Afwijking instelling werkt alleen met PWM')
        self.motor1 = HBridge(mot1_pins, mot1_pwm)
        self.motor2 = HBridge(mot2_pins, mot2_pwm)
        self.afwijking = afwijking

    def vooruit(self, snelheid=100, snelheid_2=None):
        if snelheid_2 is None:          # snelheid motor 2
            snelheid_2 = snelheid       # zelfde snelheid als motor 1
        # aanpassen snelheid motor1 met afwijking
        if self.afwijking > 0:          # afwijking positief
            snelheid = snelheid - self.afwijking
            if snelheid < 0:            # snelheid niet negatief !
                snelheid = 0
        elif self.afwijking < 0:        # afwijking negatief
            snelheid_2 = snelheid_2 - abs(self.afwijking)
            if snelheid_2 < 0:
                snelheid_2 = 0          # snelheid niet negatief
        # motoren aansturen
        self.motor1.vooruit(snelheid)
        self.motor2.vooruit(snelheid_2)

    def achteruit(self, snelheid=100, snelheid_2=None):
        if speed_2 is None:             # snelheid motor 2
            speed_2 = speed             # zelfde snelheid als motor 1
        # aanpassen snelheid motor1 met afwijking
        if self.afwijking > 0:          # afwijking positief
            snelheid = snelheid - self.afwijking
            if snelheid < 0:            # snelheid niet negatief !
                snelheid = 0
        elif self.afwijking < 0:        # afwijking negatief
            snelheid_2 = snelheid_2 - abs(self.afwijking)
            if snelheid_2 < 0:
                snelheid_2 = 0          # snelheid niet negatief
        # motoren aansturen
        self.motor1.achteruit(snelheid)
        self.motor2.achteruit(snelheid_2)

    def stoppen(self):
        self.motor1.stoppen()
        self.motor2.stoppen()
