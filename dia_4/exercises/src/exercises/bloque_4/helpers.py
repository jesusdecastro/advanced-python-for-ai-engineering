"""
Funciones helper para calcular métricas de ML.

YA ESTÁN IMPLEMENTADAS — úsalas desde tus clases.
"""

import numpy as np


def accuracy(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Porcentaje de predicciones correctas. Devuelve 0.0 a 1.0."""
    return float(np.mean(y_true == y_pred))


def f1_binary(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """F1 score para clasificación binaria. Devuelve 0.0 a 1.0."""
    tp = float(np.sum((y_true == 1) & (y_pred == 1)))
    fp = float(np.sum((y_true == 0) & (y_pred == 1)))
    fn = float(np.sum((y_true == 1) & (y_pred == 0)))
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    return (
        2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0
    )


def auc_roc(y_true: np.ndarray, y_proba: np.ndarray) -> float:
    """AUC-ROC simplificado. Devuelve 0.0 a 1.0."""
    # Ordena por probabilidad descendente y calcula TPR/FPR
    order = np.argsort(-y_proba)
    y_sorted = y_true[order]
    tps = np.cumsum(y_sorted)
    fps = np.cumsum(1 - y_sorted)
    tpr = tps / tps[-1] if tps[-1] > 0 else tps
    fpr = fps / fps[-1] if fps[-1] > 0 else fps
    return float(np.trapz(tpr, fpr))


def rmse(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Root Mean Squared Error. Devuelve >= 0."""
    return float(np.sqrt(np.mean((y_true - y_pred) ** 2)))


def mae(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Mean Absolute Error. Devuelve >= 0."""
    return float(np.mean(np.abs(y_true - y_pred)))
