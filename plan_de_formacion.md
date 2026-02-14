# Módulo 1: Advanced Python for AI Engineering

**Duración:** 48 horas (6 días × 8 horas)
**Enfoque:** Software Engineering para AI Applications

---

## HORARIO GENERAL

Cada día de formación sigue esta estructura:

| Bloque | Franja | Actividad |
|--------|--------|-----------|
| 1 | 9:00 – 10:30 | Sesión teórica/práctica |
| Descanso | 10:30 – 10:45 | Descanso |
| 2 | 10:45 – 12:15 | Sesión teórica/práctica |
| Descanso | 12:15 – 12:30 | Descanso |
| 3 | 12:30 – 14:00 | Sesión teórica/práctica |
| Comida | 14:00 – 15:00 | Comida |
| 4 | 15:00 – 16:30 | Sesión práctica/ejercicios |
| Descanso | 16:30 – 16:45 | Descanso |
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

### DÍA 4: Arquitectura de Software y Principios SOLID
**Duración:** 8 horas

**Conceptos clave:**
- Modelado de datos: @property, dataclasses, Pydantic
- Pydantic v2: validación, Field, validators, discriminated unions
- Composición sobre herencia
- Protocols vs Abstract Base Classes
- Single Responsibility Principle (SRP)
- Dependency Inversion Principle (DIP)
- Open/Closed Principle (OCP)
- Liskov Substitution Principle (LSP)
- Interface Segregation Principle (ISP)

**Para el proyecto integrador:**
- Crear modelos de datos con Pydantic (schemas, validación automática)
- Implementar Protocols para abstracciones
- Diseñar clases usando composición sobre herencia
- Aplicar SRP: cada clase una responsabilidad clara
- Aplicar DIP: depender de abstracciones (Protocols)
- Aplicar OCP: diseñar para extensión sin modificación
- Refactorizar "God classes" en componentes cohesivos
- Implementar Strategy pattern para comportamientos intercambiables

---

### DÍA 5: Testing y Trabajo en Proyecto Integrador
**Duración:** 8 horas

**Conceptos clave:**
- Unit testing fundamentals (qué, por qué, cuándo)
- Anatomía de un test: Arrange, Act, Assert
- pytest: fixtures, parametrize, marks
- Test coverage y métricas
- Mocking y test doubles (fakes, stubs, mocks)
- Test-Driven Development (TDD): Red-Green-Refactor
- Testing best practices: independencia, determinismo, velocidad
- Organización de tests: estructura de directorios, naming conventions

**Para el proyecto integrador:**
- Escribir tests unitarios para todas las funciones críticas
- Crear fixtures para datos de prueba reutilizables
- Implementar mocking para dependencias externas (archivos, APIs, bases de datos)
- Usar parametrize para probar múltiples casos con el mismo test
- Alcanzar 80%+ de cobertura de código
- Aplicar TDD para nuevas features
- Refactorizar código existente con confianza gracias a los tests
- Documentar casos edge y comportamientos esperados mediante tests

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

Los estudiantes trabajarán en grupos de 3 personas en uno de los proyectos descritos en el directorio [proyectos_integradores/](proyectos_integradores/). Cada día agregarán funcionalidad aplicando los conceptos aprendidos.

**Opciones disponibles:**

### Nivel Básico
1. **Data Pipeline Package** - Sistema ETL configurable
2. **Log Analyzer Tool** - Análisis de logs con métricas y reportes
3. **CSV Data Cleaner** - Limpieza y validación de datos CSV
4. **Config File Manager** - Gestión de configuraciones multi-formato

### Nivel Medio
5. **Data Validator Library** - Framework de validación de datos tabulares
6. **Text Processing Toolkit** - Procesamiento y análisis de texto

Ver [proyectos_integradores/README.md](proyectos_integradores/README.md) para detalles completos de cada proyecto, arquitectura sugerida y cómo cada día del curso contribuye a su desarrollo.

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
- Ver [proyectos_integradores/README.md](proyectos_integradores/README.md) y las guías individuales para dependencias específicas de cada proyecto
