'''
5.a. Genere aprox. 30 ciclos de una señal diente de sierra periódica de 15 Hz, y 200 puntos 
por ciclo a usando la función "mod".  
'''

import matplotlib.pyplot as plt
import numpy as np

#parametros generales
cicles = 30
f = 15
sampling_rate = 200
f_sampling = f*sampling_rate
T_sampling = 1/f_sampling

min = 0
max = 5

# ---------- ALTERNATIVA 1: ---------- #

#vector de tiempo
sampling_time = np.arange(0, cicles/f, T_sampling)
value = 0

saw_thooth_1 = []
for i in sampling_time:
    saw_thooth_1.append( (max/sampling_rate)*value % max)
    value += 1

saw_thooth_1 = np.array(saw_thooth_1)
    

# ---------- ALTERNATIVA 2: ---------- #

sampling_cicle = np.arange(0, sampling_rate, 1)
cicle_count = np.arange(0,cicles,1)

saw_thooth_2 = []
for i in cicle_count:
    for j in sampling_cicle:
        saw_thooth_2.append( (max/sampling_rate) * j)

saw_thooth_2 = np.array(saw_thooth_2)


#visualización de señales
fig, ax = plt.subplots(2, 1)

ax[0].plot(sampling_time, saw_thooth_1, label='Sawtooth 1')
ax[0].set_xlabel("Tiempo [s]")
ax[0].set_ylabel("Amplitud [V]")
ax[0].legend()
ax[0].set_title("Alternativa 1")

ax[1].plot(sampling_time, saw_thooth_2, label='Sawtooth 2')
ax[1].set_xlabel("Tiempo [s]")
ax[1].set_ylabel("Amplitud [V]")
ax[1].legend()
ax[1].set_title("Alternativa 2")


plt.tight_layout()
plt.show()