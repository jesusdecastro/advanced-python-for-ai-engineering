# Ejercicios: Python Idioms

## Descripción

Estos ejercicios te permitirán practicar los conceptos fundamentales de Python idiomático que viste en el notebook `01_python_idioms_intro.ipynb`:

- **List Comprehensions**: Transformar y filtrar listas de forma elegante
- **Dict Comprehensions**: Crear y manipular diccionarios eficientemente
- **Generators**: Producir valores bajo demanda con `yield`
- **Context Managers**: Gestionar recursos de forma segura con `__enter__` y `__exit__`
- **Decorators**: Añadir funcionalidad a funciones sin modificar su código

## Estructura de Archivos

```
dia_1/exercises/
├── 01_python_idioms.py          # Archivo con ejercicios (completa las funciones)
├── tests/
│   └── test_01_python_idioms.py # Tests unitarios
└── README_01_idioms.md          # Este archivo
```

## Instrucciones

### 1. Configurar Entorno

Asegúrate de tener pytest instalado:

```bash
pip install pytest
```

### 2. Completar Ejercicios

Abre el archivo `01_python_idioms.py` y completa las funciones marcadas con `# TODO`.

Cada función tiene:
- **Docstring** con descripción y ejemplos
- **Type hints** para entender los tipos de entrada/salida
- **Comentario TODO** donde debes escribir tu código

### 3. Ejecutar Tests

Desde el directorio `dia_1/exercises/`, ejecuta:

```bash
# Ejecutar todos los tests
pytest tests/test_01_python_idioms.py -v

# Ejecutar tests de una clase específica
pytest tests/test_01_python_idioms.py::TestListComprehensions -v

# Ejecutar un test específico
pytest tests/test_01_python_idioms.py::TestListComprehensions::test_square_evens_basic -v

# Ver output detallado
pytest tests/test_01_python_idioms.py -v -s
```

### 4. Verificar Progreso

Los tests te dirán:
- ✅ **PASSED**: Ejercicio completado correctamente
- ❌ **FAILED**: Hay un error en tu implementación
- ⚠️ **ERROR**: Problema de sintaxis o import

## Ejercicios por Nivel

### Nivel 1: Comprehensions (Básico)

**Ejercicio 1.1: `square_evens`**
- Usa list comprehension con filtro `if`
- Filtra números pares y eleva al cuadrado

**Ejercicio 1.2: `transform_strings`**
- Usa list comprehension con filtro
- Filtra palabras largas y convierte a mayúsculas

**Ejercicio 2.1: `word_lengths`**
- Usa dict comprehension
- Crea diccionario palabra → longitud

**Ejercicio 2.2: `invert_dict`**
- Usa dict comprehension
- Invierte claves y valores

**Ejercicio 2.3: `filter_dict_by_value`**
- Usa dict comprehension con filtro
- Filtra por valor mayor que threshold

### Nivel 2: Generators (Intermedio)

**Ejercicio 3.1: `countdown`**
- Usa `yield` en un loop
- Genera números descendentes

**Ejercicio 3.2: `even_numbers`**
- Usa `yield` con condición
- Genera solo números pares en rango

**Ejercicio 3.3: `fibonacci_generator`**
- Usa `yield` con lógica de Fibonacci
- Mantén estado entre yields

### Nivel 3: Context Managers (Intermedio-Avanzado)

**Ejercicio 4.1: `Timer`**
- Implementa `__enter__` para iniciar timer
- Implementa `__exit__` para calcular tiempo transcurrido
- Guarda resultado en `self.elapsed`

**Ejercicio 4.2: `FileWriter`**
- Implementa `__enter__` para abrir archivo
- Implementa `__exit__` para cerrar archivo
- Asegura cierre incluso con excepciones

### Nivel 4: Decorators (Avanzado)

**Ejercicio 5.1: `uppercase_decorator`**
- Crea función `wrapper` que llama a función original
- Convierte resultado a mayúsculas
- Retorna `wrapper`

**Ejercicio 5.2: `repeat`**
- Crea decorador con parámetro
- Usa closure para capturar `times`
- Ejecuta función `times` veces

**Ejercicio 5.3: `validate_positive`**
- Valida argumentos antes de ejecutar función
- Lanza `ValueError` si algún argumento no es positivo
- Usa `*args` para capturar todos los argumentos

### Nivel 5: Challenge (Avanzado)

**Ejercicio 6.1: `process_sales_data`**
- Combina múltiples dict comprehensions
- Calcula revenues, filtra high_revenue, suma total
- Retorna diccionario con resultados

**Ejercicio 6.2: `batch_generator`**
- Usa `yield` para generar lotes
- Maneja último lote parcial correctamente
- Usa slicing para crear batches

## Pistas y Consejos

### List Comprehensions

```python
# Sintaxis básica
[expresion for item in lista]

# Con filtro
[expresion for item in lista if condicion]

# Ejemplo
squares = [x**2 for x in range(10) if x % 2 == 0]
```

### Dict Comprehensions

```python
# Sintaxis básica
{key: value for item in lista}

# Con filtro
{key: value for item in lista if condicion}

# Ejemplo
lengths = {word: len(word) for word in words if len(word) > 3}
```

### Generators con yield

```python
def my_generator(n):
    for i in range(n):
        yield i  # Pausa aquí y devuelve i
        # Continúa desde aquí en siguiente next()
```

### Context Managers

```python
class MyContext:
    def __enter__(self):
        # Setup: abrir recursos
        return self  # Retorna objeto para 'as' variable
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Cleanup: cerrar recursos
        return False  # No suprimir excepciones
```

### Decorators

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        # Código antes
        result = func(*args, **kwargs)  # Llama función original
        # Código después
        return result
    return wrapper
```

### Decorators con Parámetros

```python
def decorator_with_param(param):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Usa 'param' aquí
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

## Solución de Problemas

### Error: "ModuleNotFoundError"

```bash
# Asegúrate de estar en el directorio correcto
cd dia_1/exercises

# O ejecuta desde la raíz del proyecto
pytest dia_1/exercises/tests/test_01_python_idioms.py -v
```

### Error: "fixture 'tmp_path' not found"

```bash
# Actualiza pytest
pip install --upgrade pytest
```

### Tests pasan pero quieres ver el output

```bash
# Usa -s para ver prints
pytest tests/test_01_python_idioms.py -v -s
```

### Ver solo tests que fallan

```bash
pytest tests/test_01_python_idioms.py -v --tb=short
```

## Criterios de Éxito

Has completado los ejercicios exitosamente cuando:

✅ Todos los tests pasan (verde)
✅ Tu código usa las técnicas correctas (comprehensions, yield, etc.)
✅ No hay código duplicado
✅ Las funciones son concisas y legibles

## Recursos Adicionales

- [Python List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [Python Generators](https://docs.python.org/3/tutorial/classes.html#generators)
- [Context Managers](https://docs.python.org/3/reference/datamodel.html#context-managers)
- [Python Decorators](https://docs.python.org/3/glossary.html#term-decorator)

## Próximos Pasos

Una vez completes estos ejercicios:

1. Revisa las soluciones en `SOLUTIONS.md` (si está disponible)
2. Compara tu código con las mejores prácticas
3. Continúa con los ejercicios del siguiente notebook

¡Buena suerte! 🚀
