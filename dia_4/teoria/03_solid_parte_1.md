# SOLID para AI Engineers — Parte 1: SRP y DIP

## Tabla de Contenidos

1. [Objetivos de Aprendizaje](#objetivos-de-aprendizaje)
2. [Prerrequisitos](#prerrequisitos)
3. [Introducción](#introducción)
4. [Single Responsibility Principle (SRP)](#1-single-responsibility-principle-srp)
5. [Dependency Inversion Principle (DIP)](#2-dependency-inversion-principle-dip)
6. [SRP + DIP Juntos](#3-srp--dip-juntos)
7. [Aprendizaje Clave](#aprendizaje-clave)
8. [Resumen de Principios](#resumen-de-principios)
9. [Referencias](#referencias)
10. [Ejercicio Individual](#ejercicio-individual)
11. [Ejercicio Grupal](#ejercicio-grupal)

---

## Objetivos de Aprendizaje

Al completar esta lección serás capaz de:

- Identificar violaciones de SRP en código de Data/IA y separar responsabilidades
- Aplicar DIP usando Protocols para desacoplar módulos de alto nivel de implementaciones concretas
- Reconocer la conexión entre SRP, DIP y lo visto en el Bloque 2 (composición + Protocols)
- Refactorizar una "God class" de pipeline ML aplicando ambos principios

---

## Prerrequisitos

- Día 3: Funciones pequeñas con una responsabilidad, separación estructura vs objeto
- Bloque 1 hoy: Pydantic para modelar datos
- Bloque 2 hoy: Composición sobre herencia, Protocols como contratos

---

## Introducción

### Contexto: Por Qué Importa

**Problema real en Data/IA**:

Tienes una clase `MLPipeline` de 400 líneas. Carga datos de S3, valida el schema, hace feature engineering, entrena un modelo, calcula métricas, guarda el modelo en el registry y envía una notificación a Slack. Para testear el entrenamiento, necesitas una conexión a S3, un modelo registry y un webhook de Slack. Para cambiar el proveedor de LLM, tienes que modificar la misma clase que gestiona los datos. Un cambio en la notificación rompe los tests de entrenamiento.

**Ejemplo concreto**:

Un equipo necesita cambiar de scikit-learn a XGBoost. El código de entrenamiento está en la misma clase que la ingestión y el guardado del modelo. Cambiar el trainer implica tocar una clase de 400 líneas donde un error en la línea 350 (guardado) rompe la línea 50 (ingestión). Resultado: 3 días de refactorización para lo que debería ser cambiar una pieza.

**Consecuencias de violar SOLID**:

- **Cambios en cascada**: Tocar una funcionalidad rompe otra que no tiene relación
- **Tests imposibles**: Para probar una parte, necesitas montar todo el sistema
- **Código rígido**: Cambiar un componente (modelo, storage, notificación) obliga a modificar una clase central
- **Onboarding lento**: Un nuevo miembro necesita entender 400 líneas para cambiar una cosa

### Principio Fundamental

> "A module should have one, and only one, reason to change."
>
> — Robert C. Martin, *Clean Architecture* (2017)

SOLID no son reglas arbitrarias — son principios que emergen de la experiencia de mantener código a largo plazo. Hoy vamos a ver los dos que más impacto tienen en el día a día de un junior: SRP (separar responsabilidades) y DIP (depender de abstracciones).

### El Concepto

**SOLID son 5 principios**:

- **S** — Single Responsibility Principle (hoy)
- **O** — Open/Closed Principle (Bloque 4)
- **L** — Liskov Substitution Principle (Bloque 4)
- **I** — Interface Segregation Principle (Bloque 4)
- **D** — Dependency Inversion Principle (hoy)

**¿Por qué SRP y DIP primero?**

Porque son los que más impacto tienen en código junior. SRP es lo que te impide crear "God classes". DIP es lo que te permite cambiar piezas sin tocar el resto — y es la base teórica de lo que ya practicamos en el Bloque 2 con composición y Protocols.

**Conexión con lo anterior**:

Si el Bloque 2 fue el "cómo" (composición, Protocols), este bloque es el "por qué". SRP y DIP son los principios que justifican las decisiones de diseño que tomamos antes.

---

## 1. Single Responsibility Principle (SRP)

### Por Qué Importa

SRP no dice "una clase hace una sola cosa" — eso es demasiado simplista. SRP dice que **una clase debe tener una sola razón para cambiar**. Esa "razón" es un actor o stakeholder: si el equipo de datos quiere cambiar la ingestión y el equipo de ML quiere cambiar el entrenamiento, esos dos cambios no deberían afectar a la misma clase.

### Ejemplo Incorrecto

```python
import json
import logging
from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split

logger = logging.getLogger(__name__)


class MLPipeline:
    """God class — hace TODO. Cambia por CUALQUIER razón."""

    def __init__(self, data_path: str, model_dir: str):
        self.data_path = data_path
        self.model_dir = model_dir
        self.data = None
        self.model = None
        self.metrics = {}

    # ---- Razón de cambio 1: Formato/fuente de datos ----

    def load_data(self):
        logger.info(f"Loading data from {self.data_path}")
        self.data = pd.read_csv(self.data_path)

    def validate_data(self):
        required_cols = ["feature_1", "feature_2", "target"]
        missing = [c for c in required_cols if c not in self.data.columns]
        if missing:
            raise ValueError(f"Missing columns: {missing}")

    def clean_data(self):
        self.data = self.data.dropna()
        self.data = self.data.drop_duplicates()

    # ---- Razón de cambio 2: Algoritmo de ML ----

    def train(self):
        X = self.data.drop("target", axis=1)
        y = self.data["target"]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        self.model = RandomForestClassifier(n_estimators=100)
        self.model.fit(X_train, y_train)
        predictions = self.model.predict(X_test)
        self.metrics = {
            "accuracy": accuracy_score(y_test, predictions),
            "f1": f1_score(y_test, predictions, average="weighted"),
        }

    # ---- Razón de cambio 3: Almacenamiento ----

    def save_model(self):
        Path(self.model_dir).mkdir(parents=True, exist_ok=True)
        model_path = f"{self.model_dir}/model.pkl"
        joblib.dump(self.model, model_path)
        logger.info(f"Model saved to {model_path}")

    def save_metrics(self):
        metrics_path = f"{self.model_dir}/metrics.json"
        with open(metrics_path, "w") as f:
            json.dump(self.metrics, f, indent=2)

    # ---- Razón de cambio 4: Notificaciones ----

    def notify(self):
        # Hardcoded Slack webhook
        print(f"Slack: Model trained with accuracy {self.metrics['accuracy']:.4f}")

    # ---- Orquestación ----

    def run(self):
        self.load_data()
        self.validate_data()
        self.clean_data()
        self.train()
        self.save_model()
        self.save_metrics()
        self.notify()


# Uso
pipeline = MLPipeline("data.csv", "models/")
pipeline.run()
```

**Problemas**:

- **4 razones para cambiar en una clase**: datos, algoritmo, almacenamiento, notificaciones
- **Estado mutable compartido**: `self.data`, `self.model`, `self.metrics` — cada método depende de que otro haya corrido antes
- **Imposible probar en aislamiento**: Para probar `train()`, necesitas que `load_data()` y `clean_data()` hayan corrido primero
- **Acoplamiento a implementaciones**: Hardcoded a CSV, RandomForest, joblib, Slack

### Qué Cambiar y Por Qué

1. Una clase con 4 razones de cambio → 4 piezas independientes (una responsabilidad cada una)
2. Estado mutable compartido → datos que fluyen como argumentos entre piezas
3. Acoplamiento a implementaciones → Protocols para contratos (esto es DIP, que veremos a continuación)
4. Orquestador que lo hace todo → orquestador que solo compone piezas

### Ejemplo Correcto

Primero, las estructuras de datos (coherente con Day 3 y Bloque 1):

```python
from dataclasses import dataclass

import pandas as pd
from pydantic import BaseModel, Field


# --- Estructuras de datos: solo datos ---

class DatasetConfig(BaseModel):
    """Configuración del dataset — validada con Pydantic."""
    path: str
    required_columns: list[str]
    test_size: float = Field(default=0.2, gt=0, lt=1)


@dataclass(frozen=True)
class SplitDataset:
    """Resultado del split — inmutable."""
    X_train: pd.DataFrame
    X_test: pd.DataFrame
    y_train: pd.Series
    y_test: pd.Series


@dataclass(frozen=True)
class TrainingResult:
    """Resultado del entrenamiento — inmutable."""
    model: object
    accuracy: float
    f1: float
```

Ahora, cada responsabilidad como pieza independiente:

```python
import logging

import pandas as pd
from sklearn.model_selection import train_test_split

logger = logging.getLogger(__name__)


# --- Responsabilidad 1: Ingestión y validación de datos ---

class CSVDataLoader:
    """Carga y valida datos desde CSV. UNA razón para cambiar: formato de datos."""

    def load(self, config: DatasetConfig) -> pd.DataFrame:
        logger.info(f"Loading data from {config.path}")
        data = pd.read_csv(config.path)

        missing = [c for c in config.required_columns if c not in data.columns]
        if missing:
            raise ValueError(f"Missing columns: {missing}")

        cleaned = data.dropna().drop_duplicates()
        logger.info(f"Loaded {len(data)} rows, {len(cleaned)} after cleaning")
        return cleaned


# --- Responsabilidad 2: Preparación de features ---

def split_dataset(
    data: pd.DataFrame, target_column: str, test_size: float,
) -> SplitDataset:
    """Función pura — separa features y target. Sin estado."""
    X = data.drop(target_column, axis=1)
    y = data[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)
    return SplitDataset(X_train=X_train, X_test=X_test, y_train=y_train, y_test=y_test)
```

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score


# --- Responsabilidad 3: Entrenamiento ---

class RandomForestTrainer:
    """Entrena un RandomForest. UNA razón para cambiar: algoritmo de ML."""

    def __init__(self, n_estimators: int = 100):
        self._n_estimators = n_estimators

    def train(self, dataset: SplitDataset) -> TrainingResult:
        model = RandomForestClassifier(n_estimators=self._n_estimators)
        model.fit(dataset.X_train, dataset.y_train)

        predictions = model.predict(dataset.X_test)
        return TrainingResult(
            model=model,
            accuracy=accuracy_score(dataset.y_test, predictions),
            f1=f1_score(dataset.y_test, predictions, average="weighted"),
        )
```

```python
import json
from pathlib import Path

import joblib


# --- Responsabilidad 4: Almacenamiento ---

class LocalModelSaver:
    """Guarda modelo y métricas en disco. UNA razón para cambiar: dónde/cómo guardar."""

    def __init__(self, output_dir: str):
        self._output_dir = Path(output_dir)

    def save(self, result: TrainingResult) -> None:
        self._output_dir.mkdir(parents=True, exist_ok=True)
        joblib.dump(result.model, self._output_dir / "model.pkl")

        metrics = {"accuracy": result.accuracy, "f1": result.f1}
        with open(self._output_dir / "metrics.json", "w") as f:
            json.dump(metrics, f, indent=2)

        logger.info(f"Model and metrics saved to {self._output_dir}")
```

Y el orquestador, que **solo compone piezas**:

```python
class TrainingOrchestrator:
    """Orquesta el flujo. NO tiene lógica de negocio — solo coordina."""

    def __init__(self, loader, trainer, saver):
        self._loader = loader
        self._trainer = trainer
        self._saver = saver

    def run(self, config: DatasetConfig) -> TrainingResult:
        data = self._loader.load(config)
        dataset = split_dataset(data, target_column="target", test_size=config.test_size)
        result = self._trainer.train(dataset)
        self._saver.save(result)

        logger.info(f"Training complete: accuracy={result.accuracy:.4f}, f1={result.f1:.4f}")
        return result


# --- Uso ---
orchestrator = TrainingOrchestrator(
    loader=CSVDataLoader(),
    trainer=RandomForestTrainer(n_estimators=200),
    saver=LocalModelSaver("models/experiment_1"),
)

config = DatasetConfig(
    path="data.csv",
    required_columns=["feature_1", "feature_2", "target"],
)
result = orchestrator.run(config)
```

**Ventajas**:

- **Una razón de cambio por pieza**: Cambiar el algoritmo solo toca `RandomForestTrainer`. Cambiar el storage solo toca `LocalModelSaver`
- **Probable en aislamiento**: Puedes probar `RandomForestTrainer` con un `SplitDataset` creado en memoria, sin CSV ni disco
- **Sin estado mutable compartido**: Los datos fluyen como argumentos
- **Coherente con Day 3**: Estructuras de datos (`DatasetConfig`, `SplitDataset`, `TrainingResult`) separadas de objetos con comportamiento

### ¿Cuándo es "demasiado SRP"?

SRP no significa "una función por archivo". El criterio es: **¿tienen la misma razón para cambiar?** Si carga de datos y validación de schema cambian siempre juntas (porque dependen del formato de datos), pueden ir en la misma clase. Si entrenamiento y guardado de modelo cambian por razones independientes, van separados.

Señales de que te pasaste separando:

- Tienes 20 clases de 5 líneas cada una y el flujo es imposible de seguir
- Dos piezas siempre cambian juntas — deberían ser una sola
- El orquestador necesita 10 dependencias para hacer algo simple

---

## 2. Dependency Inversion Principle (DIP)

### Por Qué Importa

DIP dice que los módulos de alto nivel (orquestación, lógica de negocio) no deben depender de módulos de bajo nivel (CSV, S3, Slack). Ambos deben depender de abstracciones. En Python moderno, esas abstracciones son **Protocols**.

DIP es lo que convierte el código del Bloque 2 en algo más que "composición bonita". Sin DIP, tu orquestador depende de `CSVDataLoader` concreto. Con DIP, depende de un Protocol `DataLoader` — y puedes cambiar la implementación sin tocar el orquestador.

### Ejemplo Incorrecto

```python
from sklearn.ensemble import RandomForestClassifier
import boto3


class TrainingService:
    """Servicio de alto nivel que depende de implementaciones concretas."""

    def __init__(self):
        # Dependencias concretas hardcoded — DIP violado
        self._model = RandomForestClassifier(n_estimators=100)
        self._s3_client = boto3.client("s3")

    def train_and_save(self, data_path: str, bucket: str) -> dict:
        data = pd.read_csv(data_path)  # Acoplado a CSV
        X, y = data.drop("target", axis=1), data["target"]

        self._model.fit(X, y)  # Acoplado a RandomForest
        predictions = self._model.predict(X)
        accuracy = accuracy_score(y, predictions)

        # Acoplado a S3
        model_bytes = joblib.dumps(self._model)
        self._s3_client.put_object(
            Bucket=bucket, Key="model.pkl", Body=model_bytes
        )

        return {"accuracy": accuracy}
```

**Problemas**:

- **Alto nivel depende de bajo nivel**: `TrainingService` (orquestación) depende directamente de `RandomForestClassifier` (implementación), `boto3` (implementación), `pd.read_csv` (implementación)
- **Imposible probar sin infraestructura real**: Necesitas S3 corriendo para probar el entrenamiento
- **Cambiar modelo = cambiar el servicio**: Si quieres XGBoost, tienes que modificar `TrainingService`
- **Cambiar storage = cambiar el servicio**: Si quieres guardar en disco local, tienes que modificar `TrainingService`

### Qué Cambiar y Por Qué

1. Dependencias concretas en `__init__` → Protocols inyectados (el orquestador no sabe qué implementación usa)
2. `RandomForestClassifier()` hardcoded → `ModelTrainer` Protocol (cualquier modelo que cumpla el contrato)
3. `boto3.client("s3")` hardcoded → `ModelSaver` Protocol (cualquier storage)
4. Las implementaciones dependen del Protocol, no al revés

### Ejemplo Correcto

```python
from typing import Protocol

import pandas as pd


# --- Abstracciones (Protocols) — definidas por el módulo de ALTO nivel ---

class DataLoader(Protocol):
    """Contrato: carga datos desde cualquier fuente."""
    def load(self, source: str) -> pd.DataFrame: ...


class ModelTrainer(Protocol):
    """Contrato: entrena un modelo con datos ya preparados."""
    def train(self, dataset: SplitDataset) -> TrainingResult: ...


class ModelSaver(Protocol):
    """Contrato: persiste un modelo entrenado."""
    def save(self, result: TrainingResult) -> None: ...
```

El módulo de alto nivel depende de los Protocols, NO de implementaciones:

```python
class TrainingService:
    """Módulo de ALTO nivel — depende SOLO de abstracciones (Protocols)."""

    def __init__(
        self,
        loader: DataLoader,       # ← Protocol, no CSVDataLoader
        trainer: ModelTrainer,    # ← Protocol, no RandomForestTrainer
        saver: ModelSaver,        # ← Protocol, no LocalModelSaver
    ):
        self._loader = loader
        self._trainer = trainer
        self._saver = saver

    def run(self, config: DatasetConfig) -> TrainingResult:
        data = self._loader.load(config.path)
        dataset = split_dataset(data, "target", config.test_size)
        result = self._trainer.train(dataset)
        self._saver.save(result)
        return result
```

Las implementaciones de bajo nivel cumplen los Protocols:

```python
# --- Implementaciones de BAJO nivel — cumplen los Protocols ---

class CSVDataLoader:  # Cumple DataLoader
    def load(self, source: str) -> pd.DataFrame:
        return pd.read_csv(source)


class S3DataLoader:  # Cumple DataLoader
    def __init__(self, bucket: str):
        self._bucket = bucket

    def load(self, source: str) -> pd.DataFrame:
        # Descarga de S3 y lee
        ...


class RandomForestTrainer:  # Cumple ModelTrainer
    def __init__(self, n_estimators: int = 100):
        self._n_estimators = n_estimators

    def train(self, dataset: SplitDataset) -> TrainingResult:
        ...


class XGBoostTrainer:  # Cumple ModelTrainer — nueva implementación sin tocar nada
    def train(self, dataset: SplitDataset) -> TrainingResult:
        ...


class S3ModelSaver:  # Cumple ModelSaver
    def __init__(self, bucket: str, prefix: str):
        self._bucket = bucket
        self._prefix = prefix

    def save(self, result: TrainingResult) -> None:
        ...
```

La composición ocurre en el punto de entrada:

```python
# --- Composición en el punto de entrada (main, factory, config) ---

# Producción: S3 + XGBoost + S3
service = TrainingService(
    loader=S3DataLoader(bucket="ml-data"),
    trainer=XGBoostTrainer(),
    saver=S3ModelSaver(bucket="ml-models", prefix="v2/"),
)

# Testing: CSV local + RandomForest + disco local
test_service = TrainingService(
    loader=CSVDataLoader(),
    trainer=RandomForestTrainer(),
    saver=LocalModelSaver("test_output/"),
)

# Ambos usan el MISMO TrainingService — solo cambian las piezas
```

**Ventajas**:

- **Alto nivel no cambia**: `TrainingService` no se modifica al cambiar modelo, storage o fuente de datos
- **Probable sin infraestructura**: Inyectas implementaciones fake/in-memory para tests
- **Extensible**: Añadir `XGBoostTrainer` no toca código existente
- **Las abstracciones las define el alto nivel**: Los Protocols reflejan lo que el orquestador necesita, no lo que las implementaciones ofrecen

### DIP Visual

```
SIN DIP (dependencia directa):

TrainingService ──→ RandomForestClassifier
                ──→ boto3.client("s3")
                ──→ pd.read_csv

→ Alto nivel depende de bajo nivel. Cambiar bajo nivel → cambiar alto nivel.


CON DIP (dependencia invertida):

TrainingService ──→ ModelTrainer (Protocol)  ←── RandomForestTrainer
                ──→ ModelSaver (Protocol)    ←── S3ModelSaver
                ──→ DataLoader (Protocol)    ←── CSVDataLoader

→ Ambos dependen de abstracciones. Cambiar bajo nivel → NO cambia alto nivel.
```

La "inversión" está en la dirección de la dependencia: antes el alto nivel dependía del bajo nivel. Ahora el bajo nivel depende de la abstracción definida por el alto nivel.

---

## 3. SRP + DIP Juntos

### La Conexión

SRP y DIP se refuerzan mutuamente:

- **SRP** te dice que separes responsabilidades en piezas independientes
- **DIP** te dice que esas piezas se conecten mediante abstracciones (Protocols), no referencias directas

Sin SRP, no tienes piezas que componer. Sin DIP, las piezas están acopladas entre sí. Juntos producen el patrón que ya vimos en el Bloque 2: composición con Protocols.

### Conexión con Bloques Anteriores

| Concepto | Bloque 2 (Composición) | Bloque 3 (SOLID) |
| --- | --- | --- |
| Separar en piezas | "Usa composición en vez de herencia" | SRP: "Una razón para cambiar" |
| Conectar con contratos | "Usa Protocols para type hints" | DIP: "Depende de abstracciones" |
| Datos como estructuras | "`@dataclass` para resultados" | "Pydantic/dataclass para datos, objetos para comportamiento" |

No son conceptos diferentes — son el mismo principio visto desde ángulos distintos. El Bloque 2 te dio las herramientas (composición, Protocols). Este bloque te da los principios que justifican cuándo y por qué usarlas.

---

## Aprendizaje Clave

### Puntos Críticos a Recordar

1. **SRP = una razón para cambiar**, no "una cosa". Si dos funcionalidades cambian siempre juntas, pueden estar en la misma clase
2. **DIP = depende de abstracciones (Protocols)**, no de implementaciones concretas. Las abstracciones las define el módulo de alto nivel
3. **SRP sin DIP = piezas acopladas**. Separas responsabilidades pero las conectas directamente
4. **DIP sin SRP = abstracciones sobre God classes**. Tienes un Protocol sobre una clase que hace todo
5. **La composición ocurre en el punto de entrada** (main, factory) — es ahí donde decides qué implementaciones concretas usar

### Cómo Desarrollar Intuición

**¿Estoy violando SRP?**

- ¿Tu clase tiene métodos que cambian por razones diferentes? (datos vs ML vs storage) → Sí, viola SRP
- ¿Para probar un método necesitas que otro haya corrido antes? (`self.data` de `load_data()`) → Sí, estado compartido = responsabilidades mezcladas
- ¿Tu clase tiene más de ~100 líneas sin contar docstrings? → No es regla fija, pero es señal de alarma

**¿Estoy violando DIP?**

- ¿Tu clase hace `import boto3` o `from sklearn import X` y lo usa directamente? → Sí, depende de implementación concreta
- ¿Para probar necesitas infraestructura real (S3, DB, API)? → Sí, falta abstracción que permita inyectar un fake
- ¿Cambiar un componente (modelo, storage) te obliga a modificar el orquestador? → Sí, las dependencias van en la dirección incorrecta

**¿Cuándo NO aplicar DIP?**

- Scripts pequeños y únicos (un notebook de análisis exploratorio)
- Dependencias estables que nunca cambias (`logging`, `pathlib`, `json`)
- Cuando solo hay una implementación posible y no planeas tests con fakes

### Anti-patterns Rápidos

| ❌ No hagas esto | ✅ Haz esto |
| --- | --- |
| Una clase con ingestión + training + guardado + notificación | Una pieza por responsabilidad, orquestador que compone |
| `self._model = RandomForestClassifier()` en el orquestador | `trainer: ModelTrainer` Protocol inyectado |
| `self.data` mutado por 5 métodos que se llaman en orden | Datos que fluyen como argumentos: `load() → clean() → train()` |
| Test que necesita S3 real para probar lógica de entrenamiento | Inyectar `FakeDataLoader` que devuelve DataFrame fijo |
| Abstracciones definidas por el módulo de bajo nivel | Protocols definidos por el módulo de alto nivel (que los necesita) |
| 20 clases de 5 líneas para cumplir SRP | Agrupar lo que cambia junto; separar lo que cambia por diferente razón |

---

## Resumen de Principios

SRP dice que cada pieza de tu código debe tener una sola razón para cambiar. DIP dice que las piezas de alto nivel (orquestación) no deben depender de las piezas de bajo nivel (implementaciones), sino de abstracciones que ambas comparten. En Python, esas abstracciones son Protocols. Juntos, SRP y DIP producen el patrón que ya practicamos en el Bloque 2: piezas independientes con una responsabilidad, conectadas mediante Protocols, compuestas en el punto de entrada. Las estructuras de datos (Pydantic, dataclass) fluyen entre las piezas como argumentos — nunca como estado mutable compartido.

---

## Referencias

1. Martin, R. C. (2017). *Clean Architecture: A Craftsman's Guide to Software Structure and Design*. Prentice Hall. Part III: Design Principles.
2. Martin, R. C. (2008). *Clean Code*. Prentice Hall. Chapter 10: Classes.
3. PEP 544 – Protocols: Structural subtyping: <https://peps.python.org/pep-0544/>
4. Martin, R. C. (2002). "The Single Responsibility Principle": <https://blog.cleancoder.com/uncle-bob/2014/05/08/SingleReponsibilityPrinciple.html>
5. Martin, R. C. (1996). "The Dependency Inversion Principle": <https://web.archive.org/web/20110714224327/http://www.objectmentor.com/resources/articles/dip.pdf>

---

## Ejercicio Individual

**Objetivo**: Identificar violaciones de SRP y DIP en una clase y planificar la refactorización.

**Tiempo estimado**: 15 minutos

### Código para Analizar

```python
import requests
import pandas as pd
from sklearn.preprocessing import StandardScaler


class DataEnricher:
    """Enriquece datos con información de una API externa."""

    def __init__(self, api_url: str, api_key: str):
        self.api_url = api_url
        self.api_key = api_key
        self.data = None
        self.enriched_data = None

    def load_csv(self, path: str):
        self.data = pd.read_csv(path)

    def fetch_enrichment(self, id_column: str):
        """Llama a API para cada ID y añade datos."""
        enrichments = []
        for _, row in self.data.iterrows():
            response = requests.get(
                f"{self.api_url}/enrich/{row[id_column]}",
                headers={"Authorization": f"Bearer {self.api_key}"},
            )
            enrichments.append(response.json())
        enrichment_df = pd.DataFrame(enrichments)
        self.enriched_data = pd.concat([self.data, enrichment_df], axis=1)

    def scale_features(self, columns: list[str]):
        scaler = StandardScaler()
        self.enriched_data[columns] = scaler.fit_transform(
            self.enriched_data[columns]
        )

    def save_parquet(self, output_path: str):
        self.enriched_data.to_parquet(output_path)

    def run(self, csv_path: str, id_column: str, scale_cols: list[str], output: str):
        self.load_csv(csv_path)
        self.fetch_enrichment(id_column)
        self.scale_features(scale_cols)
        self.save_parquet(output)
```

### Tarea

No escribas código todavía. Responde estas preguntas:

1. **¿Cuántas razones para cambiar tiene `DataEnricher`?** Lista cada una
2. **¿Qué dependencias concretas tiene hardcoded?** (violaciones de DIP)
3. **¿Qué Protocols definirías?** (nombre y firma del método principal)
4. **¿Qué estructuras de datos crearías?** (inputs y outputs como dataclass/Pydantic)
5. **Dibuja** cómo quedaría la composición (qué piezas, qué Protocols, qué datos fluyen)

### Criterios de Éxito

- [ ] Identificaste al menos 3 razones de cambio independientes
- [ ] Identificaste al menos 2 dependencias concretas (violaciones DIP)
- [ ] Propusiste al menos 2 Protocols con firmas claras
- [ ] Propusiste al menos 1 estructura de datos para el flujo
- [ ] Tu diagrama muestra piezas conectadas por Protocols, no por herencia

### Pistas

- `requests.get` es una dependencia concreta. ¿Qué Protocol lo abstraería?
- `pd.read_csv` es una dependencia concreta. ¿Ya definimos un Protocol para esto en el Bloque 2?
- `StandardScaler` es una dependencia concreta. ¿Siempre querrás el mismo tipo de scaling?
- `self.data` → `self.enriched_data` es estado mutable compartido — ¿cómo lo eliminas?

---

## Ejercicio Grupal

**Objetivo**: Refactorizar una "God class" de pipeline de ML a piezas con SRP conectadas por DIP.

**Contexto**: Tu equipo mantiene un sistema de scoring de crédito. La clase principal carga datos de clientes, consulta un servicio de bureau de crédito, calcula features, entrena un modelo de scoring, lo evalúa, lo guarda y publica las métricas. Todo en una clase. Cada sprint, cambios en una funcionalidad rompen otra. Los tests tardan 10 minutos porque necesitan conexión al bureau real.

**Tiempo estimado**: 45 minutos

### Dinámica

1. **Análisis** (10 min): Identifiquen razones de cambio y violaciones DIP
2. **Diseño** (10 min): Definan Protocols, estructuras de datos y composición
3. **Implementación** (20 min): Refactoricen a piezas SRP + DIP
4. **Demo** (5 min): Muestren cómo testearían el trainer sin conexión al bureau

### Código a Refactorizar

```python
import json
import logging
from datetime import datetime
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import requests
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

logger = logging.getLogger(__name__)


class CreditScoringPipeline:
    """Pipeline completo de scoring de crédito — God class."""

    def __init__(self, bureau_api_url: str, bureau_api_key: str, model_dir: str):
        self.bureau_api_url = bureau_api_url
        self.bureau_api_key = bureau_api_key
        self.model_dir = model_dir
        self.raw_data = None
        self.enriched_data = None
        self.features = None
        self.model = None
        self.scaler = StandardScaler()
        self.metrics = {}

    def load_customer_data(self, data_path: str):
        """Carga datos de clientes desde CSV."""
        self.raw_data = pd.read_csv(data_path)
        logger.info(f"Loaded {len(self.raw_data)} customers")

    def enrich_with_bureau(self):
        """Consulta bureau de crédito para cada cliente."""
        bureau_data = []
        for _, row in self.raw_data.iterrows():
            response = requests.get(
                f"{self.bureau_api_url}/credit-check/{row['customer_id']}",
                headers={"Authorization": f"Bearer {self.bureau_api_key}"},
                timeout=30,
            )
            bureau_data.append(response.json())
        bureau_df = pd.DataFrame(bureau_data)
        self.enriched_data = pd.merge(
            self.raw_data, bureau_df, on="customer_id", how="left"
        )
        logger.info(f"Enriched {len(bureau_data)} records from bureau")

    def engineer_features(self):
        """Crea features derivadas."""
        df = self.enriched_data.copy()
        df["debt_to_income"] = df["total_debt"] / df["annual_income"].replace(0, np.nan)
        df["credit_utilization"] = df["used_credit"] / df["credit_limit"].replace(0, np.nan)
        df["payment_ratio"] = df["on_time_payments"] / df["total_payments"].replace(0, np.nan)
        df = df.fillna(0)

        feature_cols = [
            "debt_to_income", "credit_utilization", "payment_ratio",
            "annual_income", "years_employed", "num_accounts",
        ]
        self.features = df[feature_cols + ["default"]]
        logger.info(f"Engineered {len(feature_cols)} features")

    def train_model(self):
        """Entrena GradientBoosting."""
        X = self.features.drop("default", axis=1)
        y = self.features["default"]
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )

        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)

        self.model = GradientBoostingClassifier(
            n_estimators=200, max_depth=5, learning_rate=0.1
        )
        self.model.fit(X_train_scaled, y_train)

        predictions = self.model.predict(X_test_scaled)
        probabilities = self.model.predict_proba(X_test_scaled)[:, 1]
        self.metrics = {
            "accuracy": accuracy_score(y_test, predictions),
            "precision": precision_score(y_test, predictions),
            "recall": recall_score(y_test, predictions),
            "auc_roc": roc_auc_score(y_test, probabilities),
        }
        logger.info(f"Model trained: AUC-ROC={self.metrics['auc_roc']:.4f}")

    def save_artifacts(self):
        """Guarda modelo, scaler y métricas."""
        output = Path(self.model_dir) / datetime.now().strftime("%Y%m%d_%H%M%S")
        output.mkdir(parents=True, exist_ok=True)

        joblib.dump(self.model, output / "model.pkl")
        joblib.dump(self.scaler, output / "scaler.pkl")

        with open(output / "metrics.json", "w") as f:
            json.dump(self.metrics, f, indent=2)

        logger.info(f"Artifacts saved to {output}")

    def publish_metrics(self):
        """Publica métricas a un dashboard."""
        # Hardcoded a un endpoint específico
        requests.post(
            "https://internal-dashboard.company.com/api/metrics",
            json={"model": "credit_scoring", "metrics": self.metrics},
            timeout=10,
        )

    def run(self, data_path: str):
        self.load_customer_data(data_path)
        self.enrich_with_bureau()
        self.engineer_features()
        self.train_model()
        self.save_artifacts()
        self.publish_metrics()
```

### Instrucciones por Persona

- **Persona 1**: Definir Protocols (`DataLoader`, `DataEnricher`, `ModelTrainer`, `ArtifactSaver`, `MetricsPublisher`) y estructuras de datos (`CustomerData`, `EnrichedData`, `TrainingResult`)
- **Persona 2**: Implementar `CSVCustomerLoader` y `BureauEnricher` que cumplan los Protocols. Datos fluyen como argumentos
- **Persona 3**: Implementar `FeatureEngineer` (sin Protocol necesario — solo hay una implementación por ahora), `GBClassifierTrainer` y `LocalArtifactSaver`
- **Persona 4**: Implementar `DashboardPublisher`, crear el `ScoringOrchestrator` que compone todo, y demostrar cómo probar con fakes

### Criterios de Éxito

- [ ] `CreditScoringPipeline` descompuesta en al menos 5 piezas con una responsabilidad cada una
- [ ] Al menos 3 Protocols definidos para las dependencias que podrían cambiar
- [ ] Cero estado mutable compartido (`self.data`, `self.enriched_data`, etc.)
- [ ] Todas las estructuras de datos son `@dataclass(frozen=True)` o Pydantic `BaseModel`
- [ ] El orquestador solo compone — no tiene lógica de negocio
- [ ] Se puede probar el `GBClassifierTrainer` sin conexión al bureau ni disco
- [ ] Se puede probar el `ScoringOrchestrator` completo con fakes inyectados
- [ ] Añadir un nuevo `MetricsPublisher` (ej: a Datadog) no toca código existente

### Pistas

**Para Persona 1 — Estructuras de datos**:

```python
@dataclass(frozen=True)
class TrainingResult:
    model: object
    scaler: object
    metrics: dict[str, float]
```

**Para Persona 2 — Enriquecimiento con Protocol**:

```python
class DataEnricher(Protocol):
    def enrich(self, data: pd.DataFrame) -> pd.DataFrame: ...

class BureauEnricher:  # Cumple DataEnricher — NO hereda
    def __init__(self, api_url: str, api_key: str): ...
    def enrich(self, data: pd.DataFrame) -> pd.DataFrame: ...
```

**Para Persona 4 — Fake para testing**:

```python
class FakeBureauEnricher:
    """Fake para tests — cumple DataEnricher sin HTTP."""

    def enrich(self, data: pd.DataFrame) -> pd.DataFrame:
        data["credit_score"] = 700  # Valores fijos para test
        data["total_debt"] = 10000
        return data
```

### Preguntas para Reflexión

1. ¿Cuántas razones de cambio tenía `CreditScoringPipeline`? ¿Cuántas tiene cada pieza ahora?
2. ¿Cuánto tardarían los tests antes (con bureau real) vs ahora (con fakes)?
3. Si mañana el equipo quiere cambiar de GradientBoosting a LightGBM, ¿qué piezas tocan?
4. ¿Hay alguna pieza donde NO definiste Protocol? ¿Por qué? ¿Es correcto no definirlo siempre?
5. ¿Cómo se relaciona este ejercicio con la composición del Bloque 2?

---

## Aplicación al Proyecto de Equipo

- [ ] Identifica si tu proyecto tiene alguna "God class" con más de 2 razones de cambio y planifica la separación
- [ ] Revisa si tu orquestador depende de implementaciones concretas. Si hace `import boto3` o `from sklearn import X` directamente, evalúa si un Protocol mejoraría la testeabilidad
- [ ] Asegúrate de que los tests de lógica de negocio no dependen de infraestructura real (S3, APIs, bases de datos)
- [ ] Verifica que las estructuras de datos (configs, resultados) son Pydantic o dataclass — no dicts sueltos