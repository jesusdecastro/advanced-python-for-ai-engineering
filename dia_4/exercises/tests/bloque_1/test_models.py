"""Tests para ejercicios del Bloque 1: Modelado de Datos con Pydantic."""

import pytest
from pydantic import ValidationError

from exercises.bloque_1.models import (
    CleaningJobConfig,
    CleaningStep,
    LocalSourceConfig,
    OutputConfig,
    URLSourceConfig,
)


# ============================================================================
# TESTS: CleaningStep
# ============================================================================
def test_cleaning_step_with_valid_operation():
    """Test CleaningStep accepts valid operations."""
    step = CleaningStep(operation="drop_nulls", params={})
    assert step.operation == "drop_nulls"
    assert step.params == {}


def test_invalid_cleaning_operation_raises_error():
    """Test CleaningStep rejects invalid operations."""
    with pytest.raises(ValidationError):
        CleaningStep(operation="invalid_operation", params={})


def test_cleaning_step_params_optional():
    """Test CleaningStep params is optional."""
    step = CleaningStep(operation="drop_duplicates")
    assert step.params == {}


# ============================================================================
# TESTS: LocalSourceConfig
# ============================================================================
def test_valid_local_source_config_creates_successfully(valid_local_source):
    """Test LocalSourceConfig with valid data."""
    config = LocalSourceConfig(**valid_local_source)
    assert config.source_type == "local"
    assert config.path == "data/reviews.csv"
    assert config.encoding == "utf-8"


def test_local_source_encoding_defaults_to_utf8():
    """Test LocalSourceConfig encoding defaults to utf-8."""
    config = LocalSourceConfig(source_type="local", path="data/test.csv")
    assert config.encoding == "utf-8"


# ============================================================================
# TESTS: URLSourceConfig
# ============================================================================
def test_valid_url_source_config_creates_successfully(valid_url_source):
    """Test URLSourceConfig with valid data."""
    config = URLSourceConfig(**valid_url_source)
    assert config.source_type == "url"
    assert config.url == "https://api.example.com/data"
    assert config.timeout_seconds == 30


def test_url_timeout_out_of_range_raises_validation_error():
    """Test URLSourceConfig rejects timeout out of range."""
    with pytest.raises(ValidationError):
        URLSourceConfig(
            source_type="url",
            url="https://api.example.com/data",
            timeout_seconds=150,
            api_token="token",
        )

    with pytest.raises(ValidationError):
        URLSourceConfig(
            source_type="url",
            url="https://api.example.com/data",
            timeout_seconds=0,
            api_token="token",
        )


def test_secret_str_hides_api_token(valid_url_source):
    """Test SecretStr hides api_token in repr."""
    config = URLSourceConfig(**valid_url_source)
    config_str = str(config)
    assert "secret_token_123" not in config_str
    assert config.api_token.get_secret_value() == "secret_token_123"


# ============================================================================
# TESTS: Discriminated Union
# ============================================================================
def test_discriminated_union_selects_correct_model(valid_local_source, valid_url_source):
    """Test discriminated union selects correct model based on source_type."""
    from exercises.bloque_1.models import SourceConfig

    # Local source
    local_config = SourceConfig(**valid_local_source)
    assert isinstance(local_config, LocalSourceConfig)

    # URL source
    url_config = SourceConfig(**valid_url_source)
    assert isinstance(url_config, URLSourceConfig)


def test_unknown_source_type_raises_error():
    """Test discriminated union rejects unknown source_type."""
    from exercises.bloque_1.models import SourceConfig

    with pytest.raises(ValidationError):
        SourceConfig(source_type="unknown", path="data.csv")


# ============================================================================
# TESTS: OutputConfig
# ============================================================================
def test_parquet_without_compression_raises_error():
    """Test OutputConfig requires compression for parquet."""
    with pytest.raises(ValidationError):
        OutputConfig(format="parquet", directory="output/")


def test_parquet_with_invalid_compression_raises_error():
    """Test OutputConfig rejects invalid compression for parquet."""
    with pytest.raises(ValidationError):
        OutputConfig(format="parquet", directory="output/", compression="invalid")


def test_parquet_with_valid_compression_is_valid():
    """Test OutputConfig accepts valid compression for parquet."""
    config = OutputConfig(format="parquet", directory="output/", compression="snappy")
    assert config.compression == "snappy"

    config = OutputConfig(format="parquet", directory="output/", compression="gzip")
    assert config.compression == "gzip"


def test_csv_without_compression_is_valid(valid_csv_output):
    """Test OutputConfig accepts CSV without compression."""
    config = OutputConfig(**valid_csv_output)
    assert config.format == "csv"
    assert config.compression is None


def test_csv_with_compression_raises_error():
    """Test OutputConfig rejects compression for CSV."""
    with pytest.raises(ValidationError):
        OutputConfig(format="csv", directory="output/", compression="gzip")


def test_jsonl_without_compression_is_valid():
    """Test OutputConfig accepts JSONL without compression."""
    config = OutputConfig(format="jsonl", directory="output/")
    assert config.format == "jsonl"
    assert config.compression is None


# ============================================================================
# TESTS: CleaningJobConfig
# ============================================================================
def test_empty_job_name_raises_validation_error():
    """Test CleaningJobConfig rejects empty job_name."""
    with pytest.raises(ValidationError):
        CleaningJobConfig(
            job_name="",
            source={"source_type": "local", "path": "data.csv"},
            steps=[],
            output={"format": "csv", "directory": "output/"},
        )


def test_job_name_normalized_to_snake_case(full_config_dict):
    """Test CleaningJobConfig normalizes job_name to snake_case."""
    config = CleaningJobConfig(**full_config_dict)
    assert config.job_name == "clean_product_reviews"


def test_full_config_round_trip(full_config_dict):
    """Test full config can be created, dumped, and recreated."""
    # Create from dict
    config1 = CleaningJobConfig(**full_config_dict)

    # Dump to dict
    dumped = config1.model_dump()

    # Create from dumped dict
    config2 = CleaningJobConfig(**dumped)

    # Should be equal
    assert config1.job_name == config2.job_name
    assert config1.source.source_type == config2.source.source_type
    assert len(config1.steps) == len(config2.steps)
    assert config1.output.format == config2.output.format


def test_model_dump_json_produces_valid_json(full_config_dict):
    """Test CleaningJobConfig can serialize to JSON."""
    config = CleaningJobConfig(**full_config_dict)
    json_str = config.model_dump_json()

    assert isinstance(json_str, str)
    assert "clean_product_reviews" in json_str
    assert "local" in json_str


def test_config_with_url_source():
    """Test CleaningJobConfig with URL source."""
    config_dict = {
        "job_name": "API Job",
        "source": {
            "source_type": "url",
            "url": "https://api.example.com/data",
            "timeout_seconds": 60,
            "api_token": "secret",
        },
        "steps": [{"operation": "drop_nulls"}],
        "output": {"format": "jsonl", "directory": "output/"},
    }

    config = CleaningJobConfig(**config_dict)
    assert config.job_name == "api_job"
    assert config.source.source_type == "url"
