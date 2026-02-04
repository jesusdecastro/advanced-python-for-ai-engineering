"""
Tests for memory profiling exercises.
"""

import pytest
import numpy as np
import sys

# Import the module
sys.path.insert(0, 'day_5')
from exercises import memory_profiling as mp


class TestCreateOptimizedArrays:
    """Tests for create_optimized_arrays function."""
    
    def test_ages_dtype(self):
        """Test that ages use int8 dtype."""
        ages = [25, 30, 35, 40, 45]
        scores = [85, 90, 78, 92, 88]
        ids = [1001, 1002, 1003, 1004, 1005]
        
        result = mp.create_optimized_arrays(ages, scores, ids)
        
        assert result['ages'].dtype == np.int8
    
    def test_scores_dtype(self):
        """Test that scores use int8 dtype."""
        ages = [25, 30, 35]
        scores = [85, 90, 78]
        ids = [1001, 1002, 1003]
        
        result = mp.create_optimized_arrays(ages, scores, ids)
        
        assert result['scores'].dtype == np.int8
    
    def test_ids_dtype(self):
        """Test that ids use int32 dtype."""
        ages = [25, 30, 35]
        scores = [85, 90, 78]
        ids = [100000, 200000, 300000]
        
        result = mp.create_optimized_arrays(ages, scores, ids)
        
        assert result['ids'].dtype == np.int32
    
    def test_values_preserved(self):
        """Test that values are preserved after optimization."""
        ages = [25, 30, 35]
        scores = [85, 90, 78]
        ids = [1001, 1002, 1003]
        
        result = mp.create_optimized_arrays(ages, scores, ids)
        
        assert result['ages'].tolist() == ages
        assert result['scores'].tolist() == scores
        assert result['ids'].tolist() == ids


class TestSquaresGenerator:
    """Tests for squares_generator function."""
    
    def test_generates_squares(self):
        """Test that generator produces correct squares."""
        result = list(mp.squares_generator(5))
        expected = [0, 1, 4, 9, 16]
        
        assert result == expected
    
    def test_is_generator(self):
        """Test that function returns a generator."""
        result = mp.squares_generator(10)
        
        assert hasattr(result, '__iter__')
        assert hasattr(result, '__next__')
    
    def test_empty_case(self):
        """Test generator with n=0."""
        result = list(mp.squares_generator(0))
        
        assert result == []
    
    def test_large_n(self):
        """Test generator with large n."""
        result = list(mp.squares_generator(100))
        
        assert len(result) == 100
        assert result[99] == 99**2


class TestProcessLargeListInChunks:
    """Tests for process_large_list_in_chunks function."""
    
    def test_correct_sum(self):
        """Test that chunked processing produces correct sum."""
        data = range(1000)
        result = mp.process_large_list_in_chunks(data, chunk_size=100)
        expected = sum(x**2 for x in range(1000))
        
        assert result == expected
    
    def test_different_chunk_sizes(self):
        """Test with different chunk sizes."""
        data = range(500)
        result1 = mp.process_large_list_in_chunks(data, chunk_size=50)
        result2 = mp.process_large_list_in_chunks(data, chunk_size=100)
        expected = sum(x**2 for x in range(500))
        
        assert result1 == expected
        assert result2 == expected
    
    def test_small_data(self):
        """Test with data smaller than chunk size."""
        data = range(10)
        result = mp.process_large_list_in_chunks(data, chunk_size=100)
        expected = sum(x**2 for x in range(10))
        
        assert result == expected
    
    def test_exact_chunk_size(self):
        """Test when data size is exact multiple of chunk size."""
        data = range(1000)
        result = mp.process_large_list_in_chunks(data, chunk_size=100)
        expected = sum(x**2 for x in range(1000))
        
        assert result == expected


class TestFilterLargeDataset:
    """Tests for filter_large_dataset function."""
    
    def test_filters_correctly(self):
        """Test that filtering works correctly."""
        data = [1, 5, 3, 8, 2, 9, 4]
        result = list(mp.filter_large_dataset(data, 4))
        expected = [5, 8, 9]
        
        assert result == expected
    
    def test_is_generator(self):
        """Test that function returns a generator."""
        data = [1, 2, 3, 4, 5]
        result = mp.filter_large_dataset(data, 3)
        
        assert hasattr(result, '__iter__')
        assert hasattr(result, '__next__')
    
    def test_no_matches(self):
        """Test when no values match threshold."""
        data = [1, 2, 3]
        result = list(mp.filter_large_dataset(data, 10))
        
        assert result == []
    
    def test_all_match(self):
        """Test when all values match threshold."""
        data = [5, 6, 7, 8, 9]
        result = list(mp.filter_large_dataset(data, 4))
        
        assert result == data
    
    def test_boundary_value(self):
        """Test filtering at boundary value."""
        data = [3, 4, 5, 6]
        result = list(mp.filter_large_dataset(data, 4))
        
        assert result == [5, 6]


class TestCompareListVsGenerator:
    """Tests for compare_list_vs_generator function."""
    
    def test_returns_dict(self):
        """Test that function returns a dictionary."""
        result = mp.compare_list_vs_generator(100)
        
        assert isinstance(result, dict)
        assert 'list_size' in result
        assert 'generator_size' in result
    
    def test_list_larger_than_generator(self):
        """Test that list uses more memory than generator."""
        result = mp.compare_list_vs_generator(1000)
        
        assert result['list_size'] > result['generator_size']
    
    def test_sizes_are_positive(self):
        """Test that sizes are positive integers."""
        result = mp.compare_list_vs_generator(100)
        
        assert result['list_size'] > 0
        assert result['generator_size'] > 0
    
    def test_different_n_values(self):
        """Test with different n values."""
        result1 = mp.compare_list_vs_generator(100)
        result2 = mp.compare_list_vs_generator(10000)
        
        # List size should grow with n
        assert result2['list_size'] > result1['list_size']
        # Generator size should stay relatively constant
        assert abs(result2['generator_size'] - result1['generator_size']) < 1000
