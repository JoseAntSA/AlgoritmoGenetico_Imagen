from Individuo import Individuo


class Poblacion:
    
    def __init__(self, imgOrig, numFig, tamanio):
        self.tamanio = tamanio
        self.imgOrig = imgOrig
        self.dimensiones = self.imgOrig.shape
        self.numFig = numFig


    def init(self):
        poblacion = []
        for i in range(self.tamanio):
            ind = Individuo(self.numFig, self.dimensiones)
            ind.init()
            poblacion.append(ind)
            
        self.poblacion = poblacion
