# Formateo de Código

## Tabla de Contenidos

1. [Introducción](#introducción)
2. [Consistencia y Legibilidad](#1-consistencia-y-legibilidad)
3. [Herramientas de Formateo Automático](#2-herramientas-de-formateo-automático)
4. [Reglas de Formato Esenciales](#3-reglas-de-formato-esenciales)
5. [Organización de Imports](#4-organización-de-imports)
6. [Integración con Desarrollo](#5-integración-con-desarrollo)
7. [Resumen](#resumen-de-principios)

---

## Introducción

El formateo de código no es una cuestión de preferencias personales, sino de comunicación efectiva. Un código bien formateado se lee como prosa bien escrita, facilitando la comprensión y el mantenimiento.

**Referencia principal**: Martin, R. C. (2008). *Clean Code: A Handbook of Agile Software Craftsmanship*. Prentice Hall. Chapter 5: Formatting.

### Contexto: Por Qué Importa

**Problema real en Data/IA**:
Estás en un equipo de Data Science con 5 personas. Cada uno formatea el código diferente: uno usa 2 espacios, otro 4, otro mezcla tabs. Uno pone imports al azar, otro los ordena alfabéticamente. Cuando haces code review, pasas más tiempo discutiendo formato que lógica. Los merge conflicts son constantes por diferencias de espacios en blanco.

**Ejemplo concreto**:
Abres un notebook de un compañero para entender su modelo. El código tiene líneas de 200 caracteres, imports desordenados, funciones de 100 líneas sin espacios. Te toma 30 minutos entender algo que debería tomar 5. Cuando intentas modificarlo, rompes el formato y el linter explota con 50 errores.

**Consecuencias de NO usarlo**:
- **Code reviews lentos**: Discusiones sobre formato en vez de lógica
- **Merge conflicts**: Por diferencias de espacios y tabs
- **Código ilegible**: Difícil de entender y mantener
- **Onboarding lento**: Nuevos miembros tardan en adaptarse
- **Bugs ocultos**: Errores escondidos en código mal formateado
- **Pérdida de tiempo**: Horas formateando manualmente

### Principio Fundamental

> "Code formatting is about communication, and communication is the professional developer's first order of business."
>
> — Robert C. Martin, Clean Code

El código se lee muchas más veces de las que se escribe. El formateo consistente reduce la carga cognitiva y permite enfocarse en la lógica.

---

### El Concepto

**Definición técnica**:
El formateo de código es el conjunto de reglas y convenciones sobre cómo estructurar visualmente el código: indentación, espacios, longitud de líneas, orden de imports, etc. En Python, seguimos PEP 8 y usamos herramientas automáticas como Black y Ruff.

**Cómo funciona internamente**:
1. **Parser**: Herramienta lee el código y construye AST (Abstract Syntax Tree)
2. **Análisis**: Identifica violaciones de reglas de formato
3. **Transformación**: Reescribe el código siguiendo las reglas
4. **Output**: Genera código formateado consistentemente

**Terminología clave**:
- **PEP 8**: Guía de estilo oficial de Python
- **Black**: Formateador automático "sin opiniones"
- **Ruff**: Linter y formateador ultra-rápido (reemplazo de Flake8, isort, etc.)
- **AST**: Abstract Syntax Tree - representación estructural del código
- **Linter**: Herramienta que detecta problemas de estilo y errores potenciales

---

## 1. Consistencia y Legibilidad

### Por Qué Importa

La consistencia en el formato reduce la carga cognitiva. Cuando todo el código sigue las mismas reglas, el cerebro puede enfocarse en la lógica en vez de descifrar el formato.

**Referencia**: van Rossum, G., Warsaw, B., & Coghlan, N. (2001). PEP 8 – Style Guide for Python Code. <https://peps.python.org/pep-0008/>

---

### Ejemplo Incorrecto: Formato Inconsistente

```python
import os
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from typing import List,Dict
import numpy as np
from sklearn.model_selection import train_test_split

def train_model(data,target,test_size=0.2,random_state=42,n_estimators=100,max_depth=None):
    X=data.drop(columns=[target])
    y=data[target]
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=test_size,random_state=random_state)
    model=RandomForestClassifier(n_estimators=n_estimators,max_depth=max_depth,random_state=random_state)
    model.fit(X_train,y_train)
    train_score=model.score(X_train,y_train)
    test_score=model.score(X_test,y_test)
    return {'model':model,'train_score':train_score,'test_score':test_score,'feature_importance':dict(zip(X.columns,model.feature_importances_))}

# Línea super larga que hace muchas cosas y es difícil de leer porque no tiene saltos de línea y continúa y continúa
result = train_model(my_data, 'target_column', test_size=0.3, random_state=123, n_estimators=200, max_depth=10)
```

**Problemas**:

- **Imports desordenados**: Mezcla stdlib, third-party, sin orden
- **Sin espacios**: `List,Dict` en vez de `List, Dict`
- **Líneas largas**: Imposible leer sin scroll horizontal
- **Sin espacios alrededor de operadores**: `X=data` en vez de `X = data`
- **Parámetros sin espacios**: `test_size=0.2` en llamada
- **Función muy larga**: Todo en una línea
- **Sin type hints completos**: Falta tipo de retorno

---

### Ejemplo Correcto: Formato Consistente

```python
# Standard library
import os
from typing import Any

# Third-party
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def train_model(
    data: pd.DataFrame,
    target: str,
    test_size: float = 0.2,
    random_state: int = 42,
    n_estimators: int = 100,
    max_depth: int | None = None,
) -> dict[str, Any]:
    """
    Train a Random Forest model and return results.
    
    :param data: Training dataset
    :type data: pd.DataFrame
    :param target: Name of target column
    :type target: str
    :param test_size: Proportion of test set
    :type test_size: float
    :param random_state: Random seed
    :type random_state: int
    :param n_estimators: Number of trees
    :type n_estimators: int
    :param max_depth: Maximum tree depth
    :type max_depth: int | None
    :return: Dictionary with model and metrics
    :rtype: dict[str, Any]
    """
    # Prepare features and target
    X = data.drop(columns=[target])
    y = data[target]
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    
    # Train model
    model = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        random_state=random_state,
    )
    model.fit(X_train, y_train)
    
    # Evaluate
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)
    
    # Feature importance
    feature_importance = dict(
        zip(X.columns, model.feature_importances_)
    )
    
    return {
        "model": model,
        "train_score": train_score,
        "test_score": test_score,
        "feature_importance": feature_importance,
    }


# Usage with proper line breaks
result = train_model(
    data=my_data,
    target="target_column",
    test_size=0.3,
    random_state=123,
    n_estimators=200,
    max_depth=10,
)
```

**Ventajas**:

- **Imports ordenados**: stdlib → third-party → local, con separación
- **Espacios consistentes**: Alrededor de operadores y después de comas
- **Líneas cortas**: Máximo 88 caracteres (Black default)
- **Parámetros en líneas separadas**: Fácil de leer y modificar
- **Type hints completos**: Tipos de entrada y salida
- **Docstring**: Documentación clara en formato Sphinx
- **Comentarios**: Secciones lógicas separadas

---

## 2. Herramientas de Formateo Automático

### Por Qué Importa

El formateo manual es lento, propenso a errores, y genera discusiones improductivas. Las herramientas automáticas eliminan estas fricciones y aseguran consistencia.

**Referencia**: Langa, Ł. (2018). Black: The Uncompromising Code Formatter. <https://black.readthedocs.io/>

---

### Black: El Formateador Sin Opiniones

**Filosofía**: "Any color you like, as long as it's black". Black no ofrece opciones de configuración (excepto longitud de línea), eliminando debates sobre estilo.

**Instalación**:
```bash
pip install black
```

**Uso básico**:
```bash
# Formatear un archivo
black my_script.py

# Formatear un directorio
black src/

# Ver cambios sin aplicar (dry-run)
black --check src/

# Ver diff de cambios
black --diff src/
```

**Configuración** (`pyproject.toml`):
```toml
[tool.black]
line-length = 88
target-version = ['py311']
include = '\.pyi?$'
extend-exclude = '''
/(
  # directories
  \.eggs
  | \.git
  | \.venv
  | build
  | dist
)/
'''
```

---

### Ruff: Linter y Formateador Ultra-Rápido

**Ventaja**: Ruff combina múltiples herramientas (Flake8, isort, pyupgrade, etc.) en una sola, escrita en Rust para máxima velocidad.

**Instalación**:
```bash
pip install ruff
```

**Uso básico**:
```bash
# Lint código
ruff check src/

# Formatear código (compatible con Black)
ruff format src/

# Auto-fix problemas detectados
ruff check --fix src/

# Ver qué cambiaría sin aplicar
ruff format --check src/
```

**Configuración** (`pyproject.toml`):
```toml
[tool.ruff]
line-length = 88
target-version = "py311"

[tool.ruff.lint]
select = [
    "E",   # pycodestyle errors
    "W",   # pycodestyle warnings
    "F",   # pyflakes
    "I",   # isort (import sorting)
    "N",   # pep8-naming
    "UP",  # pyupgrade
    "B",   # flake8-bugbear
    "C4",  # flake8-comprehensions
    "SIM", # flake8-simplify
]
ignore = [
    "E501",  # line too long (handled by formatter)
]

[tool.ruff.lint.isort]
known-first-party = ["my_package"]
```

---

## 3. Reglas de Formato Esenciales

### Por Qué Importa

Conocer las reglas fundamentales de PEP 8 te permite escribir código que será aceptado por cualquier formateador y entendido por cualquier desarrollador Python.

---

### Longitud de Línea

**Regla**: Máximo 88 caracteres (Black) o 79 (PEP 8 estricto).

**Correcto**:
```python
def process_data(
    input_file: str,
    output_file: str,
    chunk_size: int = 1000,
) -> None:
    """Process data in chunks."""
    pass
```

**Incorrecto**:
```python
def process_data(input_file: str, output_file: str, chunk_size: int = 1000) -> None:
    """Process data in chunks."""
    pass
```

---

### Espacios Alrededor de Operadores

**Regla**: Un espacio antes y después de operadores binarios.

**Correcto**:
```python
x = 1 + 2
y = x * 3
result = (x + y) / 2
is_valid = x > 0 and y < 10
```

**Incorrecto**:
```python
x=1+2
y=x*3
result=(x+y)/2
is_valid=x>0 and y<10
```

---

### Espacios Después de Comas

**Regla**: Un espacio después de comas, no antes.

**Correcto**:
```python
my_list = [1, 2, 3, 4]
my_dict = {"a": 1, "b": 2}
result = function(arg1, arg2, arg3)
```

**Incorrecto**:
```python
my_list = [1,2,3,4]
my_dict = {"a":1,"b":2}
result = function(arg1,arg2,arg3)
```

---

### Líneas en Blanco

**Reglas**:
- 2 líneas en blanco antes de funciones/clases top-level
- 1 línea en blanco entre métodos de clase
- 1 línea en blanco entre grupos de imports

**Correcto**:
```python
import os
import sys

import pandas as pd


def function1():
    """First function."""
    pass


def function2():
    """Second function."""
    pass


class MyClass:
    """Example class."""
    
    def method1(self):
        """First method."""
        pass
    
    def method2(self):
        """Second method."""
        pass
```

---

### Trailing Commas

**Regla**: Usar trailing commas en estructuras multi-línea facilita diffs y añadir elementos.

**Correcto**:
```python
my_list = [
    "item1",
    "item2",
    "item3",  # Trailing comma
]

my_dict = {
    "key1": "value1",
    "key2": "value2",  # Trailing comma
}

result = function(
    arg1,
    arg2,
    arg3,  # Trailing comma
)
```

**Ventaja**: Añadir un cuarto elemento solo modifica una línea en el diff, no dos.

---

## 4. Organización de Imports

### Por Qué Importa

Los imports desordenados dificultan encontrar dependencias y pueden causar errores sutiles por orden de importación.

**Referencia**: PEP 8 - Imports: <https://peps.python.org/pep-0008/#imports>

---

### Orden de Imports

**Regla**: Tres grupos separados por línea en blanco, cada uno ordenado alfabéticamente.

1. **Standard library**: Módulos incluidos con Python
2. **Third-party**: Paquetes instalados con pip
3. **Local**: Módulos de tu proyecto

**Correcto**:
```python
# Standard library
import os
import sys
from pathlib import Path
from typing import Any, Dict, List

# Third-party
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Local
from my_package.models import MyModel
from my_package.utils import helper_function
```

---

### Imports Absolutos vs Relativos

**Regla**: Preferir imports absolutos para claridad.

**Correcto**:
```python
from my_package.models import MyModel
from my_package.utils.preprocessing import clean_data
```

**Evitar** (imports relativos):
```python
from ..models import MyModel
from .preprocessing import clean_data
```

**Excepción**: Imports relativos son aceptables dentro de un paquete para evitar nombres largos.

---

### Imports Específicos vs Wildcard

**Regla**: Nunca usar wildcard imports (`from module import *`).

**Correcto**:
```python
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
```

**Incorrecto**:
```python
from sklearn.ensemble import *  # ¿Qué importaste?
```

**Razón**: Wildcard imports:
- Ocultan qué nombres están disponibles
- Pueden causar conflictos de nombres
- Dificultan el análisis estático

---

## 5. Integración con Desarrollo

### Por Qué Importa

El formateo automático debe ser parte del flujo de trabajo, no un paso manual que se olvida.

---

### Integración con VS Code

**Configuración** (`.vscode/settings.json`):
```json
{
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.fixAll": "explicit",
      "source.organizeImports": "explicit"
    }
  },
  "ruff.lint.args": ["--config=pyproject.toml"],
  "ruff.format.args": ["--config=pyproject.toml"]
}
```

**Extensiones recomendadas**:
- **Ruff**: `charliermarsh.ruff`
- **Python**: `ms-python.python`

---

### Pre-commit Hooks

**Propósito**: Ejecutar formateo automáticamente antes de cada commit.

**Instalación**:
```bash
pip install pre-commit
```

**Configuración** (`.pre-commit-config.yaml`):
```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.9
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
```

**Activar**:
```bash
pre-commit install
```

**Uso**: Ahora cada commit ejecutará automáticamente las verificaciones.

---

### CI/CD Integration

**Propósito**: Verificar formato en pipeline de integración continua.

**GitHub Actions** (`.github/workflows/lint.yml`):
```yaml
name: Lint and Format

on: [push, pull_request]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: pip install ruff
      
      - name: Lint with ruff
        run: ruff check .
      
      - name: Check formatting
        run: ruff format --check .
```

---

## Aprendizaje Clave

### Puntos Críticos a Recordar

1. **Automatiza**: Usa Black/Ruff, no formatees manualmente
2. **Consistencia > Preferencias**: El equipo usa el mismo formato
3. **PEP 8**: Sigue la guía oficial de Python
4. **88 caracteres**: Límite de línea (Black default)
5. **Ordena imports**: stdlib → third-party → local
6. **Format on save**: Configura tu editor para formatear automáticamente
7. **Pre-commit hooks**: Verifica formato antes de commit

---

### Cómo Desarrollar Intuición

**Pregúntate**: "¿Puedo leer esto sin scroll horizontal?"
- NO → Rompe la línea
- SÍ → Está bien

**Pregúntate**: "¿Otro desarrollador entendería esto rápido?"
- NO → Mejora el formato
- SÍ → Está bien

**Pregúntate**: "¿Estoy formateando manualmente?"
- SÍ → Configura herramientas automáticas
- NO → Correcto

---

### Cuándo Usar Cada Herramienta

**Black cuando**:
- Quieres formateo sin configuración
- Prefieres estándar establecido
- Trabajas en equipo grande

**Ruff cuando**:
- Quieres velocidad máxima
- Necesitas linting + formateo
- Quieres reemplazar múltiples herramientas

**Ambos son compatibles**: Ruff format es compatible con Black.

---

## Resumen de Principios

El formateo consistente no es vanidad, es profesionalismo:

1. **Automatiza**: Black/Ruff en save y pre-commit
2. **PEP 8**: Sigue la guía oficial
3. **88 caracteres**: Límite de línea
4. **Ordena imports**: stdlib → third-party → local
5. **CI/CD**: Verifica formato en pipeline
6. **Sin debates**: Herramientas automáticas eliminan discusiones
7. **Legibilidad**: Código se lee más que se escribe

**Regla de oro**: Si estás formateando manualmente, configura herramientas automáticas. El tiempo ahorrado se multiplica por cada desarrollador en el equipo.

---

## Referencias

1. Martin, R. C. (2008). *Clean Code: A Handbook of Agile Software Craftsmanship*. Prentice Hall. Chapter 5: Formatting.
2. van Rossum, G., Warsaw, B., & Coghlan, N. (2001). PEP 8 – Style Guide for Python Code. <https://peps.python.org/pep-0008/>
3. Black Documentation: <https://black.readthedocs.io/>
4. Ruff Documentation: <https://docs.astral.sh/ruff/>
5. pre-commit Framework: <https://pre-commit.com/>
6. Python Packaging User Guide: <https://packaging.python.org/>

---

## Ejercicio Práctico Individual

Configura tu entorno de desarrollo con formateo automático:

1. Instala Ruff: `pip install ruff`
2. Configura VS Code para format on save
3. Crea `pyproject.toml` con configuración de Ruff
4. Instala pre-commit hooks
5. Formatea un archivo existente y observa los cambios

**Criterios de éxito**:
- [ ] Ruff instalado y funcionando
- [ ] Editor formatea automáticamente al guardar
- [ ] Pre-commit hooks configurados
- [ ] Código pasa `ruff check` sin errores
- [ ] Código pasa `ruff format --check` sin cambios

---
