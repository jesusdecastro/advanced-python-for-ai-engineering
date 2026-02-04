#!/bin/bash
# Script to run tests for Day 1 exercises

echo "Running Type Hinting Exercises Tests..."
echo "========================================"
echo ""

# Run pytest with verbose output
pytest exercises/tests/test_02_type_hinting.py -v

# Check exit code
if [ $? -eq 0 ]; then
    echo ""
    echo "✓ All tests passed!"
    echo ""
    echo "Next steps:"
    echo "1. Validate type hints with Pyright: pyright exercises/02_type_hinting.py"
    echo "2. Format code with Ruff: ruff format exercises/02_type_hinting.py"
    echo "3. Check code quality: ruff check exercises/02_type_hinting.py"
else
    echo ""
    echo "✗ Some tests failed. Review the output above."
    exit 1
fi
