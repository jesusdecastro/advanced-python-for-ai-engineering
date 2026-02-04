"""
Tests for Classes and SRP exercises.
"""

import pytest


class TestSRP:
    """Tests for Single Responsibility Principle exercises."""
    
    def test_user_class_exists(self):
        """Test that User class exists."""
        from exercises.03_classes_srp import User
        user = User("alice", "alice@example.com", "password123")
        assert user.username == "alice"
