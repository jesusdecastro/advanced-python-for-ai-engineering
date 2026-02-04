# Día 4: Programación Orientada a Objetos

## Descripción General

El Día 4 se enfoca en los principios fundamentales de la Programación Orientada a Objetos (OOP) en Python. Aprenderás a diseñar clases efectivas, aplicar los principios SOLID, y crear arquitecturas de software mantenibles y extensibles.

## Contenido

### Notebooks

1. **01_objects_vs_data_structures.ipynb** - Objetos vs Estructuras de Datos
   - Diferencias entre objetos y estructuras de datos
   - Cuándo usar clases vs diccionarios vs dataclasses
   - Encapsulación y ocultamiento de datos

2. **02_pydantic_vs_dataclasses.ipynb** - Pydantic vs Dataclasses
   - Dataclasses para estructuras de datos simples
   - Pydantic para validación automática
   - Cuándo usar cada herramienta

3. **03_classes_srp.ipynb** - Clases y el Principio de Responsabilidad Única
   - Single Responsibility Principle (SRP)
   - Diseño de clases cohesivas
   - Refactorización para cumplir con SRP

4. **04_inheritance_vs_composition.ipynb** - Herencia vs Composición
   - Diferencias entre herencia y composición
   - Favor composition over inheritance
   - Diseño flexible con composición

5. **05_abstract_base_classes.ipynb** - Abstract Base Classes (ABC)
   - Definición de interfaces con ABC
   - Métodos abstractos
   - Contratos y polimorfismo

6. **06_solid_principles.ipynb** - Principios SOLID
   - Los cinco principios SOLID
   - Aplicación en Python
   - Diseño de software mantenible

### Ejercicios

Cada notebook tiene ejercicios correspondientes en la carpeta `exercises/`:
- `01_objects_vs_data_structures.py`
- `02_pydantic_vs_dataclasses.py`
- `03_classes_srp.py`
- `04_inheritance_vs_composition.py`
- `05_abstract_base_classes.py`
- `06_solid_principles.py`

### Tests

Los tests para validar tus soluciones están en `exercises/tests/`:
- `test_01_objects_vs_data_structures.py`
- `test_02_pydantic_vs_dataclasses.py`
- `test_03_classes_srp.py`
- `test_04_inheritance_vs_composition.py`
- `test_05_abstract_base_classes.py`
- `test_06_solid_principles.py`

## Cómo Usar Este Material

1. **Lee los notebooks** en orden secuencial
2. **Completa los ejercicios** en la carpeta `exercises/`
3. **Ejecuta los tests** para validar tus soluciones:
   ```bash
   pytest exercises/tests/
   ```

## Objetivos de Aprendizaje

Al finalizar el Día 4, serás capaz de:

- Distinguir entre objetos y estructuras de datos
- Aplicar el Principio de Responsabilidad Única
- Elegir entre herencia y composición apropiadamente
- Usar Abstract Base Classes para definir interfaces
- Aplicar los cinco principios SOLID en tu código
- Diseñar sistemas OOP mantenibles y extensibles

## Requisitos

- Python 3.10+
- pydantic (para el notebook 02)
- pytest (para ejecutar los tests)

## Recursos Adicionales

- [Python Classes Tutorial](https://docs.python.org/3/tutorial/classes.html)
- [PEP 557 - Data Classes](https://www.python.org/dev/peps/pep-0557/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [SOLID Principles in Python](https://realpython.com/solid-principles-python/)
