"""Fixtures para tests del Bloque 2."""

import pytest


@pytest.fixture
def common_stopwords():
    """Common English stopwords."""
    return {"the", "is", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for"}


@pytest.fixture
def sample_text():
    """Sample text for preprocessing."""
    return "  The QUICK brown FOX jumps over the lazy DOG  "


@pytest.fixture
def sample_text_with_punctuation():
    """Sample text with punctuation."""
    return "Hello, world! This is a test."


@pytest.fixture
def text_with_short_tokens():
    """Text with short tokens."""
    return "I am a big cat"
