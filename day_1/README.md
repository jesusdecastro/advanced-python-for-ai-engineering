# Día 1: Configuración de Proyectos Python

## Contenido

1. **01_python_idioms_intro.ipynb** - Bienvenida con Python Idioms
2. **02_virtual_environments.ipynb** - Entornos Virtuales
3. **03_modules_and_imports.ipynb** - Módulos e Imports
4. **04_type_hinting.ipynb** - Type Hinting
5. **05_code_quality_tools.ipynb** - Herramientas de Calidad
6. **06_package_distribution.ipynb** - Distribución de Paquetes

## Enfoque Pedagógico

El Día 1 comienza con código Python elegante (notebook 01) para generar engagement inmediato. Luego progresa a la configuración profesional de proyectos.

## Dependencias

**Notebook 01:** No requiere instalación - usa solo Python stdlib

**Notebooks 02-06:** Instalar dependencias:

```bash
pip install -r day_1/requirements.txt
```

Esto instala las herramientas fundamentales:
- Jupyter y Notebook
- Ruff (linter y formateador)
- Pyright (type checker)
- Pytest (testing framework)

## Ejercicios

Ejecutar tests:
```bash
pytest day_1/exercises/tests/
```

Validar código:
```bash
ruff check day_1/exercises/
pyright day_1/exercises/
```
