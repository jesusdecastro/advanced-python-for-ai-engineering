# Recomendaciones para el Curso de Python Avanzado para IA

## Fecha de Análisis
4 de febrero de 2026

## Metodología
Este documento fue generado siguiendo el curso como un estudiante real, leyendo notebooks, intentando completar ejercicios, ejecutando tests, y documentando todos los problemas, inconsistencias y áreas de mejora encontradas.

---

## PROBLEMAS CRÍTICOS

### 1. **Pyright no está instalado pero los tests lo requieren**
**Severidad:** CRÍTICA  
**Ubicación:** `day_1/exercises/tests/test_02_type_hinting.py`

**Problema:**
- Los tests incluyen `test_pyright_passes` que ejecuta `pyright` como subprocess
- Pyright NO está listado en `pyproject.toml` como dependencia
- El test falla con `FileNotFoundError` cuando el estudiante ejecuta los tests
- Esto es confuso porque el README dice "Valida con Pyright" pero no está instalado

**Impacto:**
- Los estudiantes ven 1 test fallando de 41 tests
- Mensaje de error confuso en español: "El sistema no puede encontrar el archivo especificado"
- Rompe la experiencia del estudiante que espera que todos los tests pasen

**Solución:**
```toml
# En pyproject.toml, añadir a dev dependencies:
dev = [
    "pytest>=7.4.0",
    "ruff>=0.8.0",
    "pyright>=1.1.0",  # YA ESTÁ AQUÍ
]
```

**Pero el problema es que pyright YA ESTÁ en pyproject.toml!**

El problema real es que el test ejecuta `pyright` como comando de shell, pero en Windows con venv, pyright no está en el PATH. Necesita ejecutarse como módulo de Python.

**Solución correcta:**
```python
# En test_02_type_hinting.py, cambiar:
result = subprocess.run(
    ["pyright", str(exercises_file), "--outputjson"],
    capture_output=True,
    text=True,
)

# Por:
result = subprocess.run(
    [sys.executable, "-m", "pyright", str(exercises_file), "--outputjson"],
    capture_output=True,
    text=True,
)
```

---

### 2. **Inconsistencia en pyproject.toml - setuptools.packages.find apunta a carpeta incorrecta**
**Severidad:** ALTA  
**Ubicación:** `pyproject.toml`

**Problema:**
```toml
[tool.setuptools.packages.find]
where = ["mi_entregable_brutal/src"]
```

Esta configuración apunta a una carpeta específica de proyecto integrador, pero:
- El curso tiene múltiples días (day_1, day_2, etc.)
- Los ejercicios están en `day_X/exercises/`
- Esta configuración solo funciona si el estudiante crea exactamente esa estructura
- Es confusa para estudiantes que siguen el curso día a día

**Impacto:**
- Los imports de ejercicios pueden fallar
- Los tests pueden no encontrar los módulos
- Confusión sobre la estructura del proyecto

**Solución:**
```toml
[tool.setuptools.packages.find]
where = ["src"]  # O eliminar esta sección si no hay src layout aún
```

O mejor aún, documentar claramente que esta configuración es para el proyecto integrador del Día 6.

---

### 3. **Inconsistencia en build-backend**
**Severidad:** MEDIA  
**Ubicación:** `pyproject.toml`

**Problema:**
```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"
```

Pero `INSTALACION.md` menciona:
```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

**Impacto:**
- Confusión sobre qué herramienta de build usar
- Documentación inconsistente con el código real

**Solución:**
Decidir una herramienta y ser consistente. Recomiendo `hatchling` porque es más moderno y simple.

---

## PROBLEMAS DE DOCUMENTACIÓN

### 4. **README principal dice "Comienza el curso en day_1/README.md" pero no hay guía clara de inicio**
**Severidad:** MEDIA

**Problema:**
- El README principal termina con "Comienza el curso en `day_1/README.md`"
- Pero `day_1/README.md` es muy breve y no explica el flujo completo
- No hay una guía paso a paso clara de "qué hacer primero"

**Solución sugerida:**
Añadir una sección "Primeros Pasos" en el README principal:

```markdown
## Primeros Pasos

### Día 1 - Configuración

1. **Lee INSTALACION.md** para configurar tu entorno
2. **Abre day_1/01_python_idioms_intro.ipynb** - No requiere instalación
3. **Configura tu entorno virtual** siguiendo day_1/02_virtual_environments.ipynb
4. **Instala dependencias** editando pyproject.toml
5. **Continúa con los notebooks** en orden numérico
6. **Completa los ejercicios** en day_1/exercises/
7. **Ejecuta los tests** con pytest

### Flujo Diario Recomendado

Para cada día del curso:
1. Lee el README del día
2. Trabaja los notebooks en orden
3. Completa los ejercicios
4. Ejecuta los tests
5. Valida con ruff y pyright
```

---

### 5. **Notebook 04_type_hinting.ipynb tiene título incorrecto**
**Severidad:** BAJA  
**Ubicación:** `day_1/04_type_hinting.ipynb`

**Problema:**
El notebook dice:
```markdown
# Día 2: Type Hinting en Python
```

Pero está en `day_1/`. Debería decir "Día 1".

**Impacto:**
- Confusión sobre en qué día del curso estamos
- Inconsistencia con la estructura del repositorio

**Solución:**
Cambiar a `# Día 1: Type Hinting en Python`

---

### 6. **Ejercicios README dice "Tu tarea es agregar type hints" pero el código YA TIENE type hints**
**Severidad:** ALTA  
**Ubicación:** `day_1/exercises/README.md` vs `day_1/exercises/02_type_hinting.py`

**Problema:**
El README dice:
> "El código en `02_type_hinting.py` **ya está implementado y funciona correctamente**, pero le faltan type hints"

Pero cuando abres `02_type_hinting.py`, el código NO tiene type hints (solo tiene comentarios TODO).

**Esto es CORRECTO**, pero el README es confuso porque dice "ya está implementado" cuando en realidad el estudiante debe:
1. Importar tipos necesarios
2. Añadir type hints a parámetros
3. Añadir type hints a returns
4. Actualizar docstrings

**Solución:**
Clarificar el README:
```markdown
## Objetivo del Ejercicio

El código en `02_type_hinting.py` **ya tiene la lógica implementada**, pero le faltan:

1. **Imports de tipos** del módulo `typing`
2. **Type hints** en parámetros de funciones
3. **Type hints** en valores de retorno
4. **Type hints** en atributos de clases
5. **Anotaciones Sphinx** en docstrings (:param, :type, :return, :rtype)

Tu trabajo es agregar todos los type hints necesarios sin modificar la lógica del código.
```

---

## PROBLEMAS DE ESTRUCTURA

### 7. **Falta claridad sobre cuándo instalar dependencias**
**Severidad:** MEDIA

**Problema:**
- `INSTALACION.md` explica el enfoque incremental
- Pero los notebooks no mencionan cuándo instalar qué
- El estudiante debe recordar consultar `day_X/requirements.txt` y editar `pyproject.toml`

**Solución:**
Añadir al inicio de cada notebook que requiere dependencias:

```markdown
## ⚠️ Dependencias Requeridas

Este notebook requiere las siguientes dependencias. Si aún no las has instalado:

1. Consulta `day_X/requirements.txt` para ver qué necesitas
2. Edita `pyproject.toml` añadiendo las dependencias
3. Ejecuta `pip install -e ".[dev]"`

Ver [INSTALACION.md](../INSTALACION.md) para detalles completos.
```

---

### 8. **No hay ejercicios para todos los notebooks**
**Severidad:** MEDIA

**Problema:**
- Day 1 tiene 6 notebooks pero solo 3 archivos de ejercicios:
  - `02_type_hinting.py`
  - `04_package_distribution.py`
  - `05_code_quality_tools.py`

- Faltan ejercicios para:
  - 01_python_idioms_intro.ipynb
  - 02_virtual_environments.ipynb
  - 03_modules_and_imports.ipynb

**Impacto:**
- Estudiantes no practican conceptos de algunos notebooks
- Inconsistencia en la experiencia de aprendizaje

**Solución:**
Decidir si:
1. Añadir ejercicios para todos los notebooks, O
2. Documentar claramente que algunos notebooks son solo teóricos

---

## PROBLEMAS DE CONTENIDO

### 9. **Notebook 02_virtual_environments.ipynb tiene código que falla**
**Severidad:** MEDIA  
**Ubicación:** `day_1/02_virtual_environments.ipynb`

**Problema:**
La celda que intenta importar pandas falla:
```python
import pandas as pd
# ModuleNotFoundError: No module named 'pandas'
```

Esto es porque pandas no se instala hasta el Día 5, pero el notebook lo intenta importar.

**Impacto:**
- El estudiante ve un error en el notebook
- Confusión sobre si algo está mal configurado

**Solución:**
1. Eliminar esa celda, O
2. Cambiar el ejemplo para usar solo paquetes ya instalados (jupyter, notebook), O
3. Añadir una nota explicando que es un ejemplo y que pandas se instalará más adelante

---

### 10. **Inconsistencia en la numeración de ejercicios**
**Severidad:** BAJA

**Problema:**
- Los archivos de ejercicios tienen prefijos numéricos: `02_type_hinting.py`, `04_package_distribution.py`
- Pero no hay `01_`, `03_`, etc.
- Los números corresponden a los notebooks, pero no todos los notebooks tienen ejercicios

**Impacto:**
- Confusión sobre si faltan archivos
- Dificulta encontrar ejercicios correspondientes

**Solución:**
Usar nombres descriptivos sin números, O documentar claramente la convención.

---

## PROBLEMAS DE TESTING

### 11. **Los tests usan importación dinámica compleja**
**Severidad:** BAJA  
**Ubicación:** `day_1/exercises/tests/test_02_type_hinting.py`

**Problema:**
```python
_module_path = Path(__file__).parent.parent / "02_type_hinting.py"
_spec = importlib.util.spec_from_file_location("type_hinting_exercises", _module_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
```

Esto es complejo para estudiantes que están aprendiendo. Un simple `from exercises import type_hinting` sería más claro.

**Impacto:**
- Si un estudiante mira el código de tests, puede confundirse
- Dificulta que los estudiantes escriban sus propios tests

**Solución:**
Simplificar la importación o añadir comentarios explicativos.

---

## PROBLEMAS DE CONFIGURACIÓN

### 12. **pytest.ini_options apunta a carpeta "tests" que no existe en la raíz**
**Severidad:** BAJA  
**Ubicación:** `pyproject.toml`

**Problema:**
```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
```

Pero los tests están en `day_X/exercises/tests/`, no en una carpeta `tests/` en la raíz.

**Impacto:**
- Si el estudiante ejecuta `pytest` desde la raíz sin especificar ruta, no encuentra tests
- Confusión sobre dónde están los tests

**Solución:**
```toml
[tool.pytest.ini_options]
testpaths = [
    "day_1/exercises/tests",
    "day_2/exercises/tests",
    "day_3/exercises/tests",
    "day_4/exercises/tests",
    "day_5/exercises/tests",
]
```

O documentar que los tests deben ejecutarse desde cada carpeta day_X.

---

## RECOMENDACIONES GENERALES

### 13. **Añadir un script de validación completa**
**Severidad:** MEDIA

**Sugerencia:**
Crear un script `validate_setup.py` que verifique:
- Python 3.11+ instalado
- Entorno virtual activado
- Todas las dependencias instaladas
- Ruff y Pyright funcionando
- Estructura de carpetas correcta

Esto ayudaría a los estudiantes a verificar que todo está configurado correctamente antes de empezar.

---

### 14. **Añadir un CHANGELOG o PROGRESS.md**
**Severidad:** BAJA

**Sugerencia:**
Crear un archivo donde los estudiantes puedan marcar su progreso:

```markdown
# Mi Progreso en el Curso

## Día 1
- [ ] 01_python_idioms_intro.ipynb
- [ ] 02_virtual_environments.ipynb
- [ ] 03_modules_and_imports.ipynb
- [ ] 04_type_hinting.ipynb
- [ ] 05_code_quality_tools.ipynb
- [ ] 06_package_distribution.ipynb
- [ ] Ejercicios completados
- [ ] Tests pasando

## Día 2
...
```

---

### 15. **Mejorar mensajes de error en tests**
**Severidad:** BAJA

**Problema:**
Cuando un test falla, el mensaje podría ser más educativo.

**Ejemplo actual:**
```
FAILED - AssertionError
```

**Ejemplo mejorado:**
```python
def test_calculate_rectangle_area(self) -> None:
    """Test basic rectangle area calculation."""
    result = calculate_rectangle_area(5.0, 3.0)
    expected = 15.0
    assert result == expected, (
        f"calculate_rectangle_area(5.0, 3.0) should return {expected}, "
        f"but got {result}. Check your implementation."
    )
```

---

## ASPECTOS POSITIVOS

### Lo que está bien hecho:

1. ✅ **Estructura clara por días** - Fácil de seguir
2. ✅ **Notebooks bien documentados** - Explicaciones claras en castellano
3. ✅ **Código en inglés** - Siguiendo estándares profesionales
4. ✅ **Docstrings en formato Sphinx** - Profesional y consistente
5. ✅ **Tests comprehensivos** - Buena cobertura de casos
6. ✅ **Enfoque incremental de dependencias** - Pedagógicamente sólido
7. ✅ **Proyectos integradores** - Aplicación práctica de conceptos
8. ✅ **Referencias oficiales** - Enlaces a documentación oficial

---

## PRIORIZACIÓN DE FIXES

### Prioridad CRÍTICA (Hacer inmediatamente)
1. Fix del test de Pyright (ejecutar como módulo de Python)
2. Corregir pyproject.toml setuptools.packages.find
3. Clarificar README de ejercicios sobre qué debe hacer el estudiante

### Prioridad ALTA (Hacer pronto)
4. Añadir guía de "Primeros Pasos" clara
5. Fix del notebook que intenta importar pandas
6. Decidir y documentar build-backend (setuptools vs hatchling)

### Prioridad MEDIA (Mejorar experiencia)
7. Añadir avisos de dependencias en notebooks
8. Crear ejercicios para todos los notebooks o documentar por qué no los hay
9. Fix pytest.ini_options testpaths
10. Añadir script de validación de setup

### Prioridad BAJA (Nice to have)
11. Corregir título de notebook (Día 2 → Día 1)
12. Simplificar importaciones en tests
13. Mejorar mensajes de error en tests
14. Añadir archivo de progreso
15. Revisar numeración de ejercicios

---

## HALLAZGOS ADICIONALES

### 16. **Diferencia entre Day 1 y Day 2 en tipo de ejercicios**
**Severidad:** BAJA (Documentación)

**Observación:**
- **Day 1 ejercicios:** El código está implementado, solo faltan type hints
- **Day 2 ejercicios:** El código NO está implementado (solo `pass`), el estudiante debe implementar TODO

Esta es una diferencia pedagógica válida, pero debería estar claramente documentada.

**Solución:**
Añadir al README de cada día una nota clara:

**Day 1:**
```markdown
## Tipo de Ejercicios

Los ejercicios del Día 1 tienen el código ya implementado. Tu tarea es:
- Añadir type hints
- Completar docstrings
- Validar con Pyright
```

**Day 2:**
```markdown
## Tipo de Ejercicios

Los ejercicios del Día 2 requieren implementación completa. Tu tarea es:
- Implementar la lógica de cada función usando comprehensions
- Añadir type hints
- Completar docstrings
- Pasar todos los tests
```

---

### 17. **Mismo problema de Pyright en todos los días**
**Severidad:** CRÍTICA

**Confirmado:**
El problema del test de Pyright se repite en Day 2 (y probablemente en todos los días).

**Impacto:**
- Cada día tendrá 1 test fallando
- Experiencia frustrante para el estudiante
- Mensaje de error confuso

**Solución:**
Aplicar el fix de `sys.executable` a TODOS los archivos de test que usan Pyright.

---

## ANÁLISIS DE COBERTURA DE EJERCICIOS

### Day 1 - Configuración de Proyectos
- 6 notebooks
- 3 archivos de ejercicios (50% cobertura)
- Notebooks sin ejercicios:
  - 01_python_idioms_intro.ipynb (OK - es introductorio)
  - 02_virtual_environments.ipynb (OK - es configuración)
  - 03_modules_and_imports.ipynb (FALTA - podría tener ejercicios)

### Day 2 - Código Pythónico
- 6 notebooks
- 6 archivos de ejercicios (100% cobertura) ✅

**Observación:** Day 2 tiene mejor cobertura de ejercicios que Day 1.

---

## ESTADÍSTICAS DE TESTS

### Day 1 - Type Hinting
- Total tests: 41
- Tests funcionales: 40
- Tests de Pyright: 1 (FALLA)
- Tasa de éxito: 97.6% (40/41)

### Day 2 - Comprehensions
- Total tests: 70
- Tests funcionales: 69 (todos fallan porque no hay implementación)
- Tests de Pyright: 1 (FALLA)
- Comportamiento esperado: Estudiante debe implementar

**Observación:** Day 2 tiene casi el doble de tests que Day 1, lo cual es excelente para práctica.

---

## RECOMENDACIONES PEDAGÓGICAS

### 18. **Añadir un "Test de Humo" (Smoke Test)**
**Severidad:** MEDIA

**Sugerencia:**
Crear un script `smoke_test.py` que verifique rápidamente:
- Entorno virtual activado
- Dependencias instaladas
- Estructura de carpetas correcta
- Imports básicos funcionando

Esto ayudaría a los estudiantes a detectar problemas de configuración antes de empezar.

---

### 19. **Crear un README.md en la raíz de exercises/**
**Severidad:** BAJA

**Sugerencia:**
Cada carpeta `day_X/exercises/` debería tener un README que explique:
- Qué tipo de ejercicios son (implementación vs type hints)
- Cómo ejecutar los tests
- Qué se espera del estudiante
- Tiempo estimado

---

### 20. **Añadir ejemplos de solución parcial**
**Severidad:** BAJA

**Sugerencia:**
Para ejercicios complejos, considerar añadir:
- Hints en comentarios
- Ejemplos de solución parcial
- Referencias a la sección del notebook relevante

Ejemplo:
```python
def flatten_matrix(matrix):
    """
    Flatten a 2D matrix into a 1D list.
    
    Hint: Use nested list comprehension
    Hint: [item for row in matrix for item in row]
    
    See notebook section "Advanced Comprehensions" for examples.
    """
    pass
```

---

## CONCLUSIÓN

El curso tiene una **base sólida** con contenido bien estructurado y pedagógicamente sound. Los problemas identificados son principalmente de:
- **Configuración** (pyright, pyproject.toml)
- **Documentación** (claridad en instrucciones)
- **Consistencia** (entre documentación y código)

Ninguno de los problemas es fundamental, pero arreglarlos mejoraría significativamente la experiencia del estudiante y reduciría la fricción en el aprendizaje.

**Puntos fuertes del curso:**
- ✅ Estructura clara y progresiva
- ✅ Notebooks bien documentados con ejemplos
- ✅ Tests comprehensivos (especialmente Day 2)
- ✅ Mezcla de teoría y práctica
- ✅ Enfoque en estándares profesionales (Sphinx, type hints, ruff)
- ✅ Proyectos integradores para aplicación práctica

**Recomendación final:** Priorizar los fixes críticos antes de que más estudiantes usen el curso, y luego iterar en las mejoras de experiencia.
