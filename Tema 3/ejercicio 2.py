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
ciclos = 1
T = 1  # Período
D = 0.5  # Ciclo activo del 50%
N1 = 100  # Número de muestras por período (caso 1)
N2 = 1000  # Número de muestras por período (caso 2)

#muestreo
f_sampling_1 = 1/T*N1
f_sampling_2 = 1/T*N2

sampling_time_1 = np.arange(0, ciclos/f_sampling_1, 1/f_sampling_1)
sampling_time_2 = np.arange(0, ciclos/f_sampling_2, 1/f_sampling_2)


# Función para generar la señal discreta
square_wave = []
for i in range(T):
    if i < D*T:
        square_wave.append(1)
    else:
        square_wave.append(0)
square_wave = np.array(square_wave)

#visualización de señales
plt.plot(sampling_time_1, square_wave, label='N=100')
plt.plot(sampling_time_2, square_wave, label='N=1000')
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud [V]")
plt.legend()
#plt.grid()
plt.show()