"""
Tests for Inheritance vs Composition exercises.
"""

import pytest


class TestComposition:
    """Tests for composition exercises."""
    
    def test_car_exists(self):
        """Test that Car class exists."""
        from exercises.04_inheritance_vs_composition import Car
        car = Car()
        assert car is not None
