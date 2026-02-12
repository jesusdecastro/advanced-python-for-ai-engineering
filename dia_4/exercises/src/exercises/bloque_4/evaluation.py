"""
Sistema de evaluación de modelos — practica OCP, LSP e ISP.

Tu trabajo:
1. Implementar métricas concretas que cumplan los Protocols
2. Implementar evaluadores que reciben listas de métricas (composición)
3. Verificar que añadir una métrica nueva NO toca código existente (OCP)
"""

from dataclasses import dataclass

import numpy as np

from .helpers import accuracy, auc_roc, f1_binary, mae, rmse
from .protocols import ClassificationMetric, ProbabilisticMetric, RegressionMetric


# --- Estructura de datos: resultado de la evaluación ---


@dataclass(frozen=True)
class EvaluationResult:
    """
    Resultado de evaluar un modelo.

    Hints:
    - Campos: metrics (dict[str, float]), model_name (str)
    """

    ...


# --- Métricas de clasificación (cumplen ClassificationMetric) ---


class AccuracyMetric:
    """
    Calcula accuracy. Cumple ClassificationMetric.

    Hints:
    - @property name devuelve "accuracy" (un string fijo).
    - compute() llama a accuracy() de helpers.py. UNA línea.
    """

    ...


class F1Metric:
    """
    Calcula F1 score. Cumple ClassificationMetric.

    Hints:
    - @property name devuelve "f1".
    - compute() llama a f1_binary() de helpers.py. UNA línea.
    """

    ...


# --- Métrica probabilística (cumple ProbabilisticMetric) ---


class AUCROCMetric:
    """
    Calcula AUC-ROC. Cumple ProbabilisticMetric (NO ClassificationMetric).

    Hints:
    - @property name devuelve "auc_roc".
    - compute() llama a auc_roc() de helpers.py.
    - NOTA: recibe y_proba (probabilidades), no y_pred (predicciones).
      Por eso es un Protocol DISTINTO.
    """

    ...


# --- Métricas de regresión (cumplen RegressionMetric) ---


class RMSEMetric:
    """
    Calcula RMSE. Cumple RegressionMetric.

    Hints:
    - @property name devuelve "rmse".
    - compute() llama a rmse() de helpers.py.
    """

    ...


class MAEMetric:
    """
    Calcula MAE. Cumple RegressionMetric.

    Hints:
    - @property name devuelve "mae".
    - compute() llama a mae() de helpers.py.
    """

    ...


# --- Evaluador de clasificación ---


class ClassificationEvaluator:
    """
    Evalúa un modelo de clasificación con N métricas.

    Hints:
    - __init__ recibe:
      * metrics: list[ClassificationMetric]
      * probabilistic_metrics: list[ProbabilisticMetric] (default lista vacía)
      * model_name: str (default "unnamed")
    - Método evaluate(y_true, y_pred, y_proba=None) -> EvaluationResult:
      1. Calcula cada métrica de clasificación: m.compute(y_true, y_pred)
      2. Si y_proba no es None, calcula cada métrica probabilística
      3. Junta todo en un dict y devuelve EvaluationResult

    CLAVE OCP: este evaluador NO sabe qué métricas tiene. Solo itera
    sobre la lista. Añadir RecallMetric = crear clase, pasarla en la lista.
    Cero cambios aquí.
    """

    ...


# --- Evaluador de regresión ---


class RegressionEvaluator:
    """
    Evalúa un modelo de regresión con N métricas.

    Hints:
    - Mismo patrón que ClassificationEvaluator pero con RegressionMetric.
    - __init__ recibe: metrics: list[RegressionMetric], model_name: str
    - Método evaluate(y_true, y_pred) -> EvaluationResult
    """

    ...
