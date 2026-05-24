
'''

4.c. Defina los vectores necesarios para representar alrededor de 100 ciclos de 2 señales 
senoidales de amplitud unitaria, de la misma frecuencia, pero distinta fase.  
i. Explore cómo cambia la coherencia entre las 2 señales al ir cambiando la fase 
de una de ellas entre 0 y 90 grados.  

'''

import numpy as np
import matplotlib.pyplot as plt
from math import pi

print("\n ----- EJERCICIO 4.c. --------------------------------------------------------- \n")

ciclos = 10

#amplitudes
amp = 1
#frecuencias
f1 = 1
f2 = 1
w1 = 2*pi*f1
w2 = 2*pi*f2
#desfase
ø1 = 0
ø2 = 0

#muestreo
f_sampling = max(f1,f2)*50
T_sampling = 1/f_sampling
sampling_time = np.arange(0, ciclos/max(f1,f2), T_sampling) #sampleo 100 ciclos

#genero vectores de amplitud para signal 1 y 2
signal_1 = amp*np.sin(w1*sampling_time + ø1)
signal_2 = amp*np.sin(w2*sampling_time + ø2)

#'''
#agrego ruido a las señales
ruido_1 = np.random.normal(0, amp*0.05, size=len(sampling_time))
ruido_2 = np.random.normal(0, amp*0.05, size=len(sampling_time))

#Se lo sumamos a las señales originales
signal_1 = signal_1 + ruido_1
signal_2 = signal_2 + ruido_2
#'''

#visualización de señales
plt.plot(sampling_time, signal_1, label='Signal 1')
plt.plot(sampling_time, signal_2, label='Signal 2')
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud [V]")
plt.legend()
#plt.grid()
plt.show()


print("\n ----- EJERCICIO 4.c.i.: coherencia de señales -------------------------------- \n")
#Aqui ayuda con chat GPT...
from scipy.signal import welch
from scipy.signal import coherence


f_coherence, Cxy = coherence(signal_1, signal_2, f_sampling, nperseg=128)

plt.plot(f_coherence, Cxy, label='Coherencia')
plt.ylim(-0.1, 1.1)  # Obliga al eje Y a mostrar de 0 a 1 en lugar del micro-zoom

plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Coherencia")
plt.legend()
plt.show()