"""
Tests for SOLID Principles exercises.
"""

import pytest


class TestSOLID:
    """Tests for SOLID principles exercises."""
    
    def test_report_generator_exists(self):
        """Test that ReportGenerator class exists."""
        from exercises.06_solid_principles import ReportGenerator
        generator = ReportGenerator()
        assert generator is not None
