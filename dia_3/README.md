# Día 3: Clean Code Práctico

Manejo de errores, logging, defensive programming y diseño de objetos aplicado a Data/IA.

## Inicio Rápido

```bash
cd dia_3/exercises
uv sync                    # Instalar entorno
uv run pytest tests        # Ejecutar tests
```

## Estructura

```
dia_3/
├── clean_code/           # Material de referencia (lectura opcional)
│   ├── 01_error_handling_and_logging.md
│   ├── 02_objects_and_data_structures.md
│   ├── 03_formatting.md
│   ├── 04_type_hints_practical.md
│   ├── 05_separation_of_concerns.md
│   └── 06_defensive_programming.md
│
└── exercises/            # Ejercicios prácticos con tests
    ├── src/exercises/
    │   ├── error_handling.py
    │   ├── logging_practice.py
    │   ├── defensive.py
    │   └── objects_data_structures.py
    └── tests/
```

## Contenido

### 1. Error Handling & Logging
- Excepciones específicas vs genéricas
- Logging estratégico en pipelines ML
- Contexto en errores para debugging
- **Ejercicios**: `error_handling.py`, `logging_practice.py`

### 2. Defensive Programming
- Validación de inputs (tipos, rangos, formatos)
- Fail fast pattern
- Type hints con Union y Optional
- Constantes vs magic numbers
- **Ejercicios**: `defensive.py`

### 3. Objects & Data Structures
- Objetos vs estructuras de datos
- Ley de Demeter
- Cuándo usar @dataclass vs encapsulación
- Evitar híbridos confusos
- **Ejercicios**: `objects_data_structures.py`

## Material de Referencia

Los documentos en `clean_code/` son lectura opcional (15-20 min cada uno) para profundizar conceptos. Los ejercicios ya integran los conceptos clave.

**Cuándo consultar:**
- Durante ejercicios si necesitas más contexto
- Como referencia para proyectos
- Para debate en equipo sobre trade-offs

## Conexión con Otros Días

- **Día 1**: Type hints, módulos, herramientas (ruff, pyright)
- **Día 2**: Meaningful names, funciones limpias, DRY/SRP
- **Día 3**: Robustez con error handling y defensive programming
- **Día 4**: Arquitectura y patrones de diseño
