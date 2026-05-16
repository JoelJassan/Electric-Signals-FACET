'''
Funciones predefinidas. 
a. Encuentre los valores máximo, mínimo y media, utilizando las funciones "np.max", 
"np.min" y "np.mean" respectivamente.  

b. El comando "??" proporciona ayuda sobre las funciones definidas en el entorno; por 
ejemplo: "?? np.max" le explicará el objetivo y uso de la función "max".  

Averigüe la función y uso de los comandos "round", "math.ceil", "abs". Observación: 
Para math.ceil deberá importar la librería math (import math). 
'''

import numpy as np

v = np.array([[1, 3, 7, 0]])        #1x4
w = np.array([[5], [6], [2]])       #3x1
x = np.array([[0], [-2], [3], [7]]) #4x1

M = w @ v #3x1 @ 1x4 = 3x4
N = M @ x #3x4 @ 4x1 = 3x1
P = np.transpose(w) @ M #1x3 @ 3x4 = 1x4

print("\n ----- EJERCICIO 2.a. --------------------------------------------------------- \n")

print("Valores máximo, mínimo y media de v:")
print("Máximo:", np.max(v))
print("Mínimo:", np.min(v))
print("Media:", np.mean(v))

print("\n ----- EJERCICIO 2.b. --------------------------------------------------------- \n")

help(np.max)

