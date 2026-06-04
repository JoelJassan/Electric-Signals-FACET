# FFT Analyzer - Módulo de Análisis de Transformadas de Fourier

## Estructura del Proyecto

```
fft_analyzer/
├── __init__.py          # Inicializador del paquete
├── README.md            # Este archivo
└── src/
    ├── __init__.py      # Inicializador del submódulo
    └── fft_analyzer.py  # Implementación de la clase FFTAnalyzer
```

## Descripción

El paquete `fft_analyzer` proporciona herramientas genéricas para:

- **Calcular FFT** de señales discretas
- **Extraer armónicos** específicos y almacenarlos en listas
- **Visualizar espectros** de frecuencias
- **Analizar información** detallada de armónicos

## Uso

### Importar la clase

```python
from fft_analyzer import FFTAnalyzer
```

### Ejemplo básico

```python
import numpy as np

# Crear analizador con una señal, frecuencia de muestreo y cantidad de armónicos
analyzer = FFTAnalyzer(signal, sampling_frequency=1000, num_harmonics=5)

# Calcular FFT
frequencies, magnitudes = analyzer.calculate_fft()

# Extraer armónicos
harmonics_list = analyzer.extract_harmonics()

# Obtener información detallada
harmonic_info = analyzer.get_harmonic_info()

# Visualizar espectro
analyzer.plot_spectrum(title="Mi Espectro")
```

## Métodos Principales

### `calculate_fft()`
Calcula la transformada rápida de Fourier de la señal.

**Retorna:** `(frecuencias, magnitudes)` de la mitad positiva del espectro

### `extract_harmonics()`
Extrae los primeros N armónicos y los almacena en una lista interna.

**Retorna:** `list` con los valores de magnitud de los armónicos

### `get_harmonics()`
Obtiene la lista de armónicos calculados.

**Retorna:** `list` con magnitudes de los armónicos

### `get_harmonic_info()`
Retorna información detallada de cada armónico.

**Retorna:** `list` de dicts con `{'numero', 'frecuencia', 'magnitud'}`

### `plot_spectrum(title, show_harmonics)`
Visualiza el espectro de frecuencias con opción de resaltar armónicos.

## Parámetros del Constructor

- **signal**: Array con las muestras de la señal
- **sampling_frequency**: Frecuencia de muestreo en Hz
- **num_harmonics**: Cantidad de armónicos a extraer (default: 5)

## Autor

Tema 3 - Electric Signals FACET
