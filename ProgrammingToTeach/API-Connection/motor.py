from gpiozero import Motor
from time import sleep

class motor:

    def __init__(self, motorA, motorB, motorC, motorD, pwmBool = True):
        self.motorE = Motor(motorA, motorB)
        self.motorD = Motor(motorC, motorD)
        self.motorE.pwm(pwmBool)
        self.motorD.pwm(pwmBool)
        self.pwm = 0.5

    def andarFrente(self, tempo = 1):
        pwm = 0.5                   #pwm em 50%
        self.motorE.forward(pwm)
        self.motorD.forward(pwm)
        sleep(tempo)

    def andarTras(self, tempo = 1):
        self.motorE.backward(self.pwm)
        self.motorD.backward(self.pwm)
        sleep(tempo)
    
    def girarEsquerda(self, angulo = 90):
        self.motorE.backward(self.pwm)
        self.motorD.forward(self.pwm)
        sleep(angulo/360)

    def girarDireita(self, angulo = 90):
        self.motorE.forward(self.pwm)
        self.motorD.backward(self.pwm)
        sleep(angulo/360)

    def parar(self, tempo = 1):
        self.motorE.stop()
        self.motorD.stop()
        sleep(tempo)