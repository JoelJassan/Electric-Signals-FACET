'''
Generar 100 mil muestras de una señal aleatoria con distribución uniforme, y 100 mil 
de una señal aleatoria con distribución normal. Use las funciones "rand" y "randn". 
Compruebe mínimamente la distribución estadística de las muestras de cada caso 
empleando un histograma.  
'''
import matplotlib.pyplot as plt
import numpy as np

#help(np.random.rand)
#help(np.random.randn)

#parametros generales
n = 100000
bins = 100

#generacion de muestras
uniforme = np.random.rand(n)
normal = np.random.randn(n)

#modifico sigma y mu
sigma = .5 #desviacion estandar
mu = 5 #media
normal_mod = mu + sigma*normal

#visualización de graficas
fig, ax = plt.subplots(1, 2)

ax[0].hist(uniforme, bins, density=True, edgecolor='black', linewidth=.5)
ax[0].set_xlabel("Rango de valores")
ax[0].set_ylabel("Densidad de probabilidad uniforme")
#ax[1].set_title("Histograma")

ax[1].hist(normal, bins, density=True, edgecolor='black', linewidth=.5)
ax[1].hist(normal_mod, bins, density=True, edgecolor='black', linewidth=.5)
ax[1].set_xlabel("Rango de valores")
ax[1].set_ylabel("Densidad de probabilidad normal")

plt.tight_layout()
plt.show()
