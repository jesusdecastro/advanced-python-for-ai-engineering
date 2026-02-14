"""Tests para ejercicios del Bloque 3: SRP + DIP."""

import pytest
from pydantic import ValidationError

from exercises.bloque_3.scoring import (
    InMemoryResultSaver,
    InMemoryReviewLoader,
    KeywordSentimentAnalyzer,
    Review,
    ScoringResult,
    ScoringService,
)


# ============================================================================
# TESTS: Review Model
# ============================================================================
def test_review_validation_rejects_rating_zero():
    """Test Review rejects rating 0."""
    with pytest.raises(ValidationError):
        Review(text="Test review", rating=0, product="Widget")


def test_review_validation_rejects_rating_six():
    """Test Review rejects rating 6."""
    with pytest.raises(ValidationError):
        Review(text="Test review", rating=6, product="Widget")


def test_review_validation_rejects_empty_text():
    """Test Review rejects empty text."""
    with pytest.raises(ValidationError):
        Review(text="", rating=5, product="Widget")


def test_review_valid_creates_successfully():
    """Test Review with valid data creates successfully."""
    review = Review(text="Great product", rating=5, product="Widget")
    assert review.text == "Great product"
    assert review.rating == 5
    assert review.product == "Widget"


# ============================================================================
# TESTS: KeywordSentimentAnalyzer
# ============================================================================
def test_keyword_analyzer_positive_text(positive_words, negative_words):
    """Test analyzer returns positive score for positive text."""
    analyzer = KeywordSentimentAnalyzer(
        positive_words=positive_words, negative_words=negative_words
    )
    score = analyzer.analyze("great amazing wonderful")
    assert score > 0


def test_keyword_analyzer_negative_text(positive_words, negative_words):
    """Test analyzer returns negative score for negative text."""
    analyzer = KeywordSentimentAnalyzer(
        positive_words=positive_words, negative_words=negative_words
    )
    score = analyzer.analyze("terrible awful bad")
    assert score < 0


def test_keyword_analyzer_neutral_text(positive_words, negative_words):
    """Test analyzer returns neutral score for neutral text."""
    analyzer = KeywordSentimentAnalyzer(
        positive_words=positive_words, negative_words=negative_words
    )
    score = analyzer.analyze("the product arrived yesterday")
    assert score == 0.0


def test_keyword_analyzer_score_is_clamped(positive_words, negative_words):
    """Test analyzer clamps score to [-1.0, 1.0]."""
    analyzer = KeywordSentimentAnalyzer(
        positive_words=positive_words, negative_words=negative_words
    )
    score = analyzer.analyze("great great great great great")
    assert -1.0 <= score <= 1.0


def test_keyword_analyzer_empty_text_returns_zero(positive_words, negative_words):
    """Test analyzer returns 0.0 for empty text."""
    analyzer = KeywordSentimentAnalyzer(
        positive_words=positive_words, negative_words=negative_words
    )
    score = analyzer.analyze("")
    assert score == 0.0


# ============================================================================
# TESTS: ScoringService
# ============================================================================
def test_scoring_service_processes_all_reviews(
    sample_reviews, positive_words, negative_words
):
    """Test ScoringService processes all reviews."""
    loader = InMemoryReviewLoader(reviews=sample_reviews)
    analyzer = KeywordSentimentAnalyzer(
        positive_words=positive_words, negative_words=negative_words
    )
    saver = InMemoryResultSaver()

    service = ScoringService(loader=loader, analyzer=analyzer, saver=saver)
    results = service.run()

    assert len(results) == 3
    assert len(saver.results) == 3


def test_scoring_service_uses_injected_analyzer(sample_reviews):
    """Test ScoringService uses injected analyzer (DIP verification)."""

    # Fake analyzer that always returns 0.99
    class FakeAnalyzer:
        def analyze(self, text: str) -> float:
            return 0.99

    loader = InMemoryReviewLoader(reviews=sample_reviews)
    analyzer = FakeAnalyzer()
    saver = InMemoryResultSaver()

    service = ScoringService(loader=loader, analyzer=analyzer, saver=saver)
    results = service.run()

    # All scores should be 0.99 because we injected FakeAnalyzer
    for result in results:
        assert result.sentiment_score == 0.99


def test_scoring_service_labels_are_correct(positive_words, negative_words):
    """Test ScoringService assigns correct labels."""
    from exercises.bloque_3.scoring import Review

    reviews = [
        Review(text="great amazing wonderful excellent", rating=5, product="A"),
        Review(text="terrible awful bad horrible", rating=1, product="B"),
        Review(text="the product is okay", rating=3, product="C"),
    ]

    loader = InMemoryReviewLoader(reviews=reviews)
    analyzer = KeywordSentimentAnalyzer(
        positive_words=positive_words, negative_words=negative_words
    )
    saver = InMemoryResultSaver()

    service = ScoringService(loader=loader, analyzer=analyzer, saver=saver)
    results = service.run()

    # First review should be positive
    assert results[0].label == "positive"
    # Second review should be negative
    assert results[1].label == "negative"
    # Third review should be neutral
    assert results[2].label == "neutral"


def test_scoring_result_is_immutable():
    """Test ScoringResult is frozen (immutable)."""
    result = ScoringResult(
        review_text="test",
        sentiment_score=0.5,
        label="positive",
        scored_at="2024-01-01T00:00:00",
    )

    with pytest.raises(Exception):  # FrozenInstanceError
        result.sentiment_score = 0.9


def test_in_memory_saver_accumulates_results():
    """Test InMemoryResultSaver accumulates results from multiple saves."""
    saver = InMemoryResultSaver()

    results1 = [
        ScoringResult(
            review_text="test1",
            sentiment_score=0.5,
            label="positive",
            scored_at="2024-01-01T00:00:00",
        )
    ]
    results2 = [
        ScoringResult(
            review_text="test2",
            sentiment_score=-0.5,
            label="negative",
            scored_at="2024-01-01T00:00:01",
        )
    ]

    saver.save(results1)
    saver.save(results2)

    assert len(saver.results) == 2
    assert saver.results[0].review_text == "test1"
    assert saver.results[1].review_text == "test2"


def test_scoring_service_creates_results_with_timestamps(
    sample_reviews, positive_words, negative_words
):
    """Test ScoringService creates results with timestamps."""
    loader = InMemoryReviewLoader(reviews=sample_reviews)
    analyzer = KeywordSentimentAnalyzer(
        positive_words=positive_words, negative_words=negative_words
    )
    saver = InMemoryResultSaver()

    service = ScoringService(loader=loader, analyzer=analyzer, saver=saver)
    results = service.run()

    for result in results:
        assert isinstance(result.scored_at, str)
        assert len(result.scored_at) > 0
