'''
A partir de la pdf, calcule el valor medio y los valores eficaces de la señal del ítem 2.c 
y compare con los promedios temporales.  

Respuesta: Utilice las siguientes funciones: 
- Valor medio: np.mean() -> Media estadística. 
- Valor eficaz ac: np.std() -> Desviación estándar. 
- Valor eficaz: np.sqrt() -> Raíz cuadrada. 
- Para elevar un número a un exponente utilizar doble asterisco. Por ejemplo, 
        - Dos a la cuarta: 2**4 
        - Elevar una variable (suponer que se llama x) al cubo: x**3
'''

#Este no se resuelve porque no está el 2.c, pero se resuelve el 4.a.ii que es lo mismo pero con la suma y resta de señales.

import numpy as np
import matplotlib.pyplot as plt
from math import pi

print("\n ----- EJERCICIO 4.a. --------------------------------------------------------- \n")

ciclos = 1

#amplitudes
amp1 = 3
amp2 = 4
#frecuencias
f1 = 20
f2 = 33.57

#muestreo
f_sampling = f2*20 #asociado al peor caso
T_sampling = 1/f_sampling
sampling_time = np.arange(0, ciclos/f1, T_sampling) #sampleo 100 ciclos de la menor frec.

#genero vectores de amplitud para signal 1 y 2
signal_1 = amp1*np.sin(2*pi*f1*sampling_time)
signal_2 = amp2*np.sin(2*pi*f2*sampling_time)

Vmed_1 = np.mean(signal_1)
Vmed_2 = np.mean(signal_2)
Vrms_1 = np.sqrt(np.mean(signal_1**2))
Vrms_2 = np.sqrt(np.mean(signal_2**2))
Vrms_ac_1 = np.std(signal_1)
Vrms_ac_2 = np.std(signal_2)

print("Vmed 1: ", Vmed_1)
print("Vmed 2: ", Vmed_2)
print("Vrms 1: ", Vrms_1)
print("Vrms 2: ", Vrms_2)
print("Vrms_ac 1: ", Vrms_ac_1)
print("Vrms_ac 2: ", Vrms_ac_2)