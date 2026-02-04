"""
Tests for Clean Functions exercises.
"""

import pytest
import sys
from pathlib import Path

# Add parent directory to path to import exercises
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# Import using importlib to handle module name starting with number
import importlib.util
spec = importlib.util.spec_from_file_location(
    "clean_functions",
    Path(__file__).parent.parent / "01_clean_functions.py"
)
clean_functions = importlib.util.module_from_spec(spec)
spec.loader.exec_module(clean_functions)

process_customer_order = clean_functions.process_customer_order
create_product = clean_functions.create_product
generate_sales_report = clean_functions.generate_sales_report


class TestExercise1RefactorMultipleResponsibilities:
    """Test refactoring of function with multiple responsibilities."""
    
    def test_process_customer_order_calculates_total(self):
        """Test that order processing calculates correct total with tax."""
        order_data = {
            'customer_id': 'CUST123',
            'items': [
                {'price': 10.0, 'quantity': 2, 'discount': 0},
                {'price': 5.0, 'quantity': 1, 'discount': 0.1}
            ]
        }
        
        # Subtotal: (10 * 2) + (5 * 1 * 0.9) = 20 + 4.5 = 24.5
        # With 8% tax: 24.5 * 1.08 = 26.46
        result = process_customer_order(order_data)
        assert abs(result - 26.46) < 0.01
    
    def test_process_customer_order_validates_customer_id(self):
        """Test that missing customer ID raises error."""
        order_data = {
            'items': [{'price': 10.0, 'quantity': 1}]
        }
        
        with pytest.raises(ValueError, match='Customer ID required'):
            process_customer_order(order_data)
    
    def test_process_customer_order_validates_items(self):
        """Test that empty items raises error."""
        order_data = {
            'customer_id': 'CUST123',
            'items': []
        }
        
        with pytest.raises(ValueError, match='Order must have items'):
            process_customer_order(order_data)


class TestExercise2ReduceParameters:
    """Test parameter reduction using dataclasses."""
    
    def test_create_product_with_all_parameters(self):
        """Test product creation with all parameters."""
        result = create_product(
            name='Laptop',
            description='High-performance laptop',
            price=999.99,
            currency='USD',
            category='Electronics',
            brand='TechBrand',
            sku='LAP-001',
            weight=2.5,
            dimensions_length=35.0,
            dimensions_width=25.0,
            dimensions_height=2.0
        )
        
        assert result['name'] == 'Laptop'
        assert result['price'] == 999.99
        assert result['dimensions']['length'] == 35.0
    
    def test_create_product_groups_dimensions(self):
        """Test that dimensions are properly grouped."""
        result = create_product(
            'Mouse', 'Wireless mouse', 29.99, 'USD', 'Accessories',
            'TechBrand', 'MOU-001', 0.1, 10.0, 6.0, 3.0
        )
        
        assert 'dimensions' in result
        assert result['dimensions']['length'] == 10.0
        assert result['dimensions']['width'] == 6.0
        assert result['dimensions']['height'] == 3.0


class TestExercise3SeparateAbstractionLevels:
    """Test separation of abstraction levels."""
    
    def test_generate_sales_report_filters_valid_sales(self):
        """Test that report only includes completed sales."""
        sales_data = [
            {'status': 'completed', 'amount': 100.0, 'product_id': 'P1'},
            {'status': 'pending', 'amount': 50.0, 'product_id': 'P2'},
            {'status': 'completed', 'amount': 75.0, 'product_id': 'P1'},
        ]
        
        report = generate_sales_report(sales_data)
        
        # Should only include completed sales: 100 + 75 = 175
        assert 'Total Revenue: $175.00' in report
    
    def test_generate_sales_report_calculates_average(self):
        """Test that report calculates correct average."""
        sales_data = [
            {'status': 'completed', 'amount': 100.0, 'product_id': 'P1'},
            {'status': 'completed', 'amount': 50.0, 'product_id': 'P2'},
        ]
        
        report = generate_sales_report(sales_data)
        
        # Average: (100 + 50) / 2 = 75
        assert 'Average Sale: $75.00' in report
    
    def test_generate_sales_report_groups_by_product(self):
        """Test that report groups sales by product."""
        sales_data = [
            {'status': 'completed', 'amount': 100.0, 'product_id': 'P1'},
            {'status': 'completed', 'amount': 75.0, 'product_id': 'P1'},
            {'status': 'completed', 'amount': 50.0, 'product_id': 'P2'},
        ]
        
        report = generate_sales_report(sales_data)
        
        assert 'P1' in report
        assert 'P2' in report
        # P1 should have 2 sales totaling $175
        assert '2 sales' in report
    
    def test_generate_sales_report_handles_empty_data(self):
        """Test that report handles empty sales data."""
        sales_data = []
        
        report = generate_sales_report(sales_data)
        
        assert 'Total Revenue: $0.00' in report
        assert 'Average Sale: $0.00' in report


# Additional tests for refactored functions (students will implement these)
class TestRefactoredFunctions:
    """Tests for refactored helper functions."""
    
    def test_refactored_functions_exist(self):
        """Test that students have created the refactored functions."""
        # This test will pass once students implement the refactored versions
        try:
            validate_order_data = getattr(clean_functions, 'validate_order_data', None)
            calculate_items_subtotal = getattr(clean_functions, 'calculate_items_subtotal', None)
            apply_tax = getattr(clean_functions, 'apply_tax', None)
            
            if validate_order_data and calculate_items_subtotal and apply_tax:
                assert callable(validate_order_data)
                assert callable(calculate_items_subtotal)
                assert callable(apply_tax)
            else:
                pytest.skip("Refactored functions not yet implemented")
        except Exception:
            pytest.skip("Refactored functions not yet implemented")
