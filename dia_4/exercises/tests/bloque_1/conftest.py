"""Fixtures para tests del Bloque 1."""

import pytest


@pytest.fixture
def valid_local_source():
    """Valid local source configuration."""
    return {
        "source_type": "local",
        "path": "data/reviews.csv",
        "encoding": "utf-8",
    }


@pytest.fixture
def valid_url_source():
    """Valid URL source configuration."""
    return {
        "source_type": "url",
        "url": "https://api.example.com/data",
        "timeout_seconds": 30,
        "api_token": "secret_token_123",
    }


@pytest.fixture
def valid_cleaning_steps():
    """Valid cleaning steps."""
    return [
        {"operation": "drop_nulls", "params": {}},
        {"operation": "rename_columns", "params": {"old": "rev", "new": "review"}},
    ]


@pytest.fixture
def valid_parquet_output():
    """Valid parquet output configuration."""
    return {
        "format": "parquet",
        "directory": "output/",
        "compression": "snappy",
    }


@pytest.fixture
def valid_csv_output():
    """Valid CSV output configuration."""
    return {
        "format": "csv",
        "directory": "output/",
    }


@pytest.fixture
def full_config_dict(valid_local_source, valid_cleaning_steps, valid_parquet_output):
    """Complete valid configuration."""
    return {
        "job_name": "  Clean Product Reviews  ",
        "source": valid_local_source,
        "steps": valid_cleaning_steps,
        "output": valid_parquet_output,
    }
