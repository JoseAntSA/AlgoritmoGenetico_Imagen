import cv2
import numpy as np

class FitnessFunction:
    def __init__(self, imgOrig):
        self.imgOrig = imgOrig

    def evaluate2(self, cromosoma):
        imgIntento = cromosoma.getImagenGen()
        
        ##gray_img = cv2.cvtColor(self.imgOrig, cv2.COLOR_BGR2GRAY)
        histograma_Orig = cv2. calcHist([self.imgOrig], [0], None, [256], [0, 256])

        ##gray_img = cv2.cvtColor(imgIntento, cv2.COLOR_BGR2GRAY)
        histograma_Intento = cv2. calcHist([imgIntento], [0], None, [256], [0, 256])
        
        c1 = 0

        i = 0
        while i<len(histograma_Orig) and i<len(histograma_Intento):
            c1 += (histograma_Orig[i]-histograma_Intento[i])**2
            i += 1

        c1 = c1**(1/2)

        return sum(c1)


    def evaluate(self, cromosoma):
        imgIntento = cromosoma.getImagenGen()
        
        diferencia = cv2.absdiff(imgIntento, self.imgOrig)

        sumaDiferencias = np.sum(diferencia, axis=0)
        sumaPlanos = sum(sumaDiferencias)
 
        return sumaPlanos

    def evaluat3(self, cromosoma):
        imgIntento = cromosoma.getImagenGen()

        alto, ancho = self.imgOrig.shape
        #print(self.imgOrig.shape)
        #print(imgIntento.shape)
        
        cont = ancho*alto

        for i in range(0,alto):
            for j in range(0,ancho):
            	if(self.imgOrig.item(i, j)==imgIntento.item(i, j,0)):
                    cont -= 1;
        
        return cont
