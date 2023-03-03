import random


class Figura:

    def __init__(self, dimensiones):
        self.radios = [0,0]
        self.posicion = [0,0]
        self.color  = 0
        self.dimensiones = dimensiones;

    
    def init(self):
        posY = random.randint(0, self.dimensiones[0])
        posX = random.randint(0, self.dimensiones[1])
        rMayor = random.randint(0, 6)
        rMenor = random.randint(0, 6)

        self.radios = [rMayor, rMenor]
        self.posicion = [posX, posY]
        self.color = random.randint(0, 255)
