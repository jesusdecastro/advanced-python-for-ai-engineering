# Día 1: Configuración de Proyectos Python

## Contenido

1. **01_virtual_environments.ipynb** - Entornos Virtuales
2. **02_type_hinting.ipynb** - Type Hinting
3. **03_modules_and_imports.ipynb** - Módulos e Imports
4. **04_package_distribution.ipynb** - Distribución de Paquetes
5. **05_code_quality_tools.ipynb** - Herramientas de Calidad

## Dependencias

Instalar dependencias del Día 1:

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
