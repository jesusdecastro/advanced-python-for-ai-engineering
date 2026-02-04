"""
Tests for pandas optimization exercises.
"""

import pytest
import pandas as pd
import numpy as np

# Import the module
import sys
sys.path.insert(0, 'day_5')
from exercises import pandas_optimization as po


class TestOptimizeDataframeDtypes:
    """Tests for optimize_dataframe_dtypes function."""
    
    def test_optimize_small_integers(self):
        """Test optimization of small integer values to int8."""
        df = pd.DataFrame({'age': [25, 30, 35, 40, 45]})
        result = po.optimize_dataframe_dtypes(df)
        
        assert result['age'].dtype == np.int8
    
    def test_optimize_medium_integers(self):
        """Test optimization of medium integer values to int16."""
        df = pd.DataFrame({'value': [1000, 2000, 3000, 4000]})
        result = po.optimize_dataframe_dtypes(df)
        
        assert result['value'].dtype in [np.int8, np.int16]
    
    def test_optimize_floats(self):
        """Test optimization of float64 to float32."""
        df = pd.DataFrame({'price': [10.5, 20.3, 30.7]})
        result = po.optimize_dataframe_dtypes(df)
        
        assert result['price'].dtype == np.float32
    
    def test_preserve_data_integrity(self):
        """Test that optimization preserves data values."""
        df = pd.DataFrame({'a': [1, 2, 3], 'b': [1.5, 2.5, 3.5]})
        result = po.optimize_dataframe_dtypes(df)
        
        pd.testing.assert_frame_equal(result, df, check_dtype=False)


class TestConvertToCategorical:
    """Tests for convert_to_categorical function."""
    
    def test_convert_low_cardinality(self):
        """Test conversion of low cardinality column to categorical."""
        df = pd.DataFrame({'country': ['USA', 'Canada', 'USA', 'Mexico', 'Canada']})
        result = po.convert_to_categorical(df, threshold=0.5)
        
        assert result['country'].dtype.name == 'category'
    
    def test_keep_high_cardinality(self):
        """Test that high cardinality columns are not converted."""
        df = pd.DataFrame({'id': ['A', 'B', 'C', 'D', 'E']})
        result = po.convert_to_categorical(df, threshold=0.5)
        
        assert result['id'].dtype == object
    
    def test_multiple_columns(self):
        """Test conversion with multiple columns."""
        df = pd.DataFrame({
            'country': ['USA', 'Canada', 'USA'],
            'city': ['NYC', 'Toronto', 'LA']
        })
        result = po.convert_to_categorical(df, threshold=0.5)
        
        assert result['country'].dtype.name == 'category'
    
    def test_custom_threshold(self):
        """Test conversion with custom threshold."""
        df = pd.DataFrame({'status': ['active', 'inactive', 'active', 'pending']})
        result = po.convert_to_categorical(df, threshold=0.8)
        
        assert result['status'].dtype.name == 'category'


class TestCalculateFinalPrices:
    """Tests for calculate_final_prices function."""
    
    def test_basic_calculation(self):
        """Test basic price calculation."""
        df = pd.DataFrame({
            'price': [100.0, 200.0],
            'quantity': [2, 1],
            'discount': [0.1, 0.2]
        })
        result = po.calculate_final_prices(df)
        
        assert 'final_price' in result.columns
        assert result['final_price'].tolist() == [180.0, 160.0]
    
    def test_no_discount(self):
        """Test calculation with zero discount."""
        df = pd.DataFrame({
            'price': [100.0],
            'quantity': [2],
            'discount': [0.0]
        })
        result = po.calculate_final_prices(df)
        
        assert result['final_price'].iloc[0] == 200.0
    
    def test_full_discount(self):
        """Test calculation with 100% discount."""
        df = pd.DataFrame({
            'price': [100.0],
            'quantity': [2],
            'discount': [1.0]
        })
        result = po.calculate_final_prices(df)
        
        assert result['final_price'].iloc[0] == 0.0
    
    def test_preserves_original_columns(self):
        """Test that original columns are preserved."""
        df = pd.DataFrame({
            'price': [100.0],
            'quantity': [2],
            'discount': [0.1]
        })
        result = po.calculate_final_prices(df)
        
        assert 'price' in result.columns
        assert 'quantity' in result.columns
        assert 'discount' in result.columns


class TestCompareMemoryUsage:
    """Tests for compare_memory_usage function."""
    
    def test_memory_comparison(self):
        """Test memory usage comparison."""
        df1 = pd.DataFrame({'a': np.arange(1000, dtype='int64')})
        df2 = pd.DataFrame({'a': np.arange(1000, dtype='int8')})
        
        result = po.compare_memory_usage(df1, df2)
        
        assert 'original_mb' in result
        assert 'optimized_mb' in result
        assert 'reduction_percent' in result
    
    def test_reduction_calculation(self):
        """Test that reduction percentage is calculated correctly."""
        df1 = pd.DataFrame({'a': np.arange(1000, dtype='int64')})
        df2 = pd.DataFrame({'a': np.arange(1000, dtype='int8')})
        
        result = po.compare_memory_usage(df1, df2)
        
        assert result['reduction_percent'] > 0
        assert result['reduction_percent'] < 100
    
    def test_optimized_smaller(self):
        """Test that optimized DataFrame uses less memory."""
        df1 = pd.DataFrame({'a': np.arange(1000, dtype='int64')})
        df2 = pd.DataFrame({'a': np.arange(1000, dtype='int8')})
        
        result = po.compare_memory_usage(df1, df2)
        
        assert result['optimized_mb'] < result['original_mb']


class TestCategorizeScores:
    """Tests for categorize_scores function."""
    
    def test_low_scores(self):
        """Test categorization of low scores."""
        df = pd.DataFrame({'score': [45, 50, 55]})
        result = po.categorize_scores(df)
        
        assert all(result['category'] == 'low')
    
    def test_medium_scores(self):
        """Test categorization of medium scores."""
        df = pd.DataFrame({'score': [60, 70, 75]})
        result = po.categorize_scores(df)
        
        assert all(result['category'] == 'medium')
    
    def test_high_scores(self):
        """Test categorization of high scores."""
        df = pd.DataFrame({'score': [80, 90, 95]})
        result = po.categorize_scores(df)
        
        assert all(result['category'] == 'high')
    
    def test_mixed_scores(self):
        """Test categorization of mixed scores."""
        df = pd.DataFrame({'score': [45, 70, 85, 92]})
        result = po.categorize_scores(df)
        
        expected = ['low', 'medium', 'high', 'high']
        assert result['category'].tolist() == expected
    
    def test_boundary_values(self):
        """Test categorization at boundary values."""
        df = pd.DataFrame({'score': [59, 60, 79, 80]})
        result = po.categorize_scores(df)
        
        expected = ['low', 'medium', 'medium', 'high']
        assert result['category'].tolist() == expected
    
    def test_custom_column_name(self):
        """Test with custom score column name."""
        df = pd.DataFrame({'test_score': [45, 70, 85]})
        result = po.categorize_scores(df, score_column='test_score')
        
        assert 'category' in result.columns
