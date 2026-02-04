"""
Tests for Unit Testing with pytest exercises.

This test module demonstrates pytest fundamentals including:
- Basic test structure with AAA pattern
- Testing exceptions
- Using fixtures for setup and teardown
- Mocking external dependencies
- Parametrized tests
"""

import pytest
import os
import sys
import tempfile
import shutil
from pathlib import Path
from unittest.mock import Mock, patch
import requests

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import from the exercise module
from unit_testing_pytest import (
    validate_email,
    FileManager,
    WeatherService,
    ShoppingCart
)


# ============================================================================
# Tests for Exercise 1: Email Validation
# ============================================================================

def test_validate_email_valid_simple():
    """Test email validation with a simple valid email."""
    assert validate_email("user@example.com") is True


def test_validate_email_valid_with_dots():
    """Test email validation with dots in username."""
    assert validate_email("first.last@example.com") is True


def test_validate_email_valid_with_plus():
    """Test email validation with plus sign in username."""
    assert validate_email("user+tag@example.com") is True


def test_validate_email_valid_subdomain():
    """Test email validation with subdomain."""
    assert validate_email("user@mail.example.com") is True


def test_validate_email_invalid_no_at():
    """Test email validation fails without @ symbol."""
    assert validate_email("userexample.com") is False


def test_validate_email_invalid_no_domain():
    """Test email validation fails without domain."""
    assert validate_email("user@") is False


def test_validate_email_invalid_no_tld():
    """Test email validation fails without top-level domain."""
    assert validate_email("user@example") is False


def test_validate_email_empty_string():
    """Test email validation fails with empty string."""
    assert validate_email("") is False


def test_validate_email_none():
    """Test email validation fails with None."""
    assert validate_email(None) is False


def test_validate_email_invalid_type():
    """Test email validation fails with non-string type."""
    assert validate_email(12345) is False


# ============================================================================
# Fixtures for Exercise 2: File Manager
# ============================================================================

@pytest.fixture
def temp_dir():
    """
    Create a temporary directory for testing.
    Automatically cleans up after the test.
    """
    # Setup: create temp directory
    dirpath = tempfile.mkdtemp()
    
    # Provide the path to the test
    yield dirpath
    
    # Teardown: remove temp directory and all contents
    if os.path.exists(dirpath):
        shutil.rmtree(dirpath)


@pytest.fixture
def file_manager(temp_dir):
    """
    Provide a FileManager instance with a temporary directory.
    """
    return FileManager(temp_dir)


# ============================================================================
# Tests for Exercise 2: File Manager
# ============================================================================

def test_file_manager_create_file(file_manager, temp_dir):
    """Test creating a file."""
    # Arrange
    filename = "test.txt"
    content = "test content"
    
    # Act
    filepath = file_manager.create_file(filename, content)
    
    # Assert
    assert os.path.exists(filepath)
    assert filepath == os.path.join(temp_dir, filename)


def test_file_manager_read_file(file_manager):
    """Test reading a file."""
    # Arrange
    filename = "test.txt"
    content = "test content"
    file_manager.create_file(filename, content)
    
    # Act
    read_content = file_manager.read_file(filename)
    
    # Assert
    assert read_content == content


def test_file_manager_list_files(file_manager):
    """Test listing files in directory."""
    # Arrange
    file_manager.create_file("file1.txt", "content1")
    file_manager.create_file("file2.txt", "content2")
    file_manager.create_file("file3.txt", "content3")
    
    # Act
    files = file_manager.list_files()
    
    # Assert
    assert len(files) == 3
    assert "file1.txt" in files
    assert "file2.txt" in files
    assert "file3.txt" in files


def test_file_manager_delete_file(file_manager, temp_dir):
    """Test deleting a file."""
    # Arrange
    filename = "test.txt"
    file_manager.create_file(filename, "content")
    filepath = os.path.join(temp_dir, filename)
    
    # Act
    file_manager.delete_file(filename)
    
    # Assert
    assert not os.path.exists(filepath)


def test_file_manager_list_empty_directory(file_manager):
    """Test listing files in empty directory."""
    # Act
    files = file_manager.list_files()
    
    # Assert
    assert files == []


def test_file_manager_delete_nonexistent_file(file_manager):
    """Test deleting a file that doesn't exist (should not raise error)."""
    # Act & Assert (should not raise exception)
    file_manager.delete_file("nonexistent.txt")


# ============================================================================
# Tests for Exercise 3: Weather Service with Mocking
# ============================================================================

@pytest.fixture
def weather_service():
    """Provide a WeatherService instance."""
    return WeatherService(api_key="test_api_key")


@patch('requests.get')
def test_weather_service_get_temperature_success(mock_get, weather_service):
    """Test getting temperature successfully."""
    # Arrange: configure the mock
    mock_response = Mock()
    mock_response.json.return_value = {"temperature": 25.5}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response
    
    # Act
    temperature = weather_service.get_temperature("London")
    
    # Assert
    assert temperature == 25.5
    mock_get.assert_called_once_with(
        "https://api.weather.com/v1/current",
        params={"city": "London", "api_key": "test_api_key"}
    )


@patch('requests.get')
def test_weather_service_get_temperature_http_error(mock_get, weather_service):
    """Test getting temperature with HTTP error."""
    # Arrange: simulate HTTP error
    mock_get.side_effect = requests.HTTPError("404 Not Found")
    
    # Act & Assert
    with pytest.raises(requests.HTTPError):
        weather_service.get_temperature("InvalidCity")


@patch('requests.get')
def test_weather_service_get_forecast_success(mock_get, weather_service):
    """Test getting forecast successfully."""
    # Arrange
    mock_response = Mock()
    mock_response.json.return_value = {
        "forecast": [
            {"day": 1, "temp": 20.0},
            {"day": 2, "temp": 22.0},
            {"day": 3, "temp": 19.0}
        ]
    }
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response
    
    # Act
    forecast = weather_service.get_forecast("Paris", 3)
    
    # Assert
    assert len(forecast) == 3
    assert forecast[0]["temp"] == 20.0
    mock_get.assert_called_once_with(
        "https://api.weather.com/v1/forecast",
        params={"city": "Paris", "days": 3, "api_key": "test_api_key"}
    )


@patch('requests.get')
def test_weather_service_get_forecast_invalid_response(mock_get, weather_service):
    """Test getting forecast with invalid JSON response."""
    # Arrange: simulate invalid JSON
    mock_response = Mock()
    mock_response.json.side_effect = ValueError("Invalid JSON")
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response
    
    # Act & Assert
    with pytest.raises(ValueError):
        weather_service.get_forecast("Berlin", 5)


# ============================================================================
# Fixtures for Exercise 4: Shopping Cart
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
# Tests for Exercise 4: Shopping Cart
# ============================================================================

def test_shopping_cart_add_item(empty_cart):
    """Test adding an item to the cart."""
    # Act
    empty_cart.add_item("Apple", 1.0, 2)
    
    # Assert
    assert len(empty_cart.items) == 1
    assert empty_cart.items[0]["name"] == "Apple"
    assert empty_cart.items[0]["price"] == 1.0
    assert empty_cart.items[0]["quantity"] == 2


def test_shopping_cart_add_item_default_quantity(empty_cart):
    """Test adding an item with default quantity."""
    # Act
    empty_cart.add_item("Apple", 1.0)
    
    # Assert
    assert empty_cart.items[0]["quantity"] == 1


def test_shopping_cart_remove_item(cart_with_items):
    """Test removing an item from the cart."""
    # Act
    cart_with_items.remove_item("Banana")
    
    # Assert
    assert len(cart_with_items.items) == 2
    assert all(item["name"] != "Banana" for item in cart_with_items.items)


def test_shopping_cart_total(cart_with_items):
    """Test calculating cart total."""
    # Expected: (1.0 * 2) + (0.5 * 3) + (0.75 * 1) = 2.0 + 1.5 + 0.75 = 4.25
    assert cart_with_items.total() == 4.25


def test_shopping_cart_total_empty(empty_cart):
    """Test calculating total of empty cart."""
    assert empty_cart.total() == 0.0


def test_shopping_cart_item_count(cart_with_items):
    """Test counting items in cart."""
    # Expected: 2 + 3 + 1 = 6
    assert cart_with_items.item_count() == 6


def test_shopping_cart_item_count_empty(empty_cart):
    """Test counting items in empty cart."""
    assert empty_cart.item_count() == 0


def test_shopping_cart_clear(cart_with_items):
    """Test clearing all items from cart."""
    # Act
    cart_with_items.clear()
    
    # Assert
    assert len(cart_with_items.items) == 0
    assert cart_with_items.total() == 0.0


# ============================================================================
# Parametrized Tests (Bonus)
# ============================================================================

@pytest.mark.parametrize("email,expected", [
    ("user@example.com", True),
    ("first.last@example.com", True),
    ("user+tag@example.com", True),
    ("user@mail.example.com", True),
    ("invalid", False),
    ("@example.com", False),
    ("user@", False),
    ("", False),
])
def test_validate_email_parametrized(email, expected):
    """Test email validation with multiple cases using parametrize."""
    assert validate_email(email) == expected
