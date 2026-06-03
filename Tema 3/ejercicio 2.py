'''
A partir de una versión discreta de la señal del ejercicio 1 (ciclo activo de 50%), calcule numéricamente una estimación de los primeros 5 coeficientes de la serie trigonométrica de 
Fourier. 
Haga esto utilizando primero 100 muestras por período y luego repita para 1000 muestras por 
período.  Compare con los valores teóricos mostrando en una gráfica el espectro teórico y el 
calculado numéricamente para cada uno de los dos casos.  
'''

import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal
ciclos = 3
T = 1  # Período
D = 0.3  # Ciclo activo del 50%
N1 = 100  # Número de muestras por período (caso 1)
N2 = 1000  # Número de muestras por período (caso 2)

# Muestreo
f_sampling_1 = N1
f_sampling_2 = N2

sampling_time_1 = np.arange(0, ciclos*T, 1/f_sampling_1)
sampling_time_2 = np.arange(0, ciclos*T, 1/f_sampling_2)



# Generación de señales discretas (onda cuadrada)
square_wave_1 = []
for t in sampling_time_1:
    tau = (t + T/2) % T - T/2 

    if abs(tau) <= D*T/2: #centrado en la mitad del pulso activo
        square_wave_1.append(1)
    else:
        square_wave_1.append(0)
square_wave_1 = np.array(square_wave_1)

square_wave_2 = []
for t in sampling_time_2:
    tau = (t + T/2) % T - T/2 

    if abs(tau) <= D*T/2: 
        square_wave_2.append(1)
    else:
        square_wave_2.append(0)
square_wave_2 = np.array(square_wave_2)



# ----- Fourier ------------------------- #
from dataclasses import dataclass, field
import math

@dataclass
class FourierCoefficients:
    a0: float = 0.0
    an: list = field(default_factory=list)
    bn: list = field(default_factory=list)




#visualización de señales
plt.plot(sampling_time_1, square_wave_1, label='N=100')
plt.plot(sampling_time_2, square_wave_2, label='N=1000')
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud [V]")
plt.legend()
#plt.grid()
plt.show()