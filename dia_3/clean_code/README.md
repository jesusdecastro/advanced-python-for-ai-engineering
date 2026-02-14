# Material de Referencia - Clean Code

Documentos de referencia sobre Clean Code para complementar los ejercicios del día 3.

## Contenido

1. **`01_error_handling_and_logging.md`** (20 min)
   - Excepciones específicas vs genéricas
   - Logging efectivo en pipelines ML
   - Niveles de logging y contexto en errores

2. **`02_objects_and_data_structures.md`** (20 min)
   - Objetos vs estructuras de datos
   - Ley de Demeter
   - Cuándo usar @dataclass vs encapsulación

3. **`03_formatting.md`** (20 min)
   - Archivos cohesivos (200-500 líneas)
   - Separación vertical y ordenamiento
   - Herramientas: Black, Ruff

4. **`04_type_hints_practical.md`** (15 min)
   - Union y Optional en ML/Data
   - Cuándo usar type hints

5. **`05_separation_of_concerns.md`** (15 min)
   - Separar I/O, lógica, presentación
   - Arquitectura en capas

6. **`06_defensive_programming.md`** (20 min)
   - Validación de entrada
   - Fail fast pattern
   - Constantes vs magic numbers

## Uso Recomendado

**Estos documentos son opcionales.** Los conceptos clave están en los ejercicios.

**Cuándo consultar:**
- Durante ejercicios para profundizar
- Como referencia en proyectos
- Para debate sobre trade-offs

## Relación con Ejercicios

- `error_handling.py` + `logging_practice.py` → Documento 01
- `objects_data_structures.py` → Documento 02
- `defensive.py` → Documento 06

Los documentos 03, 04, 05 son contexto adicional sobre formato, types y arquitectura.
