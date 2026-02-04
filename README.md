# Curso de Python Avanzado para IA

Curso intensivo de 6 días enfocado en Python avanzado aplicado a Ingeniería de IA, con énfasis en Clean Code, arquitectura de software y mejores prácticas de desarrollo.

## Descripción

Este curso está diseñado para desarrolladores que desean dominar Python avanzado aplicado a proyectos de Inteligencia Artificial. A través de 6 días intensivos, aprenderás desde la configuración profesional de proyectos hasta el desarrollo de paquetes Python production-ready, aplicando principios de Clean Code, SOLID y TDD.

**Duración:** 48 horas (6 días × 8 horas)  
**Modalidad:** Remoto con proyecto integrador grupal  
**Nivel:** Intermedio-Avanzado

## Objetivos del Curso

Al finalizar este curso, serás capaz de:

- Configurar proyectos Python profesionales con estructura modular
- Aplicar principios de Clean Code y SOLID en Python
- Desarrollar código pythónico usando idioms y patrones avanzados
- Diseñar arquitecturas orientadas a objetos robustas y mantenibles
- Implementar testing completo con pytest (TDD, fixtures, mocking)
- Optimizar código para procesamiento de datos con NumPy y pandas
- Crear paquetes Python distribuibles y production-ready

## Contenido por Día

### Día 1: Fundamentos - Configuración de Proyectos Python
- Entornos virtuales (venv, uv)
- Sistema de módulos e imports
- Estructura de paquetes (src layout)
- pyproject.toml y gestión de dependencias
- Distribución de paquetes (wheels)
- Herramientas de calidad (ruff, pyright)

### Día 2: Código Pythónico - Idioms y Programación Funcional
- Comprehensions (list, dict, set)
- Generadores e iteradores
- Decoradores prácticos
- Programación funcional (map, filter, reduce)
- Context managers
- Métodos mágicos

### Día 3: Código Limpio - Legibilidad y Robustez
- Clean Functions (SRP, funciones pequeñas)
- Meaningful Names
- Type hints avanzados
- Error handling y excepciones custom
- Documentación y docstrings
- Principios DRY y KISS

### Día 4: Diseño - Programación Orientada a Objetos
- Objects vs Data Structures
- Pydantic vs dataclasses
- Classes y Single Responsibility Principle
- Herencia vs composición
- Abstract Base Classes (ABC)
- Principios SOLID en Python

### Día 5: Procesamiento de Datos y Testing
- NumPy vectorization
- pandas optimization
- Memory profiling
- Unit testing con pytest
- Test-Driven Development (TDD)

### Día 6: Proyecto Integrador
- Finalización del proyecto grupal
- Integración de todos los conceptos
- Documentación completa
- Presentación de proyectos

## Inicio Rápido

### Requisitos Previos

- Python 3.11 o superior instalado
- Git instalado
- VS Code con las siguientes extensiones:
  - Python (Microsoft)
  - Ruff (Astral Software)
- Conocimientos básicos de Python

### Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/tu-usuario/advanced-python-for-ai-engineering.git
cd advanced-python-for-ai-engineering
```

2. Sigue las instrucciones en `day_1/README.md` para configurar tu entorno de desarrollo.

El curso utiliza un enfoque incremental: cada día instalarás solo las dependencias necesarias. Consulta [INSTALACION.md](INSTALACION.md) para la guía completa.

## Estructura del Repositorio

```
advanced-python-for-ai-engineering/
├── day_1/                          # Día 1: Configuración de proyectos
├── day_2/                          # Día 2: Código pythónico
├── day_3/                          # Día 3: Código limpio
├── day_4/                          # Día 4: OOP y diseño
├── day_5/                          # Día 5: Testing y optimización
├── proyectos_integradores/         # Guías de proyectos
├── INSTALACION.md                  # Guía de instalación incremental
├── plan_de_formacion.md            # Plan detallado del curso
└── pyproject.toml                  # Configuración del proyecto
```

## Cómo Usar Este Repositorio

### Notebooks

Cada día contiene notebooks Jupyter con explicaciones teóricas, ejemplos ejecutables, ejercicios prácticos y referencias oficiales.

```bash
cd day_1
jupyter notebook
```

### Ejercicios

Cada día incluye ejercicios prácticos con tests unitarios:

```bash
# Completa los ejercicios
code day_1/exercises/02_type_hinting.py

# Ejecuta los tests
pytest day_1/exercises/tests/ -v
```

### Validación de Código

```bash
# Type checking
pyright exercises/

# Linting y formateo
ruff check exercises/
ruff format exercises/
```

## Proyecto Integrador

Trabajarás en grupos de 3 personas en uno de estos proyectos:

1. **Data Pipeline Package** - Sistema ETL configurable
2. **Log Analyzer Tool** - Análisis de logs con métricas
3. **CSV Data Cleaner** - Limpieza y validación de CSV
4. **Config File Manager** - Gestión de configuraciones
5. **Data Validator Library** - Framework de validación
6. **Text Processing Toolkit** - Procesamiento de texto

Ver [proyectos_integradores/README.md](proyectos_integradores/README.md) para detalles completos.

## Stack Tecnológico

**Core:**
- Python 3.11+
- pytest (testing)
- ruff (linting y formateo)
- pyright (type checking)

**Librerías principales:**
- pydantic (validación de datos)
- numpy (computación numérica)
- pandas (análisis de datos)

**Herramientas:**
- Jupyter Notebook
- Git
- VS Code

## Evaluación

La evaluación se centra en la comprensión y aplicación de los conceptos en el proyecto integrador grupal. Los grupos deberán defender su proyecto demostrando:

- **Comprensión**: Entendimiento profundo de los principios aplicados
- **Comunicación**: Capacidad de explicar decisiones técnicas
- **Colaboración**: Trabajo efectivo en equipo
- **Finalización**: Proyecto funcional y completo

### Criterios del Proyecto

- Funcionalidad completa según especificación
- Tests con cobertura ≥ 80%
- Código pasa ruff y pyright sin errores
- Docstrings completos en formato Sphinx
- README con instalación y ejemplos de uso
- Paquete distribuible (wheel)

## Licencia

Este material educativo está disponible bajo licencia MIT para uso educativo y formación.

---

Comienza el curso en `day_1/README.md`.
