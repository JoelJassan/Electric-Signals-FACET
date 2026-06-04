'''
A partir de una versión discreta de la señal del ejercicio 1 (ciclo activo de 50%), calcule numéricamente una estimación de los primeros 5 coeficientes de la serie trigonométrica de 
Fourier. 
Haga esto utilizando primero 100 muestras por período y luego repita para 1000 muestras por 
período.  Compare con los valores teóricos mostrando en una gráfica el espectro teórico y el 
calculado numéricamente para cada uno de los dos casos.  
'''

import numpy as np
import matplotlib.pyplot as plt

# Importar clases de módulos locales
from fft_analyzer import FFTAnalyzer
from fourier_theoretical import FourierTheoretical
from fourier_series import FourierSeries


# ===== Generación de Señales Cuadradas ===== #

# Parámetros de la señal
f = 10
T = 1/f  # Período
D = 0.9  # Ciclo activo del 50%
N1 = 100  # Número de muestras por período (caso 1)
N2 = 1000  # Número de muestras por período (caso 2)

# Muestreo - Usar solo 1 período para comparación correcta con coeficientes teóricos
f_sampling_1 = N1/T
f_sampling_2 = N2/T

sampling_time_1 = np.arange(0, T, 1/f_sampling_1)
sampling_time_2 = np.arange(0, T, 1/f_sampling_2)


# Generación de señales discretas (onda cuadrada)
square_wave_1 = []
for t in sampling_time_1:
    tau = (t + T/2) % T - T/2 

    if abs(tau) <= D*T/2:  # centrado en la mitad del pulso activo
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


# ===== Análisis FFT con POO ===== #

# Cantidad de armónicos a calcular
num_harmonics = 6

# Crear analizadores para cada caso
analyzer_1 = FFTAnalyzer(square_wave_1, f_sampling_1, num_harmonics)
analyzer_2 = FFTAnalyzer(square_wave_2, f_sampling_2, num_harmonics)

# Calcular FFT y extraer armónicos
analyzer_1.calculate_fft()
analyzer_1.extract_harmonics()

analyzer_2.calculate_fft()
analyzer_2.extract_harmonics()

# ===== Análisis Teórico de Fourier ===== #

# Definir la función de la onda cuadrada para cálculo teórico
def square_wave_func(t):
    """Función de onda cuadrada para integración analítica"""
    tau = (t + T/2) % T - T/2
    return 1.0 if abs(tau) <= D*T/2 else 0.0

# Crear analizadores teóricos
theoretical = FourierTheoretical(
    signal_func=square_wave_func,
    period=T,
    amplitude=1.0,
    duty_cycle=D,
    num_harmonics=num_harmonics
)

# Calcular coeficientes teóricos
theoretical.calculate_all_coefficients()

# ===== Análisis de Serie de Fourier ===== #

# Crear serie de Fourier usando coeficientes teóricos
# Extraer coeficientes an y bn (sin incluir índice 0 que es DC)
an_coefficients = theoretical.an_coefficients
bn_coefficients = theoretical.bn_coefficients

fourier_series = FourierSeries(
    a0=theoretical.a0,
    an_coefficients=an_coefficients,
    bn_coefficients=bn_coefficients,
    period=T
)

# Generar array de tiempos continuo para reconstrucción
time_continuous = np.linspace(0, T, 1000)

print("\n" + "=" * 60)
print("=" * 60)
print(f"CASO 1: {N1} muestras por período")
print("=" * 60)
print(f"\nArmónicos calculados (primeros {num_harmonics}):")
for info in analyzer_1.get_harmonic_info():
    print(f"  Armónico {info['numero']}: Frecuencia = {info['frecuencia']:.2f} Hz, Magnitud = {info['magnitud']:.6f}")

print(f"\nLista de magnitudes de armónicos: {analyzer_1.get_harmonics()}")

print("\n" + "=" * 60)
print(f"CASO 2: {N2} muestras por período")
print("=" * 60)
print(f"\nArmónicos calculados (primeros {num_harmonics}):")
for info in analyzer_2.get_harmonic_info():
    print(f"  Armónico {info['numero']}: Frecuencia = {info['frecuencia']:.2f} Hz, Magnitud = {info['magnitud']:.6f}")

print(f"\nLista de magnitudes de armónicos: {analyzer_2.get_harmonics()}")

# ===== Mostrar Coeficientes Teóricos de Fourier ===== #

print("\n" + "=" * 60)
print("COEFICIENTES TEÓRICOS DE FOURIER")
print("=" * 60)
theoretical.print_coefficients()

# Obtener espectros para comparación
freq_1, mag_1 = analyzer_1.frequencies, analyzer_1.magnitudes
freq_2, mag_2 = analyzer_2.frequencies, analyzer_2.magnitudes
freq_theo, mag_theo = theoretical.frequencies, theoretical.get_magnitude_spectrum()

# Calcular envolvente teórica continua: sin(n*π*D)/(n*π)
omega_0 = 2 * np.pi / T
f_0 = 1.0 / T  # Frecuencia fundamental (1 Hz para T=1)
n_continuous = np.linspace(0.1, num_harmonics + 2, 200)
f_continuous = n_continuous * f_0
envelope_theo = np.abs(np.sin(n_continuous * np.pi * D) / (n_continuous * np.pi))

# Crear figura con 2x2 subplots
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Subplot 1 (arriba izq): Señales en el tiempo
axes[0, 0].plot(sampling_time_1, square_wave_1, label='N=100', marker='o', markersize=3, alpha=0.7)
axes[0, 0].plot(sampling_time_2, square_wave_2, label='N=1000', marker='.', markersize=2, alpha=0.7)
axes[0, 0].set_xlabel("Tiempo [s]")
axes[0, 0].set_ylabel("Amplitud [V]")
axes[0, 0].set_title("Señales Cuadradas Discretas (1 período)")
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# Subplot 2 (arriba der): Espectro Teórico con Envolvente
axes[0, 1].stem(freq_theo, mag_theo, basefmt=' ', linefmt='g-', markerfmt='go', label='Armónicos')
axes[0, 1].plot(f_continuous, envelope_theo, 'r--', linewidth=2, label='Envolvente: sin(nπD)/(nπ)')
axes[0, 1].set_xlabel("Frecuencia [Hz]")
axes[0, 1].set_ylabel("Magnitud")
axes[0, 1].set_title(f"Espectro Teórico ({num_harmonics} armónicos)")
axes[0, 1].legend()
axes[0, 1].grid(True, alpha=0.3)
axes[0, 1].set_xlim(left=0)

# Subplot 3 (abajo izq): FFT N=100 vs Envolvente Teórica
axes[1, 0].stem(freq_1, mag_1, basefmt=' ', linefmt='b-', markerfmt='bs', label='FFT N=100')
axes[1, 0].plot(f_continuous, envelope_theo, 'r--', linewidth=2, label='Envolvente teórica')
axes[1, 0].set_xlabel("Frecuencia [Hz]")
axes[1, 0].set_ylabel("Magnitud")
axes[1, 0].set_title(f"Comparación: FFT N={N1} vs Envolvente Teórica")
axes[1, 0].legend()
axes[1, 0].grid(True, alpha=0.3)
axes[1, 0].set_xlim(left=0)

# Subplot 4 (abajo der): FFT N=1000 vs Envolvente Teórica
axes[1, 1].stem(freq_2, mag_2, basefmt=' ', linefmt='b-', markerfmt='bs', label='FFT N=1000')
axes[1, 1].plot(f_continuous, envelope_theo, 'r--', linewidth=2, label='Envolvente teórica')
axes[1, 1].set_xlabel("Frecuencia [Hz]")
axes[1, 1].set_ylabel("Magnitud")
axes[1, 1].set_title(f"Comparación: FFT N={N2} vs Envolvente Teórica")
axes[1, 1].legend()
axes[1, 1].grid(True, alpha=0.3)
axes[1, 1].set_xlim(left=0)

plt.tight_layout()
plt.show()

# ===== Visualización de Reconstrucción de la Serie de Fourier ===== #

# Figura 1: Comparación de reconstrucción con todos los armónicos
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Subplot 1: Señal original vs reconstruida (N=100)
reconstructed_1 = fourier_series.reconstruct_signal(sampling_time_1)
axes[0].plot(sampling_time_1, square_wave_1, 'bo-', label='Original (N=100)', markersize=4, linewidth=2)
axes[0].plot(sampling_time_1, reconstructed_1, 'r--', label=f'Reconstruida ({num_harmonics} armónicos)', linewidth=2)
axes[0].set_xlabel("Tiempo [s]")
axes[0].set_ylabel("Amplitud")
axes[0].set_title(f"Reconstrucción: N=100 muestras")
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Subplot 2: Señal original vs reconstruida (N=1000)
reconstructed_2 = fourier_series.reconstruct_signal(sampling_time_2)
axes[1].plot(sampling_time_2, square_wave_2, 'b-', label='Original (N=1000)', linewidth=2)
axes[1].plot(sampling_time_2, reconstructed_2, 'r--', label=f'Reconstruida ({num_harmonics} armónicos)', linewidth=2)
axes[1].set_xlabel("Tiempo [s]")
axes[1].set_ylabel("Amplitud")
axes[1].set_title(f"Reconstrucción: N=1000 muestras")
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Figura 2: Convergencia de la serie (múltiples armónicos)
print("\n" + "=" * 60)
print("CONVERGENCIA DE LA SERIE DE FOURIER")
print("=" * 60)

fourier_series.plot_convergence(square_wave_2, sampling_time_2, max_terms=num_harmonics, 
                                title=f"Convergencia: Reconstrucción con 1 a {num_harmonics} armónicos")
plt.tight_layout()
plt.show()

# Figura 3: Cálculo de errores para diferentes números de armónicos
errors = []
num_terms_list = list(range(1, num_harmonics + 1))

for nt in num_terms_list:
    error = fourier_series.get_error(square_wave_2, sampling_time_2, num_terms=nt)
    errors.append(error)
    print(f"  {nt} armónico{'s' if nt > 1 else ''}: MSE = {error:.6f}")

plt.figure(figsize=(10, 5))
plt.semilogy(num_terms_list, errors, 'bo-', linewidth=2, markersize=8)
plt.xlabel("Número de armónicos")
plt.ylabel("Error cuadrático medio (MSE)")
plt.title("Convergencia del error al aumentar armónicos")
plt.grid(True, alpha=0.3, which='both')
plt.tight_layout()
plt.show()

print("\n✓ Análisis de serie de Fourier completado")
print("\nGráficos mostrados exitosamente.")