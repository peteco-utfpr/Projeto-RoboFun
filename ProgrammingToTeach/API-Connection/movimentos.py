from linha import SensorDeLinha as SL
from motor import motor

def seguirLinha():
    while(True):
        if(!(SL.getValue(2) > 0.2)):         #sensor central pegando em cima da linha
            motor.andarFrente(0.3)
        elif(!(SL.getValue(1) > 0.2)):       #sensor esquerdo pegando em cima da linha
            motor.girarEsquerda(30)
        elif(!(SL.getValue(3) > 0.2)):       #sensor direito pegando em cima da linha
            motor.girarDireita(30)