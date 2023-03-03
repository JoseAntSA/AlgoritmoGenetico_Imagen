import numpy as np
import random
from Poblacion import Poblacion
from MecanismoSeleccion import MecanismoSeleccion
from FitnessFunction import FitnessFunction


class AlgoritmoEvolutivo:
    def __init__(self, imgOrig, numFig = 3000, size = 300):
        self.size = size
        self.pob = None
        self.imgOrig = imgOrig
        self.dimensiones = imgOrig.shape
        self.numFig = numFig
        
    def init(self):
        pob = Poblacion(self.imgOrig, self.numFig, self.size)
        pob.init()
        self.pob = pob
        self.seleccion = MecanismoSeleccion()
        self.ff = FitnessFunction(self.imgOrig)

    def muestraMejor(self):
        #aptitudes = [self.ff.evaluate(ind) for ind in self.pob.poblacion] # Obtengo las aptitutes de la 
        
        #idxMejor = np.argmin(aptitudes)
        #mejorInd = self.pob.poblacion[idxMejor]
        
        return self.pob.poblacion[0]#mejorInd

    def evolucion(self):                        # Metodo para evolucionar una poblacion
        # 1) Evaluar individuos
        # 2) Seleccionar padres para cruza
        # 3) Generar hijos (cruza)
        # 4) Mutar a algunos
        # 5) Evaluar hijos
        # 6) Seleccionar miembros de la siguiente población

        ####################################
        #####      IMPLEMENTACION      #####
        ####################################    

        if self.pob is None:                    # Condicion por si la poblacion
            print("Inicialice la población")    # inicial no se inicializo, entonces
            return                              # terminamos el programa.
        
        
        # 1) Evaluar individuos     
        poblacion = self.pob.poblacion                             # Aislamos la poblacion
        aptitudes = [self.ff.evaluate(ind) for ind in self.pob.poblacion]   # Obtenemos sus aptitutes
        
        # 2) Seleccionar padres para cruza
        k = int(self.size/2)                          # Divide el tamaño de la poblacion en 2
        if k%2 == 1:                                  # Condicional por si k es impar, por lo que
            k += 1                                    # le sumamos 1 para evitar problemas en la cruza
        idx = self.seleccion.selecciona(aptitudes, k) # Guarda k individuos seleccionados, se le manda 
                                                      # las aptitudes y un numero k
                                                      
        #3) Generar hijos (cruza)
        descendencia = []                   # Arreglo para guardar la descendencia
        for i in list(range(0,k-1,2)):      # Ciclo para recorrer la poblacion cada 2 individuos
            ip = idx[i]                     # Selecciona el indice del padre
            im = idx[i+1]                   # Selecciona el indice de la madre
            papa = poblacion[ip]            # Apartamos al padre guardadolo en una variable
            mama = poblacion[im]            # Apartamos a la madre guardadola en una variable
            hijos = papa.cruza(mama)       # Cruzamos al papa con la mama y obtenemos a los hijos
            descendencia.append(hijos[0])   # Agregamos a la descendencia el primer hijo
            descendencia.append(hijos[1])   # Agregamos a la descendencia el segundo hijo
        
        
        # 4) Mutar a algunos (5%)
        totalMutar = int(np.ceil(len(descendencia)*0.1))   # Convierte a entero un numero redondeado
                                                           # del 1 porciento del tamaño de la            
                                                           # descendencia siendo el numero obtenido
                                                           # la cantidad de individuos a mutar
        for i in range(totalMutar):                        # Ciclo para mutar individuos segun el 
                                                           # numero obtenido anteriormente, donde
            idx = random.choice(range(len(descendencia)))  # los individuos son elegidos
            descendencia[idx].mutar()                      # aleatoriamente
        
        
        # 5) Evaluar hijos
        for hijo in descendencia:                                # Ciclo para recorrer la descendencia y
            poblacion.append(hijo)                               # agregar los hijos a la poblacion
            
        aptitudes = [self.ff.evaluate(ind) for ind in self.pob.poblacion]  # Obtengo las aptitutes de la poblacion
        
        # 6) Seleccionar miembros de la siguiente población
        # ELITISMO!!!!!
        idxMejor = np.argmin(aptitudes)                         # Obtiene al individuo con la mejor 
                                                                # aptitud
        siguientePob = []                                       # Se crea la lista de individuos de la 
                                                                # siguiente generación               
        siguientePob.append(poblacion[idxMejor])                # Agrega a la siguiente poblacion al 
                                                                # individuo con la mejor aptitud
        idx = self.seleccion.selecciona(aptitudes, self.size)   # Selecciona a los siguientes individuos
        
        for i in idx:                                           # Ciclo para reccorer a los individuos     
            siguientePob.append(poblacion[i])                   # seleccionados y agregarlos en la
                                                                # siguiente poblacion

        self.pob.poblacion = siguientePob                       # Guardo la siguiente poblacion para 
                                                                # su evolución
