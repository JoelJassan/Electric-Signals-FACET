"""
Módulo para cálculo de coeficientes teóricos de series de Fourier.
Proporciona la clase FourierTheoretical para calcular coeficientes
a0, an, bn de manera analítica.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate


class FourierTheoretical:
    """
    Clase para calcular analíticamente los coeficientes de la serie
    trigonométrica de Fourier: a0, an, bn.
    """
    
    def __init__(self, signal_func, period, amplitude=1.0, duty_cycle=0.5, num_harmonics=5):
        """
        Inicializa el calculador de Fourier teórico.
        
        Args:
            signal_func: Función que define la señal f(t) en un período
            period: Período de la señal
            amplitude: Amplitud de la señal
            duty_cycle: Ciclo activo (para señales cuadradas, 0 < duty_cycle < 1)
            num_harmonics: Cantidad de armónicos (an, bn) a calcular
        """
        self.signal_func = signal_func
        self.T = period
        self.amplitude = amplitude
        self.duty_cycle = duty_cycle
        self.num_harmonics = num_harmonics
        
        # Listas para almacenar coeficientes
        self.a0 = 0.0
        self.an_coefficients = []  # Coeficientes coseno (a1, a2, ..., an)
        self.bn_coefficients = []  # Coeficientes seno (b1, b2, ..., bn)
        self.frequencies = []  # Frecuencias correspondientes (incluye DC en índice 0 después de calcular)
        self.magnitudes = []
        
    def calculate_a0(self):
        """
        Calcula el coeficiente a0 (componente DC).
        a0 = (2/T) * ∫[0,T] f(t) dt
        
        Returns:
            float: Valor de a0
        """
        # Integración numérica
        integral, _ = integrate.quad(self.signal_func, 0, self.T)
        self.a0 = (2.0 / self.T) * integral
        
        return self.a0
    
    def calculate_an(self, n):
        """
        Calcula el coeficiente an para un armónico específico.
        an = (2/T) * ∫[0,T] f(t) * cos(n*ω*t) dt
        
        Args:
            n: Número de armónico
            
        Returns:
            float: Valor de an
        """
        omega = 2 * np.pi / self.T
        
        def integrand(t):
            return self.signal_func(t) * np.cos(n * omega * t)
        
        integral, _ = integrate.quad(integrand, 0, self.T)
        an = (2.0 / self.T) * integral
        
        return an
    
    def calculate_bn(self, n):
        """
        Calcula el coeficiente bn para un armónico específico.
        bn = (2/T) * ∫[0,T] f(t) * sin(n*ω*t) dt
        
        Args:
            n: Número de armónico
            
        Returns:
            float: Valor de bn
        """
        omega = 2 * np.pi / self.T
        
        def integrand(t):
            return self.signal_func(t) * np.sin(n * omega * t)
        
        integral, _ = integrate.quad(integrand, 0, self.T)
        bn = (2.0 / self.T) * integral
        
        return bn
    
    def calculate_all_coefficients(self):
        """
        Calcula todos los coeficientes (a0, an, bn).
        
        Returns:
            tuple: (a0, an_list, bn_list)
        """
        # Calcular a0
        self.calculate_a0()
        
        # Calcular an y bn para cada armónico
        self.an_coefficients = []
        self.bn_coefficients = []
        self.frequencies = []
        
        omega_0 = 2 * np.pi / self.T
        
        for n in range(1, self.num_harmonics + 1):
            an = self.calculate_an(n)
            bn = self.calculate_bn(n)
            
            self.an_coefficients.append(an)
            self.bn_coefficients.append(bn)
            self.frequencies.append(n * omega_0 / (2 * np.pi))  # Frecuencia en Hz
        # Construir espectro de magnitud y añadir componente DC (a0/2)
        magnitudes = [np.sqrt(an**2 + bn**2) for an, bn in zip(self.an_coefficients, self.bn_coefficients)]
        # Incluir DC al inicio
        self.frequencies = [0.0] + self.frequencies
        self.magnitudes = [self.a0 / 2.0] + magnitudes

        return self.a0, self.an_coefficients, self.bn_coefficients
    
    def get_magnitude_spectrum(self):
        """
        Calcula el espectro de magnitud a partir de los coeficientes.
        Magnitud = sqrt(an^2 + bn^2) para cada armónico.
        
        Returns:
            list: Magnitudes de los armónicos
        """
        if len(self.magnitudes) == 0:
            self.calculate_all_coefficients()

        return self.magnitudes
    
    def get_phase_spectrum(self):
        """
        Calcula el espectro de fase a partir de los coeficientes.
        Fase = atan2(bn, an) para cada armónico.
        
        Returns:
            list: Fases de los armónicos en radianes
        """
        if len(self.an_coefficients) == 0:
            self.calculate_all_coefficients()
        
        phases = []
        for an, bn in zip(self.an_coefficients, self.bn_coefficients):
            phase = np.arctan2(bn, an)
            phases.append(phase)
        
        return phases
    
    def print_coefficients(self):
        """Imprime los coeficientes de forma legible."""
        if len(self.an_coefficients) == 0:
            self.calculate_all_coefficients()

        print(f"a0 = {self.a0:.6f}")
        print("\nCoeficientes an (coseno):")
        for n, an in enumerate(self.an_coefficients, 1):
            print(f"  a{n} = {an:.6f}")
        
        print("\nCoeficientes bn (seno):")
        for n, bn in enumerate(self.bn_coefficients, 1):
            print(f"  b{n} = {bn:.6f}")
        
        magnitudes_full = self.get_magnitude_spectrum()
        magnitudes = magnitudes_full[1:]
        print("\nEspectro de magnitud (√(an² + bn²)):")
        for n, mag in enumerate(magnitudes, 1):
            print(f"  C{n} = {mag:.6f}")
    
    def plot_spectrum(self, title="Espectro Teórico de Fourier"):
        """
        Grafica el espectro de magnitud con envolvente analítica.
        
        Args:
            title: Título del gráfico
        """
        if len(self.an_coefficients) == 0:
            self.calculate_all_coefficients()
        
        magnitudes = self.get_magnitude_spectrum()
        
        plt.figure(figsize=(10, 5))
        
        # Gráfico de los armónicos discretos
        plt.stem(self.frequencies, magnitudes, basefmt=' ', linefmt='b-', markerfmt='bo', label='Armónicos')
        
        # Calcular y graficar la envolvente teórica para ondas cuadradas
        # Envolvente: |sin(n*π*D)/(n*π)|
        omega_0 = 2 * np.pi / self.T
        f_0 = omega_0 / (2 * np.pi)  # Frecuencia fundamental
        
        # Generar puntos continuos para la envolvente
        n_continuous = np.linspace(0.1, self.num_harmonics + 2, 200)
        f_continuous = n_continuous * f_0
        
        # Envolvente teórica para onda cuadrada: sin(n*π*D)/(n*π)
        envelope = np.abs(np.sin(n_continuous * np.pi * self.duty_cycle) / (n_continuous * np.pi))
        
        plt.plot(f_continuous, envelope, 'r--', linewidth=2, label='Envolvente teórica')
        
        plt.xlabel("Frecuencia [Hz]")
        plt.ylabel("Magnitud")
        plt.title(title)
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.xlim(left=0)
