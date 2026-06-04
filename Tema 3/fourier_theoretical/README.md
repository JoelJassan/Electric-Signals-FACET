# Fourier Theoretical - Cálculo Analítico de Coeficientes

## Estructura del Proyecto

```
fourier_theoretical/
├── __init__.py          # Inicializador del paquete
├── README.md            # Este archivo
└── src/
    ├── __init__.py      # Inicializador del submódulo
    └── fourier_theoretical.py  # Implementación de la clase FourierTheoretical
```

## Descripción

El paquete `fourier_theoretical` proporciona herramientas para calcular analíticamente:

- **Coeficiente a0** (componente DC)
- **Coeficientes an** (términos coseno)
- **Coeficientes bn** (términos seno)
- **Espectro de magnitud** (√(an² + bn²))
- **Espectro de fase** (arctan(bn/an))

## Uso

### Importar la clase

```python
from fourier_theoretical import FourierTheoretical
```

### Ejemplo: Onda Cuadrada

```python
import numpy as np

# Definir la función de la onda cuadrada
def square_wave(t, period=1.0, duty_cycle=0.5):
    tau = (t + period/2) % period - period/2
    return 1.0 if abs(tau) <= duty_cycle * period / 2 else 0.0

# Crear analizador teórico
theoretical = FourierTheoretical(
    signal_func=square_wave,
    period=1.0,
    amplitude=1.0,
    duty_cycle=0.5,
    num_harmonics=5
)

# Calcular coeficientes
a0, an_list, bn_list = theoretical.calculate_all_coefficients()

# Mostrar información
theoretical.print_coefficients()

# Obtener espectro de magnitud
magnitudes = theoretical.get_magnitude_spectrum()

# Visualizar
theoretical.plot_spectrum()
```

## Métodos Principales

### `calculate_a0()`
Calcula el coeficiente DC.

**Retorna:** `float` - Valor de a0

### `calculate_an(n)`
Calcula el coeficiente an para un armónico específico.

**Parámetros:**
- n: Número de armónico

**Retorna:** `float` - Valor de an

### `calculate_bn(n)`
Calcula el coeficiente bn para un armónico específico.

**Parámetros:**
- n: Número de armónico

**Retorna:** `float` - Valor de bn

### `calculate_all_coefficients()`
Calcula todos los coeficientes.

**Retorna:** `tuple` - (a0, an_list, bn_list)

### `get_magnitude_spectrum()`
Calcula el espectro de magnitud.

**Retorna:** `list` - Magnitudes √(an² + bn²)

### `get_phase_spectrum()`
Calcula el espectro de fase.

**Retorna:** `list` - Fases en radianes

### `print_coefficients()`
Imprime todos los coeficientes de forma legible.

### `plot_spectrum(title)`
Visualiza el espectro de magnitud.

## Parámetros del Constructor

- **signal_func**: Función que define la señal f(t)
- **period**: Período de la señal
- **amplitude**: Amplitud de la señal
- **duty_cycle**: Ciclo activo (para ondas cuadradas)
- **num_harmonics**: Cantidad de armónicos a calcular

## Notas Matemáticas

Para una serie trigonométrica de Fourier:
$$f(t) = \frac{a_0}{2} + \sum_{n=1}^{\infty} [a_n \cos(n\omega_0 t) + b_n \sin(n\omega_0 t)]$$

Donde:
- $a_0 = \frac{2}{T} \int_0^{T/2} f(t) \, dt$
- $a_n = \frac{2}{T} \int_0^T f(t) \cos(n\omega_0 t) \, dt$
- $b_n = \frac{2}{T} \int_0^T f(t) \sin(n\omega_0 t) \, dt$
- $\omega_0 = \frac{2\pi}{T}$

## Autor

Tema 3 - Electric Signals FACET
