# Bloque 4: OCP, LSP, ISP

## Objetivo

Practicar Open-Closed Principle (OCP), Liskov Substitution Principle (LSP) e Interface Segregation Principle (ISP).

## Concepto que se Practica

- Open-Closed Principle (OCP): Añadir métricas sin modificar evaluador
- Liskov Substitution Principle (LSP): Todas las métricas del mismo Protocol son intercambiables
- Interface Segregation Principle (ISP): Protocols segregados para clasificación vs regresión vs probabilístico

## Qué NO es el Foco

- Implementar métricas desde cero
- Se les da helpers.py con las fórmulas resueltas

## Descripción

Vas a crear un sistema extensible de métricas para evaluación de modelos. Las fórmulas están resueltas en helpers.py. Tu trabajo es diseñar las clases de métricas y los evaluadores que las componen.

## Archivos Proporcionados

- `helpers.py`: Fórmulas de métricas YA IMPLEMENTADAS
- `protocols.py`: Tres Protocols distintos (ISP)
- `evaluation.py`: Esqueleto con hints para implementar

## Por Qué Tres Protocols (ISP)

- **ClassificationMetric**: Métricas que comparan y_true con y_pred
- **ProbabilisticMetric**: Métricas que necesitan probabilidades (y_proba)
- **RegressionMetric**: Métricas para problemas de regresión

¿Por qué separados? Porque no todos los modelos tienen `predict_proba`, y métricas de regresión (RMSE) no tienen sentido para clasificación.

## Tips para Implementar

### 1. Empieza por AccuracyMetric

```bash
uv run pytest tests/bloque_4/test_evaluation.py::test_accuracy_metric_perfect -v
```

Cada métrica es 5-8 líneas:
```python
class AccuracyMetric:
    @property
    def name(self) -> str:
        return "accuracy"
    
    def compute(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        return accuracy(y_true, y_pred)
```

### 2. Las Demás Métricas

```bash
uv run pytest tests/bloque_4/ -k "metric" -v
```

Las clases de métrica son casi idénticas entre sí — la diferencia es qué función de helpers llaman y qué nombre devuelven.

- **F1Metric**: llama a `f1_binary()`
- **AUCROCMetric**: llama a `auc_roc()` (recibe y_proba, no y_pred)
- **RMSEMetric**: llama a `rmse()`
- **MAEMetric**: llama a `mae()`

### 3. ClassificationEvaluator

```bash
uv run pytest tests/bloque_4/test_evaluation.py::test_classification_evaluator_applies_all_metrics -v
```

El método `evaluate()` es un dict comprehension:
```python
metrics_dict = {m.name: m.compute(y_true, y_pred) for m in self._metrics}
```

Si `y_proba` no es None, añade las métricas probabilísticas:
```python
if y_proba is not None:
    for m in self._probabilistic_metrics:
        metrics_dict[m.name] = m.compute(y_true, y_proba)
```

### 4. RegressionEvaluator

```bash
uv run pytest tests/bloque_4/test_evaluation.py::test_regression_evaluator_applies_all_metrics -v
```

Mismo patrón que ClassificationEvaluator pero con RegressionMetric.

### 5. Test OCP (el más importante)

```bash
uv run pytest tests/bloque_4/test_evaluation.py::test_adding_new_metric_no_changes_needed -v
```

Este test define un `RecallMetric` DENTRO del test y lo pasa al evaluador. Si funciona sin tocar tu evaluador, cumples OCP.

## La Pregunta Clave para Verificar OCP

Si mañana quieres añadir una métrica nueva (por ejemplo, Precision), ¿qué código tocas?

**Respuesta correcta**: Solo creas la clase `PrecisionMetric` y la pasas en la lista. `ClassificationEvaluator` no cambia. Eso es OCP.

## Ejecutar Tests

```bash
# Todos los tests del bloque
uv run pytest tests/bloque_4/ -v

# Tests de métricas individuales
uv run pytest tests/bloque_4/ -k "metric" -v

# Tests de evaluadores
uv run pytest tests/bloque_4/ -k "evaluator" -v

# Test de OCP (el más importante)
uv run pytest tests/bloque_4/test_evaluation.py::test_adding_new_metric_no_changes_needed -v

# Test de LSP
uv run pytest tests/bloque_4/test_evaluation.py::test_all_classification_metrics_return_0_to_1 -v
```

## Criterios de Éxito

- [ ] Cada métrica es 5-8 líneas (property + compute)
- [ ] Todas las métricas usan funciones de helpers.py
- [ ] ClassificationEvaluator itera sobre lista de métricas
- [ ] RegressionEvaluator itera sobre lista de métricas
- [ ] Test OCP pasa (RecallMetric definido en test funciona)
- [ ] Test LSP pasa (todas las métricas devuelven float en [0, 1])
- [ ] EvaluationResult es inmutable (frozen=True)
- [ ] Todos los tests pasan

## Recursos

- **SOLID Principles**: https://en.wikipedia.org/wiki/SOLID
- **Open-Closed Principle**: https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle
- **Liskov Substitution**: https://en.wikipedia.org/wiki/Liskov_substitution_principle
- **Interface Segregation**: https://en.wikipedia.org/wiki/Interface_segregation_principle
