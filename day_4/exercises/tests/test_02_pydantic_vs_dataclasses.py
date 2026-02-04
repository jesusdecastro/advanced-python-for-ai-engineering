"""
Tests for Pydantic vs Dataclasses exercises.

This test module validates the exercise implementations for dataclasses
and Pydantic models, including validation, JSON parsing, and nested models.
"""

# Import the exercise module
# Note: Students need to complete the exercises for these tests to pass
# Using importlib to handle module name starting with number
import importlib.util
import json
import math
import sys
from pathlib import Path

import pytest
from pydantic import ValidationError

try:
    # Dynamically import the exercise module
    module_path = Path(__file__).parent.parent / "03_pydantic_vs_dataclasses.py"
    spec = importlib.util.spec_from_file_location("pydantic_vs_dataclasses", module_path)
    if spec and spec.loader:
        exercise_module = importlib.util.module_from_spec(spec)
        sys.modules["pydantic_vs_dataclasses"] = exercise_module
        spec.loader.exec_module(exercise_module)

        # Import the required classes and functions
        DataConfig = exercise_module.DataConfig
        DatasetConfig = exercise_module.DatasetConfig
        ExperimentConfig = exercise_module.ExperimentConfig
        MLModelConfig = exercise_module.MLModelConfig
        MLModelConfigPydantic = exercise_module.MLModelConfigPydantic
        ModelConfig = exercise_module.ModelConfig
        PipelineConfig = exercise_module.PipelineConfig
        TrainingConfig = exercise_module.TrainingConfig
        TrainingDataPoint = exercise_module.TrainingDataPoint
        create_default_pipeline_config = exercise_module.create_default_pipeline_config
        parse_experiment_from_json = exercise_module.parse_experiment_from_json
        validate_training_batch = exercise_module.validate_training_batch
    else:
        raise ImportError("Could not load module spec")
except (ImportError, AttributeError) as e:
    # If imports fail, tests will be skipped
    pytest.skip(f"Exercise module not yet implemented: {e}", allow_module_level=True)


# ============================================================================
# Exercise 1: MLModelConfig Tests
# ============================================================================


class TestMLModelConfig:
    """Tests for basic dataclass MLModelConfig."""

    def test_mlmodelconfig_creation(self):
        """Test creating MLModelConfig with valid parameters."""
        config = MLModelConfig(
            model_name="ResNet50", learning_rate=0.001, batch_size=32, epochs=100
        )
        assert config.model_name == "ResNet50"
        assert config.learning_rate == 0.001
        assert config.batch_size == 32
        assert config.epochs == 100

    def test_mlmodelconfig_attributes(self):
        """Test MLModelConfig has all required attributes."""
        config = MLModelConfig(model_name="BERT", learning_rate=0.0001, batch_size=16, epochs=50)
        assert hasattr(config, "model_name")
        assert hasattr(config, "learning_rate")
        assert hasattr(config, "batch_size")
        assert hasattr(config, "epochs")


class TestMLModelConfigPydantic:
    """Tests for Pydantic version of MLModelConfig with validation."""

    def test_valid_config(self):
        """Test creating valid Pydantic config."""
        config = MLModelConfigPydantic(
            model_name="ResNet50", learning_rate=0.001, batch_size=32, epochs=100
        )
        assert config.model_name == "ResNet50"
        assert config.learning_rate == 0.001
        assert config.batch_size == 32
        assert config.epochs == 100

    def test_empty_model_name_fails(self):
        """Test that empty model name raises validation error."""
        with pytest.raises(ValidationError):
            MLModelConfigPydantic(model_name="", learning_rate=0.001, batch_size=32, epochs=100)

    def test_learning_rate_too_low_fails(self):
        """Test that learning rate below 0 raises validation error."""
        with pytest.raises(ValidationError):
            MLModelConfigPydantic(
                model_name="ResNet50", learning_rate=-0.1, batch_size=32, epochs=100
            )

    def test_learning_rate_too_high_fails(self):
        """Test that learning rate above 1 raises validation error."""
        with pytest.raises(ValidationError):
            MLModelConfigPydantic(
                model_name="ResNet50", learning_rate=1.5, batch_size=32, epochs=100
            )

    def test_batch_size_zero_fails(self):
        """Test that batch size of 0 raises validation error."""
        with pytest.raises(ValidationError):
            MLModelConfigPydantic(
                model_name="ResNet50", learning_rate=0.001, batch_size=0, epochs=100
            )

    def test_batch_size_negative_fails(self):
        """Test that negative batch size raises validation error."""
        with pytest.raises(ValidationError):
            MLModelConfigPydantic(
                model_name="ResNet50", learning_rate=0.001, batch_size=-32, epochs=100
            )

    def test_epochs_too_low_fails(self):
        """Test that epochs below 1 raises validation error."""
        with pytest.raises(ValidationError):
            MLModelConfigPydantic(
                model_name="ResNet50", learning_rate=0.001, batch_size=32, epochs=0
            )

    def test_epochs_too_high_fails(self):
        """Test that epochs above 1000 raises validation error."""
        with pytest.raises(ValidationError):
            MLModelConfigPydantic(
                model_name="ResNet50", learning_rate=0.001, batch_size=32, epochs=1001
            )

    def test_boundary_values(self):
        """Test boundary values for all fields."""
        # Minimum valid values
        config_min = MLModelConfigPydantic(
            model_name="A", learning_rate=0.0, batch_size=1, epochs=1
        )
        assert config_min.learning_rate == 0.0
        assert config_min.epochs == 1

        # Maximum valid values
        config_max = MLModelConfigPydantic(
            model_name="VeryLongModelName", learning_rate=1.0, batch_size=1024, epochs=1000
        )
        assert config_max.learning_rate == 1.0
        assert config_max.epochs == 1000


# ============================================================================
# Exercise 2: DatasetConfig Tests
# ============================================================================


class TestDatasetConfig:
    """Tests for DatasetConfig with custom split validation."""

    def test_valid_dataset_config(self):
        """Test creating valid dataset configuration."""
        config = DatasetConfig(
            dataset_name="MNIST",
            num_samples=60000,
            num_features=784,
            train_split=0.8,
            test_split=0.2,
        )
        assert config.dataset_name == "MNIST"
        assert config.num_samples == 60000
        assert config.num_features == 784
        assert config.train_split == 0.8
        assert config.test_split == 0.2

    def test_splits_sum_to_one(self):
        """Test that train and test splits can sum to exactly 1.0."""
        config = DatasetConfig(
            dataset_name="CIFAR10",
            num_samples=50000,
            num_features=3072,
            train_split=0.7,
            test_split=0.3,
        )
        assert config.train_split + config.test_split == 1.0

    def test_splits_sum_less_than_one(self):
        """Test that splits can sum to less than 1.0 (validation split)."""
        config = DatasetConfig(
            dataset_name="ImageNet",
            num_samples=1000000,
            num_features=150528,
            train_split=0.7,
            test_split=0.2,
        )
        assert config.train_split + config.test_split < 1.0

    def test_splits_sum_exceeds_one_fails(self):
        """Test that splits summing to more than 1.0 raises validation error."""
        with pytest.raises(ValidationError):
            DatasetConfig(
                dataset_name="MNIST",
                num_samples=60000,
                num_features=784,
                train_split=0.8,
                test_split=0.5,
            )

    def test_empty_dataset_name_fails(self):
        """Test that empty dataset name raises validation error."""
        with pytest.raises(ValidationError):
            DatasetConfig(
                dataset_name="",
                num_samples=60000,
                num_features=784,
                train_split=0.8,
                test_split=0.2,
            )

    def test_negative_num_samples_fails(self):
        """Test that negative num_samples raises validation error."""
        with pytest.raises(ValidationError):
            DatasetConfig(
                dataset_name="MNIST",
                num_samples=-100,
                num_features=784,
                train_split=0.8,
                test_split=0.2,
            )

    def test_zero_num_features_fails(self):
        """Test that zero num_features raises validation error."""
        with pytest.raises(ValidationError):
            DatasetConfig(
                dataset_name="MNIST",
                num_samples=60000,
                num_features=0,
                train_split=0.8,
                test_split=0.2,
            )

    def test_train_split_out_of_range_fails(self):
        """Test that train_split outside [0, 1] raises validation error."""
        with pytest.raises(ValidationError):
            DatasetConfig(
                dataset_name="MNIST",
                num_samples=60000,
                num_features=784,
                train_split=1.5,
                test_split=0.2,
            )

    def test_test_split_negative_fails(self):
        """Test that negative test_split raises validation error."""
        with pytest.raises(ValidationError):
            DatasetConfig(
                dataset_name="MNIST",
                num_samples=60000,
                num_features=784,
                train_split=0.8,
                test_split=-0.1,
            )


# ============================================================================
# Exercise 3: ExperimentConfig and JSON Parsing Tests
# ============================================================================


class TestExperimentConfig:
    """Tests for ExperimentConfig model."""

    def test_valid_experiment_config(self):
        """Test creating valid experiment configuration."""
        config = ExperimentConfig(
            experiment_name="exp_001",
            model_type="transformer",
            learning_rate=0.0001,
            batch_size=64,
            epochs=50,
            metrics=["accuracy", "f1_score", "precision"],
        )
        assert config.experiment_name == "exp_001"
        assert config.model_type == "transformer"
        assert config.learning_rate == 0.0001
        assert config.batch_size == 64
        assert config.epochs == 50
        assert len(config.metrics) == 3

    def test_empty_experiment_name_fails(self):
        """Test that empty experiment name raises validation error."""
        with pytest.raises(ValidationError):
            ExperimentConfig(
                experiment_name="",
                model_type="cnn",
                learning_rate=0.001,
                batch_size=32,
                epochs=100,
                metrics=["accuracy"],
            )

    def test_empty_metrics_list_fails(self):
        """Test that empty metrics list raises validation error."""
        with pytest.raises(ValidationError):
            ExperimentConfig(
                experiment_name="exp_002",
                model_type="rnn",
                learning_rate=0.001,
                batch_size=32,
                epochs=100,
                metrics=[],
            )

    def test_invalid_learning_rate_fails(self):
        """Test that invalid learning rate raises validation error."""
        with pytest.raises(ValidationError):
            ExperimentConfig(
                experiment_name="exp_003",
                model_type="cnn",
                learning_rate=2.0,
                batch_size=32,
                epochs=100,
                metrics=["accuracy"],
            )

    def test_invalid_epochs_fails(self):
        """Test that invalid epochs raises validation error."""
        with pytest.raises(ValidationError):
            ExperimentConfig(
                experiment_name="exp_004",
                model_type="transformer",
                learning_rate=0.001,
                batch_size=32,
                epochs=1500,
                metrics=["accuracy"],
            )


class TestParseExperimentFromJson:
    """Tests for JSON parsing functionality."""

    def test_parse_valid_json(self):
        """Test parsing valid JSON string to ExperimentConfig."""
        json_str = json.dumps(
            {
                "experiment_name": "exp_json_001",
                "model_type": "cnn",
                "learning_rate": 0.001,
                "batch_size": 32,
                "epochs": 100,
                "metrics": ["accuracy", "loss"],
            }
        )
        config = parse_experiment_from_json(json_str)
        assert config.experiment_name == "exp_json_001"
        assert config.model_type == "cnn"
        assert config.learning_rate == 0.001
        assert config.batch_size == 32
        assert config.epochs == 100
        assert config.metrics == ["accuracy", "loss"]

    def test_parse_json_with_validation_error(self):
        """Test that parsing invalid JSON raises validation error."""
        json_str = json.dumps(
            {
                "experiment_name": "",  # Invalid: empty string
                "model_type": "cnn",
                "learning_rate": 0.001,
                "batch_size": 32,
                "epochs": 100,
                "metrics": ["accuracy"],
            }
        )
        with pytest.raises(ValidationError):
            parse_experiment_from_json(json_str)

    def test_parse_malformed_json_fails(self):
        """Test that malformed JSON string raises error."""
        json_str = "{'invalid': json}"  # Not valid JSON
        with pytest.raises((json.JSONDecodeError, ValidationError)):
            parse_experiment_from_json(json_str)

    def test_parse_json_missing_field_fails(self):
        """Test that JSON missing required field raises validation error."""
        json_str = json.dumps(
            {
                "experiment_name": "exp_incomplete",
                "model_type": "rnn",
                # Missing learning_rate, batch_size, epochs, metrics
            }
        )
        with pytest.raises(ValidationError):
            parse_experiment_from_json(json_str)


# ============================================================================
# Exercise 4: TrainingDataPoint and Batch Validation Tests
# ============================================================================


class TestTrainingDataPoint:
    """Tests for TrainingDataPoint with feature validation."""

    def test_valid_training_data_point(self):
        """Test creating valid training data point."""
        data = TrainingDataPoint(features=[1.0, 2.5, 3.7, 4.2], label=1, sample_id="sample_001")
        assert len(data.features) == 4
        assert data.label == 1
        assert data.sample_id == "sample_001"
        assert data.timestamp is None

    def test_training_data_with_timestamp(self):
        """Test creating training data point with timestamp."""
        data = TrainingDataPoint(
            features=[1.0, 2.0], label=0, sample_id="sample_002", timestamp=1234567890.0
        )
        assert data.timestamp == 1234567890.0

    def test_empty_features_fails(self):
        """Test that empty features list raises validation error."""
        with pytest.raises(ValidationError):
            TrainingDataPoint(features=[], label=1, sample_id="sample_003")

    def test_empty_sample_id_fails(self):
        """Test that empty sample_id raises validation error."""
        with pytest.raises(ValidationError):
            TrainingDataPoint(features=[1.0, 2.0], label=1, sample_id="")

    def test_invalid_label_fails(self):
        """Test that label not in {0, 1} raises validation error."""
        with pytest.raises(ValidationError):
            TrainingDataPoint(features=[1.0, 2.0], label=2, sample_id="sample_004")

    def test_infinite_feature_fails(self):
        """Test that infinite feature value raises validation error."""
        with pytest.raises(ValidationError):
            TrainingDataPoint(features=[1.0, float("inf"), 3.0], label=1, sample_id="sample_005")

    def test_nan_feature_fails(self):
        """Test that NaN feature value raises validation error."""
        with pytest.raises(ValidationError):
            TrainingDataPoint(features=[1.0, float("nan"), 3.0], label=0, sample_id="sample_006")

    def test_negative_infinity_feature_fails(self):
        """Test that negative infinity feature raises validation error."""
        with pytest.raises(ValidationError):
            TrainingDataPoint(features=[1.0, float("-inf"), 3.0], label=1, sample_id="sample_007")

    def test_all_finite_features_pass(self):
        """Test that all finite features pass validation."""
        data = TrainingDataPoint(
            features=[-100.0, 0.0, 100.0, 1e-10, 1e10], label=0, sample_id="sample_008"
        )
        assert all(math.isfinite(f) for f in data.features)


class TestValidateTrainingBatch:
    """Tests for batch validation functionality."""

    def test_validate_all_valid_batch(self):
        """Test validating batch with all valid data points."""
        data_points = [
            {"features": [1.0, 2.0], "label": 1, "sample_id": "s1"},
            {"features": [3.0, 4.0], "label": 0, "sample_id": "s2"},
            {"features": [5.0, 6.0], "label": 1, "sample_id": "s3"},
        ]
        valid_data = validate_training_batch(data_points)
        assert len(valid_data) == 3
        assert all(isinstance(d, TrainingDataPoint) for d in valid_data)

    def test_validate_batch_with_invalid_data(self):
        """Test validating batch with some invalid data points."""
        data_points = [
            {"features": [1.0, 2.0], "label": 1, "sample_id": "s1"},  # Valid
            {"features": [float("inf"), 4.0], "label": 0, "sample_id": "s2"},  # Invalid
            {"features": [5.0, 6.0], "label": 1, "sample_id": "s3"},  # Valid
            {"features": [], "label": 1, "sample_id": "s4"},  # Invalid: empty features
        ]
        valid_data = validate_training_batch(data_points)
        assert len(valid_data) == 2
        assert valid_data[0].sample_id == "s1"
        assert valid_data[1].sample_id == "s3"

    def test_validate_empty_batch(self):
        """Test validating empty batch returns empty list."""
        valid_data = validate_training_batch([])
        assert len(valid_data) == 0

    def test_validate_batch_all_invalid(self):
        """Test validating batch with all invalid data returns empty list."""
        data_points = [
            {"features": [float("nan")], "label": 1, "sample_id": "s1"},
            {"features": [], "label": 0, "sample_id": "s2"},
            {"features": [1.0], "label": 5, "sample_id": "s3"},  # Invalid label
        ]
        valid_data = validate_training_batch(data_points)
        assert len(valid_data) == 0


# ============================================================================
# Exercise 5: Nested Models Tests
# ============================================================================


class TestModelConfig:
    """Tests for ModelConfig nested model."""

    def test_valid_model_config(self):
        """Test creating valid model configuration."""
        config = ModelConfig(
            model_name="ResNet50",
            model_type="cnn",
            parameters={"layers": 50, "pretrained": True},
        )
        assert config.model_name == "ResNet50"
        assert config.model_type == "cnn"
        assert config.parameters["layers"] == 50


class TestDataConfig:
    """Tests for DataConfig nested model."""

    def test_valid_data_config(self):
        """Test creating valid data configuration."""
        config = DataConfig(dataset_name="CIFAR10", batch_size=64, num_workers=4)
        assert config.dataset_name == "CIFAR10"
        assert config.batch_size == 64
        assert config.num_workers == 4

    def test_batch_size_zero_fails(self):
        """Test that batch_size of 0 raises validation error."""
        with pytest.raises(ValidationError):
            DataConfig(dataset_name="MNIST", batch_size=0, num_workers=2)

    def test_negative_num_workers_fails(self):
        """Test that negative num_workers raises validation error."""
        with pytest.raises(ValidationError):
            DataConfig(dataset_name="MNIST", batch_size=32, num_workers=-1)

    def test_zero_num_workers_allowed(self):
        """Test that num_workers of 0 is allowed."""
        config = DataConfig(dataset_name="MNIST", batch_size=32, num_workers=0)
        assert config.num_workers == 0


class TestTrainingConfig:
    """Tests for TrainingConfig nested model."""

    def test_valid_training_config(self):
        """Test creating valid training configuration."""
        config = TrainingConfig(learning_rate=0.001, epochs=100, optimizer="adam")
        assert config.learning_rate == 0.001
        assert config.epochs == 100
        assert config.optimizer == "adam"

    def test_learning_rate_boundary_fails(self):
        """Test that learning_rate at boundaries raises validation error."""
        with pytest.raises(ValidationError):
            TrainingConfig(learning_rate=0.0, epochs=100, optimizer="sgd")

        with pytest.raises(ValidationError):
            TrainingConfig(learning_rate=1.0, epochs=100, optimizer="sgd")

    def test_epochs_out_of_range_fails(self):
        """Test that epochs outside [1, 1000] raises validation error."""
        with pytest.raises(ValidationError):
            TrainingConfig(learning_rate=0.001, epochs=0, optimizer="adam")

        with pytest.raises(ValidationError):
            TrainingConfig(learning_rate=0.001, epochs=1001, optimizer="adam")


class TestPipelineConfig:
    """Tests for complete PipelineConfig with nested models."""

    def test_valid_pipeline_config(self):
        """Test creating valid complete pipeline configuration."""
        model_cfg = ModelConfig(
            model_name="BERT", model_type="transformer", parameters={"hidden_size": 768}
        )
        data_cfg = DataConfig(dataset_name="GLUE", batch_size=32, num_workers=4)
        training_cfg = TrainingConfig(learning_rate=0.0001, epochs=10, optimizer="adamw")

        pipeline = PipelineConfig(model=model_cfg, data=data_cfg, training=training_cfg)

        assert pipeline.model.model_name == "BERT"
        assert pipeline.data.batch_size == 32
        assert pipeline.training.epochs == 10

    def test_pipeline_config_nested_validation(self):
        """Test that nested model validation works in pipeline."""
        model_cfg = ModelConfig(model_name="ResNet", model_type="cnn", parameters={"layers": 18})
        data_cfg = DataConfig(dataset_name="ImageNet", batch_size=128, num_workers=8)

        # Invalid training config (epochs too high)
        with pytest.raises(ValidationError):
            training_cfg = TrainingConfig(learning_rate=0.01, epochs=2000, optimizer="sgd")
            PipelineConfig(model=model_cfg, data=data_cfg, training=training_cfg)


class TestCreateDefaultPipelineConfig:
    """Tests for default pipeline configuration creation."""

    def test_create_default_config(self):
        """Test creating default pipeline configuration."""
        config = create_default_pipeline_config()
        assert isinstance(config, PipelineConfig)
        assert isinstance(config.model, ModelConfig)
        assert isinstance(config.data, DataConfig)
        assert isinstance(config.training, TrainingConfig)

    def test_default_config_has_valid_values(self):
        """Test that default configuration has valid values."""
        config = create_default_pipeline_config()
        assert config.model.model_name == "default_model"
        assert config.data.batch_size > 0
        assert 0 < config.training.learning_rate < 1
        assert 1 <= config.training.epochs <= 1000

    def test_default_config_is_valid(self):
        """Test that default configuration passes all validations."""
        config = create_default_pipeline_config()
        # If this doesn't raise, the config is valid
        assert config is not None


# ============================================================================
# Integration Tests
# ============================================================================


class TestIntegration:
    """Integration tests combining multiple exercises."""

    def test_json_to_pydantic_to_dict(self):
        """Test round-trip: JSON -> Pydantic -> dict."""
        original_data = {
            "experiment_name": "integration_test",
            "model_type": "transformer",
            "learning_rate": 0.0001,
            "batch_size": 64,
            "epochs": 50,
            "metrics": ["accuracy", "f1"],
        }
        json_str = json.dumps(original_data)
        config = parse_experiment_from_json(json_str)
        result_dict = config.model_dump()

        assert result_dict["experiment_name"] == original_data["experiment_name"]
        assert result_dict["model_type"] == original_data["model_type"]
        assert result_dict["learning_rate"] == original_data["learning_rate"]

    def test_nested_config_serialization(self):
        """Test that nested configuration can be serialized."""
        config = create_default_pipeline_config()
        config_dict = config.model_dump()

        assert "model" in config_dict
        assert "data" in config_dict
        assert "training" in config_dict
        assert isinstance(config_dict["model"], dict)
        assert isinstance(config_dict["data"], dict)
        assert isinstance(config_dict["training"], dict)

    def test_batch_validation_with_mixed_data(self):
        """Test batch validation with various edge cases."""
        data_points = [
            # Valid points
            {"features": [1.0, 2.0, 3.0], "label": 1, "sample_id": "valid_1"},
            {
                "features": [0.0, 0.0, 0.0],
                "label": 0,
                "sample_id": "valid_2",
                "timestamp": 1234567890.0,
            },
            # Invalid points
            {"features": [float("inf"), 2.0], "label": 1, "sample_id": "invalid_1"},
            {"features": [1.0, float("nan")], "label": 0, "sample_id": "invalid_2"},
            {"features": [], "label": 1, "sample_id": "invalid_3"},
            {"features": [1.0], "label": 3, "sample_id": "invalid_4"},  # Bad label
        ]

        valid_data = validate_training_batch(data_points)
        assert len(valid_data) == 2
        assert all(isinstance(d, TrainingDataPoint) for d in valid_data)
        assert valid_data[0].sample_id == "valid_1"
        assert valid_data[1].sample_id == "valid_2"
