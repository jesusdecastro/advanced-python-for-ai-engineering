# Día 4: Programación Orientada a Objetos

## Contenido

1. **01_objects_vs_data_structures.ipynb** - Objetos vs Estructuras de Datos
2. **02_pydantic_vs_dataclasses.ipynb** - Pydantic vs Dataclasses
3. **03_classes_srp.ipynb** - Clases y Single Responsibility Principle
4. **04_inheritance_vs_composition.ipynb** - Herencia vs Composición
5. **05_abstract_base_classes.ipynb** - Abstract Base Classes
6. **06_solid_principles.ipynb** - Principios SOLID

## Dependencias

Consulta `day_4/requirements.txt` para ver qué necesitas. Edita `pyproject.toml` añadiendo pydantic:

```toml
[project]
dependencies = [
    "pydantic>=2.0.0",
]
```

Actualiza la instalación:
```bash
pip install -e ".[dev]"
```

## Ejercicios

Ejecutar tests:

```bash
pytest day_4/exercises/tests/
```
