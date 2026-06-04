# Fourier Series - Reconstrucción de Señales

## Estructura del Proyecto

```
fourier_series/
├── __init__.py          # Inicializador del paquete
├── README.md            # Este archivo
└── src/
    ├── __init__.py      # Inicializador del submódulo
    └── fourier_series.py  # Implementación de la clase FourierSeries
```

## Descripción

El paquete `fourier_series` proporciona herramientas para:

- **Evaluar la serie de Fourier** en cualquier punto del tiempo
- **Reconstruir señales** usando aproximaciones con N armónicos
- **Visualizar convergencia** de la serie a la señal original
- **Calcular errores** (MSE) entre la reconstrucción y el original

## Uso

### Importar la clase

```python
from fourier_series import FourierSeries
```

### Ejemplo: Reconstruir una onda cuadrada

```python
import numpy as np

# Coeficientes teóricos ya calculados
a0 = 0.5
an = [0.6366, 0.0, -0.2122, 0.0, 0.1273, 0.0]
bn = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

# Crear serie de Fourier
series = FourierSeries(a0, an, bn, period=1.0)

# Evaluar en un punto
valor_en_t = series.evaluate(t=0.25)

# Reconstruir señal en un rango de tiempo
tiempo = np.linspace(0, 1, 1000)
señal_reconstruida = series.reconstruct_signal(tiempo)

# Visualizar aproximación
series.plot_approximation(original_signal, tiempo)

# Visualizar convergencia
series.plot_convergence(original_signal, tiempo, max_terms=6)

# Calcular error
mse = series.get_error(original_signal, tiempo)
```

## Métodos Principales

### `evaluate(t)`
Evalúa la serie completa en el tiempo t.

**Retorna:** Valor escalar o array según entrada

### `evaluate_partial(t, num_terms)`
Evalúa la serie con solo los primeros num_terms armónicos.

**Parámetros:**
- t: Tiempo(s)
- num_terms: Número de armónicos

### `reconstruct_signal(time_array, num_terms)`
Reconstruye la señal en un array de tiempos.

**Retorna:** Array con la señal reconstruida

### `plot_approximation(original_signal, time_array, title)`
Visualiza la señal original vs reconstruida.

### `plot_convergence(original_signal, time_array, max_terms, title)`
Visualiza múltiples aproximaciones con armónicos crecientes.

### `get_error(original_signal, time_array, num_terms)`
Calcula MSE entre reconstrucción y original.

**Retorna:** float - Error cuadrático medio

### `print_info()`
Imprime información sobre la serie.

## Parámetros del Constructor

- **a0**: Coeficiente DC
- **an_coefficients**: Lista de coeficientes coseno
- **bn_coefficients**: Lista de coeficientes seno
- **period**: Período de la señal (default: 1.0)

## Notas Matemáticas

$$f(t) = \frac{a_0}{2} + \sum_{n=1}^{N} [a_n \cos(n\omega_0 t) + b_n \sin(n\omega_0 t)]$$

Donde:
- $\omega_0 = \frac{2\pi}{T}$ (frecuencia angular fundamental)
- N es el número de armónicos

## Autor

Tema 3 - Electric Signals FACET
