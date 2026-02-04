"""
Tests for package distribution exercises.
"""

import importlib.util
import sys
import tempfile
from pathlib import Path

import pytest

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# Dynamically import module with numeric prefix
_module_path = Path(__file__).parent.parent / "04_package_distribution.py"
_spec = importlib.util.spec_from_file_location("package_distribution_exercises", _module_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)

generate_pyproject_toml = _module.generate_pyproject_toml
parse_wheel_filename = _module.parse_wheel_filename
validate_package_metadata = _module.validate_package_metadata
is_valid_package_structure = _module.is_valid_package_structure
get_distribution_format_info = _module.get_distribution_format_info


class TestGeneratePyprojectToml:
    """Tests for pyproject.toml generation."""

    def test_basic_configuration(self):
        """Test generating basic pyproject.toml content."""
        config = generate_pyproject_toml(
            package_name="testapp",
            version="0.1.0",
            description="A test application",
            author_name="Test Author",
            author_email="test@example.com",
        )

        assert 'name = "testapp"' in config
        assert 'version = "0.1.0"' in config
        assert 'description = "A test application"' in config
        assert "Test Author" in config
        assert "test@example.com" in config

    def test_with_dependencies(self):
        """Test generating config with dependencies."""
        config = generate_pyproject_toml(
            package_name="testapp",
            version="0.1.0",
            description="Test",
            author_name="Author",
            author_email="author@example.com",
            dependencies=["requests>=2.28.0", "numpy>=1.24.0"],
        )

        assert "requests>=2.28.0" in config
        assert "numpy>=1.24.0" in config

    def test_custom_python_version(self):
        """Test generating config with custom Python version."""
        config = generate_pyproject_toml(
            package_name="testapp",
            version="0.1.0",
            description="Test",
            author_name="Author",
            author_email="author@example.com",
            python_version=">=3.11",
        )

        assert ">=3.11" in config

    def test_includes_build_system(self):
        """Test that config includes build-system section."""
        config = generate_pyproject_toml(
            package_name="testapp",
            version="0.1.0",
            description="Test",
            author_name="Author",
            author_email="author@example.com",
        )

        assert "[build-system]" in config
        assert "setuptools" in config


class TestParseWheelFilename:
    """Tests for wheel filename parsing."""

    def test_parse_pure_python_wheel(self):
        """Test parsing a pure Python wheel filename."""
        info = parse_wheel_filename("mypackage-1.0.0-py3-none-any.whl")

        assert info["package_name"] == "mypackage"
        assert info["version"] == "1.0.0"
        assert info["python_tag"] == "py3"
        assert info["abi_tag"] == "none"
        assert info["platform_tag"] == "any"

    def test_parse_compiled_wheel(self):
        """Test parsing a compiled wheel filename."""
        info = parse_wheel_filename("numpy-1.24.0-cp310-cp310-win_amd64.whl")

        assert info["package_name"] == "numpy"
        assert info["version"] == "1.24.0"
        assert info["python_tag"] == "cp310"
        assert info["abi_tag"] == "cp310"
        assert info["platform_tag"] == "win_amd64"

    def test_parse_wheel_with_build_number(self):
        """Test parsing wheel with build number."""
        info = parse_wheel_filename("package-2.0.0-1-py3-none-any.whl")

        assert info["package_name"] == "package"
        assert info["version"] == "2.0.0"
        assert info.get("build_number") == "1"

    def test_parse_wheel_with_dashes_in_name(self):
        """Test parsing wheel with dashes in package name."""
        info = parse_wheel_filename("my-cool-package-0.5.0-py3-none-any.whl")

        assert info["package_name"] == "my-cool-package"
        assert info["version"] == "0.5.0"

    def test_invalid_wheel_filename(self):
        """Test that invalid wheel filename raises error."""
        with pytest.raises((ValueError, KeyError)):
            parse_wheel_filename("not-a-wheel.tar.gz")


class TestValidatePackageMetadata:
    """Tests for package metadata validation."""

    def test_valid_metadata(self):
        """Test validation of complete metadata."""
        metadata = {
            "name": "mypackage",
            "version": "1.0.0",
            "description": "A test package",
            "author": "Test Author",
        }

        assert validate_package_metadata(metadata) is True

    def test_missing_required_field(self):
        """Test validation fails with missing required field."""
        metadata = {
            "name": "mypackage",
            "version": "1.0.0",
            # Missing description and author
        }

        assert validate_package_metadata(metadata) is False

    def test_invalid_version_format(self):
        """Test validation fails with invalid version."""
        metadata = {
            "name": "mypackage",
            "version": "not-a-version",
            "description": "Test",
            "author": "Author",
        }

        assert validate_package_metadata(metadata) is False

    def test_valid_semantic_versions(self):
        """Test various valid semantic version formats."""
        valid_versions = ["1.0.0", "0.1.0", "2.3.4", "1.0.0-alpha", "1.0.0+build"]

        for version in valid_versions:
            metadata = {
                "name": "pkg",
                "version": version,
                "description": "Test",
                "author": "Author",
            }
            assert validate_package_metadata(metadata) is True

    def test_optional_fields_accepted(self):
        """Test that optional fields don't break validation."""
        metadata = {
            "name": "mypackage",
            "version": "1.0.0",
            "description": "Test",
            "author": "Author",
            "license": "MIT",
            "keywords": ["test", "package"],
            "dependencies": ["requests"],
        }

        assert validate_package_metadata(metadata) is True


class TestIsValidPackageStructure:
    """Tests for package structure validation."""

    def test_valid_package_structure(self):
        """Test validation of valid package structure."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create valid structure
            Path(tmpdir, "pyproject.toml").touch()
            Path(tmpdir, "README.md").touch()
            pkg_dir = Path(tmpdir, "mypackage")
            pkg_dir.mkdir()
            Path(pkg_dir, "__init__.py").touch()

            assert is_valid_package_structure(tmpdir) is True

    def test_missing_pyproject_toml(self):
        """Test validation fails without pyproject.toml."""
        with tempfile.TemporaryDirectory() as tmpdir:
            Path(tmpdir, "README.md").touch()
            pkg_dir = Path(tmpdir, "mypackage")
            pkg_dir.mkdir()
            Path(pkg_dir, "__init__.py").touch()

            assert is_valid_package_structure(tmpdir) is False

    def test_missing_package_directory(self):
        """Test validation fails without package directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            Path(tmpdir, "pyproject.toml").touch()
            Path(tmpdir, "README.md").touch()

            assert is_valid_package_structure(tmpdir) is False

    def test_missing_init_file(self):
        """Test validation fails without __init__.py."""
        with tempfile.TemporaryDirectory() as tmpdir:
            Path(tmpdir, "pyproject.toml").touch()
            Path(tmpdir, "README.md").touch()
            pkg_dir = Path(tmpdir, "mypackage")
            pkg_dir.mkdir()
            # No __init__.py

            assert is_valid_package_structure(tmpdir) is False

    def test_missing_readme(self):
        """Test validation fails without README.md."""
        with tempfile.TemporaryDirectory() as tmpdir:
            Path(tmpdir, "pyproject.toml").touch()
            pkg_dir = Path(tmpdir, "mypackage")
            pkg_dir.mkdir()
            Path(pkg_dir, "__init__.py").touch()

            assert is_valid_package_structure(tmpdir) is False


class TestGetDistributionFormatInfo:
    """Tests for distribution format detection."""

    def test_wheel_format(self):
        """Test detection of wheel format."""
        info = get_distribution_format_info("mypackage-1.0.0-py3-none-any.whl")

        assert info["format"] == "wheel"
        assert info["requires_compilation"] is False
        assert info["install_speed"] == "fast"

    def test_source_distribution_format(self):
        """Test detection of source distribution format."""
        info = get_distribution_format_info("mypackage-1.0.0.tar.gz")

        assert info["format"] == "sdist"
        assert info["requires_compilation"] is True
        assert info["install_speed"] == "slow"

    def test_compiled_wheel(self):
        """Test detection of compiled wheel."""
        info = get_distribution_format_info("numpy-1.24.0-cp310-cp310-win_amd64.whl")

        assert info["format"] == "wheel"
        # Even compiled wheels don't require compilation at install time
        assert info["requires_compilation"] is False
        assert info["install_speed"] == "fast"

    def test_unknown_format(self):
        """Test handling of unknown format."""
        with pytest.raises((ValueError, KeyError)):
            get_distribution_format_info("package.zip")
