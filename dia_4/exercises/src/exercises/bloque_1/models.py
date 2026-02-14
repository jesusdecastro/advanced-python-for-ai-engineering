"""
Modelos Pydantic para configuración de un pipeline de limpieza de CSV.

Tu trabajo:
1. Implementar los modelos que validen la configuración
2. Usar Field() para restricciones
3. Usar @field_validator y @model_validator para reglas de negocio
4. Usar discriminated unions para source_type
"""

from typing import Annotated, Literal, Union

from pydantic import BaseModel, Field, SecretStr, TypeAdapter, field_validator, model_validator


class CleaningStep(BaseModel):
    """
    Un paso de limpieza.

    Hints:
    - operation debe ser uno de: "drop_nulls", "drop_duplicates",
      "fill_nulls", "rename_columns". Usa Literal para restringirlo.
    - params es un dict opcional (puede no venir). Usa dict con default.
    """

    operation: Literal["drop_nulls", "drop_duplicates", "fill_nulls", "rename_columns"]
    params: dict = {}


class LocalSourceConfig(BaseModel):
    """
    Fuente de datos local.

    Hints:
    - Necesita un campo source_type que siempre valga "local".
      Usa Literal["local"] con valor por defecto.
    - path es obligatorio (str).
    - encoding es opcional con default "utf-8".
    """

    source_type: Literal["local"] = "local"
    path: str
    encoding: str = "utf-8"


class URLSourceConfig(BaseModel):
    """
    Fuente de datos remota.

    Hints:
    - Necesita un campo source_type que siempre valga "url".
    - url es obligatorio (str).
    - timeout_seconds debe estar entre 1 y 120. Usa Field(ge=..., le=...).
    - api_token es un secreto. Usa SecretStr para que no se filtre en logs.
    """

    source_type: Literal["url"] = "url"
    url: str
    timeout_seconds: int = Field(ge=1, le=120)
    api_token: SecretStr


# Discriminated union type
_SourceConfigType = Annotated[
    Union[LocalSourceConfig, URLSourceConfig], Field(discriminator="source_type")
]

# TypeAdapter for instantiation
_source_config_adapter = TypeAdapter(_SourceConfigType)


# Factory function that acts like a class constructor
def SourceConfig(**data) -> LocalSourceConfig | URLSourceConfig:  # noqa: N802
    """
    Factory function to instantiate the correct source config based on discriminator.
    
    This allows using SourceConfig(**data) syntax with discriminated unions.
    
    :param data: Configuration data with source_type discriminator
    :return: Either LocalSourceConfig or URLSourceConfig instance
    """
    return _source_config_adapter.validate_python(data)


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

    format: Literal["csv", "parquet", "jsonl"]
    directory: str
    compression: str | None = None

    @model_validator(mode="after")
    def validate_compression(self):
        """Validate compression rules based on format."""
        if self.format == "parquet":
            if self.compression not in ("snappy", "gzip"):
                raise ValueError(
                    "parquet format requires compression to be 'snappy' or 'gzip'"
                )
        else:  # csv or jsonl
            if self.compression is not None:
                raise ValueError(f"{self.format} format must not have compression")
        return self


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

    job_name: str = Field(min_length=1)
    source: _SourceConfigType
    steps: list[CleaningStep]
    output: OutputConfig

    @field_validator("job_name")
    @classmethod
    def normalize_job_name(cls, v: str) -> str:
        """Normalize job_name to snake_case."""
        return v.strip().lower().replace(" ", "_")
