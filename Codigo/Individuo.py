from Figura import Figura
import random
import numpy as np
import cv2

class Individuo:

    def __init__(self, numFig, dimensiones):
        self.numFig = numFig
        self.dimensiones = dimensiones
        self.imagen = np.zeros((self.dimensiones[0], self.dimensiones[1], 1), dtype = np.uint8)
        self.cromosoma = []


    def init(self):
        for i in range(self.numFig):
            fig = Figura(self.dimensiones)
            fig.init()
            #cv2.circle(self.imagen, tuple(fig.posicion), fig.radio, tuple(fig.color), -1)
            cv2.ellipse(self.imagen, fig.posicion, fig.radios, 0, 0, 360, fig.color, -1) 

            self.cromosoma.append(fig)

    def llenarImagen(self):
        for i in range(self.numFig):
            fig = self.cromosoma[i]
            #cv2.circle(self.imagen, tuple(fig.posicion), fig.radio, tuple(fig.color), -1)
            cv2.ellipse(self.imagen, fig.posicion, fig.radios, 0, 0, 360, fig.color, -1)

    def cruza(self, madre):
        padre = self.cromosoma
        madre = madre.cromosoma

        corte1 = int(np.floor((self.numFig-1)/3.))
        corte2 = 2*corte1
        
        crom1 = padre[0:corte1]
        crom1.extend(madre[corte1:corte2])
        crom1.extend(padre[corte2:])

        crom2 = madre[0:corte1]
        crom2.extend(padre[corte1:corte2])
        crom2.extend(madre[corte2:])

        h1 = Individuo(self.numFig, self.dimensiones)
        h2 = Individuo(self.numFig, self.dimensiones)

        h1.cromosoma = crom1
        h2.cromosoma = crom2

        h1.llenarImagen()
        h2.llenarImagen()

        return[h1, h2]
    

    def mutar(self):
        idx = random.randint(0, self.numFig-1)
        fig = Figura(self.dimensiones);
        fig.init()
        self.cromosoma[idx] = fig
        self.imagen = np.zeros((self.dimensiones[0], self.dimensiones[1], 1), dtype = np.uint8)
        self.llenarImagen()

    def getImagenGen(self):
        return self.imagen