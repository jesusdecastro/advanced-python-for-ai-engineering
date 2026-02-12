"""
Modelos Pydantic para configuración de un pipeline de limpieza de CSV.

Tu trabajo:
1. Implementar los modelos que validen la configuración
2. Usar Field() para restricciones
3. Usar @field_validator y @model_validator para reglas de negocio
4. Usar discriminated unions para source_type
"""

from typing import Annotated, Literal, Union

from pydantic import BaseModel, Field, SecretStr, field_validator, model_validator


class CleaningStep(BaseModel):
    """
    Un paso de limpieza.

    Hints:
    - operation debe ser uno de: "drop_nulls", "drop_duplicates",
      "fill_nulls", "rename_columns". Usa Literal para restringirlo.
    - params es un dict opcional (puede no venir). Usa dict con default.
    """

    ...


class LocalSourceConfig(BaseModel):
    """
    Fuente de datos local.

    Hints:
    - Necesita un campo source_type que siempre valga "local".
      Usa Literal["local"] con valor por defecto.
    - path es obligatorio (str).
    - encoding es opcional con default "utf-8".
    """

    ...


class URLSourceConfig(BaseModel):
    """
    Fuente de datos remota.

    Hints:
    - Necesita un campo source_type que siempre valga "url".
    - url es obligatorio (str).
    - timeout_seconds debe estar entre 1 y 120. Usa Field(ge=..., le=...).
    - api_token es un secreto. Usa SecretStr para que no se filtre en logs.
    """

    ...


# Discriminated union: Pydantic elige LocalSourceConfig o URLSourceConfig
# según el valor de "source_type".
# Hint: Annotated[Union[...], Field(discriminator="source_type")]
SourceConfig = ...


class OutputConfig(BaseModel):
    """
    Configuración de salida.

    Hints:
    - format es "csv", "parquet" o "jsonl". Usa Literal.
    - directory es str.
    - compression es str | None con default None.
    - Regla de negocio (usa @model_validator):
      * Si format es "parquet", compression DEBE existir y ser "snappy" o "gzip".
      * Si format es "csv" o "jsonl", compression DEBE ser None.
    """

    ...


class CleaningJobConfig(BaseModel):
    """
    Modelo raíz que agrupa toda la configuración.

    Hints:
    - job_name debe tener al menos 1 carácter. Usa Field(min_length=1).
    - Usa un @field_validator para normalizar job_name a snake_case:
      strip() → lower() → reemplazar espacios por "_"
    - source usa el tipo SourceConfig (la discriminated union de arriba).
    - steps es una lista de CleaningStep.
    - output es un OutputConfig.
    """

    ...
