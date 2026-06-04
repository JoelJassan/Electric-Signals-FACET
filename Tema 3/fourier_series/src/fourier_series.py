"""
Módulo para reconstrucción de señales mediante series de Fourier.
Permite evaluar la serie de Fourier en cualquier punto y visualizar
la aproximación de la señal original.
"""

import numpy as np
import matplotlib.pyplot as plt


class FourierSeries:
    """
    Clase para reconstruir y evaluar series trigonométricas de Fourier.
    """
    
    def __init__(self, a0, an_coefficients, bn_coefficients, period=1.0):
        """
        Inicializa la serie de Fourier.
        
        Args:
            a0: Coeficiente DC (componente a0)
            an_coefficients: Lista de coeficientes coseno [a1, a2, ..., an]
            bn_coefficients: Lista de coeficientes seno [b1, b2, ..., bn]
            period: Período de la señal
        """
        self.a0 = a0
        self.an = np.array(an_coefficients)
        self.bn = np.array(bn_coefficients)
        self.T = period
        self.num_harmonics = len(an_coefficients)
        
    def evaluate(self, t):
        """
        Evalúa la serie de Fourier en el tiempo t.
        
        f(t) = a0/2 + Σ[an*cos(n*ω*t) + bn*sin(n*ω*t)]
        
        Args:
            t: Tiempo(s) en el que evaluar (escalar o array)
            
        Returns:
            float o array: Valor de la serie en tiempo t
        """
        omega_0 = 2 * np.pi / self.T
        
        # Término DC
        result = self.a0 / 2.0
        
        # Sumatoria de armónicos
        for n in range(1, self.num_harmonics + 1):
            an = self.an[n - 1]
            bn = self.bn[n - 1]
            result += an * np.cos(n * omega_0 * t) + bn * np.sin(n * omega_0 * t)
        
        return result
    
    def evaluate_partial(self, t, num_terms):
        """
        Evalúa la serie de Fourier usando solo los primeros num_terms armónicos.
        
        Args:
            t: Tiempo(s) en el que evaluar (escalar o array)
            num_terms: Número de armónicos a incluir (máximo num_harmonics)
            
        Returns:
            float o array: Valor de la serie parcial en tiempo t
        """
        num_terms = min(num_terms, self.num_harmonics)
        omega_0 = 2 * np.pi / self.T
        
        # Término DC
        result = self.a0 / 2.0
        
        # Sumatoria de los primeros num_terms armónicos
        for n in range(1, num_terms + 1):
            an = self.an[n - 1]
            bn = self.bn[n - 1]
            result += an * np.cos(n * omega_0 * t) + bn * np.sin(n * omega_0 * t)
        
        return result
    
    def reconstruct_signal(self, time_array, num_terms=None):
        """
        Reconstruye la señal en un array de tiempos.
        
        Args:
            time_array: Array de tiempos
            num_terms: Número de armónicos a usar (None = todos)
            
        Returns:
            array: Señal reconstruida
        """
        if num_terms is None:
            num_terms = self.num_harmonics
        
        signal = np.array([self.evaluate_partial(t, num_terms) for t in time_array])
        return signal
    
    def plot_approximation(self, original_signal, time_array, title="Reconstrucción de Serie de Fourier"):
        """
        Grafica la señal original y su aproximación mediante serie de Fourier.
        
        Args:
            original_signal: Array con la señal original
            time_array: Array de tiempos
            title: Título del gráfico
        """
        reconstructed = self.reconstruct_signal(time_array)
        
        plt.figure(figsize=(12, 5))
        
        plt.plot(time_array, original_signal, 'b-', label='Señal original', linewidth=2)
        plt.plot(time_array, reconstructed, 'r--', label=f'Serie Fourier ({self.num_harmonics} armónicos)', linewidth=2)
        
        plt.xlabel("Tiempo [s]")
        plt.ylabel("Amplitud")
        plt.title(title)
        plt.legend()
        plt.grid(True, alpha=0.3)
        
    def plot_convergence(self, original_signal, time_array, max_terms=None, title="Convergencia de la Serie de Fourier"):
        """
        Grafica múltiples aproximaciones con número creciente de armónicos.
        
        Args:
            original_signal: Array con la señal original
            time_array: Array de tiempos
            max_terms: Máximo número de armónicos a mostrar (None = todos)
            title: Título del gráfico
        """
        if max_terms is None:
            max_terms = self.num_harmonics
        
        plt.figure(figsize=(14, 6))
        
        # Señal original
        plt.plot(time_array, original_signal, 'k-', label='Original', linewidth=2.5, zorder=10)
        
        # Aproximaciones con diferente número de armónicos
        colors = plt.cm.viridis(np.linspace(0, 1, max_terms))
        
        for n in range(1, min(max_terms + 1, self.num_harmonics + 1)):
            reconstructed = self.reconstruct_signal(time_array, num_terms=n)
            plt.plot(time_array, reconstructed, '--', color=colors[n-1], 
                    label=f'{n} armónico{"" if n == 1 else "s"}', alpha=0.7, linewidth=1.5)
        
        plt.xlabel("Tiempo [s]")
        plt.ylabel("Amplitud")
        plt.title(title)
        plt.legend(loc='best', fontsize=9)
        plt.grid(True, alpha=0.3)
    
    def get_error(self, original_signal, time_array, num_terms=None):
        """
        Calcula el error cuadrático medio (MSE) entre la serie y la señal original.
        
        Args:
            original_signal: Array con la señal original
            time_array: Array de tiempos
            num_terms: Número de armónicos a usar (None = todos)
            
        Returns:
            float: Error cuadrático medio
        """
        if num_terms is None:
            num_terms = self.num_harmonics
        
        reconstructed = self.reconstruct_signal(time_array, num_terms=num_terms)
        mse = np.mean((original_signal - reconstructed)**2)
        
        return mse
    
    def print_info(self):
        """Imprime información sobre la serie de Fourier."""
        print(f"Coeficiente a0: {self.a0:.6f}")
        print(f"Período: {self.T:.6f} s")
        print(f"Número de armónicos: {self.num_harmonics}")
        print(f"\nPrimeros armónicos:")
        for n in range(min(5, self.num_harmonics)):
            print(f"  Armónico {n+1}: a{n+1}={self.an[n]:.6f}, b{n+1}={self.bn[n]:.6f}")
        if self.num_harmonics > 5:
            print(f"  ... ({self.num_harmonics - 5} más)")
