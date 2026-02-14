"""Tests for defensive programming exercises."""

import pytest
from exercises.defensive import (
    MIN_AGE,
    MAX_AGE,
    MIN_HEIGHT,
    MAX_HEIGHT,
    MIN_SCORE,
    MAX_SCORE,
    calculate_bmi,
    get_user_age,
    process_transaction,
    parse_numeric_value,
    find_user_by_id,
    calculate_average_score,
    normalize_dataset,
)


class TestConstants:
    """Test that constants are defined."""

    def test_constants_exist(self):
        """Should have all required constants defined."""
        assert MIN_AGE == 0
        assert MAX_AGE == 150
        assert MIN_HEIGHT == 0.5
        assert MAX_HEIGHT == 2.5
        assert MIN_SCORE == 0
        assert MAX_SCORE == 100


class TestCalculateBMI:
    """Test calculate_bmi function."""

    def test_calculates_bmi_correctly(self):
        """Should calculate BMI correctly."""
        assert calculate_bmi(70, 1.75) == 22.86

    def test_raises_type_error_for_non_numeric_weight(self):
        """Should raise TypeError for non-numeric weight."""
        with pytest.raises(TypeError):
            calculate_bmi("70", 1.75)

    def test_raises_type_error_for_non_numeric_height(self):
        """Should raise TypeError for non-numeric height."""
        with pytest.raises(TypeError):
            calculate_bmi(70, "1.75")

    def test_raises_value_error_for_negative_weight(self):
        """Should raise ValueError for negative weight."""
        with pytest.raises(ValueError):
            calculate_bmi(-70, 1.75)

    def test_raises_value_error_for_negative_height(self):
        """Should raise ValueError for negative height."""
        with pytest.raises(ValueError):
            calculate_bmi(70, -1.75)

    def test_raises_value_error_for_unreasonable_height(self):
        """Should raise ValueError for height out of range."""
        with pytest.raises(ValueError):
            calculate_bmi(70, 0.3)  # Too short
        
        with pytest.raises(ValueError):
            calculate_bmi(70, 3.0)  # Too tall

    def test_handles_int_and_float_inputs(self):
        """Should handle both int and float inputs."""
        assert calculate_bmi(70, 1.75) == 22.86
        assert calculate_bmi(70.0, 1.75) == 22.86
        assert isinstance(calculate_bmi(70, 2), float)


class TestGetUserAge:
    """Test get_user_age function."""

    def test_extracts_age_from_valid_data(self):
        """Should extract age from user data."""
        assert get_user_age({'name': 'Alice', 'age': 30}) == 30

    def test_raises_type_error_for_non_dict(self):
        """Should raise TypeError if user_data is not a dict."""
        with pytest.raises(TypeError):
            get_user_age("not a dict")

    def test_raises_key_error_for_missing_age(self):
        """Should raise KeyError if age is missing."""
        with pytest.raises(KeyError):
            get_user_age({'name': 'Alice'})

    def test_raises_type_error_for_non_integer_age(self):
        """Should raise TypeError if age is not an integer."""
        with pytest.raises(TypeError):
            get_user_age({'name': 'Alice', 'age': '30'})

    def test_raises_value_error_for_negative_age(self):
        """Should raise ValueError for negative age."""
        with pytest.raises(ValueError):
            get_user_age({'name': 'Alice', 'age': -5})

    def test_raises_value_error_for_age_too_high(self):
        """Should raise ValueError for age > 150."""
        with pytest.raises(ValueError):
            get_user_age({'name': 'Alice', 'age': 151})

    def test_accepts_boundary_values(self):
        """Should accept age at boundaries (0 and 150)."""
        assert get_user_age({'age': 0}) == 0
        assert get_user_age({'age': 150}) == 150


class TestProcessTransaction:
    """Test process_transaction function."""

    def test_processes_valid_transaction(self):
        """Should process valid transaction correctly."""
        result = process_transaction(100, 500, 2.5)
        assert result['amount'] == 100
        assert result['fee'] == 2.5
        assert result['total'] == 102.5
        assert result['remaining_balance'] == 397.5

    def test_raises_error_for_non_numeric_inputs(self):
        """Should raise ValueError for non-numeric inputs."""
        with pytest.raises(ValueError):
            process_transaction("100", 500, 2.5)

    def test_raises_error_for_negative_amount(self):
        """Should raise ValueError for negative amount."""
        with pytest.raises(ValueError):
            process_transaction(-100, 500, 2.5)

    def test_raises_error_for_negative_balance(self):
        """Should raise ValueError for negative balance."""
        with pytest.raises(ValueError):
            process_transaction(100, -500, 2.5)

    def test_raises_error_for_invalid_fee_percent(self):
        """Should raise ValueError for fee percent out of range."""
        with pytest.raises(ValueError):
            process_transaction(100, 500, -1)
        
        with pytest.raises(ValueError):
            process_transaction(100, 500, 101)

    def test_raises_error_for_insufficient_balance(self):
        """Should raise ValueError for insufficient balance."""
        with pytest.raises(ValueError):
            process_transaction(100, 50, 2.5)


class TestParseNumericValue:
    """Test parse_numeric_value function."""

    def test_parses_string_to_float(self):
        """Should parse string to float."""
        assert parse_numeric_value("42.5") == 42.5

    def test_converts_int_to_float(self):
        """Should convert int to float."""
        assert parse_numeric_value(42) == 42.0

    def test_returns_float_as_is(self):
        """Should return float as is."""
        assert parse_numeric_value(42.5) == 42.5

    def test_raises_value_error_for_invalid_string(self):
        """Should raise ValueError for non-numeric string."""
        with pytest.raises(ValueError):
            parse_numeric_value("not a number")

    def test_raises_type_error_for_none(self):
        """Should raise TypeError for None."""
        with pytest.raises(TypeError):
            parse_numeric_value(None)

    def test_raises_type_error_for_other_types(self):
        """Should raise TypeError for other types."""
        with pytest.raises(TypeError):
            parse_numeric_value([1, 2, 3])


class TestFindUserById:
    """Test find_user_by_id function."""

    def test_finds_user_by_id(self):
        """Should find user with matching ID."""
        users = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        result = find_user_by_id(users, 1)
        assert result == {'id': 1, 'name': 'Alice'}

    def test_returns_none_if_not_found(self):
        """Should return None if user not found."""
        users = [{'id': 1, 'name': 'Alice'}]
        result = find_user_by_id(users, 99)
        assert result is None

    def test_raises_type_error_for_non_list(self):
        """Should raise TypeError if users is not a list."""
        with pytest.raises(TypeError):
            find_user_by_id("not a list", 1)

    def test_raises_type_error_for_non_integer_id(self):
        """Should raise TypeError if user_id is not an integer."""
        users = [{'id': 1, 'name': 'Alice'}]
        with pytest.raises(TypeError):
            find_user_by_id(users, "1")


class TestCalculateAverageScore:
    """Test calculate_average_score function."""

    def test_calculates_average_correctly(self):
        """Should calculate average score."""
        assert calculate_average_score([85, 90, 78, 92]) == 86.25

    def test_raises_error_for_non_list(self):
        """Should raise error if scores is not a list."""
        with pytest.raises((TypeError, ValueError)):
            calculate_average_score("not a list")

    def test_raises_error_for_empty_list(self):
        """Should raise error for empty list."""
        with pytest.raises(ValueError):
            calculate_average_score([])

    def test_raises_error_for_non_numeric_score(self):
        """Should raise error if score is not numeric."""
        with pytest.raises((TypeError, ValueError)):
            calculate_average_score([85, "90", 78])

    def test_raises_error_for_score_out_of_range(self):
        """Should raise error for score out of range."""
        with pytest.raises(ValueError):
            calculate_average_score([85, 90, 101])
        
        with pytest.raises(ValueError):
            calculate_average_score([85, -5, 90])

    def test_handles_boundary_values(self):
        """Should handle scores at boundaries."""
        assert calculate_average_score([0, 100]) == 50.0


class TestNormalizeDataset:
    """Test normalize_dataset function."""

    def test_normalizes_dataset_correctly(self):
        """Should normalize dataset to 0-1 range."""
        data = [{'age': 20, 'score': 50}, {'age': 40, 'score': 100}]
        result = normalize_dataset(data, ['age', 'score'])
        
        assert result[0]['age'] == 0.0
        assert result[1]['age'] == 1.0
        assert result[0]['score'] == 0.0
        assert result[1]['score'] == 1.0

    def test_raises_error_for_non_list_data(self):
        """Should raise error if data is not a list."""
        with pytest.raises((TypeError, ValueError)):
            normalize_dataset("not a list", ['age'])

    def test_raises_error_for_empty_data(self):
        """Should raise error for empty data."""
        with pytest.raises(ValueError):
            normalize_dataset([], ['age'])

    def test_raises_error_for_missing_feature(self):
        """Should raise error if feature is missing."""
        data = [{'age': 20}]
        with pytest.raises((KeyError, ValueError)):
            normalize_dataset(data, ['age', 'score'])

    def test_raises_error_for_non_numeric_value(self):
        """Should raise error for non-numeric feature value."""
        data = [{'age': 'twenty'}]
        with pytest.raises((TypeError, ValueError)):
            normalize_dataset(data, ['age'])



class TestTrainTestSplitSafe:
    """Test train_test_split_safe function."""

    def test_splits_data_correctly(self):
        """Should split data with correct ratio."""
        from exercises.defensive import train_test_split_safe
        
        data = list(range(10))
        train, test = train_test_split_safe(data, 0.2)
        
        assert len(test) == 2
        assert len(train) == 8
        assert len(train) + len(test) == len(data)

    def test_raises_for_non_list(self):
        """Should raise error for non-list data."""
        from exercises.defensive import train_test_split_safe
        
        with pytest.raises((TypeError, ValueError)):
            train_test_split_safe("not a list", 0.2)

    def test_raises_for_empty_data(self):
        """Should raise error for empty data."""
        from exercises.defensive import train_test_split_safe
        
        with pytest.raises(ValueError):
            train_test_split_safe([], 0.2)

    def test_raises_for_invalid_ratio(self):
        """Should raise error for invalid test_ratio."""
        from exercises.defensive import train_test_split_safe
        
        with pytest.raises(ValueError):
            train_test_split_safe([1, 2, 3], 0)
        
        with pytest.raises(ValueError):
            train_test_split_safe([1, 2, 3], 1)
        
        with pytest.raises(ValueError):
            train_test_split_safe([1, 2, 3], 1.5)


class TestDataProcessor:
    """Test DataProcessor class."""

    def test_initializes_correctly(self):
        """Should initialize with valid range."""
        from exercises.defensive import DataProcessor
        
        processor = DataProcessor(0, 100)
        assert processor is not None

    def test_raises_for_invalid_range(self):
        """Should raise error if min >= max."""
        from exercises.defensive import DataProcessor
        
        with pytest.raises(ValueError):
            DataProcessor(100, 0)
        
        with pytest.raises(ValueError):
            DataProcessor(50, 50)

    def test_validates_value_in_range(self):
        """Should validate value in range."""
        from exercises.defensive import DataProcessor
        
        processor = DataProcessor(0, 100)
        assert processor.validate_value(50) is True
        assert processor.validate_value(0) is True
        assert processor.validate_value(100) is True

    def test_validates_value_out_of_range(self):
        """Should validate value out of range."""
        from exercises.defensive import DataProcessor
        
        processor = DataProcessor(0, 100)
        assert processor.validate_value(-1) is False
        assert processor.validate_value(101) is False

    def test_processes_batch(self):
        """Should process batch of values."""
        from exercises.defensive import DataProcessor
        
        processor = DataProcessor(0, 100)
        values = [10, 50, 150, 75, -5, 90]
        result = processor.process_batch(values)
        
        assert result == [10, 50, 75, 90]

    def test_tracks_statistics(self):
        """Should track processing statistics."""
        from exercises.defensive import DataProcessor
        
        processor = DataProcessor(0, 100)
        processor.process_batch([10, 50, 150, 75])
        
        stats = processor.get_statistics()
        assert stats['processed_count'] == 4
        assert stats['valid_count'] == 3
        assert stats['invalid_count'] == 1


class TestPipelineProcessData:
    """Test pipeline_process_data function."""

    def test_processes_through_pipeline(self):
        """Should process data through transformations."""
        from exercises.defensive import pipeline_process_data
        
        data = [1, 2, 3, 4, 5]
        transforms = [
            lambda x: [i * 2 for i in x],
            lambda x: [i + 1 for i in x]
        ]
        
        result = pipeline_process_data(data, transforms)
        assert result == [3, 5, 7, 9, 11]

    def test_raises_for_non_list_data(self):
        """Should raise error for non-list data."""
        from exercises.defensive import pipeline_process_data
        
        with pytest.raises((TypeError, ValueError)):
            pipeline_process_data("not a list", [])

    def test_raises_for_empty_data(self):
        """Should raise error for empty data."""
        from exercises.defensive import pipeline_process_data
        
        with pytest.raises(ValueError):
            pipeline_process_data([], [lambda x: x])

    def test_raises_for_non_callable_transformation(self):
        """Should raise error for non-callable transformation."""
        from exercises.defensive import pipeline_process_data
        
        with pytest.raises((TypeError, ValueError)):
            pipeline_process_data([1, 2, 3], ["not callable"])


class TestSafeDivideBatch:
    """Test safe_divide_batch function."""

    def test_divides_successfully(self):
        """Should divide lists element-wise."""
        from exercises.defensive import safe_divide_batch
        
        result = safe_divide_batch([10, 20, 30], [2, 4, 5], 0)
        assert result == [5.0, 5.0, 6.0]

    def test_handles_division_by_zero(self):
        """Should use default for division by zero."""
        from exercises.defensive import safe_divide_batch
        
        result = safe_divide_batch([10, 20, 30], [2, 0, 5], -1)
        assert result == [5.0, -1, 6.0]

    def test_raises_for_length_mismatch(self):
        """Should raise error for length mismatch."""
        from exercises.defensive import safe_divide_batch
        
        with pytest.raises(ValueError):
            safe_divide_batch([10, 20], [2, 4, 5], 0)

    def test_raises_for_non_list(self):
        """Should raise error for non-list inputs."""
        from exercises.defensive import safe_divide_batch
        
        with pytest.raises((TypeError, ValueError)):
            safe_divide_batch("not a list", [1, 2], 0)


class TestProcessFilesSafely:
    """Test process_files_safely function."""

    def test_processes_existing_files(self, tmp_path):
        """Should process existing files."""
        from exercises.defensive import process_files_safely
        
        file1 = tmp_path / "file1.txt"
        file2 = tmp_path / "file2.txt"
        file1.write_text("line1\nline2\nline3")
        file2.write_text("line1\nline2")
        
        def count_lines(path):
            with open(path) as f:
                return len(f.readlines())
        
        result = process_files_safely([str(file1), str(file2)], count_lines)
        
        assert result[str(file1)] == 3
        assert result[str(file2)] == 2

    def test_handles_missing_files(self, tmp_path):
        """Should handle missing files gracefully."""
        from exercises.defensive import process_files_safely
        
        file1 = tmp_path / "exists.txt"
        file1.write_text("content")
        
        def count_lines(path):
            with open(path) as f:
                return len(f.readlines())
        
        result = process_files_safely(
            [str(file1), "nonexistent.txt"],
            count_lines
        )
        
        assert result[str(file1)] == 1
        assert "Error" in result["nonexistent.txt"] or result["nonexistent.txt"] is None


class TestModelTracker:
    """Test ModelTracker class."""

    def test_initializes_correctly(self):
        """Should initialize with model name."""
        from exercises.defensive import ModelTracker
        
        tracker = ModelTracker("MyModel")
        status = tracker.get_status()
        assert status['state'] == 'initialized'
        assert status['model_name'] == 'MyModel'

    def test_raises_for_empty_name(self):
        """Should raise error for empty model name."""
        from exercises.defensive import ModelTracker
        
        with pytest.raises(ValueError):
            ModelTracker("")

    def test_starts_training(self):
        """Should start training from initialized state."""
        from exercises.defensive import ModelTracker
        
        tracker = ModelTracker("MyModel")
        tracker.start_training()
        
        status = tracker.get_status()
        assert status['state'] == 'training'

    def test_cannot_start_training_twice(self):
        """Should not allow starting training twice."""
        from exercises.defensive import ModelTracker
        
        tracker = ModelTracker("MyModel")
        tracker.start_training()
        
        with pytest.raises((ValueError, RuntimeError)):
            tracker.start_training()

    def test_records_epoch(self):
        """Should record epoch during training."""
        from exercises.defensive import ModelTracker
        
        tracker = ModelTracker("MyModel")
        tracker.start_training()
        tracker.record_epoch(1, 0.5)
        tracker.record_epoch(2, 0.3)

    def test_cannot_record_epoch_before_training(self):
        """Should not allow recording epoch before training."""
        from exercises.defensive import ModelTracker
        
        tracker = ModelTracker("MyModel")
        
        with pytest.raises((ValueError, RuntimeError)):
            tracker.record_epoch(1, 0.5)

    def test_validates_epoch_order(self):
        """Should validate epochs are in order."""
        from exercises.defensive import ModelTracker
        
        tracker = ModelTracker("MyModel")
        tracker.start_training()
        tracker.record_epoch(1, 0.5)
        
        with pytest.raises(ValueError):
            tracker.record_epoch(1, 0.4)  # Same epoch
        
        with pytest.raises(ValueError):
            tracker.record_epoch(3, 0.3)  # Skipped epoch 2

    def test_finishes_training(self):
        """Should finish training successfully."""
        from exercises.defensive import ModelTracker
        
        tracker = ModelTracker("MyModel")
        tracker.start_training()
        tracker.record_epoch(1, 0.5)
        tracker.finish_training(0.85)
        
        status = tracker.get_status()
        assert status['state'] == 'completed'

    def test_cannot_finish_before_training(self):
        """Should not allow finishing before training."""
        from exercises.defensive import ModelTracker
        
        tracker = ModelTracker("MyModel")
        
        with pytest.raises((ValueError, RuntimeError)):
            tracker.finish_training(0.85)

    def test_validates_final_accuracy(self):
        """Should validate final accuracy is in range."""
        from exercises.defensive import ModelTracker
        
        tracker = ModelTracker("MyModel")
        tracker.start_training()
        
        with pytest.raises(ValueError):
            tracker.finish_training(1.5)
        
        with pytest.raises(ValueError):
            tracker.finish_training(-0.1)
