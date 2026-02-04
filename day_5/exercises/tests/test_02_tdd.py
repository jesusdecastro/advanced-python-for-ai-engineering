"""
Tests for Test-Driven Development (TDD) exercises.

This test module demonstrates TDD by providing tests that guide implementation.
Students should run these tests and implement functionality to make them pass.

The tests follow the Red-Green-Refactor cycle:
- RED: Tests fail initially (no implementation)
- GREEN: Implement minimal code to pass tests
- REFACTOR: Improve code while keeping tests green
"""

import sys
from pathlib import Path

import pytest

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import from the exercise module
from tdd_exercises import ShoppingCart, TextAnalyzer, validate_isbn10

# ============================================================================
# Tests for Exercise 1: ISBN-10 Validator
# ============================================================================


def test_validate_isbn10_valid_numeric():
    """Test ISBN-10 validation with valid numeric ISBN."""
    # Valid ISBN-10: 0306406152
    assert validate_isbn10("0306406152") is True


def test_validate_isbn10_valid_with_x():
    """Test ISBN-10 validation with valid ISBN ending in X."""
    # Valid ISBN-10: 043942089X
    assert validate_isbn10("043942089X") is True


def test_validate_isbn10_invalid_length_short():
    """Test ISBN-10 validation fails with too few characters."""
    assert validate_isbn10("123456789") is False


def test_validate_isbn10_invalid_length_long():
    """Test ISBN-10 validation fails with too many characters."""
    assert validate_isbn10("12345678901") is False


def test_validate_isbn10_invalid_characters():
    """Test ISBN-10 validation fails with invalid characters."""
    assert validate_isbn10("12345A7890") is False


def test_validate_isbn10_invalid_x_position():
    """Test ISBN-10 validation fails with X not at the end."""
    assert validate_isbn10("X234567890") is False


def test_validate_isbn10_invalid_checksum():
    """Test ISBN-10 validation fails with invalid checksum."""
    # Invalid checksum
    assert validate_isbn10("0306406153") is False


def test_validate_isbn10_empty_string():
    """Test ISBN-10 validation fails with empty string."""
    assert validate_isbn10("") is False


def test_validate_isbn10_none():
    """Test ISBN-10 validation fails with None."""
    assert validate_isbn10(None) is False


def test_validate_isbn10_with_hyphens():
    """Test ISBN-10 validation with hyphens (should be removed)."""
    # ISBN with hyphens: 0-306-40615-2
    assert validate_isbn10("0-306-40615-2") is True


# ============================================================================
# Fixtures for Exercise 2: Shopping Cart
# ============================================================================


@pytest.fixture
def empty_cart():
    """Provide an empty shopping cart."""
    return ShoppingCart()


@pytest.fixture
def cart_with_items():
    """Provide a cart with sample items."""
    cart = ShoppingCart()
    cart.add_item("Apple", 1.0, 2)
    cart.add_item("Banana", 0.5, 3)
    cart.add_item("Orange", 0.75, 1)
    return cart


# ============================================================================
# Tests for Exercise 2: Shopping Cart with Discounts
# ============================================================================


def test_shopping_cart_initialization(empty_cart):
    """Test creating an empty shopping cart."""
    assert empty_cart.total() == 0.0


def test_shopping_cart_add_single_item(empty_cart):
    """Test adding a single item to the cart."""
    empty_cart.add_item("Apple", 1.0, 2)
    assert empty_cart.total() == 2.0


def test_shopping_cart_add_item_default_quantity(empty_cart):
    """Test adding an item with default quantity of 1."""
    empty_cart.add_item("Apple", 1.0)
    assert empty_cart.total() == 1.0


def test_shopping_cart_add_multiple_items(cart_with_items):
    """Test cart total with multiple items."""
    # Expected: (1.0 * 2) + (0.5 * 3) + (0.75 * 1) = 4.25
    assert cart_with_items.total() == 4.25


def test_shopping_cart_remove_item(cart_with_items):
    """Test removing an item from the cart."""
    cart_with_items.remove_item("Banana")
    # Expected: (1.0 * 2) + (0.75 * 1) = 2.75
    assert cart_with_items.total() == 2.75


def test_shopping_cart_remove_nonexistent_item(cart_with_items):
    """Test removing an item that doesn't exist (should not error)."""
    original_total = cart_with_items.total()
    cart_with_items.remove_item("Grape")
    assert cart_with_items.total() == original_total


def test_shopping_cart_apply_discount_10_percent(cart_with_items):
    """Test applying 10% discount code."""
    cart_with_items.apply_discount("SAVE10")
    # Expected: 4.25 * 0.9 = 3.825
    assert cart_with_items.total_with_discount() == pytest.approx(3.825)


def test_shopping_cart_apply_discount_20_percent(cart_with_items):
    """Test applying 20% discount code."""
    cart_with_items.apply_discount("SAVE20")
    # Expected: 4.25 * 0.8 = 3.4
    assert cart_with_items.total_with_discount() == pytest.approx(3.4)


def test_shopping_cart_apply_invalid_discount(cart_with_items):
    """Test applying invalid discount code (should not change total)."""
    cart_with_items.apply_discount("INVALID")
    assert cart_with_items.total_with_discount() == cart_with_items.total()


def test_shopping_cart_total_without_discount(cart_with_items):
    """Test total without applying discount."""
    assert cart_with_items.total_with_discount() == cart_with_items.total()


def test_shopping_cart_clear(cart_with_items):
    """Test clearing all items from cart."""
    cart_with_items.clear()
    assert cart_with_items.total() == 0.0


def test_shopping_cart_discount_on_empty_cart(empty_cart):
    """Test applying discount to empty cart."""
    empty_cart.apply_discount("SAVE10")
    assert empty_cart.total_with_discount() == 0.0


# ============================================================================
# Fixtures for Exercise 3: Text Analyzer
# ============================================================================


@pytest.fixture
def simple_text():
    """Provide simple text for testing."""
    return "Hello world. This is a test."


@pytest.fixture
def complex_text():
    """Provide complex text for testing."""
    return (
        "The quick brown fox jumps over the lazy dog. "
        "The dog was not amused! "
        "Why did the fox jump? "
        "The fox jumps because the fox is quick."
    )


@pytest.fixture
def empty_analyzer():
    """Provide analyzer with empty text."""
    return TextAnalyzer("")


# ============================================================================
# Tests for Exercise 3: Text Analyzer
# ============================================================================


def test_text_analyzer_word_count_simple(simple_text):
    """Test word count with simple text."""
    analyzer = TextAnalyzer(simple_text)
    assert analyzer.word_count() == 6


def test_text_analyzer_word_count_complex(complex_text):
    """Test word count with complex text."""
    analyzer = TextAnalyzer(complex_text)
    assert analyzer.word_count() == 26


def test_text_analyzer_word_count_empty(empty_analyzer):
    """Test word count with empty text."""
    assert empty_analyzer.word_count() == 0


def test_text_analyzer_sentence_count_simple(simple_text):
    """Test sentence count with simple text."""
    analyzer = TextAnalyzer(simple_text)
    assert analyzer.sentence_count() == 2


def test_text_analyzer_sentence_count_complex(complex_text):
    """Test sentence count with complex text."""
    analyzer = TextAnalyzer(complex_text)
    assert analyzer.sentence_count() == 4


def test_text_analyzer_sentence_count_empty(empty_analyzer):
    """Test sentence count with empty text."""
    assert empty_analyzer.sentence_count() == 0


def test_text_analyzer_most_frequent_word_simple(simple_text):
    """Test most frequent word with simple text."""
    analyzer = TextAnalyzer(simple_text)
    # All words appear once, so any word is acceptable
    result = analyzer.most_frequent_word()
    assert result in ["hello", "world", "this", "is", "a", "test"]


def test_text_analyzer_most_frequent_word_complex(complex_text):
    """Test most frequent word with complex text."""
    analyzer = TextAnalyzer(complex_text)
    # "the" appears 5 times, "fox" appears 3 times
    assert analyzer.most_frequent_word() == "the"


def test_text_analyzer_most_frequent_word_empty(empty_analyzer):
    """Test most frequent word with empty text."""
    assert empty_analyzer.most_frequent_word() is None


def test_text_analyzer_average_word_length_simple(simple_text):
    """Test average word length with simple text."""
    analyzer = TextAnalyzer(simple_text)
    # "Hello"(5) + "world"(5) + "This"(4) + "is"(2) + "a"(1) + "test"(4) = 21 / 6 = 3.5
    assert analyzer.average_word_length() == pytest.approx(3.5)


def test_text_analyzer_average_word_length_empty(empty_analyzer):
    """Test average word length with empty text."""
    assert empty_analyzer.average_word_length() == 0.0


def test_text_analyzer_readability_score_simple(simple_text):
    """Test readability score with simple text."""
    analyzer = TextAnalyzer(simple_text)
    # 6 words / 2 sentences = 3.0
    assert analyzer.readability_score() == pytest.approx(3.0)


def test_text_analyzer_readability_score_complex(complex_text):
    """Test readability score with complex text."""
    analyzer = TextAnalyzer(complex_text)
    # 26 words / 4 sentences = 6.5
    assert analyzer.readability_score() == pytest.approx(6.5)


def test_text_analyzer_readability_score_empty(empty_analyzer):
    """Test readability score with empty text."""
    assert empty_analyzer.readability_score() == 0.0


def test_text_analyzer_handles_punctuation():
    """Test that analyzer properly handles punctuation."""
    text = "Hello, world! How are you?"
    analyzer = TextAnalyzer(text)
    assert analyzer.word_count() == 5
    assert analyzer.sentence_count() == 2


def test_text_analyzer_case_insensitive():
    """Test that word frequency is case-insensitive."""
    text = "The the THE"
    analyzer = TextAnalyzer(text)
    assert analyzer.most_frequent_word() == "the"


# ============================================================================
# Parametrized Tests for ISBN-10 (Bonus)
# ============================================================================


@pytest.mark.parametrize(
    "isbn,expected",
    [
        ("0306406152", True),  # Valid numeric
        ("043942089X", True),  # Valid with X
        ("0-306-40615-2", True),  # Valid with hyphens
        ("123456789", False),  # Too short
        ("12345678901", False),  # Too long
        ("12345A7890", False),  # Invalid character
        ("X234567890", False),  # X not at end
        ("0306406153", False),  # Invalid checksum
        ("", False),  # Empty
        (None, False),  # None
    ],
)
def test_validate_isbn10_parametrized(isbn, expected):
    """Test ISBN-10 validation with multiple cases."""
    assert validate_isbn10(isbn) == expected
