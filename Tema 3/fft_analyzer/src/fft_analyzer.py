"""
Módulo para análisis de FFT de señales discretas.
Proporciona la clase FFTAnalyzer para calcular y analizar
transformadas rápidas de Fourier de manera genérica.
"""

import numpy as np
import matplotlib.pyplot as plt


class FFTAnalyzer:
    """
    Clase genérica para calcular la FFT de una señal discreta.
    Permite extraer armónicos específicos y almacenarlos en una lista.
    """
    
    def __init__(self, signal, sampling_frequency, num_harmonics=5):
        """
        Inicializa el analizador FFT.
        
        Args:
            signal: Array con las muestras de la señal
            sampling_frequency: Frecuencia de muestreo en Hz
            num_harmonics: Cantidad de armónicos a calcular
        """
        self.signal = np.array(signal)
        self.fs = sampling_frequency
        self.num_harmonics = num_harmonics
        self.harmonics = []  # Lista para almacenar los armónicos
        self.frequencies = []  # Frecuencias correspondientes
        self.magnitudes = []  # Magnitudes de los armónicos
        
    def calculate_fft(self):
        """
        Calcula la FFT de la señal y retorna solo los primeros num_harmonics.
        Escala correctamente los coeficientes de Fourier.
        
        Returns:
            tuple: (frecuencias, magnitudes) de los primeros armónicos
        """
        # Aplicar FFT
        fft_values = np.fft.fft(self.signal)

        # Calcular frecuencias
        n = len(self.signal)
        frequencies = np.fft.fftfreq(n, 1/self.fs)

        # Calcular magnitudes normalizadas
        # Para coeficientes de Fourier: DC = |X[0]|/N, an (n>0) = 2*|X[n]|/N
        magnitudes = np.abs(fft_values) / n
        if n > 1:
            magnitudes[1:] = 2.0 * magnitudes[1:]

        # Tomar solo los primeros (incluyendo DC en índice 0)
        end_idx = self.num_harmonics + 1
        self.frequencies = frequencies[:end_idx]
        self.magnitudes = magnitudes[:end_idx]

        return self.frequencies, self.magnitudes
    
    def extract_harmonics(self):
        """
        Extrae los armónicos calculados y los almacena en una lista.
        
        Returns:
            list: Lista con los valores de magnitud de los armónicos
        """
        if len(self.magnitudes) == 0:
            self.calculate_fft()
        
        # Los datos ya contienen solo los armónicos solicitados
        self.harmonics = self.magnitudes.tolist()
        
        return self.harmonics
    
    def get_harmonics(self):
        """
        Retorna la lista de armónicos calculados.
        
        Returns:
            list: Lista con magnitudes de los armónicos
        """
        return self.harmonics
    
    def get_harmonic_info(self):
        """
        Retorna información detallada de los armónicos.
        
        Returns:
            list: Lista de dicts con número, frecuencia y magnitud de cada armónico
        """
        if len(self.harmonics) == 0:
            self.extract_harmonics()
        
        harmonic_info = []
        for i, magnitude in enumerate(self.harmonics):
            harmonic_number = i  # 0 corresponde a DC
            frequency = self.frequencies[i]
            harmonic_info.append({
                'numero': harmonic_number,
                'frecuencia': frequency,
                'magnitud': magnitude
            })
        
        return harmonic_info
    
    def plot_spectrum(self, title="Espectro de Frecuencias", show_harmonics=True):
        """
        Grafica el espectro de frecuencias con solo los armónicos solicitados.
        
        Args:
            title: Título del gráfico
            show_harmonics: Parámetro deprecated (mantiene compatibilidad)
        """
        if len(self.magnitudes) == 0:
            self.calculate_fft()
        
        plt.figure(figsize=(10, 5))
        plt.stem(self.frequencies, self.magnitudes, basefmt=' ')
        
        plt.xlabel("Frecuencia [Hz]")
        plt.ylabel("Magnitud")
        plt.title(title)
        plt.grid(True, alpha=0.3)
        plt.xlim(left=0)
