"""Tests for magic methods exercises."""

import importlib.util
import sys
from pathlib import Path

import pytest

# Import the module to test functionality
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# Dynamically import module with numeric prefix
_module_path = Path(__file__).parent.parent / "06_magic_methods.py"
_spec = importlib.util.spec_from_file_location("magic_methods_exercises", _module_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)

Book = _module.Book
Student = _module.Student
Library = _module.Library
EvenNumbers = _module.EvenNumbers
Multiplier = _module.Multiplier
ShoppingCart = _module.ShoppingCart


class TestBook:
    """Tests for Book class with __str__ and __repr__."""

    def test_book_str_representation(self):
        """Test __str__ returns user-friendly format."""
        book = Book("1984", "George Orwell", 1949)
        assert str(book) == "1984 by George Orwell (1949)"

    def test_book_repr_representation(self):
        """Test __repr__ returns evaluable format."""
        book = Book("1984", "George Orwell", 1949)
        assert repr(book) == "Book('1984', 'George Orwell', 1949)"

    def test_book_repr_is_evaluable(self):
        """Test that repr can recreate the object."""
        book = Book("The Hobbit", "J.R.R. Tolkien", 1937)
        book_repr = repr(book)
        # This should be evaluable
        assert "Book(" in book_repr
        assert "The Hobbit" in book_repr
        assert "J.R.R. Tolkien" in book_repr
        assert "1937" in book_repr

    def test_book_print_uses_str(self, capsys):
        """Test that print() uses __str__."""
        book = Book("Dune", "Frank Herbert", 1965)
        print(book)
        captured = capsys.readouterr()
        assert "Dune by Frank Herbert (1965)" in captured.out

    def test_book_list_uses_repr(self):
        """Test that list representation uses __repr__."""
        book = Book("Foundation", "Isaac Asimov", 1951)
        book_list = [book]
        list_str = str(book_list)
        assert "Book(" in list_str
        assert "Foundation" in list_str


class TestStudent:
    """Tests for Student class with comparison methods."""

    def test_student_equality_same_values(self):
        """Test __eq__ returns True for same values."""
        student1 = Student("Alice", 85.0)
        student2 = Student("Alice", 85.0)
        assert student1 == student2

    def test_student_equality_different_names(self):
        """Test __eq__ returns False for different names."""
        student1 = Student("Alice", 85.0)
        student2 = Student("Bob", 85.0)
        assert student1 != student2

    def test_student_equality_different_grades(self):
        """Test __eq__ returns False for different grades."""
        student1 = Student("Alice", 85.0)
        student2 = Student("Alice", 90.0)
        assert student1 != student2

    def test_student_less_than_by_grade(self):
        """Test __lt__ compares by grade."""
        student1 = Student("Alice", 75.0)
        student2 = Student("Bob", 85.0)
        assert student1 < student2

    def test_student_not_less_than_higher_grade(self):
        """Test __lt__ returns False for higher grade."""
        student1 = Student("Alice", 95.0)
        student2 = Student("Bob", 85.0)
        assert not (student1 < student2)

    def test_student_greater_than_derived(self):
        """Test that __gt__ is derived from __lt__."""
        student1 = Student("Alice", 95.0)
        student2 = Student("Bob", 85.0)
        assert student1 > student2

    def test_student_less_than_or_equal_derived(self):
        """Test that __le__ is derived."""
        student1 = Student("Alice", 85.0)
        student2 = Student("Bob", 85.0)
        student3 = Student("Charlie", 90.0)
        assert student1 <= student2  # Equal grades
        assert student1 <= student3  # Less than

    def test_student_greater_than_or_equal_derived(self):
        """Test that __ge__ is derived."""
        student1 = Student("Alice", 90.0)
        student2 = Student("Bob", 90.0)
        student3 = Student("Charlie", 85.0)
        assert student1 >= student2  # Equal grades
        assert student1 >= student3  # Greater than

    def test_student_sorting(self):
        """Test that students can be sorted by grade."""
        students = [
            Student("Charlie", 90.0),
            Student("Alice", 75.0),
            Student("Bob", 85.0),
        ]
        sorted_students = sorted(students)
        assert sorted_students[0].name == "Alice"  # Lowest grade
        assert sorted_students[1].name == "Bob"
        assert sorted_students[2].name == "Charlie"  # Highest grade

    def test_student_repr(self):
        """Test __repr__ format."""
        student = Student("Alice", 85.0)
        assert repr(student) == "Student('Alice', 85.0)"

    def test_student_comparison_with_non_student(self):
        """Test comparison with non-Student returns NotImplemented."""
        student = Student("Alice", 85.0)
        # These should not raise errors but return False
        assert student != "not a student"
        assert student != 85


class TestLibrary:
    """Tests for Library container class."""

    def test_library_len_empty(self):
        """Test __len__ for empty library."""
        library = Library("City Library")
        assert len(library) == 0

    def test_library_len_with_books(self):
        """Test __len__ with books added."""
        library = Library("City Library")
        library.add_book(Book("Book 1", "Author 1", 2020))
        library.add_book(Book("Book 2", "Author 2", 2021))
        assert len(library) == 2

    def test_library_getitem_by_index(self):
        """Test __getitem__ retrieves book by index."""
        library = Library("City Library")
        book1 = Book("First", "Author A", 2020)
        book2 = Book("Second", "Author B", 2021)
        library.add_book(book1)
        library.add_book(book2)

        assert library[0] == book1
        assert library[1] == book2

    def test_library_getitem_negative_index(self):
        """Test __getitem__ with negative indexing."""
        library = Library("City Library")
        book1 = Book("First", "Author A", 2020)
        book2 = Book("Second", "Author B", 2021)
        library.add_book(book1)
        library.add_book(book2)

        assert library[-1] == book2
        assert library[-2] == book1

    def test_library_contains_book_present(self):
        """Test __contains__ returns True for present book."""
        library = Library("City Library")
        book = Book("Present", "Author", 2020)
        library.add_book(book)

        assert book in library

    def test_library_contains_book_absent(self):
        """Test __contains__ returns False for absent book."""
        library = Library("City Library")
        book1 = Book("Present", "Author", 2020)
        book2 = Book("Absent", "Author", 2021)
        library.add_book(book1)

        assert book2 not in library

    def test_library_iteration(self):
        """Test that library is iterable via __getitem__."""
        library = Library("City Library")
        books = [
            Book("Book 1", "Author 1", 2020),
            Book("Book 2", "Author 2", 2021),
            Book("Book 3", "Author 3", 2022),
        ]
        for book in books:
            library.add_book(book)

        # Should be able to iterate
        iterated_books = list(library)
        assert len(iterated_books) == 3
        assert iterated_books == books

    def test_library_repr(self):
        """Test __repr__ format."""
        library = Library("City Library")
        library.add_book(Book("Book 1", "Author 1", 2020))
        library.add_book(Book("Book 2", "Author 2", 2021))

        assert repr(library) == "Library('City Library', 2 books)"

    def test_library_repr_singular(self):
        """Test __repr__ with one book."""
        library = Library("City Library")
        library.add_book(Book("Book 1", "Author 1", 2020))

        # Should handle singular/plural correctly
        repr_str = repr(library)
        assert "City Library" in repr_str
        assert "1" in repr_str


class TestEvenNumbers:
    """Tests for EvenNumbers iterator."""

    def test_even_numbers_iteration(self):
        """Test iterating over even numbers."""
        evens = EvenNumbers(10)
        result = list(evens)
        assert result == [0, 2, 4, 6, 8, 10]

    def test_even_numbers_small_range(self):
        """Test with small range."""
        evens = EvenNumbers(4)
        result = list(evens)
        assert result == [0, 2, 4]

    def test_even_numbers_zero(self):
        """Test with max_value of 0."""
        evens = EvenNumbers(0)
        result = list(evens)
        assert result == [0]

    def test_even_numbers_odd_max(self):
        """Test with odd max_value."""
        evens = EvenNumbers(7)
        result = list(evens)
        assert result == [0, 2, 4, 6]

    def test_even_numbers_reusable(self):
        """Test that iterator can be reused."""
        evens = EvenNumbers(6)
        result1 = list(evens)
        result2 = list(evens)
        assert result1 == result2 == [0, 2, 4, 6]

    def test_even_numbers_in_for_loop(self):
        """Test using iterator in for loop."""
        evens = EvenNumbers(8)
        collected = []
        for num in evens:
            collected.append(num)
        assert collected == [0, 2, 4, 6, 8]

    def test_even_numbers_manual_iteration(self):
        """Test manual iteration with next()."""
        evens = EvenNumbers(4)
        iterator = iter(evens)
        assert next(iterator) == 0
        assert next(iterator) == 2
        assert next(iterator) == 4

        with pytest.raises(StopIteration):
            next(iterator)


class TestMultiplier:
    """Tests for Multiplier callable class."""

    def test_multiplier_call(self):
        """Test calling multiplier as function."""
        double = Multiplier(2)
        assert double(5) == 10
        assert double(10) == 20

    def test_multiplier_different_factors(self):
        """Test multipliers with different factors."""
        double = Multiplier(2)
        triple = Multiplier(3)
        half = Multiplier(0.5)

        assert double(10) == 20
        assert triple(10) == 30
        assert half(10) == 5

    def test_multiplier_with_floats(self):
        """Test multiplier with float values."""
        multiplier = Multiplier(1.5)
        assert multiplier(10) == 15.0
        assert multiplier(20) == 30.0

    def test_multiplier_with_map(self):
        """Test using multiplier with map()."""
        double = Multiplier(2)
        numbers = [1, 2, 3, 4, 5]
        result = list(map(double, numbers))
        assert result == [2, 4, 6, 8, 10]

    def test_multiplier_negative_factor(self):
        """Test multiplier with negative factor."""
        negate = Multiplier(-1)
        assert negate(5) == -5
        assert negate(-3) == 3


class TestShoppingCart:
    """Tests for ShoppingCart with __bool__."""

    def test_shopping_cart_empty_is_falsy(self):
        """Test empty cart is falsy."""
        cart = ShoppingCart()
        assert not cart
        assert bool(cart) is False

    def test_shopping_cart_with_items_is_truthy(self):
        """Test cart with items is truthy."""
        cart = ShoppingCart()
        cart.add_item("Apple")
        assert cart
        assert bool(cart) is True

    def test_shopping_cart_in_if_statement(self):
        """Test cart in if statement."""
        cart = ShoppingCart()
        result = "empty"

        if cart:
            result = "has items"
        else:
            result = "empty"

        assert result == "empty"

        cart.add_item("Banana")

        if cart:
            result = "has items"
        else:
            result = "empty"

        assert result == "has items"

    def test_shopping_cart_len(self):
        """Test __len__ for shopping cart."""
        cart = ShoppingCart()
        assert len(cart) == 0

        cart.add_item("Item 1")
        assert len(cart) == 1

        cart.add_item("Item 2")
        assert len(cart) == 2

    def test_shopping_cart_multiple_items(self):
        """Test cart with multiple items."""
        cart = ShoppingCart()
        items = ["Apple", "Banana", "Orange"]

        for item in items:
            cart.add_item(item)

        assert len(cart) == 3
        assert cart  # Should be truthy


class TestMagicMethodsIntegration:
    """Integration tests combining multiple magic methods."""

    def test_library_with_sorted_books(self):
        """Test library with books that can be compared."""
        library = Library("Tech Library")

        # Add books (assuming Book has comparison if needed)
        books = [
            Book("Python Basics", "Author A", 2020),
            Book("Advanced Python", "Author B", 2021),
            Book("Python Mastery", "Author C", 2019),
        ]

        for book in books:
            library.add_book(book)

        assert len(library) == 3
        assert library[0] == books[0]

    def test_student_library_analogy(self):
        """Test that Student and Library work similarly to Book and Library."""
        # Create a "class roster" similar to library
        students = [
            Student("Alice", 85.0),
            Student("Bob", 92.0),
            Student("Charlie", 78.0),
        ]

        sorted_students = sorted(students)
        assert sorted_students[0].grade == 78.0  # Lowest
        assert sorted_students[-1].grade == 92.0  # Highest

    def test_even_numbers_with_multiplier(self):
        """Test combining iterator with callable."""
        evens = EvenNumbers(10)
        double = Multiplier(2)

        # Double all even numbers
        result = [double(num) for num in evens]
        assert result == [0, 4, 8, 12, 16, 20]

    def test_complex_iteration_scenario(self):
        """Test complex scenario with multiple magic methods."""
        library = Library("Main Library")

        # Add books
        for i in range(5):
            library.add_book(Book(f"Book {i}", f"Author {i}", 2020 + i))

        # Test length
        assert len(library) == 5

        # Test iteration
        book_titles = [str(book) for book in library]
        assert len(book_titles) == 5

        # Test contains
        first_book = library[0]
        assert first_book in library

        # Test indexing
        last_book = library[-1]
        assert "Book 4" in str(last_book)
