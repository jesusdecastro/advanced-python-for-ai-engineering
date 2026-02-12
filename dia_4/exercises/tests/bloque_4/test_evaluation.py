"""Tests para ejercicios del Bloque 4: OCP, LSP, ISP."""

import numpy as np
import pytest

from exercises.bloque_4.evaluation import (
    AccuracyMetric,
    AUCROCMetric,
    ClassificationEvaluator,
    EvaluationResult,
    F1Metric,
    MAEMetric,
    RegressionEvaluator,
    RMSEMetric,
)


# ============================================================================
# TESTS: AccuracyMetric
# ============================================================================
def test_accuracy_metric_perfect(binary_classification_perfect):
    """Test AccuracyMetric with perfect predictions."""
    y_true, y_pred = binary_classification_perfect
    metric = AccuracyMetric()
    score = metric.compute(y_true, y_pred)
    assert score == 1.0


def test_accuracy_metric_all_wrong(binary_classification_all_wrong):
    """Test AccuracyMetric with all wrong predictions."""
    y_true, y_pred = binary_classification_all_wrong
    metric = AccuracyMetric()
    score = metric.compute(y_true, y_pred)
    assert score == 0.0


def test_accuracy_metric_name():
    """Test AccuracyMetric name property."""
    metric = AccuracyMetric()
    assert metric.name == "accuracy"


# ============================================================================
# TESTS: F1Metric
# ============================================================================
def test_f1_metric_returns_float_between_0_and_1(binary_classification_mixed):
    """Test F1Metric returns float in [0, 1]."""
    y_true, y_pred = binary_classification_mixed
    metric = F1Metric()
    score = metric.compute(y_true, y_pred)
    assert 0.0 <= score <= 1.0


def test_f1_metric_name():
    """Test F1Metric name property."""
    metric = F1Metric()
    assert metric.name == "f1"


# ============================================================================
# TESTS: RMSEMetric
# ============================================================================
def test_rmse_metric_perfect(regression_perfect):
    """Test RMSEMetric with perfect predictions."""
    y_true, y_pred = regression_perfect
    metric = RMSEMetric()
    score = metric.compute(y_true, y_pred)
    assert score == 0.0


def test_rmse_metric_known_value(regression_known):
    """Test RMSEMetric with known value."""
    y_true, y_pred = regression_known
    metric = RMSEMetric()
    score = metric.compute(y_true, y_pred)
    assert abs(score - 1.0) < 0.01


def test_rmse_metric_name():
    """Test RMSEMetric name property."""
    metric = RMSEMetric()
    assert metric.name == "rmse"


# ============================================================================
# TESTS: MAEMetric
# ============================================================================
def test_mae_metric_known_value(regression_mae_known):
    """Test MAEMetric with known value."""
    y_true, y_pred = regression_mae_known
    metric = MAEMetric()
    score = metric.compute(y_true, y_pred)
    assert abs(score - 0.5) < 0.01


def test_mae_metric_name():
    """Test MAEMetric name property."""
    metric = MAEMetric()
    assert metric.name == "mae"


# ============================================================================
# TESTS: AUCROCMetric
# ============================================================================
def test_auc_roc_perfect_separation(binary_classification_proba_perfect):
    """Test AUCROCMetric with perfect separation."""
    y_true, y_proba = binary_classification_proba_perfect
    metric = AUCROCMetric()
    score = metric.compute(y_true, y_proba)
    assert score >= 0.95  # Should be close to 1.0


def test_auc_roc_metric_name():
    """Test AUCROCMetric name property."""
    metric = AUCROCMetric()
    assert metric.name == "auc_roc"


# ============================================================================
# TESTS: ClassificationEvaluator
# ============================================================================
def test_classification_evaluator_applies_all_metrics(binary_classification_mixed):
    """Test ClassificationEvaluator applies all metrics."""
    y_true, y_pred = binary_classification_mixed

    metrics = [AccuracyMetric(), F1Metric()]
    evaluator = ClassificationEvaluator(metrics=metrics, model_name="test_model")

    result = evaluator.evaluate(y_true, y_pred)

    assert isinstance(result, EvaluationResult)
    assert "accuracy" in result.metrics
    assert "f1" in result.metrics
    assert result.model_name == "test_model"


def test_classification_evaluator_with_probabilistic(
    binary_classification_mixed, binary_classification_proba_mixed
):
    """Test ClassificationEvaluator with probabilistic metrics."""
    y_true, y_pred = binary_classification_mixed
    _, y_proba = binary_classification_proba_mixed

    metrics = [AccuracyMetric()]
    prob_metrics = [AUCROCMetric()]
    evaluator = ClassificationEvaluator(
        metrics=metrics, probabilistic_metrics=prob_metrics
    )

    result = evaluator.evaluate(y_true, y_pred, y_proba=y_proba)

    assert "accuracy" in result.metrics
    assert "auc_roc" in result.metrics


def test_classification_evaluator_without_proba_ignores_probabilistic(
    binary_classification_mixed,
):
    """Test ClassificationEvaluator ignores probabilistic metrics without y_proba."""
    y_true, y_pred = binary_classification_mixed

    metrics = [AccuracyMetric()]
    prob_metrics = [AUCROCMetric()]
    evaluator = ClassificationEvaluator(
        metrics=metrics, probabilistic_metrics=prob_metrics
    )

    result = evaluator.evaluate(y_true, y_pred)

    assert "accuracy" in result.metrics
    assert "auc_roc" not in result.metrics


# ============================================================================
# TESTS: RegressionEvaluator
# ============================================================================
def test_regression_evaluator_applies_all_metrics(regression_mixed):
    """Test RegressionEvaluator applies all metrics."""
    y_true, y_pred = regression_mixed

    metrics = [RMSEMetric(), MAEMetric()]
    evaluator = RegressionEvaluator(metrics=metrics, model_name="test_model")

    result = evaluator.evaluate(y_true, y_pred)

    assert isinstance(result, EvaluationResult)
    assert "rmse" in result.metrics
    assert "mae" in result.metrics
    assert result.model_name == "test_model"


# ============================================================================
# TESTS: OCP (Open-Closed Principle)
# ============================================================================
def test_adding_new_metric_no_changes_needed(binary_classification_mixed):
    """Test adding new metric doesn't require changes to evaluator (OCP)."""
    y_true, y_pred = binary_classification_mixed

    # Define RecallMetric inline (not in evaluation.py)
    class RecallMetric:
        @property
        def name(self) -> str:
            return "recall"

        def compute(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
            tp = float(np.sum((y_true == 1) & (y_pred == 1)))
            fn = float(np.sum((y_true == 1) & (y_pred == 0)))
            return tp / (tp + fn) if (tp + fn) > 0 else 0.0

    # Use it with existing evaluator
    metrics = [AccuracyMetric(), RecallMetric()]
    evaluator = ClassificationEvaluator(metrics=metrics)

    result = evaluator.evaluate(y_true, y_pred)

    # Should work without any changes to ClassificationEvaluator
    assert "accuracy" in result.metrics
    assert "recall" in result.metrics


# ============================================================================
# TESTS: LSP (Liskov Substitution Principle)
# ============================================================================
@pytest.mark.parametrize(
    "metric_class",
    [AccuracyMetric, F1Metric],
)
def test_all_classification_metrics_return_0_to_1(
    metric_class, binary_classification_mixed
):
    """Test all classification metrics return float in [0, 1] (LSP)."""
    y_true, y_pred = binary_classification_mixed
    metric = metric_class()
    score = metric.compute(y_true, y_pred)
    assert 0.0 <= score <= 1.0
    assert isinstance(score, float)


# ============================================================================
# TESTS: EvaluationResult
# ============================================================================
def test_evaluation_result_is_frozen():
    """Test EvaluationResult is frozen (immutable)."""
    result = EvaluationResult(metrics={"accuracy": 0.9}, model_name="test")

    with pytest.raises(Exception):  # FrozenInstanceError
        result.metrics = {"accuracy": 0.8}


def test_evaluation_result_has_model_name():
    """Test EvaluationResult has model_name."""
    result = EvaluationResult(metrics={"accuracy": 0.9}, model_name="my_model")
    assert result.model_name == "my_model"
