"""Tests para ejercicios del Bloque 2: Composición sobre Herencia."""

import pytest

from exercises.bloque_2.preprocessing import (
    LowercaseNormalizer,
    MinLengthFilter,
    PreprocessingResult,
    RegexTokenizer,
    StopwordFilter,
    TextPreprocessingPipeline,
    WhitespaceTokenizer,
)


# ============================================================================
# TESTS: LowercaseNormalizer
# ============================================================================
def test_lowercase_normalizer():
    """Test LowercaseNormalizer converts to lowercase."""
    normalizer = LowercaseNormalizer()
    result = normalizer.normalize("Hello WORLD")
    assert result == "hello world"


def test_lowercase_normalizer_strips_extra_spaces():
    """Test LowercaseNormalizer strips extra spaces."""
    normalizer = LowercaseNormalizer()
    result = normalizer.normalize("  hello   world  ")
    assert result == "hello world"


# ============================================================================
# TESTS: WhitespaceTokenizer
# ============================================================================
def test_whitespace_tokenizer():
    """Test WhitespaceTokenizer splits by spaces."""
    tokenizer = WhitespaceTokenizer()
    result = tokenizer.tokenize("hello world foo")
    assert result == ["hello", "world", "foo"]


def test_whitespace_tokenizer_empty_string():
    """Test WhitespaceTokenizer handles empty string."""
    tokenizer = WhitespaceTokenizer()
    result = tokenizer.tokenize("")
    assert result == [""]


# ============================================================================
# TESTS: RegexTokenizer
# ============================================================================
def test_regex_tokenizer_with_comma_pattern():
    """Test RegexTokenizer with comma pattern."""
    tokenizer = RegexTokenizer(pattern=r",+")
    result = tokenizer.tokenize("a,b,,c")
    assert result == ["a", "b", "c"]


def test_regex_tokenizer_with_whitespace_pattern():
    """Test RegexTokenizer with whitespace pattern."""
    tokenizer = RegexTokenizer(pattern=r"\s+")
    result = tokenizer.tokenize("hello  world   foo")
    assert result == ["hello", "world", "foo"]


# ============================================================================
# TESTS: StopwordFilter
# ============================================================================
def test_stopword_filter(common_stopwords):
    """Test StopwordFilter removes stopwords."""
    filter_obj = StopwordFilter(stopwords=common_stopwords)
    tokens = ["the", "cat", "is", "big"]
    result = filter_obj.filter_tokens(tokens)
    assert result == ["cat", "big"]


def test_stopword_filter_no_stopwords():
    """Test StopwordFilter with no stopwords."""
    filter_obj = StopwordFilter(stopwords=set())
    tokens = ["the", "cat", "is", "big"]
    result = filter_obj.filter_tokens(tokens)
    assert result == tokens


# ============================================================================
# TESTS: MinLengthFilter
# ============================================================================
def test_min_length_filter():
    """Test MinLengthFilter removes short tokens."""
    filter_obj = MinLengthFilter(min_length=2)
    tokens = ["I", "am", "big"]
    result = filter_obj.filter_tokens(tokens)
    assert result == ["am", "big"]


def test_min_length_filter_default():
    """Test MinLengthFilter with default min_length."""
    filter_obj = MinLengthFilter()
    tokens = ["I", "am", "big"]
    result = filter_obj.filter_tokens(tokens)
    assert result == ["am", "big"]


def test_min_length_filter_min_length_3():
    """Test MinLengthFilter with min_length=3."""
    filter_obj = MinLengthFilter(min_length=3)
    tokens = ["I", "am", "big", "cat"]
    result = filter_obj.filter_tokens(tokens)
    assert result == ["big", "cat"]


# ============================================================================
# TESTS: TextPreprocessingPipeline
# ============================================================================
def test_pipeline_composes_all_steps(sample_text, common_stopwords):
    """Test pipeline composes all steps correctly."""
    normalizer = LowercaseNormalizer()
    tokenizer = WhitespaceTokenizer()
    filters = [StopwordFilter(stopwords=common_stopwords)]

    pipeline = TextPreprocessingPipeline(
        normalizer=normalizer, tokenizer=tokenizer, filters=filters
    )

    result = pipeline.process(sample_text)

    assert isinstance(result, PreprocessingResult)
    assert result.original_text == sample_text
    assert result.normalized_text == "the quick brown fox jumps over the lazy dog"
    assert "quick" in result.tokens
    assert "the" not in result.filtered_tokens
    assert "quick" in result.filtered_tokens


def test_pipeline_with_multiple_filters(common_stopwords):
    """Test pipeline with multiple filters applied in order."""
    normalizer = LowercaseNormalizer()
    tokenizer = WhitespaceTokenizer()
    filters = [
        StopwordFilter(stopwords=common_stopwords),
        MinLengthFilter(min_length=4),
    ]

    pipeline = TextPreprocessingPipeline(
        normalizer=normalizer, tokenizer=tokenizer, filters=filters
    )

    result = pipeline.process("The cat is a big animal")

    # After stopword filter: ["cat", "big", "animal"]
    # After min length filter: ["animal"]
    assert result.filtered_tokens == ["animal"]


def test_pipeline_with_different_tokenizer():
    """Test pipeline with RegexTokenizer instead of WhitespaceTokenizer."""
    normalizer = LowercaseNormalizer()
    tokenizer = RegexTokenizer(pattern=r"[,\s]+")
    filters = []

    pipeline = TextPreprocessingPipeline(
        normalizer=normalizer, tokenizer=tokenizer, filters=filters
    )

    result = pipeline.process("Hello, world, foo")

    assert result.tokens == ["hello", "world", "foo"]
    assert result.filtered_tokens == ["hello", "world", "foo"]


def test_result_is_frozen_dataclass():
    """Test PreprocessingResult is frozen (immutable)."""
    result = PreprocessingResult(
        original_text="test",
        normalized_text="test",
        tokens=["test"],
        filtered_tokens=["test"],
    )

    with pytest.raises(Exception):  # FrozenInstanceError
        result.tokens = ["modified"]


def test_normalizer_fulfills_protocol():
    """Test normalizer fulfills TextNormalizer protocol."""
    from exercises.bloque_2.protocols import TextNormalizer

    normalizer = LowercaseNormalizer()

    # Should have normalize method
    assert hasattr(normalizer, "normalize")
    assert callable(normalizer.normalize)

    # Should work as TextNormalizer
    def process_with_normalizer(norm: TextNormalizer, text: str) -> str:
        return norm.normalize(text)

    result = process_with_normalizer(normalizer, "TEST")
    assert result == "test"


def test_components_have_no_shared_state():
    """Test processing different texts produces independent results."""
    normalizer = LowercaseNormalizer()
    tokenizer = WhitespaceTokenizer()
    filters = []

    pipeline = TextPreprocessingPipeline(
        normalizer=normalizer, tokenizer=tokenizer, filters=filters
    )

    result1 = pipeline.process("First text")
    result2 = pipeline.process("Second text")

    assert result1.original_text != result2.original_text
    assert result1.tokens != result2.tokens
