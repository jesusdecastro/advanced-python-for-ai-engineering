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

Este curso utiliza un enfoque incremental para la gestión de dependencias. Cada día instalarás solo las librerías necesarias, practicando la gestión de dependencias de forma realista.

#### Configuración Inicial (5 minutos)

1. Clona el repositorio:
```bash
git clone https://github.com/tu-usuario/advanced-python-for-ai-engineering.git
cd advanced-python-for-ai-engineering
```

2. Crea y activa un entorno virtual:
```bash
python -m venv venv

# Activar
venv\Scripts\activate     # Windows
source venv/bin/activate  # Linux/Mac
```

3. Instala las dependencias del Día 1:
```bash
pip install -r day_1/requirements.txt
```

4. Verifica la instalación:
```bash
jupyter --version
ruff --version
pytest --version
```

Para la guía completa de instalación incremental por día, consulta [INSTALACION.md](INSTALACION.md).

## Estructura del Repositorio

```
advanced-python-for-ai-engineering/
├── day_1/                          # Día 1: Configuración de proyectos
│   ├── 01_virtual_environments.ipynb
│   ├── 02_type_hinting.ipynb
│   ├── 03_modules_and_imports.ipynb
│   ├── 04_package_distribution.ipynb
│   ├── 05_code_quality_tools.ipynb
│   ├── exercises/                  # Ejercicios con tests
│   └── README.md
├── day_2/                          # Día 2: Código pythónico
│   ├── 01_comprehensions.ipynb
│   ├── 02_generators_iterators.ipynb
│   ├── 03_decorators.ipynb
│   ├── 04_functional_programming.ipynb
│   ├── 05_context_managers.ipynb
│   ├── 06_magic_methods.ipynb
│   └── exercises/
├── day_3/                          # Día 3: Código limpio
│   ├── 01_clean_functions.ipynb
│   ├── 02_meaningful_names.ipynb
│   ├── 03_type_hints_advanced.ipynb
│   ├── 04_error_handling.ipynb
│   ├── 05_comments_documentation.ipynb
│   ├── 06_dry_kiss_principles.ipynb
│   └── exercises/
├── day_4/                          # Día 4: OOP y diseño
│   ├── 01_objects_vs_data_structures.ipynb
│   ├── 02_pydantic_vs_dataclasses.ipynb
│   ├── 03_classes_srp.ipynb
│   ├── 04_inheritance_vs_composition.ipynb
│   ├── 05_abstract_base_classes.ipynb
│   ├── 06_solid_principles.ipynb
│   └── exercises/
├── day_5/                          # Día 5: Testing y optimización
│   ├── 01_unit_testing_pytest.ipynb
│   ├── 02_tdd.ipynb
│   ├── 03_numpy_vectorization.ipynb
│   ├── 04_pandas_optimization.ipynb
│   ├── 05_memory_profiling.ipynb
│   └── exercises/
├── proyectos_integradores/         # Guías de proyectos
│   ├── 01_data_pipeline_guia.md
│   ├── 02_log_analyzer_guia.md
│   ├── 03_csv_cleaner_guia.md
│   ├── 04_config_manager_guia.md
│   ├── 05_data_validator_guia.md
│   ├── 06_text_processing_guia.md
│   └── README.md
├── .kiro/steering/                 # Estándares del curso
│   ├── course-standards.md
│   └── notebook-structure.md
├── plan_de_formacion.md            # Plan detallado del curso
├── requirements.txt                # Dependencias
├── pyproject.toml                  # Configuración del proyecto
└── README.md                       # Este archivo
```

## Cómo Usar Este Repositorio

### Notebooks

Cada día contiene notebooks Jupyter con:
- Explicaciones teóricas en castellano
- Ejemplos de código ejecutables
- Ejercicios prácticos
- Preguntas de autoevaluación
- Referencias oficiales

Para trabajar con los notebooks:
```bash
cd day_1
jupyter notebook
```

### Ejercicios

Cada día incluye ejercicios prácticos con tests unitarios:

```bash
# Navega al día correspondiente
cd day_1

# Completa los ejercicios en exercises/
code exercises/02_type_hinting.py

# Ejecuta los tests
pytest exercises/tests/test_02_type_hinting.py -v

# O ejecuta todos los tests del día
pytest exercises/tests/ -v

# Con el script helper
./run_tests.sh          # Linux/Mac
run_tests.bat           # Windows
```

### Validación de Código

Todos los ejercicios deben cumplir con los estándares del curso:

```bash
# Type checking con pyright
pyright exercises/

# Linting con ruff
ruff check exercises/

# Formateo automático
ruff format exercises/

# Ejecutar todo junto
ruff check exercises/ && ruff format exercises/ && pyright exercises/
```

## Proyecto Integrador

Durante el curso, trabajarás en grupos de 3 personas en uno de estos proyectos:

1. **Data Pipeline Package** (⭐⭐ Básica) - Sistema ETL configurable
2. **Log Analyzer Tool** (⭐⭐ Básica) - Análisis de logs con métricas
3. **CSV Data Cleaner** (⭐⭐ Básica) - Limpieza y validación de CSV
4. **Config File Manager** (⭐⭐ Básica) - Gestión de configuraciones
5. **Data Validator Library** (⭐⭐⭐ Media) - Framework de validación
6. **Text Processing Toolkit** (⭐⭐⭐ Media) - Procesamiento de texto

Cada día agregarás funcionalidad aplicando los conceptos aprendidos. Ver [proyectos_integradores/README.md](proyectos_integradores/README.md) para detalles completos.

## Stack Tecnológico

**Core:**
- Python 3.11+
- uv / venv (entornos virtuales)
- pytest (testing)
- ruff (linting y formateo)
- pyright (type checking)

**Librerías principales:**
- pydantic (validación de datos)
- numpy (computación numérica)
- pandas (análisis de datos)
- functools, itertools (programación funcional)

**Herramientas de desarrollo:**
- Jupyter Notebook
- Git
- VS Code / PyCharm

## Estándares del Curso

Este curso sigue estándares estrictos de calidad:

### Idioma
- **Documentación**: Castellano
- **Código**: Inglés
- **Docstrings**: Inglés (formato Sphinx)
- **Comentarios**: Inglés

### Código
- Type hints en todas las funciones
- Docstrings formato Sphinx
- Convenciones PEP 8 (snake_case, PascalCase)
- Tests unitarios con pytest
- Cobertura mínima 80%

Ver [.kiro/steering/course-standards.md](.kiro/steering/course-standards.md) para detalles completos.

## Evaluación

El curso se evalúa mediante:

1. **Ejercicios diarios** (40%) - Tests deben pasar
2. **Proyecto integrador** (50%) - Funcionalidad, tests, documentación
3. **Participación** (10%) - Preguntas, discusiones, code reviews

### Criterios del Proyecto Final

- ✅ Funcionalidad completa según especificación
- ✅ Tests con cobertura ≥ 80%
- ✅ Código pasa ruff y pyright sin errores
- ✅ Docstrings completos en formato Sphinx
- ✅ README con instalación y ejemplos de uso
- ✅ Paquete distribuible (wheel)

## Contribuciones

Este es un curso en constante mejora. Si encuentras errores o tienes sugerencias:

1. Abre un issue describiendo el problema
2. Propón mejoras mediante pull requests
3. Comparte feedback con los instructores

## Recursos Adicionales

### Documentación Oficial
- [Python Documentation](https://docs.python.org/3/)
- [PEP 8 - Style Guide](https://peps.python.org/pep-0008/)
- [Type Hints - PEP 484](https://peps.python.org/pep-0484/)
- [pytest Documentation](https://docs.pytest.org/)

### Libros Recomendados
- "Clean Code" - Robert C. Martin
- "Fluent Python" - Luciano Ramalho
- "Python Testing with pytest" - Brian Okken
- "Effective Python" - Brett Slatkin

### Herramientas
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [Pyright Documentation](https://microsoft.github.io/pyright/)
- [uv Documentation](https://docs.astral.sh/uv/)

## Contacto

Para preguntas sobre el curso:
- Instructor: [Nombre del instructor]
- Email: [email@ejemplo.com]
- Horario de consultas: [Horario]

## Licencia

Este material educativo está disponible bajo [especificar licencia].

---

Comienza el curso en `day_1/README.md`.
