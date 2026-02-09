# Guía de Ejercicios - Día 1

## Descripción General

Para cada notebook del curso, hay ejercicios prácticos asociados con tests unitarios. Esta guía te explica cómo trabajar con ellos.

## Estructura de Ejercicios

```
dia_1/
 exercises/
    __init__.py
    02_type_hinting.py              # Ejercicios a resolver
    tests/
       __init__.py
       conftest.py                 # Configuración de pytest
       test_02_type_hinting.py     # Tests unitarios
    README.md                       # Instrucciones detalladas
    SOLUTIONS.md                    # Soluciones de referencia
 run_tests.sh                        # Script para ejecutar tests (Linux/Mac)
 run_tests.bat                       # Script para ejecutar tests (Windows)
 EXERCISES_GUIDE.md                  # Este archivo
```

## Flujo de Trabajo

### 1. Lee el Notebook

Comienza leyendo el notebook correspondiente (ej: `02_type_hinting.ipynb`) para aprender los conceptos.

### 2. Abre el Archivo de Ejercicios

```bash
# Desde la carpeta dia_1
code exercises/02_type_hinting.py
```

### 3. Completa los Ejercicios

Cada función o clase tiene un comentario `# TODO: Implement this function/method`. Reemplaza el `pass` con tu implementación.

**Importante:** Mantén los type hints y docstrings exactamente como están.

### 4. Ejecuta los Tests

```bash
# Opción 1: Usar pytest directamente
pytest exercises/tests/test_02_type_hinting.py -v

# Opción 2: Usar el script helper
./run_tests.sh          # Linux/Mac
run_tests.bat           # Windows
```

### 5. Valida tu Código

```bash
# Validar type hints
pyright exercises/02_type_hinting.py

# Verificar calidad
ruff check exercises/02_type_hinting.py

# Formatear
ruff format exercises/02_type_hinting.py
```

### 6. Verifica que Todo Pase

Cuando todos los tests pasen, verás:

```
======================== 30 passed in 0.15s ========================
```

## Ejercicios Disponibles

### Día 1: Type Hinting

**Archivo:** `exercises/02_type_hinting.py`

**Ejercicios:**
1. `calculate_rectangle_area` - Función básica con type hints
2. `calculate_statistics` - Tipos complejos (dict, list)
3. `process_value` - Union types (int | str)
4. `find_user` - Optional types
5. `DataProcessor` - Clase con type hints
6. `validate_and_process` - Tipos avanzados (tuplas, múltiples tipos)

**Tests:** 30 tests unitarios

**Tiempo estimado:** 30-45 minutos

## Comandos Útiles

### Ejecutar todos los tests

```bash
pytest exercises/tests/ -v
```

### Ejecutar un test específico

```bash
pytest exercises/tests/test_02_type_hinting.py::TestCalculateRectangleArea -v
```

### Ver cobertura de tests

```bash
pytest exercises/tests/test_02_type_hinting.py --cov=exercises --cov-report=html
```

### Ejecutar tests en modo watch (requiere pytest-watch)

```bash
ptw exercises/tests/test_02_type_hinting.py
```

## Solución de Problemas

### "ModuleNotFoundError: No module named 'exercises'"

**Solución:** Asegúrate de estar en la carpeta `dia_1`:

```bash
cd dia_1
pytest exercises/tests/test_02_type_hinting.py -v
```

### "FAILED - AssertionError"

**Solución:** Lee el mensaje de error cuidadosamente. Pytest te mostrará:
- Qué test falló
- Qué valor esperaba
- Qué valor recibió

### Los tests pasan pero Pyright reporta errores

**Solución:** Verifica que:
- Los type hints sean correctos
- No haya variables sin tipo
- Los tipos de retorno sean correctos

### "pytest: command not found"

**Solución:** Instala las dependencias de desarrollo:

```bash
pip install -e ".[dev]"
```

## Estándares del Código

Tu código debe cumplir con estos estándares:

### Type Hints

- Todas las funciones deben tener type hints
- Todos los parámetros deben estar tipados
- El tipo de retorno debe estar especificado

### Docstrings

- Formato Sphinx
- Descripción clara
- Documentación de parámetros
- Documentación del retorno
- Ejemplos cuando sea posible

### Formato

- Líneas máximo 100 caracteres
- Imports organizados (stdlib, third-party, local)
- Nombres en snake_case (funciones/variables)
- Nombres en PascalCase (clases)

## Próximos Pasos

Una vez completes todos los ejercicios:

1.  Todos los tests pasan
2.  Pyright no reporta errores
3.  Ruff no reporta problemas
4.  Código formateado correctamente
5. → Pasa al siguiente notebook

## Recursos Adicionales

- **Documentación de pytest:** https://docs.pytest.org/
- **Documentación de Pyright:** https://github.com/microsoft/pyright
- **Documentación de Ruff:** https://docs.astral.sh/ruff/
- **PEP 484 - Type Hints:** https://www.python.org/dev/peps/pep-0484/

## Preguntas Frecuentes

**P: ¿Puedo modificar los type hints?**
R: No, los type hints están especificados en los ejercicios. Solo implementa la lógica.

**P: ¿Puedo agregar más funciones?**
R: Sí, pero asegúrate de que todas las funciones requeridas estén implementadas.

**P: ¿Qué pasa si mi solución es diferente a la de referencia?**
R: Está bien si pasa todos los tests. Lo importante es que funcione correctamente.

**P: ¿Necesito completar todos los ejercicios?**
R: Sí, todos los ejercicios son importantes para tu aprendizaje.

**P: ¿Cuánto tiempo debo dedicar a los ejercicios?**
R: El tiempo estimado es 30-45 minutos por notebook, pero puede variar según tu experiencia.

¡Buena suerte con los ejercicios!
