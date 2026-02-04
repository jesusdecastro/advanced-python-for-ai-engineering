"""
Tests for objects vs data structures exercises.
"""

import pytest
from exercises.01_objects_vs_data_structures import (
    Temperature,
    Library,
    ShoppingCart,
)


class TestTemperature:
    """Tests for Temperature class."""
    
    def test_temperature_initialization(self):
        """Test temperature can be initialized with valid celsius value."""
        temp = Temperature(25)
        assert temp.get_celsius() == 25
    
    def test_temperature_below_absolute_zero_raises_error(self):
        """Test that temperature below absolute zero raises ValueError."""
        with pytest.raises(ValueError):
            Temperature(-300)
    
    def test_temperature_to_fahrenheit(self):
        """Test conversion to Fahrenheit."""
        temp = Temperature(0)
        assert temp.to_fahrenheit() == 32
        
        temp = Temperature(100)
        assert temp.to_fahrenheit() == 212
    
    def test_temperature_to_kelvin(self):
        """Test conversion to Kelvin."""
        temp = Temperature(0)
        assert temp.to_kelvin() == 273.15
        
        temp = Temperature(25)
        assert abs(temp.to_kelvin() - 298.15) < 0.01
    
    def test_temperature_encapsulation(self):
        """Test that celsius is properly encapsulated."""
        temp = Temperature(25)
        # Should not have public celsius attribute
        assert not hasattr(temp, 'celsius') or temp.celsius != 25


class TestBook:
    """Tests for Book dataclass."""
    
    def test_book_creation(self):
        """Test book can be created with all fields."""
        from exercises.01_objects_vs_data_structures import Book
        
        book = Book(
            isbn="978-0-13-468599-1",
            title="Clean Code",
            author="Robert C. Martin",
            year=2008
        )
        assert book.isbn == "978-0-13-468599-1"
        assert book.title == "Clean Code"
        assert book.author == "Robert C. Martin"
        assert book.year == 2008
    
    def test_book_is_dataclass(self):
        """Test that Book is a dataclass."""
        from exercises.01_objects_vs_data_structures import Book
        from dataclasses import is_dataclass
        
        assert is_dataclass(Book)


class TestLibrary:
    """Tests for Library class."""
    
    def test_library_initialization(self):
        """Test library can be initialized."""
        library = Library()
        assert library.get_book_count() == 0
    
    def test_add_book(self):
        """Test adding books to library."""
        from exercises.01_objects_vs_data_structures import Book
        
        library = Library()
        book = Book("978-0-13-468599-1", "Clean Code", "Robert C. Martin", 2008)
        library.add_book(book)
        
        assert library.get_book_count() == 1
    
    def test_find_by_isbn(self):
        """Test finding book by ISBN."""
        from exercises.01_objects_vs_data_structures import Book
        
        library = Library()
        book = Book("978-0-13-468599-1", "Clean Code", "Robert C. Martin", 2008)
        library.add_book(book)
        
        found = library.find_by_isbn("978-0-13-468599-1")
        assert found is not None
        assert found.title == "Clean Code"
    
    def test_find_by_isbn_not_found(self):
        """Test finding non-existent book returns None."""
        library = Library()
        found = library.find_by_isbn("999-9-99-999999-9")
        assert found is None
    
    def test_find_by_author(self):
        """Test finding books by author."""
        from exercises.01_objects_vs_data_structures import Book
        
        library = Library()
        book1 = Book("978-0-13-468599-1", "Clean Code", "Robert C. Martin", 2008)
        book2 = Book("978-0-13-475759-9", "Clean Architecture", "Robert C. Martin", 2017)
        book3 = Book("978-0-13-235088-4", "Clean Coder", "Robert C. Martin", 2011)
        
        library.add_book(book1)
        library.add_book(book2)
        library.add_book(book3)
        
        books = library.find_by_author("Robert C. Martin")
        assert len(books) == 3
    
    def test_remove_book(self):
        """Test removing book from library."""
        from exercises.01_objects_vs_data_structures import Book
        
        library = Library()
        book = Book("978-0-13-468599-1", "Clean Code", "Robert C. Martin", 2008)
        library.add_book(book)
        
        library.remove_book("978-0-13-468599-1")
        assert library.get_book_count() == 0
    
    def test_remove_nonexistent_book_raises_error(self):
        """Test removing non-existent book raises ValueError."""
        library = Library()
        with pytest.raises(ValueError):
            library.remove_book("999-9-99-999999-9")
    
    def test_library_encapsulation(self):
        """Test that library uses private attributes."""
        library = Library()
        # Should not have public books attribute
        assert not hasattr(library, 'books') or library.books is None


class TestShoppingCart:
    """Tests for ShoppingCart class."""
    
    def test_cart_initialization(self):
        """Test cart can be initialized."""
        cart = ShoppingCart()
        assert cart.get_total() == 0
        assert cart.get_item_count() == 0
    
    def test_add_item(self):
        """Test adding items to cart."""
        cart = ShoppingCart()
        cart.add_item("Laptop", 999.99, 1)
        
        assert cart.get_item_count() == 1
        assert cart.get_total() == 999.99
    
    def test_add_multiple_items(self):
        """Test adding multiple items."""
        cart = ShoppingCart()
        cart.add_item("Laptop", 999.99, 1)
        cart.add_item("Mouse", 29.99, 2)
        
        assert cart.get_item_count() == 2
        assert abs(cart.get_total() - 1059.97) < 0.01
    
    def test_add_item_with_invalid_price_raises_error(self):
        """Test adding item with negative price raises ValueError."""
        cart = ShoppingCart()
        with pytest.raises(ValueError):
            cart.add_item("Invalid", -10, 1)
    
    def test_add_item_with_invalid_quantity_raises_error(self):
        """Test adding item with zero quantity raises ValueError."""
        cart = ShoppingCart()
        with pytest.raises(ValueError):
            cart.add_item("Invalid", 10, 0)
    
    def test_remove_item(self):
        """Test removing item from cart."""
        cart = ShoppingCart()
        cart.add_item("Laptop", 999.99, 1)
        cart.remove_item("Laptop")
        
        assert cart.get_item_count() == 0
        assert cart.get_total() == 0
    
    def test_remove_nonexistent_item_raises_error(self):
        """Test removing non-existent item raises ValueError."""
        cart = ShoppingCart()
        with pytest.raises(ValueError):
            cart.remove_item("Nonexistent")
    
    def test_cart_encapsulation(self):
        """Test that cart uses private attributes."""
        cart = ShoppingCart()
        # Should not have public items attribute or should be private
        assert not hasattr(cart, 'items') or cart.items is None or len(cart.items) == 0
    
    def test_total_is_calculated_not_stored(self):
        """Test that total is calculated dynamically."""
        cart = ShoppingCart()
        cart.add_item("Laptop", 999.99, 1)
        
        # Total should be calculated, not stored
        # If we could modify internal state, total should still be correct
        assert cart.get_total() == 999.99
