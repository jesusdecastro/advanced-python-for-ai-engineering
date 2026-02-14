"""Fixtures para tests del Bloque 3."""

import pytest


@pytest.fixture
def positive_words():
    """Common positive sentiment words."""
    return {"great", "amazing", "wonderful", "excellent", "good", "love", "best"}


@pytest.fixture
def negative_words():
    """Common negative sentiment words."""
    return {"terrible", "awful", "bad", "worst", "hate", "horrible", "poor"}


@pytest.fixture
def sample_reviews():
    """Sample reviews for testing."""
    from exercises.bloque_3.scoring import Review

    return [
        Review(text="This product is great and amazing", rating=5, product="Widget A"),
        Review(text="Terrible quality, very bad", rating=1, product="Widget B"),
        Review(text="The product arrived yesterday", rating=3, product="Widget C"),
    ]
