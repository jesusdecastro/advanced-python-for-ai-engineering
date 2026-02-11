"""
Tests for Objects and Data Structures exercises.

Run with: pytest tests/test_objects_data_structures.py -v
"""

import pytest
from dataclasses import is_dataclass
from exercises.objects_data_structures import (
    TrainingConfigFixed,
    ModelPipelineFixed,
    PipelineConfigFixed,
    ProcessingResult,
    DataProcessorFixed,
    ModelMetadata,
    ModelTrainer,
    get_model_accuracy_fixed,
    ExperimentFixed,
)


class TestExercise1DataClass:
    """Test Exercise 1: Convert getters/setters to @dataclass."""
    
    def test_training_config_is_dataclass(self):
        """TrainingConfigFixed should be a dataclass."""
        assert is_dataclass(TrainingConfigFixed), "TrainingConfigFixed should use @dataclass"
    
    def test_training_config_has_fields(self):
        """TrainingConfigFixed should have all required fields."""
        config = TrainingConfigFixed()
        
        assert hasattr(config, 'learning_rate'), "Missing learning_rate field"
        assert hasattr(config, 'batch_size'), "Missing batch_size field"
        assert hasattr(config, 'epochs'), "Missing epochs field"
        assert hasattr(config, 'optimizer'), "Missing optimizer field"
    
    def test_training_config_default_values(self):
        """TrainingConfigFixed should have sensible defaults."""
        config = TrainingConfigFixed()
        
        assert config.learning_rate == 0.001, "Default learning_rate should be 0.001"
        assert config.batch_size == 32, "Default batch_size should be 32"
        assert config.epochs == 100, "Default epochs should be 100"
        assert config.optimizer == "adam", "Default optimizer should be 'adam'"
    
    def test_training_config_direct_access(self):
        """TrainingConfigFixed should allow direct attribute access."""
        config = TrainingConfigFixed(learning_rate=0.01, batch_size=64)
        
        # Direct access (no getters needed)
        assert config.learning_rate == 0.01
        assert config.batch_size == 64
        
        # Direct modification (no setters needed)
        config.learning_rate = 0.001
        assert config.learning_rate == 0.001


class TestExercise2LawOfDemeter:
    """Test Exercise 2: Respect Law of Demeter."""
    
    def test_pipeline_config_hides_structure(self):
        """PipelineConfigFixed should hide internal structure."""
        # Mock storage config
        class MockStorage:
            def is_output_enabled(self):
                return True
            def get_output_path(self):
                return "/path/to/output"
        
        config = PipelineConfigFixed(MockStorage())
        
        # Should expose simple methods, not nested structure
        assert hasattr(config, 'should_save_output'), "Missing should_save_output method"
        assert hasattr(config, 'get_output_path'), "Missing get_output_path method"
        
        # Methods should work
        assert config.should_save_output() is True
        assert config.get_output_path() == "/path/to/output"
    
    def test_pipeline_uses_config_methods(self):
        """ModelPipelineFixed should use config methods, not nested access."""
        class MockConfig:
            def should_save_output(self):
                return True
            def get_output_path(self):
                return "/path/to/output"
        
        pipeline = ModelPipelineFixed(MockConfig())
        
        # Should not raise any errors
        try:
            pipeline.train()
        except NotImplementedError:
            pytest.skip("Implementation not complete yet")
        except AttributeError as e:
            pytest.fail(f"Still accessing nested structure: {e}")


class TestExercise3SeparateHybrid:
    """Test Exercise 3: Separate hybrid into object + data structure."""
    
    def test_processing_result_is_dataclass(self):
        """ProcessingResult should be a dataclass."""
        assert is_dataclass(ProcessingResult), "ProcessingResult should use @dataclass"
    
    def test_processing_result_has_fields(self):
        """ProcessingResult should have all required fields."""
        result = ProcessingResult(
            processed_data=[1, 2, 3],
            metadata={"status": "completed"},
            rows_processed=3
        )
        
        assert result.processed_data == [1, 2, 3]
        assert result.metadata == {"status": "completed"}
        assert result.rows_processed == 3
    
    def test_data_processor_returns_result(self):
        """DataProcessorFixed should return ProcessingResult."""
        processor = DataProcessorFixed()
        raw_data = [1, 2, 3]
        
        try:
            result = processor.process(raw_data)
            
            assert isinstance(result, ProcessingResult), "Should return ProcessingResult"
            assert result.processed_data is not None, "Should have processed_data"
            assert isinstance(result.metadata, dict), "Should have metadata dict"
            assert isinstance(result.rows_processed, int), "Should have rows_processed"
        except NotImplementedError:
            pytest.skip("Implementation not complete yet")
    
    def test_data_processor_hides_internal_state(self):
        """DataProcessorFixed should not expose internal state."""
        processor = DataProcessorFixed()
        
        # Should NOT have public data attributes
        assert not hasattr(processor, 'raw_data'), "Should not expose raw_data"
        assert not hasattr(processor, 'processed_data'), "Should not expose processed_data"
        assert not hasattr(processor, 'metadata'), "Should not expose metadata"


class TestExercise4DTOvsObject:
    """Test Exercise 4: Design DTO vs Object."""
    
    def test_model_metadata_is_dataclass(self):
        """ModelMetadata should be a dataclass (DTO)."""
        assert is_dataclass(ModelMetadata), "ModelMetadata should use @dataclass"
    
    def test_model_metadata_has_fields(self):
        """ModelMetadata should have all required fields."""
        metadata = ModelMetadata(
            model_name="test_model",
            version="1.0",
            accuracy=0.95,
            trained_at="2024-01-01",
            hyperparameters={"lr": 0.001}
        )
        
        assert metadata.model_name == "test_model"
        assert metadata.version == "1.0"
        assert metadata.accuracy == 0.95
        assert metadata.trained_at == "2024-01-01"
        assert metadata.hyperparameters == {"lr": 0.001}
    
    def test_model_trainer_hides_state(self):
        """ModelTrainer should hide internal state."""
        class MockModel:
            pass
        
        class MockOptimizer:
            pass
        
        trainer = ModelTrainer(MockModel(), MockOptimizer())
        
        # Should NOT expose internal state directly
        assert not hasattr(trainer, 'model') or trainer.__dict__.get('model') is None or \
               str(trainer.__dict__.get('model', '')).startswith('_'), \
               "Should use private attribute _model"
        assert not hasattr(trainer, 'optimizer') or trainer.__dict__.get('optimizer') is None or \
               str(trainer.__dict__.get('optimizer', '')).startswith('_'), \
               "Should use private attribute _optimizer"
    
    def test_model_trainer_returns_metadata(self):
        """ModelTrainer.train() should return ModelMetadata."""
        class MockModel:
            pass
        
        class MockOptimizer:
            pass
        
        trainer = ModelTrainer(MockModel(), MockOptimizer())
        
        try:
            result = trainer.train(data=[1, 2, 3], epochs=10)
            
            assert isinstance(result, ModelMetadata), "Should return ModelMetadata"
            assert hasattr(result, 'model_name'), "Metadata should have model_name"
            assert hasattr(result, 'accuracy'), "Metadata should have accuracy"
        except NotImplementedError:
            pytest.skip("Implementation not complete yet")
    
    def test_model_trainer_summary_returns_copy(self):
        """ModelTrainer.get_training_summary() should return copy, not reference."""
        class MockModel:
            pass
        
        class MockOptimizer:
            pass
        
        trainer = ModelTrainer(MockModel(), MockOptimizer())
        
        try:
            summary1 = trainer.get_training_summary()
            summary2 = trainer.get_training_summary()
            
            # Should be different objects (copies)
            assert summary1 is not summary2, "Should return copy, not reference"
            
            # Modifying one should not affect the other
            if isinstance(summary1, dict) and 'loss_history' in summary1:
                summary1['loss_history'].append(999)
                assert 999 not in summary2.get('loss_history', []), \
                    "Modifying returned summary should not affect internal state"
        except NotImplementedError:
            pytest.skip("Implementation not complete yet")


class TestExercise5LawOfDemeterFunction:
    """Test Exercise 5: Fix Law of Demeter violation in function."""
    
    def test_get_accuracy_uses_single_call(self):
        """get_model_accuracy_fixed should use single method call."""
        class MockExperiment:
            def get_accuracy(self):
                return 0.95
        
        experiment = MockExperiment()
        
        try:
            accuracy = get_model_accuracy_fixed(experiment)
            
            assert accuracy == 0.95, "Should return correct accuracy"
            assert isinstance(accuracy, float), "Should return float"
        except NotImplementedError:
            pytest.skip("Implementation not complete yet")
    
    def test_experiment_fixed_hides_structure(self):
        """ExperimentFixed should hide internal structure."""
        class MockResults:
            def get_metrics(self):
                class MockMetrics:
                    def get_accuracy(self):
                        class MockAccuracy:
                            def get_value(self):
                                return 0.95
                        return MockAccuracy()
                return MockMetrics()
        
        experiment = ExperimentFixed(MockResults())
        
        # Should expose simple method
        assert hasattr(experiment, 'get_accuracy'), "Missing get_accuracy method"
        
        try:
            accuracy = experiment.get_accuracy()
            assert accuracy == 0.95, "Should return correct accuracy"
        except NotImplementedError:
            pytest.skip("Implementation not complete yet")


class TestCodeQuality:
    """Test code quality aspects."""
    
    def test_all_classes_have_docstrings(self):
        """All classes should have docstrings."""
        classes = [
            TrainingConfigFixed,
            ModelPipelineFixed,
            PipelineConfigFixed,
            ProcessingResult,
            DataProcessorFixed,
            ModelMetadata,
            ModelTrainer,
            ExperimentFixed,
        ]
        
        for cls in classes:
            assert cls.__doc__ is not None, f"{cls.__name__} should have docstring"
            assert len(cls.__doc__.strip()) > 0, f"{cls.__name__} docstring should not be empty"
    
    def test_dataclasses_are_used_appropriately(self):
        """Data structures should use @dataclass."""
        data_structures = [TrainingConfigFixed, ProcessingResult, ModelMetadata]
        
        for cls in data_structures:
            assert is_dataclass(cls), f"{cls.__name__} should be a dataclass"
    
    def test_objects_hide_internal_state(self):
        """Objects should use private attributes."""
        # This is a guideline test - checks if private attributes are used
        processor = DataProcessorFixed()
        trainer_dict = ModelTrainer.__init__.__code__.co_names
        
        # Check if private attributes are mentioned in __init__
        has_private = any(name.startswith('_') for name in trainer_dict)
        assert has_private, "Objects should use private attributes (starting with _)"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
