"""Script de prueba para ver la salida sin gráficos"""
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Usar backend que no muestre ventanas
import matplotlib.pyplot as plt

# Importar clases de módulos locales
from fft_analyzer import FFTAnalyzer
from fourier_theoretical import FourierTheoretical

# ===== Generación de Señales Cuadradas ===== #

# Parámetros de la señal
T = 1  # Período
D = 0.5  # Ciclo activo del 50%
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

# ===== Mostrar Resultados FFT ===== #
print("=" * 60)
print(f"CASO 1: {N1} muestras por período")
print("=" * 60)
print(f"\nArmónicos calculados (primeros {num_harmonics}):")
for info in analyzer_1.get_harmonic_info():
    print(f"  Armónico {info['numero']}: Frecuencia = {info['frecuencia']:.2f} Hz, Magnitud = {info['magnitud']:.6f}")

print(f"\nLista de magnitudes de armónicos FFT: {[f'{x:.6f}' for x in analyzer_1.get_harmonics()]}")

print("\n" + "=" * 60)
print(f"CASO 2: {N2} muestras por período")
print("=" * 60)
print(f"\nArmónicos calculados (primeros {num_harmonics}):")
for info in analyzer_2.get_harmonic_info():
    print(f"  Armónico {info['numero']}: Frecuencia = {info['frecuencia']:.2f} Hz, Magnitud = {info['magnitud']:.6f}")

print(f"\nLista de magnitudes de armónicos FFT: {[f'{x:.6f}' for x in analyzer_2.get_harmonics()]}")

# ===== Mostrar Coeficientes Teóricos de Fourier ===== #

print("\n" + "=" * 60)
print("COEFICIENTES TEÓRICOS DE FOURIER")
print("=" * 60)
theoretical.print_coefficients()

print("\n" + "=" * 60)
print("COMPARACIÓN FFT N=1000 vs TEÓRICO")
print("=" * 60)
freq_2, mag_2 = analyzer_2.frequencies, analyzer_2.magnitudes
freq_theo, mag_theo = theoretical.frequencies, theoretical.get_magnitude_spectrum()

for i in range(min(len(mag_2), len(mag_theo))):
    diff = abs(mag_2[i] - mag_theo[i])
    error_pct = 100 * diff / mag_theo[i] if mag_theo[i] != 0 else 0
    print(f"  Armónico {i+1}: FFT={mag_2[i]:.6f}, Teórico={mag_theo[i]:.6f}, Diferencia={diff:.6f} ({error_pct:.2f}%)")

print("\n✓ Script ejecutado exitosamente")
