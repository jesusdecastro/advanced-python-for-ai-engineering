"""
Tests for Abstract Base Classes exercises.
"""

import pytest


class TestABC:
    """Tests for ABC exercises."""
    
    def test_data_processor_exists(self):
        """Test that DataProcessor ABC exists."""
        from exercises.05_abstract_base_classes import DataProcessor
        assert DataProcessor is not None
