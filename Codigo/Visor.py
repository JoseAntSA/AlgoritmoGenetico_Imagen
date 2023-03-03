import cv2
import os
import imutils 
def cambiarTamanio(img):

    if img.shape[0] <= img.shape[1]:
        return imutils.resize(img, height=300)
    else:
        return imutils.resize(img, width=300)

def visor(opc, path):

    if opc == 0:

        path = path + "\\Reconstruccion"
        imgOrig = cambiarTamanio(cv2.imread("Vocaloid_2.png",0))

        # Para Carpeta Reconstruccion
        cont = 5801
        paso = 10

        cv2.imshow("Imagen Original", imgOrig)

        for i in range(1,cont,paso):
            nombre = path + "\\Captura_" + str(i) + ".png" 
            imgRec = cambiarTamanio(cv2.imread(nombre))
            cv2.imshow("Imagen Recons", imgRec)
            cv2.waitKey(10) 
    else:
       
        path = path + "\\Reconstruccion_1"
        # Para Carpeta Reconstruccion
        cont = 876
        paso = 2

        for i in range(1,cont,paso):
            nombre = path + "\\Captura_" + str(i) + ".png" 
            imgRec = cv2.imread(nombre)
            cv2.imshow("Imagen Recons", imgRec)
            cv2.waitKey(10)

    cv2.waitKey(0) 

path = "C:\\Users\\anton\\Documents\\Semestre 9\\Sistemas Expertos\\P5_AlgoritmoGenetico_Imagen"

visor(0, path) 



