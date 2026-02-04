"""
Pydantic vs Dataclasses Exercises - Day 2.

This module contains exercises for practicing dataclasses and Pydantic models.
Students will learn to convert between dataclasses and Pydantic, add validation,
and work with JSON serialization.

Your tasks:
1. Add type hints to all functions and classes
2. Complete the Pydantic models with proper validation
3. Implement custom validators where indicated
4. Add proper Sphinx docstrings to all functions

Run the tests with: pytest tests/test_03_pydantic_vs_dataclasses.py
"""

# TODO: Import necessary modules
# Hint: You'll need dataclasses, pydantic (BaseModel, Field, model_validator)


# Exercise 1: Convert Dataclass to Pydantic (Basic)
# TODO: Add type hints to this dataclass
class MLModelConfig:
    """
    ML model configuration using dataclass.

    TODO: Add complete Sphinx docstring with :param, :type, :ivar, :vartype
    """

    def __init__(self, model_name, learning_rate, batch_size, epochs):
        self.model_name = model_name
        self.learning_rate = learning_rate
        self.batch_size = batch_size
        self.epochs = epochs


# TODO: Create a Pydantic version of MLModelConfig with validations:
# - model_name: non-empty string
# - learning_rate: float between 0 and 1
# - batch_size: integer greater than 0
# - epochs: integer between 1 and 1000
# class MLModelConfigPydantic(BaseModel):
#     """
#     ML model configuration with Pydantic validation.
#
#     TODO: Add complete Sphinx docstring
#     """
#     pass


# Exercise 2: Dataset Configuration with Custom Validation (Intermediate)
# TODO: Create a Pydantic model for dataset configuration
# Requirements:
# - dataset_name: non-empty string
# - num_samples: positive integer
# - num_features: positive integer
# - train_split: float between 0 and 1
# - test_split: float between 0 and 1
# - Custom validation: train_split + test_split must be <= 1.0
# class DatasetConfig(BaseModel):
#     """
#     Dataset configuration with split validation.
#
#     TODO: Add complete Sphinx docstring
#     """
#     pass


# Exercise 3: Experiment Configuration with JSON Parsing (Advanced)
# TODO: Create a Pydantic model that can parse experiment configurations from JSON
# Requirements:
# - experiment_name: non-empty string
# - model_type: string (e.g., "transformer", "cnn", "rnn")
# - learning_rate: float between 0 and 1
# - batch_size: positive integer
# - epochs: positive integer between 1 and 1000
# - metrics: list of strings (non-empty)
# class ExperimentConfig(BaseModel):
#     """
#     Experiment configuration for ML experiments.
#
#     TODO: Add complete Sphinx docstring
#     """
#     pass


# Helper function for Exercise 3
def parse_experiment_from_json(json_string):
    """
    Parse experiment configuration from JSON string.

    TODO: Add type hints
    TODO: Complete Sphinx docstring with :param, :type, :return, :rtype, :raises

    Example:
        >>> json_str = '{"experiment_name": "test", "model_type": "cnn", ...}'
        >>> config = parse_experiment_from_json(json_str)
        >>> print(config.experiment_name)
        test
    """
    # TODO: Implement JSON parsing using ExperimentConfig
    pass


# Exercise 4: Data Validation for ML Pipeline (Advanced)
# TODO: Create a Pydantic model for validating ML training data
# Requirements:
# - features: list of floats (non-empty)
# - label: integer (0 or 1 for binary classification)
# - sample_id: string (non-empty)
# - timestamp: optional float (Unix timestamp)
# - Custom validation: all features must be finite (not inf or nan)
# class TrainingDataPoint(BaseModel):
#     """
#     Single training data point with validation.
#
#     TODO: Add complete Sphinx docstring
#     """
#     pass


# Helper function for Exercise 4
def validate_training_batch(data_points):
    """
    Validate a batch of training data points.

    TODO: Add type hints
    TODO: Complete Sphinx docstring

    Example:
        >>> data = [{"features": [1.0, 2.0], "label": 1, "sample_id": "s1"}]
        >>> valid_data = validate_training_batch(data)
        >>> len(valid_data)
        1
    """
    # TODO: Implement batch validation
    # Hint: Try to create TrainingDataPoint for each item, collect valid ones
    pass


# Exercise 5: Configuration with Nested Models (Advanced)
# TODO: Create nested Pydantic models for a complete ML pipeline configuration
# Requirements:
# - ModelConfig: model_name (str), model_type (str), parameters (dict)
# - DataConfig: dataset_name (str), batch_size (int > 0), num_workers (int >= 0)
# - TrainingConfig: learning_rate (0 < float < 1), epochs (1 <= int <= 1000), optimizer (str)
# - PipelineConfig: model (ModelConfig), data (DataConfig), training (TrainingConfig)
# class ModelConfig(BaseModel):
#     """
#     Model configuration.
#
#     TODO: Add complete Sphinx docstring
#     """
#     pass


# class DataConfig(BaseModel):
#     """
#     Data loading configuration.
#
#     TODO: Add complete Sphinx docstring
#     """
#     pass


# class TrainingConfig(BaseModel):
#     """
#     Training configuration.
#
#     TODO: Add complete Sphinx docstring
#     """
#     pass


# class PipelineConfig(BaseModel):
#     """
#     Complete ML pipeline configuration with nested models.
#
#     TODO: Add complete Sphinx docstring
#     """
#     pass


def create_default_pipeline_config():
    """
    Create a default pipeline configuration.

    TODO: Add type hints
    TODO: Complete Sphinx docstring

    Example:
        >>> config = create_default_pipeline_config()
        >>> config.model.model_name
        'default_model'
    """
    # TODO: Implement default configuration creation
    pass
