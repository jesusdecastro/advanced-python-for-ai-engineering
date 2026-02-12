# Bloque 1: Modelado de Datos con Pydantic

## Objetivo

Practicar el uso de Pydantic para validar, normalizar y estructurar configuraciones complejas.

## Concepto que se Practica

- Pydantic BaseModel
- Field con restricciones (min_length, ge, le)
- Discriminated unions
- @field_validator
- @model_validator
- SecretStr

## Qué NO es el Foco

- Lógica de limpieza de datos
- Lectura de archivos
- Pandas

## Descripción

Vas a modelar la configuración de un pipeline de limpieza de CSV — el tipo de proyecto integrador que están haciendo. Recibes un diccionario raw y debes crear modelos Pydantic que lo validen automáticamente.

## Ejemplo de Configuración

```python
# Este es el tipo de dict que tu pipeline recibe hoy.
# Tu trabajo: convertirlo en modelos Pydantic que lo validen automáticamente.
raw_config = {
    "job_name": "  Clean Product Reviews  ",
    "source": {
        "source_type": "local",  # "local" o "url"
        "path": "data/reviews.csv",
        "encoding": "utf-8",
    },
    "steps": [
        {"operation": "drop_nulls", "params": {}},
        {"operation": "rename_columns", "params": {"old": "rev", "new": "review"}},
    ],
    "output": {
        "format": "parquet",  # "csv", "parquet" o "jsonl"
        "directory": "output/",
        "compression": "snappy",  # Obligatorio si format es parquet
    },
}
```

## Tips para Implementar

### 1. Empieza por CleaningStep (el más simple)

```bash
uv run pytest tests/bloque_1/test_models.py::test_cleaning_step_with_valid_operation -v
```

- `operation` debe ser uno de: "drop_nulls", "drop_duplicates", "fill_nulls", "rename_columns"
- Usa `Literal` para restringirlo
- `params` es un dict opcional con default `{}`

### 2. Sigue con LocalSourceConfig y URLSourceConfig

```bash
uv run pytest tests/bloque_1/test_models.py::test_valid_local_source_config_creates_successfully -v
uv run pytest tests/bloque_1/test_models.py::test_valid_url_source_config_creates_successfully -v
```

- La clave es el campo `source_type: Literal[...]`
- LocalSourceConfig: `source_type` siempre es "local"
- URLSourceConfig: `source_type` siempre es "url"
- URLSourceConfig: `timeout_seconds` debe estar entre 1 y 120 (usa `Field(ge=1, le=120)`)
- URLSourceConfig: `api_token` es un `SecretStr` para que no se filtre en logs

### 3. Discriminated Union

```bash
uv run pytest tests/bloque_1/test_models.py::test_discriminated_union_selects_correct_model -v
```

Mira el ejemplo del markdown del Bloque 1 (sección "Modelos Anidados"):

```python
SourceConfig = Annotated[
    Union[LocalSourceConfig, URLSourceConfig],
    Field(discriminator="source_type")
]
```

Pydantic elige automáticamente LocalSourceConfig o URLSourceConfig según el valor de "source_type".

### 4. OutputConfig con @model_validator

```bash
uv run pytest tests/bloque_1/test_models.py::test_parquet_without_compression_raises_error -v
```

Reglas de negocio:
- Si `format` es "parquet", `compression` DEBE existir y ser "snappy" o "gzip"
- Si `format` es "csv" o "jsonl", `compression` DEBE ser None

Usa `@model_validator(mode='after')` para verificar estas reglas.

### 5. CleaningJobConfig con @field_validator

```bash
uv run pytest tests/bloque_1/test_models.py::test_job_name_normalized_to_snake_case -v
```

Para normalizar `job_name` a snake_case:
1. `.strip()` — elimina espacios al inicio/final
2. `.lower()` — convierte a minúsculas
3. `.replace(" ", "_")` — reemplaza espacios por guiones bajos

Usa `@field_validator('job_name')` con `mode='after'`.

## Ejecutar Tests

```bash
# Todos los tests del bloque
uv run pytest tests/bloque_1/ -v

# Un test específico
uv run pytest tests/bloque_1/test_models.py::test_cleaning_step_with_valid_operation -v

# Tests de un concepto
uv run pytest tests/bloque_1/ -k "cleaning_step" -v
```

## Criterios de Éxito

- [ ] CleaningStep valida operaciones con Literal
- [ ] LocalSourceConfig y URLSourceConfig tienen source_type correcto
- [ ] Discriminated union funciona automáticamente
- [ ] URLSourceConfig valida timeout_seconds con Field
- [ ] SecretStr oculta api_token en repr
- [ ] OutputConfig valida reglas de compression con @model_validator
- [ ] CleaningJobConfig normaliza job_name con @field_validator
- [ ] Todos los tests pasan

## Recursos

- **Pydantic Field**: https://docs.pydantic.dev/latest/concepts/fields/
- **Discriminated Unions**: https://docs.pydantic.dev/latest/concepts/unions/#discriminated-unions
- **Validators**: https://docs.pydantic.dev/latest/concepts/validators/
- **SecretStr**: https://docs.pydantic.dev/latest/api/types/#pydantic.types.SecretStr
