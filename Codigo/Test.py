from AlgoritmoEvolutivo import AlgoritmoEvolutivo
from FitnessFunction import FitnessFunction
from Individuo import Individuo
import imutils 
import cv2
import os

def cambiarTamanio(img):

    if img.shape[0] <= img.shape[1]:
        return imutils.resize(img, height=180)
    else:
        return imutils.resize(img, width=180)

numFiguras = 1500
numPob = 400
imgOrig = cambiarTamanio(cv2.imread("Vocaloid_2.png",0))
path = "C:/Users/anton/Documents/Semestre 9/Sistemas Expertos/P5_AlgoritmoGenetico_Imagen/Reconstruccion"
scoreAntes = 10000000
scoreActual = 0
cont = 0
cont2 = 0

ff = FitnessFunction(imgOrig)
ag = AlgoritmoEvolutivo(imgOrig, numFiguras, numPob)
ag.init()

#cv2.imshow("Imagen Original", imgOrig)

for i in range(1000000):
    ag.evolucion()
    mejorInd = ag.muestraMejor()
    mejorImg = mejorInd.getImagenGen()
    scoreActual = ff.evaluate(mejorInd);

    print("Generacion ", i ,"  ---> Score: ", scoreActual);

    if scoreActual<scoreAntes:
        cont2 = cont2 + 1
    
    if cont2 == 2:
        cv2.imwrite(os.path.join(path, ("Captura_" + str(cont) + ".png")), mejorImg)
        cv2.waitKey(10)
        cont = cont + 1
        cont2 = 0
        scoreAntes = scoreActual  


