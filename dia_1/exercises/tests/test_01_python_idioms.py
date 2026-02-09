"""
Unit tests for Python Idioms exercises.

Run with: pytest test_01_python_idioms.py -v
"""

"""
Unit tests for Python Idioms exercises.

Run with: pytest test_01_python_idioms.py -v
"""

import pytest
import time
from typing import List
import sys
from pathlib import Path

# Add parent directory to path for imports
parent_dir = Path(__file__).parent.parent
sys.path.insert(0, str(parent_dir))

# Import with try/except to handle different execution contexts
# Note: Module name starts with number, so we use importlib
import importlib.util
import sys
from pathlib import Path

# Add parent directory to path
parent_dir = Path(__file__).parent.parent
sys.path.insert(0, str(parent_dir))

# Import module with numeric prefix
_spec = importlib.util.spec_from_file_location("python_idioms", parent_dir / "01_python_idioms.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)

# Assign functions for easier access
square_evens = ex.square_evens
transform_strings = ex.transform_strings
word_lengths = ex.word_lengths
invert_dict = ex.invert_dict
filter_dict_by_value = ex.filter_dict_by_value
countdown = ex.countdown
even_numbers = ex.even_numbers
fibonacci_generator = ex.fibonacci_generator
Timer = ex.Timer
FileWriter = ex.FileWriter
uppercase_decorator = ex.uppercase_decorator
repeat = ex.repeat
validate_positive = ex.validate_positive
process_sales_data = ex.process_sales_data
batch_generator = ex.batch_generator


# ============================================================================
# TEST EXERCISE 1: List Comprehensions
# ============================================================================

class TestListComprehensions:
    """Tests for list comprehension exercises."""
    
    def test_square_evens_basic(self):
        """Test square_evens with basic input."""
        assert square_evens([1, 2, 3, 4, 5, 6]) == [4, 16, 36]
    
    def test_square_evens_all_odd(self):
        """Test square_evens with all odd numbers."""
        assert square_evens([1, 3, 5, 7]) == []
    
    def test_square_evens_all_even(self):
        """Test square_evens with all even numbers."""
        assert square_evens([2, 4, 6]) == [4, 16, 36]
    
    def test_square_evens_empty(self):
        """Test square_evens with empty list."""
        assert square_evens([]) == []
    
    def test_transform_strings_basic(self):
        """Test transform_strings with basic input."""
        result = transform_strings(['hi', 'python', 'is', 'great'])
        assert result == ['PYTHON', 'GREAT']
    
    def test_transform_strings_all_short(self):
        """Test transform_strings with all short words."""
        assert transform_strings(['hi', 'is', 'ok']) == []
    
    def test_transform_strings_all_long(self):
        """Test transform_strings with all long words."""
        result = transform_strings(['python', 'java', 'rust'])
        assert result == ['PYTHON', 'JAVA', 'RUST']


# ============================================================================
# TEST EXERCISE 2: Dict Comprehensions
# ============================================================================

class TestDictComprehensions:
    """Tests for dict comprehension exercises."""
    
    def test_word_lengths_basic(self):
        """Test word_lengths with basic input."""
        result = word_lengths(['python', 'is', 'awesome'])
        assert result == {'python': 6, 'is': 2, 'awesome': 7}
    
    def test_word_lengths_empty(self):
        """Test word_lengths with empty list."""
        assert word_lengths([]) == {}
    
    def test_word_lengths_single(self):
        """Test word_lengths with single word."""
        assert word_lengths(['hello']) == {'hello': 5}
    
    def test_invert_dict_basic(self):
        """Test invert_dict with basic input."""
        result = invert_dict({'a': 1, 'b': 2, 'c': 3})
        assert result == {1: 'a', 2: 'b', 3: 'c'}
    
    def test_invert_dict_empty(self):
        """Test invert_dict with empty dict."""
        assert invert_dict({}) == {}
    
    def test_filter_dict_by_value_basic(self):
        """Test filter_dict_by_value with basic input."""
        result = filter_dict_by_value({'a': 10, 'b': 5, 'c': 20}, 8)
        assert result == {'a': 10, 'c': 20}
    
    def test_filter_dict_by_value_none_pass(self):
        """Test filter_dict_by_value where no values pass."""
        result = filter_dict_by_value({'a': 1, 'b': 2}, 10)
        assert result == {}
    
    def test_filter_dict_by_value_all_pass(self):
        """Test filter_dict_by_value where all values pass."""
        result = filter_dict_by_value({'a': 10, 'b': 20}, 5)
        assert result == {'a': 10, 'b': 20}


# ============================================================================
# TEST EXERCISE 3: Generators
# ============================================================================

class TestGenerators:
    """Tests for generator exercises."""
    
    def test_countdown_basic(self):
        """Test countdown with basic input."""
        assert list(countdown(5)) == [5, 4, 3, 2, 1]
    
    def test_countdown_one(self):
        """Test countdown from 1."""
        assert list(countdown(1)) == [1]
    
    def test_countdown_zero(self):
        """Test countdown from 0."""
        assert list(countdown(0)) == []
    
    def test_countdown_is_generator(self):
        """Test that countdown returns a generator."""
        result = countdown(3)
        assert hasattr(result, '__iter__') and hasattr(result, '__next__')
    
    def test_even_numbers_basic(self):
        """Test even_numbers with basic range."""
        assert list(even_numbers(1, 10)) == [2, 4, 6, 8]
    
    def test_even_numbers_start_even(self):
        """Test even_numbers starting with even number."""
        assert list(even_numbers(2, 8)) == [2, 4, 6]
    
    def test_even_numbers_empty_range(self):
        """Test even_numbers with empty range."""
        assert list(even_numbers(5, 5)) == []
    
    def test_fibonacci_generator_basic(self):
        """Test fibonacci_generator with basic input."""
        assert list(fibonacci_generator(7)) == [0, 1, 1, 2, 3, 5, 8]
    
    def test_fibonacci_generator_first_two(self):
        """Test fibonacci_generator for first two numbers."""
        assert list(fibonacci_generator(2)) == [0, 1]
    
    def test_fibonacci_generator_zero(self):
        """Test fibonacci_generator with n=0."""
        assert list(fibonacci_generator(0)) == []


# ============================================================================
# TEST EXERCISE 4: Context Managers
# ============================================================================

class TestContextManagers:
    """Tests for context manager exercises."""
    
    def test_timer_measures_time(self):
        """Test that Timer measures elapsed time."""
        with Timer() as t:
            time.sleep(0.1)
        
        assert t.elapsed is not None
        assert t.elapsed >= 0.1
        assert t.elapsed < 0.2  # Should not take too long
    
    def test_timer_start_and_end_set(self):
        """Test that Timer sets start and end times."""
        with Timer() as t:
            time.sleep(0.05)
        
        assert t.start is not None
        assert t.end is not None
        assert t.end > t.start
    
    def test_timer_with_exception(self):
        """Test that Timer works even with exception."""
        with pytest.raises(ValueError):
            with Timer() as t:
                raise ValueError("Test error")
        
        # Timer should still have recorded time
        assert t.elapsed is not None
    
    def test_file_writer_creates_file(self, tmp_path):
        """Test that FileWriter creates and writes to file."""
        test_file = tmp_path / "test.txt"
        
        with FileWriter(str(test_file)) as f:
            f.write("Hello World")
        
        assert test_file.exists()
        assert test_file.read_text() == "Hello World"
    
    def test_file_writer_closes_file(self, tmp_path):
        """Test that FileWriter closes file after context."""
        test_file = tmp_path / "test.txt"
        
        with FileWriter(str(test_file)) as f:
            f.write("Test")
            file_obj = f
        
        assert file_obj.closed
    
    def test_file_writer_closes_on_exception(self, tmp_path):
        """Test that FileWriter closes file even on exception."""
        test_file = tmp_path / "test.txt"
        
        with pytest.raises(ValueError):
            with FileWriter(str(test_file)) as f:
                f.write("Test")
                file_obj = f
                raise ValueError("Test error")
        
        assert file_obj.closed


# ============================================================================
# TEST EXERCISE 5: Decorators
# ============================================================================

class TestDecorators:
    """Tests for decorator exercises."""
    
    def test_uppercase_decorator_basic(self):
        """Test uppercase_decorator with basic function."""
        @uppercase_decorator
        def greet(name):
            return f"hello {name}"
        
        assert greet("world") == "HELLO WORLD"
    
    def test_uppercase_decorator_already_upper(self):
        """Test uppercase_decorator with already uppercase string."""
        @uppercase_decorator
        def shout():
            return "LOUD"
        
        assert shout() == "LOUD"
    
    def test_repeat_decorator_basic(self, capsys):
        """Test repeat decorator with basic function."""
        @repeat(3)
        def say_hello():
            print("Hello")
        
        say_hello()
        captured = capsys.readouterr()
        assert captured.out.count("Hello\n") == 3
    
    def test_repeat_decorator_once(self, capsys):
        """Test repeat decorator with times=1."""
        @repeat(1)
        def say_hi():
            print("Hi")
        
        say_hi()
        captured = capsys.readouterr()
        assert captured.out == "Hi\n"
    
    def test_validate_positive_valid_args(self):
        """Test validate_positive with valid arguments."""
        @validate_positive
        def add(a, b):
            return a + b
        
        assert add(5, 3) == 8
        assert add(1, 1) == 2
    
    def test_validate_positive_negative_arg(self):
        """Test validate_positive raises error for negative."""
        @validate_positive
        def add(a, b):
            return a + b
        
        with pytest.raises(ValueError, match="positive"):
            add(-1, 3)
    
    def test_validate_positive_zero_arg(self):
        """Test validate_positive raises error for zero."""
        @validate_positive
        def multiply(a, b):
            return a * b
        
        with pytest.raises(ValueError, match="positive"):
            multiply(0, 5)


# ============================================================================
# TEST EXERCISE 6: Combined Challenge
# ============================================================================

class TestCombinedChallenge:
    """Tests for combined challenge exercises."""
    
    def test_process_sales_data_basic(self):
        """Test process_sales_data with basic input."""
        sales = [
            {'product': 'A', 'price': 100, 'quantity': 5},
            {'product': 'B', 'price': 50, 'quantity': 10},
            {'product': 'C', 'price': 200, 'quantity': 3},
        ]
        
        result = process_sales_data(sales)
        
        assert result['revenues'] == {'A': 500, 'B': 500, 'C': 600}
        assert result['high_revenue'] == {'C': 600}
        assert result['total'] == 1600
    
    def test_process_sales_data_no_high_revenue(self):
        """Test process_sales_data with no high revenue products."""
        sales = [
            {'product': 'A', 'price': 10, 'quantity': 5},
            {'product': 'B', 'price': 20, 'quantity': 10},
        ]
        
        result = process_sales_data(sales)
        
        assert result['high_revenue'] == {}
        assert result['total'] == 250
    
    def test_process_sales_data_empty(self):
        """Test process_sales_data with empty list."""
        result = process_sales_data([])
        
        assert result['revenues'] == {}
        assert result['high_revenue'] == {}
        assert result['total'] == 0
    
    def test_batch_generator_basic(self):
        """Test batch_generator with basic input."""
        result = list(batch_generator([1, 2, 3, 4, 5], 2))
        assert result == [[1, 2], [3, 4], [5]]
    
    def test_batch_generator_exact_batches(self):
        """Test batch_generator with exact batch sizes."""
        result = list(batch_generator([1, 2, 3, 4], 2))
        assert result == [[1, 2], [3, 4]]
    
    def test_batch_generator_single_batch(self):
        """Test batch_generator with single batch."""
        result = list(batch_generator([1, 2, 3], 5))
        assert result == [[1, 2, 3]]
    
    def test_batch_generator_empty(self):
        """Test batch_generator with empty list."""
        result = list(batch_generator([], 2))
        assert result == []
    
    def test_batch_generator_is_generator(self):
        """Test that batch_generator returns a generator."""
        result = batch_generator([1, 2, 3], 2)
        assert hasattr(result, '__iter__') and hasattr(result, '__next__')


# ============================================================================
# BONUS: Integration Tests
# ============================================================================

class TestIntegration:
    """Integration tests combining multiple concepts."""
    
    def test_comprehension_with_generator(self):
        """Test using comprehension to consume generator."""
        gen = fibonacci_generator(5)
        squares = [x ** 2 for x in gen]
        assert squares == [0, 1, 1, 4, 9]
    
    def test_decorator_with_context_manager(self, tmp_path):
        """Test using decorator with context manager."""
        test_file = tmp_path / "test.txt"
        
        @uppercase_decorator
        def write_greeting(name):
            with FileWriter(str(test_file)) as f:
                f.write(f"hello {name}")
            return f"hello {name}"
        
        result = write_greeting("world")
        assert result == "HELLO WORLD"
        assert test_file.read_text() == "hello world"
