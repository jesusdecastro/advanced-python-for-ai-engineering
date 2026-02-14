"""
Protocols para el sistema de evaluación.

NO MODIFICAR.

NOTA: Hay TRES Protocols distintos, no uno gordo. Esto es ISP:
- ClassificationMetric: métricas que comparan y_true con y_pred
- ProbabilisticMetric: métricas que necesitan probabilidades (y_proba)
- RegressionMetric: métricas para problemas de regresión

¿Por qué separados? Porque no todos los modelos tienen predict_proba,
y métricas de regresión (RMSE) no tienen sentido para clasificación.
"""

from typing import Protocol

import numpy as np


class ClassificationMetric(Protocol):
    @property
    def name(self) -> str: ...

    def compute(self, y_true: np.ndarray, y_pred: np.ndarray) -> float: ...


class ProbabilisticMetric(Protocol):
    @property
    def name(self) -> str: ...

    def compute(self, y_true: np.ndarray, y_proba: np.ndarray) -> float: ...


class RegressionMetric(Protocol):
    @property
    def name(self) -> str: ...

    def compute(self, y_true: np.ndarray, y_pred: np.ndarray) -> float: ...
