import numpy as np
import random


class MecanismoSeleccion:
   
    def selecciona(self, aptitudes, k = 2):
        
        aux = aptitudes
        aux.sort(reverse=False)
        mejoresAptitudes = []                          # Arreglo para los mejores individuos   
        
        for i in range(k):
            idxMejor = aptitudes.index(aux[i])

            mejoresAptitudes.append(idxMejor)    # al arreglo de mejoresInd, luego se borran todas las
                                                 # coincidencias del mismo individuo del arreglo  
        return mejoresAptitudes