# Módulo 1: Advanced Python for AI Engineering

**Duración:** 48 horas (6 días × 8 horas)
**Enfoque:** Software Engineering para AI Applications

---

## HORARIO GENERAL

Cada día de formación sigue esta estructura:

| Bloque | Franja | Actividad |
|--------|--------|-----------|
| 1 | 9:00 – 10:30 | Sesión teórica/práctica |
| ☕ | 10:30 – 10:45 | Descanso |
| 2 | 10:45 – 12:15 | Sesión teórica/práctica |
| ☕ | 12:15 – 12:30 | Descanso |
| 3 | 12:30 – 14:00 | Sesión teórica/práctica |
| 🍽️ | 14:00 – 15:00 | Comida |
| 4 | 15:00 – 16:30 | Sesión práctica/ejercicios |
| ☕ | 16:30 – 16:45 | Descanso |
| 5 | 16:45 – 18:00 | Trabajo en proyecto + cierre |

---

## ÍNDICE DE CONTENIDOS POR DÍA

### DÍA 1: Fundamentos - Configuración de Proyectos Python
**Duración:** 8 horas

**Contenido:**
1. Python Idioms Intro - Introducción motivacional al código pythónico
2. Virtual Environments - Entornos virtuales con venv
3. Modules and Imports - Sistema de módulos e imports
4. Type Hinting - Type hints
5. Code Quality Tools - Ruff y pyright
6. Package Distribution - pyproject.toml y distribución

**Para el proyecto integrador:**
- Crear estructura de paquete con src layout
- Configurar pyproject.toml con dependencias
- Configurar ruff y pyright
- Crear módulos base con imports correctos
- Aplicar type hints a todas las funciones
- Usar entornos virtuales profesionalmente

---

### DÍA 2: Formación de Equipos, Consolidación y Clean Code
**Duración:** 8 horas

**Conceptos clave:**
- Hatchling vs setuptools (build backends)
- Módulos e imports avanzados
- Clean Functions (pequeñas, una responsabilidad)
- Meaningful Names (Clean Code)
- SRP (Single Responsibility Principle)
- DRY (Don't Repeat Yourself)
- KISS (Keep It Simple, Stupid)

**Para el proyecto integrador:**
- Formar equipos de 3 personas
- Elegir proyecto integrador del catálogo
- Montar estructura de paquete con src layout
- Configurar pyproject.toml con Hatchling
- Refactorizar funciones grandes en funciones pequeñas y específicas
- Renombrar variables/funciones con nombres descriptivos
- Aplicar DRY eliminando código duplicado

---

### DÍA 3: Código Limpio - Legibilidad y Robustez
**Duración:** 8 horas

**Conceptos clave:**
- Type hints avanzados (Union, Optional, Generic, Protocol, TypeVar)
- Error handling y excepciones custom
- Logging estratégico (niveles, formateo, handlers)
- Comments y documentación (docstrings en formato Sphinx)
- Code smells y refactoring patterns
- Defensive programming (validación de inputs, assertions)
- Separation of Concerns
- Law of Demeter (principio de mínimo conocimiento)
- Fail Fast principle
- Magic numbers y constantes

**Para el proyecto integrador:**
- Añadir type hints avanzados a todas las funciones
- Crear excepciones custom (InvalidDataError, ParsingError, etc.)
- Implementar sistema de logging estructurado
- Añadir docstrings completos en formato Sphinx
- Implementar validación de inputs con error handling robusto
- Identificar y eliminar code smells
- Extraer magic numbers a constantes con nombres descriptivos
- Aplicar defensive programming en puntos críticos
- Separar concerns (lógica de negocio vs I/O vs presentación)

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
