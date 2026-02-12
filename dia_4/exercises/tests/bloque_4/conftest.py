"""Fixtures para tests del Bloque 4."""

import numpy as np
import pytest


# ============================================================================
# Classification Fixtures
# ============================================================================
@pytest.fixture
def binary_classification_perfect():
    """Perfect binary classification predictions."""
    y_true = np.array([1, 0, 1, 0, 1])
    y_pred = np.array([1, 0, 1, 0, 1])
    return y_true, y_pred


@pytest.fixture
def binary_classification_all_wrong():
    """All wrong binary classification predictions."""
    y_true = np.array([1, 0, 1, 0, 1])
    y_pred = np.array([0, 1, 0, 1, 0])
    return y_true, y_pred


@pytest.fixture
def binary_classification_mixed():
    """Mixed binary classification predictions."""
    y_true = np.array([1, 0, 1, 0, 1, 1, 0, 0])
    y_pred = np.array([1, 0, 1, 1, 0, 1, 0, 1])
    return y_true, y_pred


@pytest.fixture
def binary_classification_proba_perfect():
    """Perfect probability predictions."""
    y_true = np.array([1, 0, 1, 0, 1])
    y_proba = np.array([0.9, 0.1, 0.95, 0.05, 0.85])
    return y_true, y_proba


@pytest.fixture
def binary_classification_proba_mixed():
    """Mixed probability predictions."""
    y_true = np.array([1, 0, 1, 0, 1, 1, 0, 0])
    y_proba = np.array([0.8, 0.2, 0.9, 0.6, 0.4, 0.7, 0.3, 0.5])
    return y_true, y_proba


# ============================================================================
# Regression Fixtures
# ============================================================================
@pytest.fixture
def regression_perfect():
    """Perfect regression predictions."""
    y_true = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    y_pred = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    return y_true, y_pred


@pytest.fixture
def regression_known():
    """Regression predictions with known RMSE=1.0."""
    y_true = np.array([0.0, 0.0])
    y_pred = np.array([1.0, 1.0])
    return y_true, y_pred


@pytest.fixture
def regression_mae_known():
    """Regression predictions with known MAE=0.5."""
    y_true = np.array([1.0, 2.0, 3.0])
    y_pred = np.array([1.5, 2.5, 3.5])
    return y_true, y_pred


@pytest.fixture
def regression_mixed():
    """Mixed regression predictions."""
    y_true = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    y_pred = np.array([1.2, 1.8, 3.1, 4.3, 4.9])
    return y_true, y_pred
