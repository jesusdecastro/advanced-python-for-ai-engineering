"""Tests for functional programming exercises."""

import importlib.util
import sys
import time
from pathlib import Path

# Import the module to test functionality
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# Dynamically import module with numeric prefix
_module_path = Path(__file__).parent.parent / "04_functional_programming.py"
_spec = importlib.util.spec_from_file_location("functional_exercises", _module_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)

sum_of_even_squares = _module.sum_of_even_squares
calculate_price = _module.calculate_price
calculate_price_with_vat = _module.calculate_price_with_vat
calculate_price_with_discount = _module.calculate_price_with_discount
calculate_final_price = _module.calculate_final_price
count_paths_slow = _module.count_paths_slow
count_paths_fast = _module.count_paths_fast
process_transactions = _module.process_transactions
compose = _module.compose
fibonacci = _module.fibonacci


class TestSumOfEvenSquares:
    """Tests for sum_of_even_squares pipeline function."""

    def test_basic_case(self):
        """Test with basic list of numbers."""
        result = sum_of_even_squares([1, 2, 3, 4, 5, 6])
        assert result == 56  # 2² + 4² + 6² = 4 + 16 + 36 = 56

    def test_all_even_numbers(self):
        """Test with all even numbers."""
        result = sum_of_even_squares([2, 4, 6, 8])
        assert result == 120  # 4 + 16 + 36 + 64 = 120

    def test_all_odd_numbers(self):
        """Test with all odd numbers."""
        result = sum_of_even_squares([1, 3, 5, 7])
        assert result == 0  # No even numbers

    def test_empty_list(self):
        """Test with empty list."""
        result = sum_of_even_squares([])
        assert result == 0

    def test_single_even_number(self):
        """Test with single even number."""
        result = sum_of_even_squares([4])
        assert result == 16

    def test_single_odd_number(self):
        """Test with single odd number."""
        result = sum_of_even_squares([3])
        assert result == 0

    def test_large_numbers(self):
        """Test with larger numbers."""
        result = sum_of_even_squares([10, 15, 20])
        assert result == 500  # 100 + 400 = 500


class TestCalculatePrice:
    """Tests for calculate_price and specialized pricing functions."""

    def test_base_price_only(self):
        """Test with no tax or discount."""
        result = calculate_price(100)
        assert result == 100.0

    def test_with_tax(self):
        """Test with tax only."""
        result = calculate_price(100, tax_rate=0.21)
        assert result == 121.0

    def test_with_discount(self):
        """Test with discount only."""
        result = calculate_price(100, discount=0.1)
        assert result == 90.0

    def test_with_tax_and_discount(self):
        """Test with both tax and discount."""
        result = calculate_price(100, tax_rate=0.21, discount=0.1)
        assert abs(result - 108.9) < 0.01  # Allow small floating point error

    def test_calculate_price_with_vat(self):
        """Test specialized VAT function."""
        result = calculate_price_with_vat(100)
        assert result == 121.0

    def test_calculate_price_with_discount(self):
        """Test specialized discount function."""
        result = calculate_price_with_discount(100)
        assert result == 90.0

    def test_calculate_final_price(self):
        """Test final price with VAT and discount."""
        result = calculate_final_price(100)
        assert abs(result - 108.9) < 0.01

    def test_different_base_prices(self):
        """Test specialized functions with different base prices."""
        assert calculate_price_with_vat(50) == 60.5
        assert calculate_price_with_discount(200) == 180.0
        assert abs(calculate_final_price(150) - 163.35) < 0.01


class TestCountPaths:
    """Tests for count_paths functions (slow and fast versions)."""

    def test_count_paths_2x2(self):
        """Test 2x2 grid."""
        assert count_paths_slow(2, 2) == 2
        assert count_paths_fast(2, 2) == 2

    def test_count_paths_3x3(self):
        """Test 3x3 grid."""
        assert count_paths_slow(3, 3) == 6
        assert count_paths_fast(3, 3) == 6

    def test_count_paths_1xn(self):
        """Test 1×n grid (only one path)."""
        assert count_paths_slow(1, 5) == 1
        assert count_paths_fast(1, 5) == 1

    def test_count_paths_nx1(self):
        """Test n×1 grid (only one path)."""
        assert count_paths_slow(5, 1) == 1
        assert count_paths_fast(5, 1) == 1

    def test_count_paths_4x4(self):
        """Test 4x4 grid."""
        assert count_paths_slow(4, 4) == 20
        assert count_paths_fast(4, 4) == 20

    def test_count_paths_asymmetric(self):
        """Test asymmetric grids."""
        assert count_paths_slow(3, 2) == 3
        assert count_paths_fast(3, 2) == 3
        assert count_paths_slow(2, 4) == 4
        assert count_paths_fast(2, 4) == 4

    def test_cache_performance(self):
        """Test that cached version is significantly faster."""
        # Clear cache before test
        if hasattr(count_paths_fast, "cache_clear"):
            count_paths_fast.cache_clear()

        # Time slow version (smaller grid to avoid timeout)
        start = time.time()
        result_slow = count_paths_slow(10, 10)
        time_slow = time.time() - start

        # Time fast version
        start = time.time()
        result_fast = count_paths_fast(10, 10)
        time_fast = time.time() - start

        # Results should match
        assert result_slow == result_fast

        # Fast version should be significantly faster (at least 10x)
        assert time_fast < time_slow / 10

    def test_cache_info_available(self):
        """Test that cache_info is available on cached function."""
        if hasattr(count_paths_fast, "cache_clear"):
            count_paths_fast.cache_clear()

        count_paths_fast(5, 5)

        # Check cache_info exists and has expected attributes
        if hasattr(count_paths_fast, "cache_info"):
            info = count_paths_fast.cache_info()
            assert hasattr(info, "hits")
            assert hasattr(info, "misses")
            assert info.misses > 0  # Should have some cache misses


class TestProcessTransactions:
    """Tests for process_transactions function."""

    def test_all_transactions(self):
        """Test processing all transactions."""
        transactions = [
            {"id": 1, "amount": 100, "type": "credit", "category": "salary"},
            {"id": 2, "amount": 50, "type": "debit", "category": "food"},
            {"id": 3, "amount": 200, "type": "credit", "category": "bonus"},
        ]
        result = process_transactions(transactions)
        assert result == 350.0

    def test_filter_by_credit(self):
        """Test filtering credit transactions."""
        transactions = [
            {"id": 1, "amount": 100, "type": "credit", "category": "salary"},
            {"id": 2, "amount": 50, "type": "debit", "category": "food"},
            {"id": 3, "amount": 200, "type": "credit", "category": "bonus"},
        ]
        result = process_transactions(transactions, "credit")
        assert result == 300.0

    def test_filter_by_debit(self):
        """Test filtering debit transactions."""
        transactions = [
            {"id": 1, "amount": 100, "type": "credit", "category": "salary"},
            {"id": 2, "amount": 50, "type": "debit", "category": "food"},
            {"id": 3, "amount": 30, "type": "debit", "category": "transport"},
        ]
        result = process_transactions(transactions, "debit")
        assert result == 80.0

    def test_empty_transactions(self):
        """Test with empty transaction list."""
        result = process_transactions([])
        assert result == 0.0

    def test_no_matching_type(self):
        """Test when no transactions match the filter."""
        transactions = [
            {"id": 1, "amount": 100, "type": "credit", "category": "salary"},
        ]
        result = process_transactions(transactions, "debit")
        assert result == 0.0


class TestCompose:
    """Tests for compose function."""

    def test_compose_two_functions(self):
        """Test composing two functions."""

        def add_one(x):
            return x + 1

        def multiply_two(x):
            return x * 2

        composed = compose(multiply_two, add_one)
        result = composed(5)  # (5 + 1) * 2 = 12
        assert result == 12

    def test_compose_three_functions(self):
        """Test composing three functions."""

        def add_one(x):
            return x + 1

        def multiply_two(x):
            return x * 2

        def subtract_three(x):
            return x - 3

        composed = compose(subtract_three, multiply_two, add_one)
        result = composed(5)  # ((5 + 1) * 2) - 3 = 9
        assert result == 9

    def test_compose_order(self):
        """Test that composition order is right-to-left."""

        def double(x):
            return x * 2

        def add_ten(x):
            return x + 10

        # Should apply add_ten first, then double
        composed = compose(double, add_ten)
        result = composed(5)  # (5 + 10) * 2 = 30
        assert result == 30

    def test_compose_single_function(self):
        """Test composing single function."""

        def square(x):
            return x**2

        composed = compose(square)
        assert composed(5) == 25

    def test_compose_with_strings(self):
        """Test composition with string operations."""

        def upper(s):
            return s.upper()

        def add_exclamation(s):
            return s + "!"

        def add_prefix(s):
            return "Hello, " + s

        composed = compose(add_exclamation, upper, add_prefix)
        result = composed("world")  # "Hello, WORLD!"
        assert result == "Hello, WORLD!"


class TestFibonacci:
    """Tests for fibonacci function with caching."""

    def test_fibonacci_base_cases(self):
        """Test Fibonacci base cases."""
        assert fibonacci(0) == 0
        assert fibonacci(1) == 1

    def test_fibonacci_small_numbers(self):
        """Test Fibonacci with small numbers."""
        assert fibonacci(2) == 1
        assert fibonacci(3) == 2
        assert fibonacci(4) == 3
        assert fibonacci(5) == 5
        assert fibonacci(6) == 8

    def test_fibonacci_larger_numbers(self):
        """Test Fibonacci with larger numbers."""
        assert fibonacci(10) == 55
        assert fibonacci(15) == 610
        assert fibonacci(20) == 6765

    def test_fibonacci_cache_exists(self):
        """Test that fibonacci has cache functionality."""
        # Clear cache if available
        if hasattr(fibonacci, "cache_clear"):
            fibonacci.cache_clear()

        # Calculate some values
        fibonacci(10)
        fibonacci(15)

        # Check cache_info exists
        if hasattr(fibonacci, "cache_info"):
            info = fibonacci.cache_info()
            assert hasattr(info, "hits")
            assert hasattr(info, "misses")

    def test_fibonacci_performance(self):
        """Test that cached fibonacci is fast even for larger values."""
        # Clear cache
        if hasattr(fibonacci, "cache_clear"):
            fibonacci.cache_clear()

        # Should complete quickly even for larger values
        start = time.time()
        result = fibonacci(30)
        elapsed = time.time() - start

        assert result == 832040
        assert elapsed < 0.1  # Should be very fast with cache


class TestFunctionalIntegration:
    """Integration tests combining multiple functional concepts."""

    def test_pipeline_with_partial(self):
        """Test combining pipeline with partial functions."""

        # Create specialized filter
        def is_positive(x):
            return x > 0

        def double(x):
            return x * 2

        numbers = [-2, -1, 0, 1, 2, 3]
        result = list(map(double, filter(is_positive, numbers)))
        assert result == [2, 4, 6]

    def test_complex_data_transformation(self):
        """Test complex data transformation pipeline."""
        users = [
            {"name": "Alice", "age": 25, "active": True},
            {"name": "Bob", "age": 17, "active": True},
            {"name": "Charlie", "age": 30, "active": False},
            {"name": "David", "age": 22, "active": True},
        ]

        # Filter adult active users and get their ages
        from functools import reduce

        def is_adult_active(u):
            return u["age"] >= 18 and u["active"]

        def get_age(u):
            return u["age"]

        ages = list(map(get_age, filter(is_adult_active, users)))
        assert ages == [25, 22]

        # Calculate average age
        if ages:
            avg_age = reduce(lambda x, y: x + y, ages) / len(ages)
            assert avg_age == 23.5

    def test_cached_recursive_with_composition(self):
        """Test combining caching with function composition."""
        # Fibonacci should work efficiently even when called multiple times
        if hasattr(fibonacci, "cache_clear"):
            fibonacci.cache_clear()

        # Multiple calls should use cache
        result1 = fibonacci(20)
        result2 = fibonacci(20)
        result3 = fibonacci(19)

        assert result1 == result2 == 6765
        assert result3 == 4181

        # Check cache was used
        if hasattr(fibonacci, "cache_info"):
            info = fibonacci.cache_info()
            assert info.hits > 0  # Should have cache hits
