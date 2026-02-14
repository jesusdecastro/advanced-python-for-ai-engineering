# Ejercicios Día 3: Clean Code Práctico

Ejercicios prácticos para dominar error handling, logging, defensive programming y diseño de objetos.

## Inicio Rápido

El proyecto ya está configurado con `pyproject.toml`. Solo necesitas:

### 1. Configurar el Entorno

```bash
# Navega al directorio de ejercicios
cd dia_3/exercises

# Sincroniza dependencias (crea .venv e instala todo automáticamente)
uv sync
```

**¿Qué hace `uv sync`?**
- Crea el entorno virtual `.venv/` si no existe
- Lee `pyproject.toml` y `uv.lock`
- Instala todas las dependencias del proyecto
- Instala las dependencias de desarrollo (pytest, pytest-cov, ruff, pyright) automáticamente
- Instala tu paquete `exercises` en modo editable
- Todo en un solo comando, sin necesidad de activar el entorno

### 2. Ejecutar Tests

```bash
# Ejecutar un archivo de tests completo
uv run pytest tests/test_error_handling.py

# Ejecutar todos los tests
uv run pytest

# Ejecutar un test individual (función)
uv run pytest tests/test_error_handling.py::test_safe_divide

# Ejecutar un test dentro de una clase
uv run pytest tests/test_defensive.py::TestCalculateBMI::test_calculates_bmi_correctly

# Con coverage
uv run pytest --cov=exercises --cov-report=term-missing
```

**¿Por qué `uv run`?**
- Ejecuta comandos dentro del entorno virtual automáticamente
- No necesitas activar/desactivar el entorno manualmente
- Más rápido y conveniente

**Nota sobre dependencias de desarrollo:**
El proyecto usa `[dependency-groups]` en lugar de `[project.optional-dependencies]`. Esto significa que `uv sync` instala automáticamente las herramientas de desarrollo (pytest, ruff, pyright) sin necesidad de flags adicionales.

## Estructura del Proyecto

```
dia_3/exercises/
├── .venv/                  # Entorno virtual (creado por uv sync)
├── src/
│   └── exercises/          # Tu paquete
│       ├── __init__.py
│       ├── error_handling.py
│       ├── logging_practice.py
│       ├── defensive.py
│       └── objects_data_structures.py
├── tests/
│   ├── __init__.py
│   ├── test_error_handling.py
│   ├── test_logging.py
│   ├── test_defensive.py
│   └── test_objects_data_structures.py
├── pyproject.toml          # Ya configurado
├── uv.lock                 # Lock file con versiones exactas
└── README.md
```

## Flujo de Trabajo

### 1. Leer el Ejercicio

Revisa el archivo correspondiente en `src/exercises/` y el material de referencia en `dia_3/clean_code/`.

### 2. Implementar la Solución

Completa las funciones marcadas con `TODO` o `pass`.

### 3. Ejecutar Tests

```bash
# Test específico del ejercicio que estás haciendo
uv run pytest tests/test_error_handling.py

# Todos los tests
uv run pytest

# Un test individual
uv run pytest tests/test_error_handling.py::test_safe_divide

# Con más detalle
uv run pytest -v
```

### 4. Verificar Calidad del Código

```bash
# Verificar estilo
uv run ruff check src/

# Formatear código automáticamente
uv run ruff format src/
```

## Cómo Funcionan los Imports

**El problema original:**
```python
from exercises.error_handling import safe_divide
# ModuleNotFoundError: No module named 'exercises'
```

**Después de `uv sync`:**
```python
from exercises.error_handling import safe_divide
# Funciona porque el paquete está instalado en modo editable
```

**¿Por qué funciona?**

1. `uv sync` instala el paquete en modo editable (`-e`)
2. Crea un link en `.venv/lib/site-packages/` que apunta a `src/exercises/`
3. Python encuentra el módulo cuando lo importas
4. Los cambios en tu código se reflejan inmediatamente (no necesitas reinstalar)

## Comandos Rápidos

```bash
# Configuración inicial (una vez)
cd dia_3/exercises
uv sync

# Ejecutar tests mientras trabajas
uv run pytest tests/test_error_handling.py                                      # Archivo completo
uv run pytest tests/test_defensive.py::TestCalculateBMI                         # Clase completa
uv run pytest tests/test_defensive.py::TestCalculateBMI::test_calculates_bmi_correctly  # Test específico
uv run pytest                                                                    # Todos los tests

# Verificar código
uv run ruff check src/                           # Verificar estilo
uv run ruff format src/                          # Formatear código

# Coverage
uv run pytest --cov=exercises --cov-report=term-missing
```

### Bloque 1: Error Handling (4 ejercicios)

**Archivo**: `src/exercises/error_handling.py`  
**Material de referencia**: `dia_3/clean_code/01_error_handling_and_logging.md`

1. **División Segura**: Manejo básico de ZeroDivisionError y TypeError
2. **Parseo de JSON**: Manejo de FileNotFoundError y JSONDecodeError
3. **Validación de API**: Validar timeout y URL con ValueError
4. **Input de Usuario**: Validar strings con TypeError y ValueError

**Conceptos**: Try-except básico, excepciones específicas, validación de inputs

### Logging Practice (5 ejercicios)

**Archivo**: `src/exercises/logging_practice.py`  
**Material de referencia**: `dia_3/clean_code/01_error_handling_and_logging.md`

1. **Setup Logging**: Configuración básica de logging
2. **Load Dataset**: Logging en carga de datos (INFO, ERROR)
3. **Validate Dataset**: Logging en validación (INFO, ERROR)
4. **Preprocess Data**: Logging de pasos de preprocesamiento (INFO, WARNING)
5. **Safe Operation**: Logging de operaciones y performance

**Conceptos**: Configuración de logging, niveles INFO/WARNING/ERROR, logging en flujos

### Bloque 2: Defensive Programming (6 ejercicios)

**Archivo**: `src/exercises/defensive.py`  
**Material de referencia**: `dia_3/clean_code/06_defensive_programming.md`

**Constantes ya proporcionadas**: MIN_AGE, MAX_AGE, MIN_HEIGHT, MAX_HEIGHT, MIN_SCORE, MAX_SCORE, etc.

1. **Calculate BMI**: Validación de tipos y rangos (4 validaciones)
2. **Get User Age**: Extracción segura de diccionario (4 validaciones)
3. **Process Transaction**: Fail-fast con 5 validaciones en orden
4. **Parse Numeric**: Union types para string/int/float
5. **Find User**: Optional return type
6. **Average & Normalize**: Validación de listas y datos

**Conceptos**: Uso de constantes, Union/Optional types, fail-fast (3-5 validaciones), input validation

### Bloque 3: Objects and Data Structures

**Archivo**: `src/exercises/objects_data_structures.py`  
**Material de referencia**: `dia_3/clean_code/02_objects_and_data_structures.md`

1. **Getters/Setters a @dataclass**: Convertir clase con getters/setters innecesarios
2. **Ley de Demeter**: Refactorizar violaciones de "no hables con extraños"
3. **Separar Híbridos**: Dividir clase híbrida en objeto + estructura de datos
4. **DTO vs Objeto**: Diseñar apropiadamente DTOs y objetos con encapsulación
5. **Encapsulación**: Ocultar estado interno y exponer solo comportamiento

## Solución de Problemas

**Error: `ModuleNotFoundError: No module named 'exercises'`**
- Solución: Ejecuta `uv sync` desde `dia_3/exercises/`

**Error: `uv: command not found`**
- Solución: Instala UV siguiendo las instrucciones en el README principal del curso

**Los tests no se ejecutan**
- Verifica que estás en el directorio correcto: `cd dia_3/exercises`
- Ejecuta: `uv sync` para asegurar que todo está instalado

**Quiero usar el entorno virtual manualmente**
```bash
# Activar entorno (opcional, uv run lo hace automáticamente)
# Windows (CMD)
.venv\Scripts\activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate

# Luego puedes usar pytest directamente
pytest tests/test_error_handling.py
```

## Recursos

- **UV**: https://docs.astral.sh/uv/
- **pytest**: https://docs.pytest.org/
- **Hatchling**: https://hatch.pypa.io/latest/
- **Ruff**: https://docs.astral.sh/ruff/
- **Material de referencia**: `dia_3/clean_code/`

## Soluciones

Las soluciones están en `.instructor/DIA_3_SOLUCIONES_*.py` para referencia del instructor.

## Criterios de Éxito

- [ ] Todos los tests pasan
- [ ] Código pasa ruff sin warnings
- [ ] Type hints correctos en todas las funciones
- [ ] Manejo apropiado de excepciones (try-except)
- [ ] Logging en niveles apropiados (INFO, WARNING, ERROR)
- [ ] Validación de inputs con mensajes claros
- [ ] Uso de constantes proporcionadas (no magic numbers)
- [ ] Uso apropiado de @dataclass para estructuras de datos
- [ ] Objetos con encapsulación correcta (atributos privados)
- [ ] Respeto a la Ley de Demeter (sin cadenas largas de llamadas)
- [ ] Separación clara entre objetos y estructuras de datos

## Notas sobre Dificultad

Los ejercicios del día 3 están diseñados para ser progresivos:

- **Error Handling**: Nivel básico-medio (4 ejercicios simples)
- **Logging**: Nivel medio (5 ejercicios con logging básico)
- **Defensive**: Nivel medio (6 ejercicios, constantes ya proporcionadas)
- **Objects**: Nivel medio-avanzado (5 ejercicios de diseño)

Si encuentras dificultades, revisa primero el material de referencia en `dia_3/clean_code/`.
