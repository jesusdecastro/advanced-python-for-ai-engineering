"""
Unit tests for generators and iterators exercises.

These tests validate both functionality and proper use of generators.

Run with: pytest tests/test_02_generators_iterators.py -v
"""

import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest

# Import the module to test functionality
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# Dynamically import module with numeric prefix
_module_path = Path(__file__).parent.parent / "02_generators_iterators.py"
_spec = importlib.util.spec_from_file_location("generators_exercises", _module_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)

chain_iterables = _module.chain_iterables
chunk_data = _module.chunk_data
countdown = _module.countdown
drop = _module.drop
fibonacci = _module.fibonacci
filter_even = _module.filter_even
flatten_nested_list = _module.flatten_nested_list
infinite_sequence = _module.infinite_sequence
process_csv_stream = _module.process_csv_stream
read_lines_stream = _module.read_lines_stream
read_multiple_sources = _module.read_multiple_sources
running_average = _module.running_average
sliding_window = _module.sliding_window
square_numbers = _module.square_numbers
take = _module.take


class TestTypeHintsWithPyright:
    """Test that Pyright validates the type hints correctly."""

    def test_pyright_passes(self) -> None:
        """Test that Pyright validation passes for the exercises file."""
        exercises_file = Path(__file__).parent.parent / "02_generators_iterators.py"

        result = subprocess.run(
            ["pyright", str(exercises_file), "--outputjson"],
            capture_output=True,
            text=True,
        )

        # Pyright returns 0 if no errors
        if result.returncode != 0:
            pytest.fail(f"Pyright found type errors:\n{result.stdout}\n{result.stderr}")


class TestFibonacci:
    """Tests for fibonacci generator."""

    def test_first_ten_fibonacci(self) -> None:
        """Test first 10 Fibonacci numbers."""
        fib_gen = fibonacci()
        result = [next(fib_gen) for _ in range(10)]
        assert result == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    def test_first_five_fibonacci(self) -> None:
        """Test first 5 Fibonacci numbers."""
        fib_gen = fibonacci()
        result = [next(fib_gen) for _ in range(5)]
        assert result == [0, 1, 1, 2, 3]

    def test_fibonacci_is_generator(self) -> None:
        """Test that fibonacci returns a generator."""
        fib_gen = fibonacci()
        assert hasattr(fib_gen, "__next__")
        assert hasattr(fib_gen, "__iter__")

    def test_fibonacci_continues_indefinitely(self) -> None:
        """Test that fibonacci can generate many values."""
        fib_gen = fibonacci()
        result = [next(fib_gen) for _ in range(20)]
        assert len(result) == 20
        assert result[-1] == 4181

    def test_multiple_fibonacci_generators(self) -> None:
        """Test that multiple generators are independent."""
        fib1 = fibonacci()
        fib2 = fibonacci()
        assert next(fib1) == 0
        assert next(fib1) == 1
        assert next(fib2) == 0


class TestCountdown:
    """Tests for countdown generator."""

    def test_basic_countdown(self) -> None:
        """Test countdown from 5."""
        assert list(countdown(5)) == [5, 4, 3, 2, 1]

    def test_countdown_from_one(self) -> None:
        """Test countdown from 1."""
        assert list(countdown(1)) == [1]

    def test_countdown_from_zero(self) -> None:
        """Test countdown from 0."""
        assert list(countdown(0)) == []

    def test_countdown_from_ten(self) -> None:
        """Test countdown from 10."""
        result = list(countdown(10))
        assert result == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    def test_countdown_is_generator(self) -> None:
        """Test that countdown returns a generator."""
        gen = countdown(5)
        assert hasattr(gen, "__next__")
        assert hasattr(gen, "__iter__")

    def test_countdown_partial_consumption(self) -> None:
        """Test consuming countdown partially."""
        gen = countdown(5)
        assert next(gen) == 5
        assert next(gen) == 4
        assert list(gen) == [3, 2, 1]


class TestInfiniteSequence:
    """Tests for infinite_sequence generator."""

    def test_sequence_from_zero(self) -> None:
        """Test infinite sequence starting from 0."""
        gen = infinite_sequence(0)
        result = [next(gen) for _ in range(5)]
        assert result == [0, 1, 2, 3, 4]

    def test_sequence_from_ten(self) -> None:
        """Test infinite sequence starting from 10."""
        gen = infinite_sequence(10)
        result = [next(gen) for _ in range(5)]
        assert result == [10, 11, 12, 13, 14]

    def test_sequence_from_negative(self) -> None:
        """Test infinite sequence starting from negative number."""
        gen = infinite_sequence(-3)
        result = [next(gen) for _ in range(5)]
        assert result == [-3, -2, -1, 0, 1]

    def test_sequence_is_generator(self) -> None:
        """Test that infinite_sequence returns a generator."""
        gen = infinite_sequence(0)
        assert hasattr(gen, "__next__")
        assert hasattr(gen, "__iter__")

    def test_sequence_continues_indefinitely(self) -> None:
        """Test that sequence can generate many values."""
        gen = infinite_sequence(0)
        result = [next(gen) for _ in range(100)]
        assert len(result) == 100
        assert result[-1] == 99


class TestChunkData:
    """Tests for chunk_data generator."""

    def test_basic_chunking(self) -> None:
        """Test chunking data into size 2."""
        result = list(chunk_data([1, 2, 3, 4, 5], 2))
        assert result == [[1, 2], [3, 4], [5]]

    def test_chunk_size_three(self) -> None:
        """Test chunking with size 3."""
        result = list(chunk_data(list(range(1, 11)), 3))
        assert result == [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]

    def test_chunk_size_one(self) -> None:
        """Test chunking with size 1."""
        result = list(chunk_data([1, 2, 3], 1))
        assert result == [[1], [2], [3]]

    def test_chunk_size_larger_than_data(self) -> None:
        """Test chunk size larger than data."""
        result = list(chunk_data([1, 2, 3], 10))
        assert result == [[1, 2, 3]]

    def test_empty_data(self) -> None:
        """Test with empty data."""
        result = list(chunk_data([], 3))
        assert result == []

    def test_chunk_data_is_generator(self) -> None:
        """Test that chunk_data returns a generator."""
        gen = chunk_data([1, 2, 3], 2)
        assert hasattr(gen, "__next__")
        assert hasattr(gen, "__iter__")


class TestFilterEven:
    """Tests for filter_even generator."""

    def test_basic_filtering(self) -> None:
        """Test filtering even numbers."""
        assert list(filter_even([1, 2, 3, 4, 5, 6])) == [2, 4, 6]

    def test_all_even(self) -> None:
        """Test with all even numbers."""
        assert list(filter_even([2, 4, 6, 8])) == [2, 4, 6, 8]

    def test_all_odd(self) -> None:
        """Test with all odd numbers."""
        assert list(filter_even([1, 3, 5, 7])) == []

    def test_empty_list(self) -> None:
        """Test with empty list."""
        assert list(filter_even([])) == []

    def test_with_zero(self) -> None:
        """Test that zero is included (even)."""
        assert list(filter_even([0, 1, 2, 3])) == [0, 2]

    def test_filter_even_is_generator(self) -> None:
        """Test that filter_even returns a generator."""
        gen = filter_even([1, 2, 3])
        assert hasattr(gen, "__next__")
        assert hasattr(gen, "__iter__")


class TestSquareNumbers:
    """Tests for square_numbers generator."""

    def test_basic_squaring(self) -> None:
        """Test squaring numbers."""
        assert list(square_numbers([1, 2, 3, 4])) == [1, 4, 9, 16]

    def test_with_zero(self) -> None:
        """Test with zero."""
        assert list(square_numbers([0, 1, 2])) == [0, 1, 4]

    def test_negative_numbers(self) -> None:
        """Test with negative numbers."""
        assert list(square_numbers([-2, -1, 0, 1, 2])) == [4, 1, 0, 1, 4]

    def test_empty_list(self) -> None:
        """Test with empty list."""
        assert list(square_numbers([])) == []

    def test_square_numbers_is_generator(self) -> None:
        """Test that square_numbers returns a generator."""
        gen = square_numbers([1, 2, 3])
        assert hasattr(gen, "__next__")
        assert hasattr(gen, "__iter__")

    def test_large_numbers(self) -> None:
        """Test with large numbers."""
        result = list(square_numbers([10, 20, 30]))
        assert result == [100, 400, 900]


class TestChainIterables:
    """Tests for chain_iterables generator."""

    def test_basic_chaining(self) -> None:
        """Test chaining multiple iterables."""
        result = list(chain_iterables([1, 2], [3, 4], [5, 6]))
        assert result == [1, 2, 3, 4, 5, 6]

    def test_chain_two_lists(self) -> None:
        """Test chaining two lists."""
        result = list(chain_iterables([1, 2, 3], [4, 5, 6]))
        assert result == [1, 2, 3, 4, 5, 6]

    def test_chain_empty_lists(self) -> None:
        """Test chaining with empty lists."""
        result = list(chain_iterables([], [1, 2], []))
        assert result == [1, 2]

    def test_chain_single_list(self) -> None:
        """Test chaining single list."""
        result = list(chain_iterables([1, 2, 3]))
        assert result == [1, 2, 3]

    def test_chain_no_lists(self) -> None:
        """Test chaining with no arguments."""
        result = list(chain_iterables())
        assert result == []

    def test_chain_iterables_is_generator(self) -> None:
        """Test that chain_iterables returns a generator."""
        gen = chain_iterables([1, 2], [3, 4])
        assert hasattr(gen, "__next__")
        assert hasattr(gen, "__iter__")


class TestFlattenNestedList:
    """Tests for flatten_nested_list generator."""

    def test_basic_flattening(self) -> None:
        """Test flattening nested list."""
        result = list(flatten_nested_list([[1, 2], [3, 4], [5]]))
        assert result == [1, 2, 3, 4, 5]

    def test_single_sublist(self) -> None:
        """Test with single sublist."""
        result = list(flatten_nested_list([[1, 2, 3]]))
        assert result == [1, 2, 3]

    def test_empty_sublists(self) -> None:
        """Test with empty sublists."""
        result = list(flatten_nested_list([[], [1, 2], []]))
        assert result == [1, 2]

    def test_empty_list(self) -> None:
        """Test with empty list."""
        result = list(flatten_nested_list([]))
        assert result == []

    def test_flatten_nested_list_is_generator(self) -> None:
        """Test that flatten_nested_list returns a generator."""
        gen = flatten_nested_list([[1, 2], [3, 4]])
        assert hasattr(gen, "__next__")
        assert hasattr(gen, "__iter__")


class TestReadMultipleSources:
    """Tests for read_multiple_sources generator."""

    def test_basic_reading(self) -> None:
        """Test reading from multiple sources."""
        sources = [["a", "b"], ["c", "d"], ["e"]]
        result = list(read_multiple_sources(sources))
        assert result == ["a", "b", "c", "d", "e"]

    def test_single_source(self) -> None:
        """Test with single source."""
        sources = [["a", "b", "c"]]
        result = list(read_multiple_sources(sources))
        assert result == ["a", "b", "c"]

    def test_empty_sources(self) -> None:
        """Test with empty sources."""
        sources = [[], ["a"], []]
        result = list(read_multiple_sources(sources))
        assert result == ["a"]

    def test_no_sources(self) -> None:
        """Test with no sources."""
        result = list(read_multiple_sources([]))
        assert result == []

    def test_read_multiple_sources_is_generator(self) -> None:
        """Test that read_multiple_sources returns a generator."""
        gen = read_multiple_sources([["a"], ["b"]])
        assert hasattr(gen, "__next__")
        assert hasattr(gen, "__iter__")


class TestReadLinesStream:
    """Tests for read_lines_stream generator."""

    def test_basic_streaming(self) -> None:
        """Test streaming lines."""
        lines = ["line1", "line2", "line3"]
        result = list(read_lines_stream(lines))
        assert result == ["line1", "line2", "line3"]

    def test_single_line(self) -> None:
        """Test with single line."""
        result = list(read_lines_stream(["line1"]))
        assert result == ["line1"]

    def test_empty_lines(self) -> None:
        """Test with empty lines."""
        result = list(read_lines_stream([]))
        assert result == []

    def test_read_lines_stream_is_generator(self) -> None:
        """Test that read_lines_stream returns a generator."""
        gen = read_lines_stream(["line1", "line2"])
        assert hasattr(gen, "__next__")
        assert hasattr(gen, "__iter__")


class TestProcessCsvStream:
    """Tests for process_csv_stream generator."""

    def test_basic_csv_processing(self) -> None:
        """Test processing CSV data."""
        csv_data = [["name", "age"], ["Alice", "30"], ["Bob", "25"]]
        result = list(process_csv_stream(csv_data))
        expected = [{"name": "Alice", "age": "30"}, {"name": "Bob", "age": "25"}]
        assert result == expected

    def test_single_row(self) -> None:
        """Test with single data row."""
        csv_data = [["name", "age"], ["Alice", "30"]]
        result = list(process_csv_stream(csv_data))
        assert result == [{"name": "Alice", "age": "30"}]

    def test_no_data_rows(self) -> None:
        """Test with only header."""
        csv_data = [["name", "age"]]
        result = list(process_csv_stream(csv_data))
        assert result == []

    def test_multiple_columns(self) -> None:
        """Test with multiple columns."""
        csv_data = [["id", "name", "city"], ["1", "Alice", "NYC"], ["2", "Bob", "LA"]]
        result = list(process_csv_stream(csv_data))
        expected = [
            {"id": "1", "name": "Alice", "city": "NYC"},
            {"id": "2", "name": "Bob", "city": "LA"},
        ]
        assert result == expected

    def test_process_csv_stream_is_generator(self) -> None:
        """Test that process_csv_stream returns a generator."""
        csv_data = [["name"], ["Alice"]]
        gen = process_csv_stream(csv_data)
        assert hasattr(gen, "__next__")
        assert hasattr(gen, "__iter__")


class TestRunningAverage:
    """Tests for running_average generator."""

    def test_basic_running_average(self) -> None:
        """Test calculating running average."""
        result = list(running_average([10, 20, 30, 40]))
        assert result == [10.0, 15.0, 20.0, 25.0]

    def test_single_number(self) -> None:
        """Test with single number."""
        result = list(running_average([10]))
        assert result == [10.0]

    def test_two_numbers(self) -> None:
        """Test with two numbers."""
        result = list(running_average([10, 20]))
        assert result == [10.0, 15.0]

    def test_with_zero(self) -> None:
        """Test with zero."""
        result = list(running_average([0, 10, 20]))
        assert result == [0.0, 5.0, 10.0]

    def test_negative_numbers(self) -> None:
        """Test with negative numbers."""
        result = list(running_average([-10, 10, 0]))
        assert result == [-10.0, 0.0, 0.0]

    def test_running_average_is_generator(self) -> None:
        """Test that running_average returns a generator."""
        gen = running_average([10, 20, 30])
        assert hasattr(gen, "__next__")
        assert hasattr(gen, "__iter__")


class TestTake:
    """Tests for take generator."""

    def test_basic_take(self) -> None:
        """Test taking first 5 items."""
        result = list(take(range(100), 5))
        assert result == [0, 1, 2, 3, 4]

    def test_take_all(self) -> None:
        """Test taking more items than available."""
        result = list(take(range(5), 10))
        assert result == [0, 1, 2, 3, 4]

    def test_take_zero(self) -> None:
        """Test taking zero items."""
        result = list(take(range(10), 0))
        assert result == []

    def test_take_one(self) -> None:
        """Test taking one item."""
        result = list(take(range(10), 1))
        assert result == [0]

    def test_take_is_generator(self) -> None:
        """Test that take returns a generator."""
        gen = take(range(10), 5)
        assert hasattr(gen, "__next__")
        assert hasattr(gen, "__iter__")


class TestDrop:
    """Tests for drop generator."""

    def test_basic_drop(self) -> None:
        """Test dropping first 5 items."""
        result = list(drop(range(10), 5))
        assert result == [5, 6, 7, 8, 9]

    def test_drop_all(self) -> None:
        """Test dropping more items than available."""
        result = list(drop(range(5), 10))
        assert result == []

    def test_drop_zero(self) -> None:
        """Test dropping zero items."""
        result = list(drop(range(5), 0))
        assert result == [0, 1, 2, 3, 4]

    def test_drop_one(self) -> None:
        """Test dropping one item."""
        result = list(drop(range(5), 1))
        assert result == [1, 2, 3, 4]

    def test_drop_is_generator(self) -> None:
        """Test that drop returns a generator."""
        gen = drop(range(10), 5)
        assert hasattr(gen, "__next__")
        assert hasattr(gen, "__iter__")


class TestSlidingWindow:
    """Tests for sliding_window generator."""

    def test_basic_sliding_window(self) -> None:
        """Test sliding window of size 3."""
        result = list(sliding_window([1, 2, 3, 4, 5], 3))
        assert result == [[1, 2, 3], [2, 3, 4], [3, 4, 5]]

    def test_window_size_two(self) -> None:
        """Test sliding window of size 2."""
        result = list(sliding_window([1, 2, 3, 4], 2))
        assert result == [[1, 2], [2, 3], [3, 4]]

    def test_window_size_one(self) -> None:
        """Test sliding window of size 1."""
        result = list(sliding_window([1, 2, 3], 1))
        assert result == [[1], [2], [3]]

    def test_window_larger_than_data(self) -> None:
        """Test window size larger than data."""
        result = list(sliding_window([1, 2], 5))
        assert result == []

    def test_window_equal_to_data(self) -> None:
        """Test window size equal to data length."""
        result = list(sliding_window([1, 2, 3], 3))
        assert result == [[1, 2, 3]]

    def test_sliding_window_is_generator(self) -> None:
        """Test that sliding_window returns a generator."""
        gen = sliding_window([1, 2, 3, 4], 2)
        assert hasattr(gen, "__next__")
        assert hasattr(gen, "__iter__")
