# SOLID para AI Engineers — Parte 2: OCP, LSP e ISP

## Tabla de Contenidos

1. [Objetivos de Aprendizaje](#objetivos-de-aprendizaje)
2. [Prerrequisitos](#prerrequisitos)
3. [Introducción](#introducción)
4. [Open/Closed Principle (OCP)](#1-openclosed-principle-ocp)
5. [Liskov Substitution Principle (LSP)](#2-liskov-substitution-principle-lsp)
6. [Interface Segregation Principle (ISP)](#3-interface-segregation-principle-isp)
7. [Aprendizaje Clave](#aprendizaje-clave)
8. [Resumen de Principios](#resumen-de-principios)
9. [Referencias](#referencias)
10. [Ejercicio Individual](#ejercicio-individual)
11. [Ejercicio Grupal](#ejercicio-grupal)

---

## Objetivos de Aprendizaje

Al completar esta lección serás capaz de:

- Extender funcionalidad sin modificar código existente (OCP) usando el Strategy pattern con Protocols
- Identificar violaciones de LSP: sustituciones que rompen contratos
- Diseñar Protocols pequeños y enfocados en vez de interfaces gordas (ISP)
- Reconocer cómo OCP, LSP e ISP refuerzan las decisiones de diseño de los bloques anteriores

---

## Prerrequisitos

- Bloque 2 hoy: Composición sobre herencia, Protocols como contratos
- Bloque 3 hoy: SRP (una razón para cambiar) y DIP (depender de abstracciones)
- Familiaridad con `typing.Protocol` y composición por inyección

---

## Introducción

### Contexto: Por Qué Importa

**Problema real en Data/IA**:

Tu pipeline RAG usa embeddings de OpenAI. El equipo quiere probar Cohere. Para añadirlo, abres `EmbeddingService` y metes un `if provider == "cohere"` junto al `if provider == "openai"`. Funciona, pero ahora cada nuevo proveedor añade otro `if/elif`, los tests del flujo de OpenAI se vuelven a ejecutar aunque no los tocaste, y un día alguien introduce un bug en el bloque de Cohere que rompe OpenAI porque comparten estado.

Más tarde, un miembro del equipo crea un `FakeEmbeddingProvider` para tests. Cumple el Protocol `EmbeddingProvider`, pero en vez de devolver vectores de dimensión 256 como los reales, devuelve vectores de dimensión 3. El pipeline downstream se rompe con un error críptico 20 líneas más abajo. El fake "cumple el contrato" según el type checker, pero viola las expectativas semánticas.

**¿Qué veremos hoy?**

Los tres principios SOLID restantes son más sutiles que SRP y DIP. No los vas a aplicar conscientemente cada día, pero sí necesitas reconocer cuándo los estás violando — porque los síntomas son bugs difíciles de diagnosticar:

- **OCP**: "Cada nuevo feature requiere modificar código que ya funciona" → riesgo de regresiones
- **LSP**: "Sustituí una implementación y se rompió todo" → contrato violado
- **ISP**: "Mi clase tiene que implementar 5 métodos pero solo usa 2" → interfaz gorda

### Principio Fundamental

> "Software entities should be open for extension, but closed for modification."
>
> — Bertrand Meyer, *Object-Oriented Software Construction* (1988)

### Conexión con Bloques Anteriores

Si aplicaste SRP y DIP correctamente en el Bloque 3, ya tienes piezas independientes conectadas por Protocols. OCP, LSP e ISP te ayudan a afinar esas piezas:

- **OCP**: ¿Puedo añadir una pieza nueva sin tocar las existentes?
- **LSP**: ¿Cualquier pieza que cumpla el Protocol realmente funciona como se espera?
- **ISP**: ¿Mis Protocols piden solo lo necesario, o fuerzan métodos que no todos necesitan?

---

## 1. Open/Closed Principle (OCP)

### Por Qué Importa

OCP dice que deberías poder **extender** el comportamiento de tu sistema (añadir un nuevo proveedor de embeddings, un nuevo formato de datos, un nuevo modelo) **sin modificar** el código existente que ya funciona y está testeado.

Cada vez que abres un archivo que funciona para añadir un `elif`, introduces riesgo de regresión. OCP te empuja a diseñar código donde añadir = crear algo nuevo, no modificar lo existente.

### Ejemplo Incorrecto

```python
import logging

import numpy as np

logger = logging.getLogger(__name__)


class EmbeddingService:
    """Servicio de embeddings — viola OCP con if/elif."""

    def __init__(self, provider: str, api_key: str):
        self.provider = provider
        self.api_key = api_key

    def embed(self, texts: list[str]) -> list[list[float]]:
        if self.provider == "openai":
            return self._embed_openai(texts)
        elif self.provider == "cohere":
            return self._embed_cohere(texts)
        elif self.provider == "bedrock":
            return self._embed_bedrock(texts)
        else:
            raise ValueError(f"Unknown provider: {self.provider}")

    def _embed_openai(self, texts: list[str]) -> list[list[float]]:
        logger.info(f"Embedding {len(texts)} texts with OpenAI")
        # Llama a API de OpenAI...
        return [[0.1] * 256 for _ in texts]  # Simulado

    def _embed_cohere(self, texts: list[str]) -> list[list[float]]:
        logger.info(f"Embedding {len(texts)} texts with Cohere")
        # Llama a API de Cohere...
        return [[0.2] * 384 for _ in texts]  # Simulado

    def _embed_bedrock(self, texts: list[str]) -> list[list[float]]:
        logger.info(f"Embedding {len(texts)} texts with Bedrock")
        # Llama a API de Bedrock...
        return [[0.3] * 1024 for _ in texts]  # Simulado
```

**Problemas**:

- **Cada nuevo proveedor modifica esta clase**: Añadir HuggingFace requiere abrir `EmbeddingService`, añadir un `elif` y un método privado
- **Riesgo de regresión**: Al editar la clase, puedes romper proveedores existentes
- **Tests acoplados**: Los tests de OpenAI se re-ejecutan cuando cambias Cohere porque es la misma clase
- **if/elif creciente**: Con 10 proveedores, `embed()` tiene 10 ramas — difícil de mantener
- **Viola SRP también**: La clase tiene N razones de cambio (una por proveedor)

### Qué Cambiar y Por Qué

1. if/elif por proveedor → una clase por proveedor, cada una cumple un Protocol (Strategy pattern)
2. Lógica de selección en la clase → composición en el punto de entrada (DIP)
3. Nuevo proveedor = modificar clase existente → nuevo proveedor = crear clase nueva

### Ejemplo Correcto: Strategy Pattern con Protocols

```python
import logging
from typing import Protocol

logger = logging.getLogger(__name__)


# --- Contrato: qué significa "un embedder" ---

class TextEmbedder(Protocol):
    """Contrato: genera embeddings para una lista de textos."""

    def embed(self, texts: list[str]) -> list[list[float]]: ...


# --- Implementaciones: una por proveedor, independientes entre sí ---

class OpenAIEmbedder:
    """Embeddings via OpenAI. NO hereda de TextEmbedder."""

    def __init__(self, api_key: str, model: str = "text-embedding-3-small"):
        self._api_key = api_key
        self._model = model

    def embed(self, texts: list[str]) -> list[list[float]]:
        logger.info(f"OpenAI embedding: {len(texts)} texts with {self._model}")
        # Llama a API de OpenAI...
        return [[0.1] * 256 for _ in texts]


class CohereEmbedder:
    """Embeddings via Cohere. Independiente de OpenAI."""

    def __init__(self, api_key: str, model: str = "embed-english-v3.0"):
        self._api_key = api_key
        self._model = model

    def embed(self, texts: list[str]) -> list[list[float]]:
        logger.info(f"Cohere embedding: {len(texts)} texts with {self._model}")
        # Llama a API de Cohere...
        return [[0.2] * 384 for _ in texts]


# --- Añadir HuggingFace: crear archivo nuevo, NO tocar los existentes ---

class HuggingFaceEmbedder:
    """NUEVO proveedor — cero modificaciones a código existente."""

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self._model_name = model_name

    def embed(self, texts: list[str]) -> list[list[float]]:
        logger.info(f"HuggingFace embedding: {len(texts)} texts with {self._model_name}")
        # Carga modelo local de sentence-transformers...
        return [[0.3] * 384 for _ in texts]
```

El servicio de alto nivel usa el Protocol — no sabe qué implementación recibe:

```python
class RAGService:
    """Servicio RAG — cerrado para modificación, abierto para extensión."""

    def __init__(self, embedder: TextEmbedder):
        self._embedder = embedder

    def index_documents(self, documents: list[str]) -> list[list[float]]:
        logger.info(f"Indexing {len(documents)} documents")
        return self._embedder.embed(documents)


# --- Composición en el punto de entrada ---

# Hoy usamos OpenAI
service = RAGService(embedder=OpenAIEmbedder(api_key="sk-..."))

# Mañana probamos HuggingFace — sin tocar RAGService ni OpenAIEmbedder
service_hf = RAGService(embedder=HuggingFaceEmbedder())
```

**Ventajas**:

- **Añadir proveedor = crear archivo nuevo**: `HuggingFaceEmbedder` no toca nada existente
- **Cero riesgo de regresión**: El código de OpenAI no se modifica al añadir Cohere
- **Tests independientes**: Cada embedder tiene sus propios tests
- **Strategy pattern natural**: El Protocol es la estrategia, las clases son implementaciones intercambiables

### OCP y el Bloque 1 (Pydantic)

Recuerda las discriminated unions del Bloque 1. Son OCP aplicado a datos: añadir un nuevo tipo de config no modifica los existentes, solo añades un nuevo modelo al `Union`.

```python
# Bloque 1: añadir BedrockEmbeddingConfig no toca OpenAIEmbeddingConfig
EmbeddingConfig = Annotated[
    Union[OpenAIEmbeddingConfig, BedrockEmbeddingConfig, CohereEmbeddingConfig],
    Field(discriminator="provider"),
]
```

---

## 2. Liskov Substitution Principle (LSP)

### Por Qué Importa

LSP dice que si tu código funciona con un Protocol `TextEmbedder`, debe funcionar **correctamente** con CUALQUIER implementación que cumpla ese Protocol. No basta con que tenga los métodos correctos — tiene que respetar las expectativas semánticas del contrato.

Dicho de otra forma: sustituir una implementación por otra que cumple el mismo Protocol no debería romper nada. Si lo hace, la implementación viola LSP.

### Ejemplo Incorrecto: Violación de LSP

```python
from typing import Protocol

import pandas as pd


class DataLoader(Protocol):
    def load(self, source: str) -> pd.DataFrame: ...


class CSVLoader:
    """Implementación correcta — cumple el contrato completo."""

    def load(self, source: str) -> pd.DataFrame:
        return pd.read_csv(source)


class CachedLoader:
    """Implementación que VIOLA LSP — cambia el comportamiento esperado."""

    def __init__(self):
        self._cache: dict[str, pd.DataFrame] = {}

    def load(self, source: str) -> pd.DataFrame:
        if source in self._cache:
            return self._cache[source]  # Devuelve datos viejos silenciosamente

        data = pd.read_csv(source)
        self._cache[source] = data
        return data


# Parece que funciona...
def refresh_dashboard(loader: DataLoader, path: str) -> dict:
    """Carga datos frescos para actualizar un dashboard."""
    data = loader.load(path)
    return {"total_rows": len(data), "last_value": data.iloc[-1].to_dict()}


# Con CSVLoader: siempre lee datos frescos ✓
# Con CachedLoader: devuelve datos viejos aunque el archivo cambió ✗
# El contrato implícito de "load" es "lee datos del source". CachedLoader no lo cumple
# si el source se actualizó desde la última llamada.
```

**Problemas**:

- `CachedLoader` cumple la firma del Protocol (tiene `.load(str) → DataFrame`)
- Pero viola la expectativa semántica: `load` debería leer del source, no de una cache interna
- `refresh_dashboard` confía en que `load` devuelve datos actuales — con `CachedLoader`, no es así
- El error no aparece en el type checker — aparece como datos incorrectos en producción

### Qué Cambiar y Por Qué

1. Si el caching es un requisito legítimo, hacerlo **explícito** en la interfaz, no escondido
2. La implementación debe cumplir las expectativas completas del contrato, no solo la firma

### Ejemplo Correcto: Cache Explícita

```python
class DataLoader(Protocol):
    """Contrato: carga datos FRESCOS desde el source."""

    def load(self, source: str) -> pd.DataFrame: ...


class CSVLoader:
    def load(self, source: str) -> pd.DataFrame:
        return pd.read_csv(source)


class CachingDataLoader:
    """Cache EXPLÍCITA — composición, no sustitución oculta."""

    def __init__(self, inner_loader: DataLoader, ttl_seconds: int = 300):
        self._inner = inner_loader
        self._ttl = ttl_seconds
        self._cache: dict[str, tuple[float, pd.DataFrame]] = {}

    def load(self, source: str) -> pd.DataFrame:
        """Carga con cache — la cache es VISIBLE en el nombre de la clase."""
        now = time.time()
        if source in self._cache:
            cached_at, data = self._cache[source]
            if now - cached_at < self._ttl:
                logger.debug(f"Cache hit for {source} (age: {now - cached_at:.0f}s)")
                return data

        data = self._inner.load(source)
        self._cache[source] = (now, data)
        return data

    def invalidate(self, source: str) -> None:
        """Permite invalidar la cache explícitamente."""
        self._cache.pop(source, None)


# Uso explícito — quien compone sabe que hay cache
loader = CachingDataLoader(inner_loader=CSVLoader(), ttl_seconds=60)
```

**Ventajas**:

- `CachingDataLoader` todavía cumple `DataLoader` Protocol (para el type checker)
- Pero la cache es **visible y controlable**: TTL, invalidación, nombre explícito
- Quien compone el pipeline elige conscientemente si quiere cache o no
- No hay sorpresas ocultas cuando sustituyes implementaciones

### Señales de Violación LSP en la Práctica

En tu día a día, las violaciones de LSP no suelen ser tan obvias como el ejemplo. Aparecen como:

- **Excepciones inesperadas**: Una implementación lanza errores que otra no lanza, y el código que llama no los maneja
- **Valores de retorno sorprendentes**: Una implementación devuelve `None` donde otra devuelve un DataFrame vacío
- **Efectos secundarios ocultos**: Una implementación escribe en disco, otra no. Una hace logging, otra no
- **Precondiciones más estrictas**: Una implementación acepta cualquier string como `source`, otra solo acepta URLs válidas

La defensa más práctica contra LSP es escribir tests con múltiples implementaciones:

```python
import pytest


# El mismo test, múltiples implementaciones — si alguna falla, viola LSP
@pytest.mark.parametrize("loader", [CSVLoader(), ParquetLoader()])
def test_loader_returns_dataframe_with_expected_columns(loader, sample_file):
    result = loader.load(sample_file)
    assert isinstance(result, pd.DataFrame)
    assert len(result) > 0
    assert "expected_column" in result.columns
```

---

## 3. Interface Segregation Principle (ISP)

### Por Qué Importa

ISP dice que ninguna clase debería verse forzada a depender de métodos que no usa. En términos de Protocols: mantén tus Protocols pequeños y enfocados. Un Protocol gordo con 5 métodos fuerza a todas las implementaciones a implementar los 5, aunque solo necesiten 2.

### Ejemplo Incorrecto

```python
class MLModelService(Protocol):
    """Protocol gordo — fuerza a implementar TODO."""

    def train(self, X: pd.DataFrame, y: pd.Series) -> None: ...
    def predict(self, X: pd.DataFrame) -> np.ndarray: ...
    def predict_proba(self, X: pd.DataFrame) -> np.ndarray: ...
    def save(self, path: str) -> None: ...
    def load(self, path: str) -> None: ...
    def get_feature_importance(self) -> dict[str, float]: ...
    def explain_prediction(self, X: pd.DataFrame) -> dict: ...


class LinearRegressionModel:
    """Implementación que NO puede cumplir todo el Protocol."""

    def train(self, X: pd.DataFrame, y: pd.Series) -> None:
        # OK
        ...

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        # OK
        ...

    def predict_proba(self, X: pd.DataFrame) -> np.ndarray:
        # Regresión lineal NO tiene probabilidades
        raise NotImplementedError("Linear regression doesn't support predict_proba")

    def save(self, path: str) -> None:
        # OK
        ...

    def load(self, path: str) -> None:
        # OK
        ...

    def get_feature_importance(self) -> dict[str, float]:
        # Coeficientes, no "importancia" — semántica diferente
        ...

    def explain_prediction(self, X: pd.DataFrame) -> dict:
        # No tiene SHAP nativo
        raise NotImplementedError("No explanation support")
```

**Problemas**:

- `LinearRegressionModel` implementa 7 métodos pero solo puede cumplir 4 genuinamente
- `raise NotImplementedError` es un code smell del Bloque 2: indica que la interfaz fuerza métodos que no aplican
- Cualquier consumidor del Protocol recibe 7 métodos aunque solo necesite `predict()`
- Es el mismo anti-pattern que vimos con el override vacío de `remove_outliers()` en el Bloque 2 — la interfaz no encaja

### Qué Cambiar y Por Qué

1. Un Protocol gordo → varios Protocols pequeños (uno por capacidad)
2. `raise NotImplementedError` desaparece — si no aplica, no lo implementes
3. Los consumidores dependen solo del Protocol que necesitan

### Ejemplo Correcto: Protocols Segregados

```python
from typing import Protocol

import numpy as np
import pandas as pd


# --- Protocols pequeños: una capacidad cada uno ---

class Trainable(Protocol):
    """Puede entrenarse con datos."""

    def train(self, X: pd.DataFrame, y: pd.Series) -> None: ...


class Predictor(Protocol):
    """Puede hacer predicciones."""

    def predict(self, X: pd.DataFrame) -> np.ndarray: ...


class ProbabilisticPredictor(Protocol):
    """Puede predecir probabilidades — NO todos los modelos pueden."""

    def predict_proba(self, X: pd.DataFrame) -> np.ndarray: ...


class Persistable(Protocol):
    """Puede guardarse y cargarse."""

    def save(self, path: str) -> None: ...
    def load(self, path: str) -> None: ...


class Explainable(Protocol):
    """Puede explicar sus predicciones — capacidad opcional."""

    def explain_prediction(self, X: pd.DataFrame) -> dict: ...
```

Las implementaciones solo implementan lo que les corresponde:

```python
class LinearRegressionModel:
    """Cumple Trainable, Predictor, Persistable. NO ProbabilisticPredictor."""

    def train(self, X: pd.DataFrame, y: pd.Series) -> None:
        ...

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        ...

    def save(self, path: str) -> None:
        ...

    def load(self, path: str) -> None:
        ...

    # No implementa predict_proba — y no tiene que hacerlo
    # No implementa explain_prediction — y no tiene que hacerlo


class RandomForestModel:
    """Cumple TODO: Trainable, Predictor, ProbabilisticPredictor, Persistable, Explainable."""

    def train(self, X: pd.DataFrame, y: pd.Series) -> None:
        ...

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        ...

    def predict_proba(self, X: pd.DataFrame) -> np.ndarray:
        ...

    def save(self, path: str) -> None:
        ...

    def load(self, path: str) -> None:
        ...

    def explain_prediction(self, X: pd.DataFrame) -> dict:
        ...
```

Los consumidores piden **solo lo que necesitan**:

```python
class BatchPredictor:
    """Solo necesita predecir — pide Predictor, no todo el modelo."""

    def __init__(self, model: Predictor):  # ← Protocol mínimo
        self._model = model

    def predict_batch(self, data: pd.DataFrame) -> np.ndarray:
        return self._model.predict(data)


class ModelEvaluator:
    """Evalúa con AUC-ROC — necesita probabilidades."""

    def __init__(self, model: ProbabilisticPredictor):  # ← Solo lo que necesita
        self._model = model

    def evaluate_auc(self, X: pd.DataFrame, y: pd.Series) -> float:
        probas = self._model.predict_proba(X)
        return roc_auc_score(y, probas[:, 1])


# LinearRegressionModel funciona con BatchPredictor ✓
batch = BatchPredictor(model=LinearRegressionModel())

# LinearRegressionModel NO funciona con ModelEvaluator — y pyright te lo dice ✗
# evaluator = ModelEvaluator(model=LinearRegressionModel())  # Type error
# Esto es CORRECTO — regresión lineal no tiene predict_proba

# RandomForestModel funciona con ambos ✓
batch_rf = BatchPredictor(model=RandomForestModel())
evaluator_rf = ModelEvaluator(model=RandomForestModel())
```

**Ventajas**:

- **Cero `NotImplementedError`**: Si una clase no implementa un método, es porque el Protocol no lo exige
- **El type checker detecta incompatibilidades**: `LinearRegressionModel` no pasa donde se espera `ProbabilisticPredictor`
- **Composición granular**: Cada consumidor pide exactamente lo que necesita
- **Extensible**: Puedes añadir un Protocol `Retrainable` sin tocar los existentes (OCP también)

### ¿Cuándo es "demasiado ISP"?

Si acabas con 10 Protocols de un método cada uno y cada consumidor necesita combinar 5, te has pasado. La regla práctica: **agrupa lo que siempre se usa junto**.

```python
# Demasiado granular — predict sin train no tiene sentido
class Trainable(Protocol):
    def train(self, X, y) -> None: ...

class Predictor(Protocol):
    def predict(self, X) -> np.ndarray: ...

# Mejor: un Protocol para lo que siempre va junto
class SupervisedModel(Protocol):
    """Train y predict siempre se usan juntos."""
    def train(self, X: pd.DataFrame, y: pd.Series) -> None: ...
    def predict(self, X: pd.DataFrame) -> np.ndarray: ...
```

Señales de que te pasaste:

- Todos los consumidores piden 3+ Protocols combinados → probablemente deberían ser uno
- Tienes Protocols de un solo método que nunca se usan solos
- El código de composición es más largo que el código de negocio

---

## Aprendizaje Clave

### Puntos Críticos a Recordar

1. **OCP = extender sin modificar**. Cada nuevo proveedor/formato/modelo es una clase nueva, no un `elif` en una clase existente
2. **LSP = las sustituciones no rompen nada**. Si cumple el Protocol, debe funcionar correctamente — no solo compilar
3. **ISP = Protocols pequeños y enfocados**. No fuerces a implementar métodos que no aplican
4. **OCP + DIP (Bloque 3) = Strategy pattern**. Las piezas intercambiables son la forma natural de cumplir OCP
5. **`raise NotImplementedError` es una señal de violación** — de ISP (Protocol gordo) o de LSP (la implementación no cumple el contrato)

### Cómo Desarrollar Intuición

**¿Estoy violando OCP?**

- ¿Cada nuevo requisito te obliga a abrir y modificar una clase existente? → Sí
- ¿Tienes cadenas de if/elif por tipo de proveedor/formato/modelo? → Sí
- ¿Los tests de funcionalidad A se re-ejecutan cuando cambias funcionalidad B? → Probablemente

**¿Estoy violando LSP?**

- ¿Una implementación lanza excepciones que otra no lanza? → Posible violación
- ¿Una implementación devuelve datos en formato diferente al esperado? → Sí
- ¿Sustituyendo una implementación por otra del mismo Protocol se rompe algo? → Sí
- Test práctico: ¿puedo correr los mismos tests con todas las implementaciones del Protocol?

**¿Estoy violando ISP?**

- ¿Alguna implementación tiene `raise NotImplementedError`? → Sí, Protocol demasiado gordo
- ¿Alguna implementación tiene métodos vacíos (`pass`)? → Sí
- ¿Tu consumidor usa solo 2 de los 6 métodos del Protocol? → Sí, necesita un Protocol más pequeño

### Anti-patterns Rápidos

| ❌ No hagas esto | ✅ Haz esto |
| --- | --- |
| if/elif por proveedor en una clase | Una clase por proveedor, Protocol común (OCP) |
| Fake que cumple la firma pero no la semántica | Fake que respeta expectativas del contrato (LSP) |
| Protocol con 7 métodos donde no todos aplican | Protocols de 1-3 métodos agrupados por uso (ISP) |
| `raise NotImplementedError` en una implementación | No implementar ese Protocol — que el type checker avise (ISP) |
| `except NotImplementedError` en el consumidor | Pedir el Protocol correcto en el type hint (ISP) |
| Cache oculta dentro de una implementación "normal" | Cache explícita como wrapper/decorador (LSP) |

---

## Resumen de Principios

OCP te permite extender tu sistema añadiendo código nuevo sin tocar código existente — en la práctica, es el Strategy pattern con Protocols e inyección de dependencias. LSP garantiza que cualquier implementación que cumpla un Protocol funcione correctamente como sustituto, no solo que compile — testea con múltiples implementaciones para verificarlo. ISP te empuja a diseñar Protocols pequeños y enfocados donde cada consumidor depende solo de los métodos que necesita — si ves `NotImplementedError`, tu Protocol es demasiado gordo. Los tres principios se conectan con SRP y DIP del Bloque 3 para producir un sistema de piezas independientes, intercambiables y combinables.

---

## Referencias

1. Martin, R. C. (2017). *Clean Architecture*. Prentice Hall. Part III: Design Principles (Chapters 8, 9, 10).
2. Meyer, B. (1988). *Object-Oriented Software Construction*. Prentice Hall. (Origen del OCP).
3. Liskov, B. & Wing, J. (1994). "A Behavioral Notion of Subtyping". *ACM TOPLAS*.
4. PEP 544 – Protocols: <https://peps.python.org/pep-0544/>
5. Gamma, E. et al. (1994). *Design Patterns*. Addison-Wesley. Strategy Pattern.

---

## Ejercicio Individual

**Objetivo**: Identificar violaciones de OCP, LSP e ISP en un fragmento de código y proponer correcciones.

**Tiempo estimado**: 15 minutos

### Código para Analizar

```python
from typing import Protocol

import numpy as np
import pandas as pd


class DataTransformer(Protocol):
    """Transforma datos para un pipeline de ML."""

    def fit(self, data: pd.DataFrame) -> None: ...
    def transform(self, data: pd.DataFrame) -> pd.DataFrame: ...
    def inverse_transform(self, data: pd.DataFrame) -> pd.DataFrame: ...
    def get_params(self) -> dict: ...
    def save_state(self, path: str) -> None: ...


class StandardScalerTransformer:
    def fit(self, data: pd.DataFrame) -> None:
        self._means = data.mean()
        self._stds = data.std()

    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        return (data - self._means) / self._stds

    def inverse_transform(self, data: pd.DataFrame) -> pd.DataFrame:
        return data * self._stds + self._means

    def get_params(self) -> dict:
        return {"means": self._means.to_dict(), "stds": self._stds.to_dict()}

    def save_state(self, path: str) -> None:
        import joblib
        joblib.dump({"means": self._means, "stds": self._stds}, path)


class OneHotEncoderTransformer:
    def fit(self, data: pd.DataFrame) -> None:
        self._categories = {col: data[col].unique() for col in data.columns}

    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        return pd.get_dummies(data)

    def inverse_transform(self, data: pd.DataFrame) -> pd.DataFrame:
        # One-hot encoding es IRREVERSIBLE en general
        raise NotImplementedError("Cannot inverse transform one-hot encoding")

    def get_params(self) -> dict:
        return {"categories": self._categories}

    def save_state(self, path: str) -> None:
        import json
        with open(path, "w") as f:
            json.dump({k: v.tolist() for k, v in self._categories.items()}, f)


class DropColumnsTransformer:
    def __init__(self, columns: list[str]):
        self._columns = columns

    def fit(self, data: pd.DataFrame) -> None:
        pass  # No necesita fit — override vacío

    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        return data.drop(columns=self._columns)

    def inverse_transform(self, data: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError("Cannot recover dropped columns")

    def get_params(self) -> dict:
        return {"columns": self._columns}

    def save_state(self, path: str) -> None:
        pass  # No tiene estado que guardar — override vacío
```

### Tarea

Responde estas preguntas:

1. **ISP**: ¿Qué métodos del Protocol `DataTransformer` no todos los transformadores pueden cumplir genuinamente? ¿Cómo lo segregarías?
2. **LSP**: ¿Qué implementaciones violan las expectativas del contrato? ¿Cómo?
3. **OCP**: Si quieres añadir un `LogTransformer`, ¿necesitas modificar algo existente? ¿Es eso bueno o malo?
4. **Propuesta**: Escribe los Protocols segregados que resolverían los problemas (solo firmas, no implementaciones)

### Criterios de Éxito

- [ ] Identificaste al menos 2 métodos del Protocol que no todos los transformadores pueden cumplir
- [ ] Identificaste los `raise NotImplementedError` y `pass` como señales de ISP violado
- [ ] Propusiste al menos 2 Protocols más pequeños (`Transformer`, `Reversible`, etc.)
- [ ] Verificaste que OCP sí se cumple (añadir un nuevo transformer no toca los existentes)
- [ ] Tus Protocols segregados eliminan la necesidad de `NotImplementedError`

### Pistas

- `inverse_transform` no aplica a todos — debería ser un Protocol separado `ReversibleTransformer`
- `fit` vacío en `DropColumnsTransformer` sugiere que `fit` + `transform` no siempre van juntos
- Piensa en: `Transformer` (solo transform), `FittableTransformer` (fit + transform), `ReversibleTransformer` (+ inverse)
- `save_state` vacío sugiere que la persistencia debería ser otro Protocol (`Persistable`)

---

## Ejercicio Grupal

**Objetivo**: Diseñar un sistema de evaluación de modelos ML extensible, aplicando OCP, LSP e ISP.

**Contexto**: Tu equipo necesita evaluar modelos ML con diferentes métricas. Hoy usan accuracy y F1, pero constantemente añaden nuevas métricas (AUC-ROC, precision, recall, RMSE para regresión). Cada vez, alguien modifica la clase `ModelEvaluator` y rompe algo. Además, no todas las métricas aplican a todos los modelos: AUC-ROC necesita probabilidades, RMSE es solo para regresión.

**Tiempo estimado**: 45 minutos

### Dinámica

1. **Diseño** (15 min): Definan los Protocols, separando capacidades de modelos y tipos de métricas
2. **Implementación** (20 min): Creen las piezas y el evaluador compuesto
3. **Extensión** (10 min): Añadan una nueva métrica sin tocar código existente — demuestren que funciona

### Código Actual a Reemplazar

```python
class ModelEvaluator:
    """Evaluador monolítico — viola OCP cada vez que añades una métrica."""

    def evaluate(
        self,
        model,
        X_test: pd.DataFrame,
        y_test: pd.Series,
        metrics: list[str],
    ) -> dict[str, float]:
        results = {}
        predictions = model.predict(X_test)

        for metric_name in metrics:
            if metric_name == "accuracy":
                results["accuracy"] = accuracy_score(y_test, predictions)
            elif metric_name == "f1":
                results["f1"] = f1_score(y_test, predictions, average="weighted")
            elif metric_name == "precision":
                results["precision"] = precision_score(y_test, predictions, average="weighted")
            elif metric_name == "auc_roc":
                # No todos los modelos tienen predict_proba
                try:
                    probas = model.predict_proba(X_test)[:, 1]
                    results["auc_roc"] = roc_auc_score(y_test, probas)
                except AttributeError:
                    results["auc_roc"] = None  # Silencia el error
            elif metric_name == "rmse":
                results["rmse"] = np.sqrt(mean_squared_error(y_test, predictions))
            else:
                raise ValueError(f"Unknown metric: {metric_name}")

        return results
```

### Instrucciones por Persona

- **Persona 1 — Protocols y tipos**: Definir `Predictor`, `ProbabilisticPredictor` (ISP — segregar capacidades del modelo) y la estructura de datos `EvaluationResult`
- **Persona 2 — Métricas de clasificación**: Implementar `AccuracyMetric`, `F1Metric`, `PrecisionMetric` como piezas independientes que cumplan un Protocol `Metric` (OCP — cada métrica es una clase)
- **Persona 3 — Métricas especiales**: Implementar `AUCROCMetric` (requiere `ProbabilisticPredictor`, no solo `Predictor`) y `RMSEMetric` (solo para regresión). Usar Protocols distintos para cada requisito (ISP + LSP)
- **Persona 4 — Evaluador compuesto**: Crear `ComposableEvaluator` que recibe una lista de métricas y las aplica. Demostrar que añadir una nueva métrica (`RecallMetric`) no toca nada existente (OCP)

### Criterios de Éxito

- [ ] Cero if/elif por nombre de métrica — cada métrica es una clase con un Protocol
- [ ] `AUCROCMetric` requiere `ProbabilisticPredictor`, no genérico (ISP)
- [ ] No hay `try/except AttributeError` — el type system previene errores (LSP)
- [ ] `results["auc_roc"] = None` desaparece — si no aplica, no se calcula
- [ ] Añadir `RecallMetric` = crear 1 clase nueva, modificar 0 clases existentes (OCP)
- [ ] Todas las métricas del mismo tipo son intercambiables sin sorpresas (LSP)
- [ ] `EvaluationResult` es `@dataclass` o Pydantic, no un dict (coherencia con Bloque 1)

### Pistas

**Para Persona 1 — Protocols segregados**:

```python
class Predictor(Protocol):
    def predict(self, X: pd.DataFrame) -> np.ndarray: ...

class ProbabilisticPredictor(Protocol):
    def predict(self, X: pd.DataFrame) -> np.ndarray: ...
    def predict_proba(self, X: pd.DataFrame) -> np.ndarray: ...
```

**Para Persona 2 — Protocol de métrica**:

```python
class ClassificationMetric(Protocol):
    """Métrica que trabaja con predicciones (no probabilidades)."""
    @property
    def name(self) -> str: ...
    def compute(self, y_true: pd.Series, y_pred: np.ndarray) -> float: ...

class AccuracyMetric:
    @property
    def name(self) -> str:
        return "accuracy"

    def compute(self, y_true: pd.Series, y_pred: np.ndarray) -> float:
        return accuracy_score(y_true, y_pred)
```

**Para Persona 3 — Métrica que requiere probabilidades**:

```python
class ProbabilisticMetric(Protocol):
    """Métrica que NECESITA probabilidades — Protocol separado."""
    @property
    def name(self) -> str: ...
    def compute(self, y_true: pd.Series, y_proba: np.ndarray) -> float: ...
```

**Para Persona 4 — Evaluador compuesto**:

```python
class ComposableEvaluator:
    def __init__(
        self,
        classification_metrics: list[ClassificationMetric],
        probabilistic_metrics: list[ProbabilisticMetric] | None = None,
    ):
        self._cls_metrics = classification_metrics
        self._prob_metrics = probabilistic_metrics or []

    def evaluate(
        self,
        model: Predictor,
        X_test: pd.DataFrame,
        y_test: pd.Series,
    ) -> EvaluationResult:
        predictions = model.predict(X_test)
        results = {m.name: m.compute(y_test, predictions) for m in self._cls_metrics}

        # Solo calcula métricas probabilísticas si el modelo las soporta
        if self._prob_metrics and isinstance(model, ProbabilisticPredictor):
            probas = model.predict_proba(X_test)
            for m in self._prob_metrics:
                results[m.name] = m.compute(y_test, probas[:, 1])

        return EvaluationResult(metrics=results)
```

### Preguntas para Reflexión

1. ¿Cuántas líneas de la clase original se modifican al añadir una métrica nueva? ¿Y en vuestra solución?
2. ¿Qué pasa con `results["auc_roc"] = None`? ¿Por qué es mejor que el type system prevenga ese caso?
3. ¿Qué Protocols definisteis? ¿Alguno tiene más de 3 métodos? Si sí, ¿debería segregarse más?
4. Si un modelo de regresión cumple `Predictor`, ¿es válido pasarlo a una `ClassificationMetric` como accuracy? ¿Es eso un problema de LSP?
5. ¿Cómo se relaciona este ejercicio con el Strategy pattern de OCP y con la composición del Bloque 2?

---

## Aplicación al Proyecto de Equipo

- [ ] Revisa si tu proyecto tiene cadenas if/elif por tipo o proveedor. Si sí, evalúa aplicar Strategy pattern (OCP)
- [ ] Busca `raise NotImplementedError` o métodos vacíos (`pass`) — son señales de Protocols gordos (ISP)
- [ ] Si tienes tests que fallan al sustituir una implementación por otra del mismo Protocol, investiga si la nueva implementación viola expectativas semánticas (LSP)
- [ ] Verifica que tus Protocols tienen 1-3 métodos cada uno. Si alguno tiene más de 4, considera segregarlo