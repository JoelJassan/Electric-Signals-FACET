'''
 Use un histograma como aproximación a la función de densidad de probabilidad de 
la señal del ítem 2.a. Tenga especial atención en el dimensionado de los ejes para 
realizar la gráfica.
'''

import matplotlib.pyplot as plt
import numpy as np

#parametros generales
cicles = 2
f = 15
sampling_rate = 200
f_sampling = f*sampling_rate
T_sampling = 1/f_sampling

min = 0
max = 5

#vector de tiempo
sampling_time = np.arange(0, cicles/f, T_sampling)
value = 0

#señal diente de sierra
saw_thooth = []
for i in sampling_time:
    saw_thooth.append( (max/sampling_rate)*value % max)
    value += 1

saw_thooth = np.array(saw_thooth)


#visualización de graficas
fig, ax = plt.subplots(2, 1)

ax[0].plot(sampling_time, saw_thooth, label='Sawtooth')
ax[0].set_xlabel("Tiempo [s]")
ax[0].set_ylabel("Amplitud [V]")
ax[0].set_title("Señal diente de sierra")

#histograma
ax[1].hist(saw_thooth, bins=100, density=True, edgecolor='black', linewidth=.5)
ax[1].set_xlabel("Amplitud [V]")
ax[1].set_ylabel("Densidad de probabilidad")
ax[1].set_title("Histograma")

plt.tight_layout()
plt.show()