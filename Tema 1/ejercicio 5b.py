'''
Genere aprox. 30 ciclos de una señal cuadrada periódica de 20 Hz, y 250 puntos por 
ciclo, a partir de una senoidal.

'''
# hacer señal senoidal -> hacer señal cuadrada

import matplotlib.pyplot as plt
import numpy as np
from math import pi

#parametros generales
amp = 1
cicles = 30
f = 20
sampling_rate = 250
f_sampling = f*sampling_rate
T_sampling = 1/f_sampling

#vector de tiempo
sampling_time = np.arange(0, cicles/f, T_sampling)

# Señales:

#senoidal
sin_wave = amp * np.sin(2*pi*f*sampling_time)

#cuadrada
square_wave = []

for i in range(len(sampling_time)):
    if sin_wave[i] > 0:
        square_wave.append(amp)
    elif sin_wave[i] < 0:
        square_wave.append(-amp)
    else:
        square_wave.append(0)

square_wave = np.array(square_wave)




plt.plot(sampling_time, sin_wave)
plt.plot(sampling_time, square_wave)
plt.legend(["Senoidal", "Cuadrada"])
plt.xlabel("Tiempo [s]")
plt.show()


