---
inclusion: always
---

# Estándares del Curso de Python Avanzado para IA

## Idioma y Documentación

- **Documentación en Markdown**: Siempre en castellano
- **Código Python**: Siempre en inglés
- **Comentarios en código**: En inglés
- **Docstrings**: En inglés, formato Sphinx
- **Nombres de variables/funciones/clases**: En inglés

## Estándares de Código

### Docstrings (Sphinx Format)

Todos los módulos, clases y funciones deben incluir docstrings en formato Sphinx:

```python
def calculate_mean(values):
    """
    Calculate the arithmetic mean of a list of numbers.
    
    :param values: List of numeric values
    :type values: list[float]
    :return: The arithmetic mean
    :rtype: float
    :raises ValueError: If the list is empty
    
    Example:
        >>> calculate_mean([1, 2, 3, 4, 5])
        3.0
    """
    if not values:
        raise ValueError("Cannot calculate mean of empty list")
    return sum(values) / len(values)
```

Para clases:

```python
class DataProcessor:
    """
    Process and transform data for machine learning pipelines.
    
    :param config: Configuration dictionary
    :type config: dict
    :ivar data: Stored data
    :vartype data: pandas.DataFrame
    """
    
    def __init__(self, config):
        """
        Initialize the DataProcessor.
        
        :param config: Configuration parameters
        :type config: dict
        """
        self.config = config
        self.data = None
```

### Linting con Ruff

Todo el código debe pasar las verificaciones de Ruff sin errores:

```bash
ruff check .
ruff format .
```

Configuración mínima en `pyproject.toml`:

```toml
[tool.ruff]
line-length = 100
target-version = "py310"

[tool.ruff.lint]
select = ["E", "F", "I", "N", "W"]
ignore = ["E501"]  # Line too long (handled by formatter)
```

### Convenciones de Nombres

- **Variables y funciones**: `snake_case`
- **Clases**: `PascalCase`
- **Constantes**: `UPPER_SNAKE_CASE`
- **Módulos**: `lowercase` o `snake_case`

### Type Hints

Usar type hints en todas las funciones:

```python
from typing import List, Dict, Optional

def process_data(data: List[float], threshold: float = 0.5) -> Dict[str, float]:
    """Process numerical data with a threshold."""
    pass
```

## Estructura de Notebooks

Cada notebook debe seguir esta estructura:

1. **Título y descripción** (en castellano)
2. **Objetivos de aprendizaje** (en castellano)
3. **Contenido teórico** con ejemplos (documentación en castellano, código en inglés)
4. **Ejercicios prácticos** (instrucciones en castellano, código en inglés)
5. **Resumen** (en castellano)

## Estructura de Módulos Python

Los ejercicios en la carpeta `exercises/` deben:

1. Incluir docstrings completos en formato Sphinx
2. Pasar Ruff sin errores
3. Incluir type hints
4. Tener tests unitarios correspondientes (cuando aplique)

## Imports

Organizar imports en este orden:

1. Standard library
2. Third-party packages
3. Local modules

```python
import os
import sys
from typing import List

import numpy as np
import pandas as pd

from exercises.utils import helper_function
```

## Buenas Prácticas

- Código limpio y legible
- Funciones pequeñas y con un solo propósito
- Evitar magic numbers (usar constantes)
- Manejo apropiado de excepciones
- Logging cuando sea apropiado
- Validación de inputs en funciones públicas
