# Día 1: Entornos Virtuales y Configuración de Python

## Descripción General

Este es el punto de entrada del curso. Aquí aprenderás a configurar tu entorno de desarrollo Python, que es fundamental para todo lo que viene después.

## Inicio Rápido (5 minutos)

### Paso 1: Navega a la Raíz del Repositorio

```bash
cd ..
```

(Si estás en `day_1/`, vuelve a la carpeta raíz del proyecto)

### Paso 2: Crea el Entorno Virtual

```bash
# Windows
python -m venv venv

# Linux/Mac
python3 -m venv venv
```

### Paso 3: Activa el Entorno

```bash
# Windows (CMD)
venv\Scripts\activate

# Windows (PowerShell)
venv\Scripts\Activate.ps1

# Linux/Mac
source venv/bin/activate
```

Deberías ver `(venv)` al inicio de tu línea de comandos.

### Paso 4: Instala las Dependencias Mínimas

```bash
pip install -r day_1/requirements-minimal.txt
```

Esto instala solo lo esencial para el Día 1 (menos de 2 minutos).

### Paso 5: Inicia Jupyter

```bash
jupyter notebook
```

Se abrirá una ventana en tu navegador. Navega a `day_1/01_virtual_environments.ipynb`.

## Contenido del Día 1

### Notebook: 01_virtual_environments.ipynb

En este notebook aprenderás:

1. **Qué son los entornos virtuales** - Conceptos fundamentales
2. **Por qué son esenciales** - Visualización del problema de conflictos de dependencias
3. **Cómo crear entornos con venv** - Paso a paso
4. **Herramientas modernas como uv** - Alternativas rápidas
5. **Mejores prácticas** - Cómo gestionar proyectos Python profesionalmente

Tiempo estimado: 45-60 minutos

## Objetivos de Aprendizaje

Al finalizar el Día 1, serás capaz de:

- Comprender la importancia de los entornos Python aislados
- Crear y gestionar entornos virtuales usando `venv`
- Utilizar herramientas modernas como `uv` para gestión rápida de dependencias
- Aplicar mejores prácticas en la configuración de proyectos Python
- Verificar que tu entorno de desarrollo esté correctamente configurado

## Requisitos Previos

- Python 3.10 o superior instalado
- Conocimientos básicos de línea de comandos
- Editor de texto o IDE (VS Code, PyCharm, etc.)

## Solución de Problemas

### "python: command not found" o "python3: command not found"
Python no está instalado o no está en tu PATH. Descárgalo desde [python.org](https://www.python.org/downloads/)

### "pip: command not found"
Asegúrate de que el entorno virtual está activado. Deberías ver `(venv)` en tu terminal.

### "ModuleNotFoundError: No module named 'jupyter'"
Verifica que instalaste las dependencias:
```bash
pip install -r day_1/requirements-minimal.txt
```

### Instalación lenta
Si la instalación es muy lenta, intenta:
```bash
pip install --upgrade pip
pip install -r day_1/requirements-minimal.txt --no-cache-dir
```

## Lista de Verificación

Antes de pasar al Día 2, asegúrate de haber:

- [ ] Creado un entorno virtual en la raíz del proyecto
- [ ] Activado el entorno virtual
- [ ] Instalado `day_1/requirements-minimal.txt`
- [ ] Ejecutado `jupyter notebook` exitosamente
- [ ] Completado todas las celdas del notebook
- [ ] Respondido las preguntas de autoevaluación

## Próximos Pasos

Una vez completes el Día 1:

1. Mantén el entorno virtual activado
2. Instala las dependencias completas: `pip install -r requirements.txt`
3. Dirígete al Día 2 para aprender sobre Type Hinting

## Recursos Adicionales - Día 1

- [Documentación de Python venv](https://docs.python.org/3/library/venv.html)
- [Documentación de uv](https://docs.astral.sh/uv/)
- [Guía de Empaquetado de Python](https://packaging.python.org/)

---

# Día 2: Type Hinting en Python

## Descripción General

Este notebook introduce los **type hints** (anotaciones de tipo), una característica fundamental de Python moderno que mejora significativamente la calidad y mantenibilidad del código.

## Contenido del Día 2

### Notebook: 02_type_hinting.ipynb

En este notebook aprenderás:

1. **Qué son los type hints** - Conceptos fundamentales
2. **Por qué son importantes** - Mejora de calidad del código
3. **Type hints básicos** - Variables, funciones y parámetros
4. **Tipos complejos** - List, Dict, Union, Optional
5. **Type hints en clases** - Documentación de atributos
6. **Validación con mypy** - Herramientas de análisis estático

Tiempo estimado: 45-60 minutos

## Objetivos de Aprendizaje - Día 2

Al finalizar el Día 2, serás capaz de:

- Comprender qué son los type hints y por qué son importantes
- Usar type hints básicos en variables y funciones
- Trabajar con tipos complejos como List, Dict, Union y Optional
- Aplicar type hints en clases de forma efectiva
- Usar mypy para validar type hints en tu código

## Conceptos Clave - Día 2

### Type Hints vs Validación en Tiempo de Ejecución

Los type hints **no se aplican en tiempo de ejecución**. Python ejecutará el código sin importar si los tipos son correctos. Los type hints son anotaciones para herramientas externas como mypy.

```python
def greet(name: str) -> str:
    return f"Hello {name}"

# Esto funciona sin error, aunque pasamos un int
greet(42)  # Python no valida el tipo
```

### Sintaxis Moderna (Python 3.10+)

Python 3.10 introdujo sintaxis más legible para type hints:

```python
# Antiguo (Python 3.5+)
from typing import Union, Optional, List

def process(values: List[int]) -> Optional[int]:
    pass

# Moderno (Python 3.10+)
def process(values: list[int]) -> int | None:
    pass
```

### Herramientas Esenciales

- **mypy**: Validador estático de tipos
  ```bash
  pip install mypy
  mypy your_file.py
  ```

- **Ruff**: Linter y formateador (incluye validación de type hints)
  ```bash
  pip install ruff
  ruff check .
  ```

## Ejercicios Prácticos - Día 2

El notebook incluye 3 ejercicios progresivos:

1. **Tarea 1**: Función con type hints básicos
2. **Tarea 2**: Función con tipos complejos
3. **Tarea 3**: Clase con type hints completos

## Solución de Problemas - Día 2

### "ModuleNotFoundError: No module named 'typing'"

El módulo `typing` viene incluido con Python 3.5+. Si ves este error, verifica tu versión de Python:

```bash
python --version
```

### mypy no encuentra errores

Asegúrate de que mypy está instalado:

```bash
pip install mypy
mypy --version
```

### Confusión entre Union y |

- `Union[int, str]` es la sintaxis antigua (Python 3.5+)
- `int | str` es la sintaxis moderna (Python 3.10+)

Usa la sintaxis moderna si tu proyecto requiere Python 3.10+.

## Lista de Verificación - Día 2

Antes de pasar al Día 3, asegúrate de haber:

- [ ] Completado todas las celdas del notebook
- [ ] Entendido la diferencia entre type hints y validación en tiempo de ejecución
- [ ] Practicado con tipos básicos (str, int, float, bool)
- [ ] Trabajado con tipos complejos (list, dict, Union, Optional)
- [ ] Aplicado type hints en una clase
- [ ] Respondido todas las preguntas de autoevaluación
- [ ] Instalado y probado mypy

## Próximos Pasos - Día 2

Una vez completes el Día 2:

1. Practica escribiendo type hints en tu código personal
2. Instala mypy y úsalo en tus proyectos
3. Familiarízate con la sintaxis moderna de Python 3.10+
4. Dirígete al Día 3 para aprender sobre módulos e importaciones

---

# Día 3: Módulos, Importaciones y Estructura de Proyectos

## Descripción General

En Python, la organización del código es fundamental para crear proyectos mantenibles y escalables. Este notebook te enseña cómo estructurar proyectos Python profesionales, crear módulos reutilizables, gestionar importaciones correctamente y configurar tu proyecto con `pyproject.toml`.

## Contenido del Día 3

### Notebook: 03_modules_and_imports.ipynb

En este notebook aprenderás:

1. **Módulos y paquetes** - Conceptos fundamentales
2. **Estructura profesional de proyectos** - Organización recomendada
3. **Importaciones** - Absoluta, relativa y mejores prácticas
4. **Configuración con pyproject.toml** - Estándar moderno
5. **Instalación en modo desarrollo** - `pip install -e`
6. **Ejemplo práctico** - Crear un proyecto completo

Tiempo estimado: 45-60 minutos

## Objetivos de Aprendizaje - Día 3

Al finalizar el Día 3, serás capaz de:

- Comprender la diferencia entre módulos, paquetes y proyectos
- Organizar código en una estructura de proyecto profesional
- Usar importaciones correctamente (absoluta, relativa, circular)
- Configurar un proyecto con `pyproject.toml`
- Instalar un proyecto en modo desarrollo con `pip install -e`
- Crear paquetes reutilizables y distribuibles

## Conceptos Clave - Día 3

### Estructura Recomendada

```
my_project/
├── pyproject.toml              # Configuración central
├── README.md                   # Documentación
├── LICENSE                     # Licencia
├── .gitignore                  # Archivos a ignorar
├── src/
│   └── my_package/
│       ├── __init__.py
│       ├── core.py
│       └── utils.py
├── tests/
│   ├── __init__.py
│   └── test_core.py
└── docs/
    └── index.md
```

### Módulos vs Paquetes

- **Módulo**: Archivo `.py` individual
- **Paquete**: Directorio con `__init__.py` que contiene módulos
- **Proyecto**: Directorio con `pyproject.toml` que contiene paquetes

### Importaciones

```python
# Importación absoluta (recomendada)
from my_package.core import calculate_average

# Importación relativa (dentro de paquetes)
from .core import calculate_average
from ..utils import helper_function
```

### `pip install -e` (Editable Install)

Instala el paquete en modo desarrollo con enlace simbólico:

```bash
pip install -e .
pip install -e ".[dev]"  # Con dependencias de desarrollo
```

Los cambios en el código se reflejan inmediatamente sin reinstalar.

## Ejercicios Prácticos - Día 3

El notebook incluye 3 ejercicios progresivos:

1. **Tarea 1**: Crear un módulo simple con funciones
2. **Tarea 2**: Crear un paquete con `__init__.py`
3. **Tarea 3**: Crear `pyproject.toml` completo

## Solución de Problemas - Día 3

### "ModuleNotFoundError: No module named 'my_package'"

Asegúrate de:
1. Estar en el directorio correcto
2. Haber instalado el paquete: `pip install -e .`
3. Que `__init__.py` exista en el directorio

### Cambios no se reflejan después de editar

Si instalaste con `pip install .` (no editable), reinstala con:
```bash
pip install -e .
```

### Importaciones circulares

Evita importar módulos que se importan entre sí. Reorganiza el código para que las dependencias fluyan en una dirección.

## Lista de Verificación - Día 3

Antes de pasar al Día 4, asegúrate de haber:

- [ ] Completado todas las celdas del notebook
- [ ] Entendido la diferencia entre módulos y paquetes
- [ ] Practicado con importaciones absolutas y relativas
- [ ] Creado un `pyproject.toml` básico
- [ ] Instalado un proyecto con `pip install -e`
- [ ] Respondido todas las preguntas de autoevaluación
- [ ] Creado un proyecto de ejemplo

## Próximos Pasos - Día 3

Una vez completes el Día 3:

1. Reorganiza tus proyectos personales con la estructura recomendada
2. Crea un `pyproject.toml` para tus proyectos
3. Practica con `pip install -e` en tus desarrollos
4. Dirígete al Día 4 para aprender sobre NumPy

## Recursos Adicionales - Día 3

- [Modules - Python Documentation](https://docs.python.org/3/tutorial/modules.html)
- [The import system](https://docs.python.org/3/reference/import_system.html)
- [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)
- [PEP 517 - Build system format](https://www.python.org/dev/peps/pep-0517/)
- [Real Python - Modules and Packages](https://realpython.com/python-modules-packages/)

## Notas Importantes - Día 3

- La estructura `src/` es la recomendación moderna
- `pyproject.toml` es el estándar moderno
- Usa `pip install -e` siempre durante el desarrollo
- Mantén `__init__.py` incluso si está vacío para claridad
- Las importaciones absolutas son más claras que las relativas

## Recursos Adicionales - Día 2

- [Documentación oficial de typing](https://docs.python.org/3/library/typing.html)
- [PEP 484 - Type Hints](https://www.python.org/dev/peps/pep-0484/)
- [mypy - Static Type Checker](https://www.mypy-lang.org/)
- [Real Python - Type Hints](https://realpython.com/python-type-hints/)

## Notas Importantes - Día 2

- Los type hints son opcionales pero altamente recomendados
- No tienen impacto en el rendimiento del código
- Son especialmente útiles en equipos de trabajo
- Integra mypy en tu flujo de CI/CD para garantizar calidad

---

# Día 4: Programación Funcional en Python

## Descripción General

La programación funcional es un paradigma que enfatiza el uso de funciones puras, evita el estado mutable y favorece la composición de funciones. Python no es un lenguaje puramente funcional, pero ofrece herramientas poderosas para programación funcional.

## Contenido del Día 4

### Notebook: 04_functional_programming.ipynb

En este notebook aprenderás:

1. **Lambda functions** - Funciones anónimas pequeñas
2. **map(), filter(), reduce()** - Funciones de orden superior
3. **List comprehensions** - Básicas y avanzadas
4. **Dict y set comprehensions** - Transformaciones de colecciones
5. **Generator expressions** - Eficiencia de memoria
6. **functools** - partial, reduce, lru_cache
7. **Cuándo usar cada herramienta** - Mejores prácticas

Tiempo estimado: 45-60 minutos

## Objetivos de Aprendizaje - Día 4

Al finalizar el Día 4, serás capaz de:

- Usar lambda functions para crear funciones anónimas
- Aplicar map(), filter() y reduce() para transformar datos
- Crear list, dict y set comprehensions
- Usar generator expressions para eficiencia de memoria
- Aplicar functools (partial, reduce, lru_cache)
- Elegir entre comprehensions y loops según el contexto

## Conceptos Clave - Día 4

### Lambda Functions

```python
# Sintaxis
lambda arguments: expression

# Ejemplos
square = lambda x: x ** 2
add = lambda x, y: x + y
```

### Map, Filter, Reduce

```python
# Map: aplica función a cada elemento
doubled = list(map(lambda x: x * 2, [1, 2, 3]))

# Filter: filtra elementos
evens = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))

# Reduce: acumula valores
from functools import reduce
total = reduce(lambda x, y: x + y, [1, 2, 3, 4])
```

### List Comprehensions

```python
# Básica
squares = [x ** 2 for x in range(1, 6)]

# Con condición
evens = [x for x in range(1, 11) if x % 2 == 0]

# Anidada
pairs = [(x, y) for x in [1, 2] for y in ["a", "b"]]
```

### Dict y Set Comprehensions

```python
# Dict comprehension
squares_dict = {x: x ** 2 for x in range(1, 6)}

# Set comprehension
unique = {x for x in [1, 2, 2, 3, 3, 3]}
```

### Generator Expressions

```python
# Sintaxis similar a list comprehension pero con ()
squares_gen = (x ** 2 for x in range(1, 6))

# Eficiente en memoria, genera bajo demanda
```

### Functools

```python
from functools import partial, lru_cache

# partial: pre-establece argumentos
double = partial(multiply, 2)

# lru_cache: cachea resultados
@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

## Ejercicios Prácticos - Día 4

El notebook incluye 3 ejercicios progresivos:

1. **Tarea 1**: Lambda y Map/Filter
2. **Tarea 2**: Comprehensions (list, dict, set)
3. **Tarea 3**: Functools y Generators

## Solución de Problemas - Día 4

### "Lambda functions son difíciles de leer"

Usa lambdas solo para funciones pequeñas. Para lógica compleja, usa `def`:

```python
# Bueno
squared = map(lambda x: x ** 2, numbers)

# Malo
result = map(lambda x: x ** 2 if x > 0 else -x if x < -10 else 0, numbers)
```

### "¿Cuándo usar comprehensions vs loops?"

Usa comprehensions cuando:
- Transformes una colección en otra
- La lógica sea simple (1-2 líneas)
- Quieras código más conciso

Usa loops cuando:
- Necesites múltiples líneas de lógica
- Tengas efectos secundarios (print, escribir archivos)
- La lógica sea compleja

### "Generator expressions son lentas"

Los generadores son más rápidos en memoria pero pueden ser más lentos en CPU. Usa listas cuando necesites acceso aleatorio o múltiples iteraciones.

## Lista de Verificación - Día 4

Antes de pasar al Día 5, asegúrate de haber:

- [ ] Completado todas las celdas del notebook
- [ ] Entendido cuándo usar lambda functions
- [ ] Practicado con map(), filter() y reduce()
- [ ] Creado list, dict y set comprehensions
- [ ] Usado generator expressions
- [ ] Aplicado functools (partial, lru_cache)
- [ ] Respondido todas las preguntas de autoevaluación

## Próximos Pasos - Día 4

Una vez completes el Día 4:

1. Refactoriza código anterior usando comprehensions
2. Usa lru_cache en funciones recursivas
3. Experimenta con generator expressions en datos grandes
4. Dirígete al Día 5 para aprender sobre NumPy

## Recursos Adicionales - Día 4

- [Functional Programming HOWTO](https://docs.python.org/3/howto/functional.html)
- [functools module](https://docs.python.org/3/library/functools.html)
- [List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [Real Python - Functional Programming](https://realpython.com/python-functional-programming/)
- [Real Python - List Comprehensions](https://realpython.com/list-comprehensions-and-generator-expressions/)

## Notas Importantes - Día 4

- Las list comprehensions son generalmente preferidas a map/filter en Python
- Los generadores son eficientes en memoria
- lru_cache es especialmente útil para funciones recursivas
- Elige la herramienta que haga tu código más legible
- La programación funcional mejora la calidad del código
---

# Día 5: Generadores e Iteradores

## Descripción General

Los generadores e iteradores son conceptos fundamentales en Python para procesar datos de forma eficiente. Los generadores permiten crear secuencias de valores bajo demanda, lo que es especialmente útil para datos grandes.

## Contenido del Día 5

### Notebook: 05_generators_and_iterators.ipynb

En este notebook aprenderás:

1. **Protocolo de iteración** - __iter__() y __next__()
2. **Iteradores personalizados** - Crear clases iterables
3. **Generadores** - Funciones con yield
4. **yield y yield from** - Delegación de generadores
5. **Streaming de datos** - Procesar archivos grandes
6. **itertools** - Combinaciones, permutaciones, productos
7. **Ejercicio: CSV de 10GB** - Procesamiento eficiente

Tiempo estimado: 45-60 minutos

## Objetivos de Aprendizaje - Día 5

Al finalizar el Día 5, serás capaz de:

- Comprender el protocolo de iteración (__iter__, __next__)
- Crear iteradores personalizados
- Usar yield y yield from para crear generadores
- Procesar datos en streaming con generadores
- Usar itertools para combinaciones complejas
- Procesar archivos grandes sin cargar todo en memoria

## Conceptos Clave - Día 5

### Protocolo de Iteración

```python
class MyIterator:
    def __iter__(self):
        return self
    
    def __next__(self):
        if condition:
            raise StopIteration
        return value
```

### Generadores

```python
def my_generator():
    yield value1
    yield value2
    yield value3

# Uso
for value in my_generator():
    print(value)
```

### Yield y Yield From

```python
# yield: pausa y retorna valor
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# yield from: delega a otro generador
def outer():
    yield from inner()
    yield 4
```

### Streaming de Datos

```python
def read_csv_rows(filepath):
    with open(filepath, 'r') as f:
        header = f.readline().strip().split(',')
        for line in f:
            values = line.strip().split(',')
            yield dict(zip(header, values))

# Procesa una fila a la vez, no carga todo en memoria
for row in read_csv_rows('data.csv'):
    process(row)
```

### Itertools

```python
import itertools

# chain: combinar iterables
itertools.chain([1, 2], [3, 4])

# combinations: todas las combinaciones
itertools.combinations(['a', 'b', 'c'], 2)

# permutations: todas las permutaciones
itertools.permutations(['a', 'b', 'c'], 2)

# product: producto cartesiano
itertools.product([1, 2], ['a', 'b'])
```

## Ejercicios Prácticos - Día 5

El notebook incluye 3 ejercicios progresivos:

1. **Tarea 1**: Crear un iterador personalizado (números pares)
2. **Tarea 2**: Crear un generador (procesar datos en chunks)
3. **Tarea 3**: Procesar CSV de 10GB con generadores

## Solución de Problemas - Día 5

### "¿Cuándo usar iteradores vs generadores?"

Usa generadores en la mayoría de casos porque son más simples. Usa iteradores cuando necesites estado más complejo o múltiples métodos.

### "Los generadores son lentos"

Los generadores son eficientes en memoria pero pueden ser más lentos en CPU. Para datos pequeños, usa listas. Para datos grandes, usa generadores.

### "¿Cómo procesar un CSV de 10GB?"

Usa un generador que lea línea por línea. Procesa una línea a la vez. Nunca cargues el archivo completo en memoria.

## Lista de Verificación - Día 5

Antes de pasar al Día 6, asegúrate de haber:

- [ ] Completado todas las celdas del notebook
- [ ] Entendido el protocolo de iteración
- [ ] Creado iteradores personalizados
- [ ] Usado yield y yield from
- [ ] Procesado datos en streaming
- [ ] Usado itertools para combinaciones
- [ ] Respondido todas las preguntas de autoevaluación

## Próximos Pasos - Día 5

Una vez completes el Día 5:

1. Refactoriza código anterior usando generadores
2. Procesa archivos grandes con generadores
3. Experimenta con itertools para combinaciones
4. Dirígete al Día 6 para aprender sobre NumPy

## Recursos Adicionales - Día 5

- [Iterators - Python Documentation](https://docs.python.org/3/library/stdtypes.html#iterator-types)
- [Generators - Python HOWTO](https://docs.python.org/3/howto/functional.html#generators)
- [itertools module](https://docs.python.org/3/library/itertools.html)
- [Real Python - Generators](https://realpython.com/generators/)
- [Real Python - itertools](https://realpython.com/python-itertools/)

## Notas Importantes - Día 5

- Los generadores son eficientes en memoria
- Usa generadores para procesar datos grandes
- itertools es muy eficiente para combinaciones complejas
- El protocolo de iteración es fundamental en Python
- Los generadores son la forma preferida de crear iteradores
---

# Día 6: Testing Fundamentals

## Descripción General

El testing es una parte esencial del desarrollo profesional de software. Los tests automáticos garantizan que tu código funciona correctamente, facilitan el refactoring y documentan el comportamiento esperado.

## Contenido del Día 6

### Notebook: 06_testing_fundamentals.ipynb

En este notebook aprenderás:

1. **Pytest basics** - Escribir y ejecutar tests
2. **Fixtures** - Reutilizar código de setup
3. **Parametrize** - Tests con múltiples valores
4. **Mocking y patching** - Aislar código bajo test
5. **Test coverage** - Medir cobertura de tests
6. **TDD** - Test-Driven Development
7. **Ejercicio: Data Validator** - Implementación con TDD

Tiempo estimado: 45-60 minutos

## Objetivos de Aprendizaje - Día 6

Al finalizar el Día 6, serás capaz de:

- Escribir tests básicos con pytest
- Usar fixtures para reutilizar código de setup
- Parametrizar tests para múltiples casos
- Usar mocking y patching para aislar código
- Medir cobertura de tests
- Aplicar TDD (Test-Driven Development)

## Conceptos Clave - Día 6

### Pytest Basics

```python
# Test simple
def test_addition():
    assert 2 + 2 == 4

# Ejecutar
pytest test_file.py
pytest -v  # Verbose
pytest -s  # Show print statements
```

### Fixtures

```python
def get_validator():
    """Create a validator instance."""
    return DataValidator()

def test_validate_email():
    validator = get_validator()
    assert validator.validate_email("user@example.com") == True
```

### Parametrize

```python
test_cases = [
    (2, True),
    (3, False),
    (4, True),
]

def test_is_even():
    for number, expected in test_cases:
        assert is_even(number) == expected
```

### Mocking y Patching

```python
from unittest.mock import Mock, patch

def test_with_mock():
    mock_func = Mock(return_value=42)
    result = mock_func()
    assert result == 42
    mock_func.assert_called_once()
```

### Test Coverage

```bash
pip install pytest-cov
pytest --cov=my_module
pytest --cov=my_module --cov-report=html
```

### TDD: Red-Green-Refactor

1. **Red**: Escribe un test que falla
2. **Green**: Escribe el código mínimo para pasar
3. **Refactor**: Mejora el código

## Ejercicios Prácticos - Día 6

El notebook incluye 3 ejercicios progresivos:

1. **Tarea 1**: Tests básicos para funciones de cálculo
2. **Tarea 2**: Fixtures para operaciones de base de datos
3. **Tarea 3**: TDD de un data validator

## Solución de Problemas - Día 6

### "¿Cuándo usar fixtures?"

Usa fixtures cuando necesites setup común en múltiples tests. Evita duplicación de código.

### "¿Cuándo usar mocking?"

Usa mocking para aislar código de dependencias externas (APIs, bases de datos, archivos).

### "¿Qué cobertura de tests es suficiente?"

Busca 80-90% de cobertura. El 100% no siempre es necesario, pero asegura que el código crítico esté probado.

## Lista de Verificación - Día 6

Antes de pasar al Día 7, asegúrate de haber:

- [ ] Completado todas las celdas del notebook
- [ ] Escrito tests básicos con pytest
- [ ] Usado fixtures en tests
- [ ] Parametrizado tests
- [ ] Usado mocking y patching
- [ ] Medido cobertura de tests
- [ ] Implementado un validador con TDD
- [ ] Respondido todas las preguntas de autoevaluación

## Próximos Pasos - Día 6

Una vez completes el Día 6:

1. Escribe tests para tus proyectos personales
2. Usa pytest en tu flujo de trabajo
3. Implementa TDD en nuevas funcionalidades
4. Dirígete al Día 7 para aprender sobre NumPy

## Recursos Adicionales - Día 6

- [pytest documentation](https://docs.pytest.org/)
- [unittest.mock](https://docs.python.org/3/library/unittest.mock.html)
- [pytest-cov](https://pytest-cov.readthedocs.io/)
- [Real Python - pytest](https://realpython.com/pytest-python-testing/)
- [Real Python - Mocking](https://realpython.com/python-mock-library/)

## Notas Importantes - Día 6

- pytest es el framework de testing más popular en Python
- Los tests son inversión en calidad
- TDD mejora el diseño del código
- Busca 80-90% de cobertura de tests
- Los tests documentan el comportamiento esperado
