# Día 4: Arquitectura de Software y Principios SOLID

Contenido avanzado sobre modelado de datos, composición, separación de responsabilidades y principios SOLID aplicados a proyectos de Data Science e IA.

## Contenido

### Teoría

1. **Dataclasses vs Pydantic** (`teoria/01_dataclasses_vs_pydantic.md`)
   - Cuándo usar dataclasses
   - Cuándo usar Pydantic
   - Comparación práctica
   - Validación de datos con Field y validators

2. **Protocols y Structural Typing** (`teoria/02_protocols_structural_typing.md`)
   - Duck typing vs Protocols
   - Definición de Protocols
   - Runtime checkable
   - Generic Protocols

3. **Principios SOLID en Python** (`teoria/03_solid_principles.md`)
   - Single Responsibility Principle (SRP)
   - Open-Closed Principle (OCP)
   - Liskov Substitution Principle (LSP)
   - Interface Segregation Principle (ISP)
   - Dependency Inversion Principle (DIP)

### Ejercicios Prácticos

Los ejercicios están organizados en 4 bloques temáticos en `exercises/`:

#### Bloque 1: Modelado de Datos con Pydantic
- Configuración de pipeline de limpieza de CSV
- Discriminated unions
- Field validation con restricciones
- Custom validators y model validators
- SecretStr para datos sensibles

#### Bloque 2: Composición sobre Herencia
- Pipeline de preprocesamiento de texto para NLP
- Protocols como contratos
- Composición de componentes
- Datos como argumentos (no estado mutable)
- Dataclasses inmutables

#### Bloque 3: SRP + DIP
- Sistema de scoring de reviews de productos
- Separación de responsabilidades
- Dependency Inversion Principle
- Inyección de dependencias
- Testing con fakes

#### Bloque 4: OCP, LSP, ISP
- Sistema extensible de métricas para evaluación de modelos
- Open-Closed Principle (extensibilidad)
- Liskov Substitution Principle (intercambiabilidad)
- Interface Segregation Principle (protocols segregados)
- Métricas de clasificación y regresión

Ver `exercises/README.md` y los README de cada bloque para instrucciones detalladas.

## Inicio Rápido

```bash
# Configurar ejercicios
cd dia_4/exercises
uv sync

# Ejecutar todos los tests
uv run pytest

# Ejecutar tests de un bloque específico
uv run pytest tests/bloque_1/ -v
uv run pytest tests/bloque_2/ -v
uv run pytest tests/bloque_3/ -v
uv run pytest tests/bloque_4/ -v
```

## Objetivos de Aprendizaje

Al completar este día serás capaz de:

- Elegir entre dataclasses y Pydantic según el caso de uso
- Usar Pydantic para validación robusta de configuraciones
- Definir Protocols para structural typing
- Aplicar composición sobre herencia en diseño de sistemas
- Separar responsabilidades siguiendo SRP
- Diseñar sistemas extensibles con OCP
- Usar inyección de dependencias (DIP)
- Crear interfaces segregadas (ISP)
- Garantizar intercambiabilidad de implementaciones (LSP)

## Prerrequisitos

- Día 3 completado (error handling, logging, defensive programming)
- Conocimiento sólido de type hints
- Familiaridad con pytest
- Comprensión de conceptos de orientación a objetos

## Estructura de los Ejercicios

Cada bloque sigue el mismo patrón:

- `helpers.py`: Lógica de dominio ya implementada (no modificar)
- `protocols.py`: Contratos que las clases deben cumplir (no modificar)
- `<modulo>.py`: Esqueleto con hints para implementar
- `conftest.py`: Fixtures para tests
- `test_<modulo>.py`: Tests completos
- `README.md`: Guía paso a paso con tips

El foco está en la arquitectura, no en implementar lógica de dominio.

## Recursos

- **Dataclasses**: https://docs.python.org/3/library/dataclasses.html
- **Pydantic**: https://docs.pydantic.dev/
- **PEP 544 - Protocols**: https://peps.python.org/pep-0544/
- **SOLID Principles**: https://en.wikipedia.org/wiki/SOLID
- **UV**: https://docs.astral.sh/uv/

## Notas Importantes

- Los ejercicios están diseñados para ser progresivos en dificultad
- Cada bloque es independiente pero los conceptos se acumulan
- La lógica de dominio está resuelta en helpers.py para enfocarse en arquitectura
- Los tests están ordenados de simple a complejo para guiar la implementación
- Se recomienda completar los bloques en orden
