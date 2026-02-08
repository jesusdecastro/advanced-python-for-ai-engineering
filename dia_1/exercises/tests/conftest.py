"""
Pytest configuration for type hinting exercises.

This file is automatically loaded by pytest and provides fixtures
and configuration for all tests.
"""

import sys
from pathlib import Path

# Add the parent directory to the path so we can import exercises
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
