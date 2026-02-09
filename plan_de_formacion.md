# Módulo 1: Advanced Python for AI Engineering

**Duración:** 48 horas (6 días × 8 horas)
**Enfoque:** Software Engineering para AI Applications

---

## ÍNDICE DE CONTENIDOS POR DÍA

### DÍA 1: Fundamentos - Configuración de Proyectos Python
**Duración:** 8 horas

#### Distribución del Tiempo

| Horario | Actividad | Duración | Notebook |
|---------|-----------|----------|----------|
| 9:00 - 9:30 | Bienvenida y setup | 30 min | - |
| 9:30 - 10:30 | Python Idioms Intro | 60 min | 01_python_idioms_intro.ipynb |
| 10:30 - 10:45 | Descanso | 15 min | - |
| 10:45 - 12:15 | Virtual Environments | 90 min | 02_virtual_environments.ipynb |
| 12:15 - 13:00 | Modules & Imports | 45 min | 03_modules_and_imports.ipynb |
| 13:00 - 14:00 | Almuerzo | 60 min | - |
| 14:00 - 15:30 | Type Hinting + Ejercicios | 90 min | 04_type_hinting.ipynb |
| 15:30 - 15:45 | Descanso | 15 min | - |
| 15:45 - 17:00 | Code Quality Tools | 75 min | 05_code_quality_tools.ipynb |
| 17:00 - 17:45 | Package Distribution | 45 min | 06_package_distribution.ipynb |
| 17:45 - 18:00 | Cierre y Q&A | 15 min | - |

#### Contenido Detallado

**1. Python Idioms Intro (30 min)**
- Introducción motivacional al código pythónico
- Comprehensions vs loops tradicionales
- Generadores para eficiencia de memoria
- Context managers
- Decoradores básicos
- Solo Python stdlib (no requiere instalación)

**2. Virtual Environments (90 min) - CRÍTICO**
- El problema de las dependencias conflictivas
- Crear y activar entornos virtuales con venv
- Gestión de dependencias con pip
- requirements.txt y buenas prácticas
- Práctica: Crear entorno virtual propio
- IMPORTANTE: Todos deben tener venv funcionando antes de continuar

**3. Modules and Imports (75 min)**
- Diferencia entre módulo y paquete
- `__init__.py`: cuándo y por qué usarlo
- Imports absolutos vs relativos
- Namespace packages vs regular packages
- Práctica: Ejecutar ejemplos en `examples/`

**4. Type Hinting (90 min) - CRÍTICO**
- Sintaxis básica de type hints
- Tipos complejos (List, Dict, Optional, Union)
- Type checking con pyright
- Beneficios reales en proyectos grandes
- EJERCICIO OBLIGATORIO: `exercises/02_type_hinting.py` (30 tests unitarios)

**5. Code Quality Tools (75 min) - CRÍTICO**
- Ruff: linting y formateo ultrarrápido
- Pyright: type checking estático
- Integración con VS Code
- Configuración en pyproject.toml
- Práctica: Configurar herramientas en entorno propio

**6. Package Distribution (45 min)**
- pyproject.toml moderno
- Src layout
- Crear wheels
- Publicar en PyPI (conceptual)
- Introducción conceptual para profundizar en días posteriores

#### Ejercicios Disponibles

**Obligatorio:**
- `exercises/02_type_hinting.py` - 30 tests unitarios

**Opcionales:**
- `exercises/01_python_idioms.py` - Para práctica extra

#### Requisitos Técnicos

- Python 3.11 o superior
- Git
- VS Code (recomendado)
- Conexión a internet

#### Para el Proyecto Integrador

Al finalizar el Día 1, los estudiantes podrán:
- Crear estructura de paquete con src layout
- Configurar pyproject.toml con dependencias
- Configurar ruff y pyright
- Crear módulos base con imports correctos
- Aplicar type hints a todas las funciones
- Usar entornos virtuales profesionalmente

---

### DÍA 2: Código Pythónico - Idioms y Programación Funcional
**Duración:** 8 horas

**Conceptos clave:**
- List/dict/set comprehensions
- Generadores e iteradores
- yield y lazy evaluation
- Decoradores prácticos
- Programación funcional (map, filter, reduce, functools)
- Context managers
- Métodos mágicos básicos

**Para el proyecto integrador:**
- Implementar generadores para lectura de archivos grandes (streaming)
- Usar comprehensions para transformaciones de datos
- Crear decoradores para logging/timing
- Implementar context managers para manejo de recursos (archivos, conexiones)
- Usar functools (lru_cache, partial) para optimización

---

### DÍA 3: Código Limpio - Legibilidad y Robustez
**Duración:** 8 horas

**Conceptos clave:**
- Clean Functions (pequeñas, una responsabilidad)
- Meaningful Names (Clean Code)
- Type hints (básicos y avanzados)
- Error handling y excepciones custom
- Comments y documentación (docstrings)
- DRY, KISS principles

**Para el proyecto integrador:**
- Refactorizar funciones grandes en funciones pequeñas y específicas
- Renombrar variables/funciones con nombres descriptivos
- Añadir type hints a todas las funciones
- Crear excepciones custom (InvalidDataError, ParsingError, etc.)
- Añadir docstrings completos en formato Sphinx
- Implementar validación de inputs con error handling robusto
- Aplicar DRY eliminando código duplicado

---

### DÍA 4: Diseño - Programación Orientada a Objetos
**Duración:** 8 horas

**Conceptos clave:**
- Objects vs Data Structures
- Pydantic vs dataclasses
- Classes (SRP, cohesión)
- Herencia vs composición
- Abstract Base Classes (ABC)
- SOLID principles en Python

**Para el proyecto integrador:**
- Crear modelos de datos con Pydantic (schemas, validación automática)
- Implementar Abstract Base Classes (BaseReader, BaseTransformer, BaseWriter)
- Diseñar clases concretas que hereden de ABCs
- Aplicar composición para combinar funcionalidades
- Refactorizar siguiendo SRP (cada clase una responsabilidad)
- Implementar interfaces claras entre componentes

---

### DÍA 5: Procesamiento de Datos y Testing
**Duración:** 8 horas

**Conceptos clave:**
- NumPy vectorization
- pandas fundamentals y optimization
- Memory profiling y dtypes
- Unit testing con pytest (fixtures, mocking, coverage)
- TDD (Test-Driven Development)

**Para el proyecto integrador:**
- Optimizar transformaciones con pandas/numpy (vectorización)
- Perfilar memoria y optimizar dtypes
- Escribir tests unitarios para todas las funciones críticas
- Crear fixtures para datos de prueba
- Implementar mocking para dependencias externas (archivos, APIs)
- Alcanzar 80%+ de cobertura de código
- Aplicar TDD para nuevas features

---

### OPCIONAL: APIs y Servicios Web
**Si el tiempo lo permite antes del Día 6**

**Conceptos:**
- HTTP requests library
- FastAPI basics
- API design

**Aplicación al proyecto:**
- Crear endpoints FastAPI para exponer funcionalidad (opcional)
- Integrar requests para fuentes de datos remotas (si aplica)

---

### DÍA 6: Proyecto Integrador - Finalización y Entrega
**Duración:** 8 horas

**Objetivo:** Finalizar mini-paquete Python production-ready integrando todos los conceptos aprendidos durante la semana

**Actividades:**
- Implementar CLI completo con argparse o typer
- Integrar todas las funcionalidades desarrolladas durante la semana
- Documentación completa (README, ejemplos de uso, docstrings)
- Alcanzar cobertura de tests 80%+
- Preparar paquete para distribución (build, wheel)
- Presentación de proyectos entre grupos

**Entregables:**
- Repositorio con código completo
- Tests pasando con cobertura 80%+
- README con instrucciones de instalación y uso
- Ejemplos de uso funcionales
- Paquete distribuible (wheel)

---

## PROYECTO INTEGRADOR

Los estudiantes trabajarán en grupos de 3 personas en uno de los proyectos descritos en el documento [proyectos_integradores.md](proyectos_integradores.md). Cada día agregarán funcionalidad aplicando los conceptos aprendidos.

**Opciones disponibles:**
1. Data Pipeline Package (⭐⭐ Básica)
2. Log Analyzer Tool (⭐⭐ Básica)
3. Document Processor (⭐⭐⭐ Media)
4. Data Validator Library (⭐⭐⭐ Media)
5. Time Series Toolkit (⭐⭐⭐⭐ Alta)
6. Web Scraper Framework (⭐⭐⭐⭐ Alta)

Ver [proyectos_integradores.md](proyectos_integradores.md) para detalles completos de cada proyecto, arquitectura sugerida y cómo cada día del curso contribuye a su desarrollo.

---

## STACK TECNOLÓGICO

**Core:**
- Python 3.11+ (versión estándar del curso)
- venv para entornos virtuales
- pytest para testing
- ruff para formateo y linting
- pyright para type checking

**Librerías específicas:**
- pydantic, dataclasses
- functools, itertools
- numpy, pandas
- requests, FastAPI (opcional)

**Librerías según proyecto:**
- Ver [proyectos_integradores.md](proyectos_integradores.md) para dependencias específicas de cada proyecto
