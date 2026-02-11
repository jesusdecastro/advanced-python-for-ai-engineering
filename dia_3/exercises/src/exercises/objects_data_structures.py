"""
Objects and Data Structures Exercises - Day 3.

Practice distinguishing between objects and data structures, applying Law of Demeter,
and avoiding hybrid structures.

Your task:
1. Convert classes with getters/setters to proper data structures
2. Refactor Law of Demeter violations
3. Separate hybrid structures into object + data structure
4. Design appropriate DTOs vs objects with encapsulation
5. Complete the docstrings with :param, :type, :return, :rtype annotations
6. Ensure your code passes Ruff linting

Run the tests with: pytest tests/test_objects_data_structures.py
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


# Exercise 1: Convert Getters/Setters to Data Structure
# TODO: Refactor this class to use @dataclass
class TrainingConfig:
    """
    Training configuration - currently has unnecessary getters/setters.
    
    This should be a simple data structure, not an object with behavior.
    Refactor to use @dataclass.
    """
    
    def __init__(self):
        self._learning_rate = 0.001
        self._batch_size = 32
        self._epochs = 100
        self._optimizer = "adam"
    
    def get_learning_rate(self):
        return self._learning_rate
    
    def set_learning_rate(self, value):
        self._learning_rate = value
    
    def get_batch_size(self):
        return self._batch_size
    
    def set_batch_size(self, value):
        self._batch_size = value
    
    def get_epochs(self):
        return self._epochs
    
    def set_epochs(self, value):
        self._epochs = value
    
    def get_optimizer(self):
        return self._optimizer
    
    def set_optimizer(self, value):
        self._optimizer = value


# TODO: Create a proper @dataclass version
# Hint: Use @dataclass decorator and define fields with type hints
# Hint: Add default values for each field
@dataclass
class TrainingConfigFixed:
    """
    Fixed training configuration as a proper data structure.
    
    TODO: Add docstring with field descriptions
    """
    pass  # Replace with proper implementation


# Exercise 2: Law of Demeter Violation
# TODO: Refactor to respect Law of Demeter
class ModelPipeline:
    """
    ML pipeline that violates Law of Demeter.
    
    Currently accesses deep nested structure. Refactor to use proper encapsulation.
    """
    
    def __init__(self, config):
        self.config = config
    
    def train(self):
        """
        Train model - violates Law of Demeter.
        
        TODO: Refactor to not access nested structure directly
        """
        # Violation: accessing config.storage.output.path.full_path
        output_path = self.config.get_storage().get_output().get_path().get_full_path()
        
        # Violation: checking nested enabled flag
        if self.config.get_storage().get_output().is_enabled():
            self._save_results(output_path)
    
    def _save_results(self, path: str):
        """Save training results."""
        pass  # Placeholder


# TODO: Create fixed version that respects Law of Demeter
class ModelPipelineFixed:
    """
    Fixed ML pipeline that respects Law of Demeter.
    
    TODO: Add proper docstring
    """
    
    def __init__(self, config):
        """
        Initialize pipeline with configuration.
        
        TODO: Add :param, :type annotations
        """
        self.config = config
    
    def train(self):
        """
        Train model - respects Law of Demeter.
        
        TODO: Implement using config methods that hide internal structure
        Hint: Config should expose should_save_output() and get_output_path()
        """
        pass  # Replace with proper implementation


# TODO: Create supporting config class that hides structure
class PipelineConfigFixed:
    """
    Configuration that hides internal structure.
    
    TODO: Add proper docstring
    """
    
    def __init__(self, storage_config):
        """
        Initialize configuration.
        
        TODO: Add :param, :type annotations
        """
        self._storage = storage_config
    
    def should_save_output(self) -> bool:
        """
        Check if output should be saved.
        
        TODO: Implement - hide how this is determined
        """
        pass
    
    def get_output_path(self) -> str:
        """
        Get output path.
        
        TODO: Implement - hide how path is obtained
        """
        pass


# Exercise 3: Separate Hybrid into Object + Data Structure
# TODO: Separate this hybrid into proper object and data structure
class DataProcessor:
    """
    Hybrid class - mixes public data with behavior.
    
    This is confusing. Separate into:
    1. ProcessingResult (data structure with @dataclass)
    2. DataProcessor (object with behavior)
    """
    
    def __init__(self):
        # Public data (like data structure)
        self.raw_data = None
        self.processed_data = None
        self.metadata = {}
        self.rows_processed = 0
        
        # Private state (like object)
        self._transformers = []
    
    def process(self):
        """Process data - depends on public state."""
        if self.raw_data is None:
            raise ValueError("Set raw_data first")
        
        self.processed_data = self._transform(self.raw_data)
        self.rows_processed = len(self.processed_data)
        self.metadata = {"status": "completed"}
    
    def _transform(self, data):
        """Transform data."""
        return data  # Placeholder


# TODO: Create data structure for results
@dataclass
class ProcessingResult:
    """
    Result of data processing - pure data structure.
    
    TODO: Add fields:
    - processed_data: Any
    - metadata: Dict[str, Any]
    - rows_processed: int
    
    TODO: Add proper docstring with field descriptions
    """
    pass  # Replace with proper implementation


# TODO: Create object for processing behavior
class DataProcessorFixed:
    """
    Data processor with proper encapsulation.
    
    TODO: Add proper docstring
    """
    
    def __init__(self):
        """
        Initialize processor.
        
        TODO: Add docstring
        """
        self._transformers = []
    
    def process(self, raw_data: Any) -> ProcessingResult:
        """
        Process data and return result.
        
        TODO: Implement - return ProcessingResult
        TODO: Add :param, :type, :return, :rtype annotations
        """
        pass  # Replace with proper implementation
    
    def _transform(self, data: Any) -> Any:
        """
        Transform data.
        
        TODO: Add :param, :type, :return, :rtype annotations
        """
        return data  # Placeholder


# Exercise 4: Design DTO vs Object with Encapsulation
# TODO: Implement both a DTO and an object for model training

# Part A: Create DTO for model metadata
@dataclass
class ModelMetadata:
    """
    DTO for model metadata - simple data transfer.
    
    TODO: Add fields:
    - model_name: str
    - version: str
    - accuracy: float
    - trained_at: str
    - hyperparameters: Dict[str, Any]
    
    TODO: Add proper docstring
    """
    pass  # Replace with proper implementation


# Part B: Create object for model trainer with encapsulation
class ModelTrainer:
    """
    Model trainer with proper encapsulation.
    
    Should hide internal state and expose only behavior.
    
    TODO: Implement with:
    - Private attributes for model, optimizer, history
    - Public method: train(data, epochs) -> ModelMetadata
    - Public method: get_training_summary() -> Dict
    - Private method: _train_epoch(data) -> float
    """
    
    def __init__(self, model, optimizer):
        """
        Initialize trainer.
        
        TODO: Add :param, :type annotations
        TODO: Initialize private attributes
        """
        pass  # Replace with proper implementation
    
    def train(self, data: Any, epochs: int) -> ModelMetadata:
        """
        Train model and return metadata.
        
        TODO: Implement training loop
        TODO: Return ModelMetadata with results
        TODO: Add :param, :type, :return, :rtype annotations
        """
        pass  # Replace with proper implementation
    
    def get_training_summary(self) -> Dict[str, Any]:
        """
        Get summary of training progress.
        
        Should return COPY of internal state, not reference.
        
        TODO: Implement
        TODO: Add :return, :rtype annotations
        """
        pass  # Replace with proper implementation
    
    def _train_epoch(self, data: Any) -> float:
        """
        Train one epoch (private method).
        
        TODO: Add :param, :type, :return, :rtype annotations
        """
        return 0.5  # Placeholder


# Exercise 5: Identify and Fix Law of Demeter Violation
# TODO: Fix this function to respect Law of Demeter
def get_model_accuracy(experiment):
    """
    Get model accuracy - currently violates Law of Demeter.
    
    Current implementation:
    accuracy = experiment.get_results().get_metrics().get_accuracy().get_value()
    
    TODO: Refactor to use a single method call on experiment
    TODO: Add :param, :type, :return, :rtype annotations
    
    :param experiment: Experiment object
    :return: Accuracy value
    """
    # Violation: chain of calls accessing internal structure
    accuracy = experiment.get_results().get_metrics().get_accuracy().get_value()
    return accuracy


# TODO: Create fixed version
def get_model_accuracy_fixed(experiment) -> float:
    """
    Get model accuracy - respects Law of Demeter.
    
    TODO: Implement using single method call
    TODO: Add :param, :type, :return, :rtype annotations
    
    Hint: experiment should expose get_accuracy() directly
    """
    pass  # Replace with proper implementation


# TODO: Create supporting Experiment class
class ExperimentFixed:
    """
    Experiment class that hides internal structure.
    
    TODO: Add proper docstring
    """
    
    def __init__(self, results):
        """
        Initialize experiment.
        
        TODO: Add :param, :type annotations
        """
        self._results = results
    
    def get_accuracy(self) -> float:
        """
        Get accuracy directly - hides internal structure.
        
        TODO: Implement - hide how accuracy is obtained
        TODO: Add :return, :rtype annotations
        """
        pass  # Replace with proper implementation
