from gpiozero import LineSensor


class SensorDeLinha:
    # Esse contrutor não recebe pinagem pois ficara fixo a posição do sensor, por enquanto indo do pinos GPIO5
    # ou 29 na placa até o GPIO26 ou 37
    def __init__(self):  
        self.sensor = [0,0,0,0,0]
        try:
            self.sensor[0] = LineSensor(5)
            self.sensor[1] = LineSensor(6)
            self.sensor[2] = LineSensor(13)
            self.sensor[3] = LineSensor(19)
            self.sensor[4] = LineSensor(26)
        except:
            print("Sensores não conectados corretamente")

    def getValue(self, numSensor):
        return self.sensor[numSensor].value

