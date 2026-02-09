"""
Package Distribution Exercises - Day 1

This module contains exercises for practicing Python package distribution concepts.
Students will work with pyproject.toml configuration, package metadata, and
understanding distribution formats.

Your task:
1. Complete the pyproject.toml configuration generator
2. Implement package metadata validation
3. Create a function to parse wheel filenames
4. Build a simple package structure validator

Run the tests with: pytest tests/test_04_package_distribution.py
"""

# TODO: Import necessary modules
# Hint: You'll need pathlib, re, and typing


# Exercise 1: Generate pyproject.toml content
# TODO: Add type hints for all parameters and return value
def generate_pyproject_toml(
    package_name,
    version,
    description,
    author_name,
    author_email,
    python_version=">=3.10",
    dependencies=None,
):
    """
    Generate a basic pyproject.toml configuration as a string.

    TODO: Add complete Sphinx docstring with:
    :param package_name: Description
    :type package_name: type
    :param version: Description
    :type version: type
    :param description: Description
    :type description: type
    :param author_name: Description
    :type author_name: type
    :param author_email: Description
    :type author_email: type
    :param python_version: Description
    :type python_version: type
    :param dependencies: Description
    :type dependencies: type
    :return: Description
    :rtype: type

    Example:
        >>> config = generate_pyproject_toml("myapp", "0.1.0", "My app", "John", "john@example.com")
        >>> "name = \\"myapp\\"" in config
        True
    """
    # TODO: Implement function to generate pyproject.toml content
    # Should include [build-system], [project] sections
    # Handle optional dependencies list
    pass


# Exercise 2: Parse wheel filename
# TODO: Add type hints
def parse_wheel_filename(wheel_filename):
    """
    Parse a wheel filename and extract its components.

    TODO: Add complete Sphinx docstring

    A wheel filename has the format:
    {distribution}-{version}(-{build})?-{python}-{abi}-{platform}.whl

    Example:
        >>> info = parse_wheel_filename("numpy-1.24.0-cp310-cp310-win_amd64.whl")
        >>> info["package_name"]
        'numpy'
        >>> info["version"]
        '1.24.0'
        >>> info["python_tag"]
        'cp310'
    """
    # TODO: Implement wheel filename parser
    # Return a dictionary with: package_name, version, python_tag, abi_tag, platform_tag
    # Handle the optional build number
    pass


# Exercise 3: Validate package metadata
# TODO: Add type hints
def validate_package_metadata(metadata):
    """
    Validate that package metadata contains all required fields.

    TODO: Add complete Sphinx docstring

    Required fields: name, version, description, author
    Optional fields: license, keywords, dependencies

    Example:
        >>> metadata = {"name": "myapp", "version": "1.0.0", "description": "My app", "author": "John"}
        >>> validate_package_metadata(metadata)
        True
        >>> validate_package_metadata({"name": "myapp"})
        False
    """
    # TODO: Implement metadata validation
    # Check for required fields
    # Validate version format (should match semantic versioning pattern)
    # Return True if valid, False otherwise
    pass


# Exercise 4: Check if package structure is valid
# TODO: Add type hints
def is_valid_package_structure(package_dir):
    """
    Check if a directory has a valid Python package structure.

    TODO: Add complete Sphinx docstring

    A valid package should have:
    - pyproject.toml file
    - A package directory with __init__.py
    - README.md file

    Example:
        >>> is_valid_package_structure("./my_package")
        True
    """
    # TODO: Implement package structure validator
    # Check for required files and directories
    # Return True if structure is valid, False otherwise
    pass


# Exercise 5: Compare distribution formats
# TODO: Add type hints
def get_distribution_format_info(filename):
    """
    Determine the distribution format and return information about it.

    TODO: Add complete Sphinx docstring

    Supports:
    - Wheel (.whl)
    - Source distribution (.tar.gz)

    Example:
        >>> info = get_distribution_format_info("mypackage-1.0.0-py3-none-any.whl")
        >>> info["format"]
        'wheel'
        >>> info["requires_compilation"]
        False
    """
    # TODO: Implement distribution format detector
    # Return dict with: format, requires_compilation, install_speed (fast/slow)
    pass
