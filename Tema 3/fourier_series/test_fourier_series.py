"""Test de FourierSeries sin gráficos"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from fourier_theoretical import FourierTheoretical
from fourier_series import FourierSeries

# Parámetros
f = 10
T = 1/f
D = 0.9
num_harmonics = 6

# Definir señal cuadrada
def square_wave_func(t):
    tau = (t + T/2) % T - T/2
    return 1.0 if abs(tau) <= D*T/2 else 0.0

# Calcular coeficientes teóricos
theoretical = FourierTheoretical(
    signal_func=square_wave_func,
    period=T,
    amplitude=1.0,
    duty_cycle=D,
    num_harmonics=num_harmonics
)
theoretical.calculate_all_coefficients()

print("=" * 60)
print("SERIE DE FOURIER - PRUEBA")
print("=" * 60)
print(f"a0 = {theoretical.a0:.6f}")
print(f"Período T = {T:.4f} s")
print(f"Duty cycle D = {D:.2f}")
print(f"Armónicos: {num_harmonics}")

# Crear serie de Fourier
fourier_series = FourierSeries(
    a0=theoretical.a0,
    an_coefficients=theoretical.an_coefficients,
    bn_coefficients=theoretical.bn_coefficients,
    period=T
)

print("\n" + "=" * 60)
print("EVALUACIÓN EN PUNTOS ESPECÍFICOS")
print("=" * 60)

test_times = [0.0, 0.025, 0.05, 0.075, 0.1]
for t in test_times:
    original = square_wave_func(t)
    reconstructed = fourier_series.evaluate(t)
    print(f"  t={t:.3f}: Original={original:.4f}, Reconstruida={reconstructed:.4f}")

print("\n" + "=" * 60)
print("ERROR CUADRÁTICO MEDIO (MSE)")
print("=" * 60)

# Generar señal para test
time_test = np.linspace(0, T, 500)
signal_original = np.array([square_wave_func(t) for t in time_test])

for nt in range(1, num_harmonics + 1):
    error = fourier_series.get_error(signal_original, time_test, num_terms=nt)
    print(f"  {nt} armónico{'s' if nt > 1 else ''}: MSE = {error:.8f}")

print("\n✓ Test de FourierSeries completado exitosamente")
