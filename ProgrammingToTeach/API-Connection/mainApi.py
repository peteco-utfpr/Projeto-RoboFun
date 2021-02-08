##from linha import SensorDeLinha
from motor import motor
##import movimentos

plano = []

## Inicializa os motores nos GPIO: 17, 18, 22, 23
motor = motor(17,18,22,23,True)

codigoPython = open("codeBlock.py", "r")
codigoPython = codigoPython.read()
## Executa a programação, e armazena o resultado na variavel plano
exec(codigoPython, globals())

positions = {"N" : 0, "L" : 1, "O" : -1, "S" : 2}
atual = "N"
for i in plano:
    difValue = positions[atual] - positions[i]
    
    if difValue == 0:
        motor.andarFrente(0.3)
    elif difValue < 0:
         motor.girarDireita(90 * (-1)*difValue)
    else:
        motor.girarEsquerda(90 * difValue)
    atual = i
    motor.parar()
motor.parar()
