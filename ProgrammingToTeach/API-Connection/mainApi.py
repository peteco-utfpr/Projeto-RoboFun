##from linha import SensorDeLinha
from motor import motor
##import movimentos

plano = []

## Inicializa os motores nos GPIO: 17, 18, 22, 23
motor = motor(17,18,22,23,True)

## Executa a programação, e armazena o resultado na variavel plano
exec(codigoPython, globals())

for i in plano:
    if i == "M":
        motor.andarFrente(0.3)
    elif i == "GA":
        motor.girarDireita(90)
    elif i == "GH":
        motor.girarEsquerda(90)
    motor.parar()
motor.parar()
