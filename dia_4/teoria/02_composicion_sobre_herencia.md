# Composición sobre Herencia

## Tabla de Contenidos

1. [Objetivos de Aprendizaje](#objetivos-de-aprendizaje)
2. [Prerrequisitos](#prerrequisitos)
3. [Introducción](#introducción)
4. [Herencia: Cuándo Sí, Cuándo No](#1-herencia-cuándo-sí-cuándo-no)
5. [Composición: Inyectar Comportamiento](#2-composición-inyectar-comportamiento)
6. [Protocols: Contratos sin Herencia](#3-protocols-contratos-sin-herencia)
7. [Aprendizaje Clave](#aprendizaje-clave)
8. [Resumen de Principios](#resumen-de-principios)
9. [Referencias](#referencias)
10. [Ejercicio Individual](#ejercicio-individual)
11. [Ejercicio Grupal](#ejercicio-grupal)

---

## Objetivos de Aprendizaje

Al completar esta lección serás capaz de:

- Identificar cuándo la herencia es apropiada (is-a real) y cuándo causa problemas
- Refactorizar herencia profunda a composición (has-a)
- Definir contratos con `typing.Protocol` en vez de herencia de clases base
- Aplicar estos patrones respetando la separación estructura de datos vs objeto (Day 3)

---

## Prerrequisitos

- Día 3: Separación estructura de datos (expone datos) vs objeto (oculta estado, expone comportamiento)
- Día 3: Funciones pequeñas, una responsabilidad
- Bloque 1 hoy: Pydantic para estructuras de datos con validación

---

## Introducción

### Contexto: Por Qué Importa

**Problema real en Data/IA**:

Tu equipo tiene un pipeline de procesamiento de datos. Alguien creó `BaseProcessor` con herencia para CSV, JSON y Parquet. Llevas 6 meses y `BaseProcessor` tiene 15 métodos, 4 niveles de herencia, y cada vez que cambias algo en la clase base se rompen procesadores que no tocaste. Nadie quiere añadir un nuevo formato porque implica entender toda la jerarquía.

**Ejemplo concreto**:

```
BaseProcessor
├── FileProcessor
│   ├── CSVProcessor
│   │   └── LargeCSVProcessor
│   └── JSONProcessor
│       └── NestedJSONProcessor
└── StreamProcessor
    └── KafkaProcessor
```

`LargeCSVProcessor` hereda de `CSVProcessor` que hereda de `FileProcessor` que hereda de `BaseProcessor`. Para entender qué hace `LargeCSVProcessor`, tienes que leer 4 clases. Para cambiar cómo se loggean los errores en `BaseProcessor`, tienes que verificar que no rompiste ninguno de los 6 hijos.

**Consecuencias de abusar de herencia**:

- **Acoplamiento fuerte**: Cambiar la clase base rompe todos los hijos
- **Fragilidad**: Un cambio "pequeño" tiene efectos en cascada
- **Rigidez**: Añadir un nuevo tipo obliga a encajar en la jerarquía existente
- **Comprensión difícil**: Para entender una clase hija hay que leer toda la cadena

### Principio Fundamental

> "Favor object composition over class inheritance."
>
> — Gang of Four, *Design Patterns* (1994)

Este principio tiene 30 años y sigue siendo uno de los más relevantes en diseño de software. No dice "nunca uses herencia" — dice que la composición debería ser tu opción por defecto.

### El Concepto

**Definición técnica**:

La herencia (`class B(A)`) establece una relación "B es un A". La composición establece "B tiene un A" — B contiene una instancia de A y delega en ella. Los Protocols (`typing.Protocol`) definen contratos estructurales: "cualquier cosa que tenga estos métodos sirve", sin necesidad de heredar de nada.

**Cómo funciona internamente**:

1. **Herencia**: Python busca métodos en la cadena MRO (Method Resolution Order). Cada clase hija hereda todos los métodos y atributos del padre
2. **Composición**: Un objeto contiene referencias a otros objetos y delega operaciones en ellos
3. **Protocol**: Define una interfaz estructural. Cualquier clase que implemente los métodos requeridos la satisface automáticamente — sin `class X(MiProtocol)`

**Terminología clave**:

- **is-a**: Relación de herencia. "Un CSVProcessor ES un FileProcessor"
- **has-a**: Relación de composición. "Un Pipeline TIENE un Processor"
- **MRO**: Method Resolution Order — orden en que Python busca métodos en la jerarquía
- **Structural subtyping**: Compatibilidad por estructura (tiene los métodos), no por herencia
- **Nominal subtyping**: Compatibilidad por nombre (hereda de la clase)

---

## 1. Herencia: Cuándo Sí, Cuándo No

### Cuándo la Herencia Es Apropiada

La herencia funciona bien cuando se cumplen **todas** estas condiciones:

1. La relación "is-a" es real y permanente (no forzada)
2. La clase hija es un caso particular del padre, no una variante con comportamiento diferente
3. La jerarquía es plana (máximo 2 niveles: base → hija)
4. La clase base es estable — no cambia frecuentemente

**Ejemplo legítimo**: Excepciones custom.

```python
# Herencia correcta — las excepciones SON un caso de uso legítimo de is-a
class PipelineError(Exception):
    """Error base del pipeline — IS-A Exception."""
    pass


class DataValidationError(PipelineError):
    """Error de validación — IS-A PipelineError."""

    def __init__(self, field: str, value: object, reason: str):
        self.field = field
        self.value = value
        self.reason = reason
        super().__init__(f"Validation failed for '{field}': {reason} (got {value!r})")


class ModelLoadError(PipelineError):
    """Error de carga de modelo — IS-A PipelineError."""

    def __init__(self, model_path: str, cause: Exception):
        self.model_path = model_path
        self.cause = cause
        super().__init__(f"Failed to load model from '{model_path}': {cause}")


# Permite capturar por nivel de especificidad
try:
    raise DataValidationError("age", -5, "must be positive")
except DataValidationError as e:
    print(f"Validation: {e.field} = {e.value}")
except PipelineError as e:
    print(f"Pipeline error: {e}")
```

Esto funciona porque `DataValidationError` genuinamente **es** un `PipelineError`, la jerarquía es plana (2 niveles), la base es estable, y Python está diseñado para capturar excepciones por jerarquía.

### Ejemplo Incorrecto: Herencia Abusada

```python
import pandas as pd


class BaseProcessor:
    """Clase base que intenta hacer demasiado."""

    def __init__(self, source_path: str):
        self.source_path = source_path
        self.data = None

    def load(self):
        raise NotImplementedError

    def validate(self):
        if self.data is None:
            raise ValueError("Data not loaded")
        if len(self.data) == 0:
            raise ValueError("Empty dataset")

    def clean(self):
        self.data = self.data.dropna()

    def save(self, output_path: str):
        self.data.to_csv(output_path, index=False)

    def process(self):
        """Template method — define el flujo."""
        self.load()
        self.validate()
        self.clean()
        self.save("output.csv")


class CSVProcessor(BaseProcessor):
    def load(self):
        self.data = pd.read_csv(self.source_path)

    # clean() heredado — pero ¿y si CSV necesita limpieza diferente?
    # save() heredado — pero ¿y si quiero guardar en Parquet?


class JSONProcessor(BaseProcessor):
    def load(self):
        self.data = pd.read_json(self.source_path)

    def clean(self):
        """Override de clean — comportamiento diferente al padre."""
        super().clean()
        # JSON puede tener listas anidadas que aplanar
        for col in self.data.columns:
            if self.data[col].apply(lambda x: isinstance(x, list)).any():
                self.data = self.data.explode(col)


class NestedJSONProcessor(JSONProcessor):
    """3 niveles de herencia — ¿qué hace clean() aquí?"""

    def clean(self):
        # ¿Llamo a super()? ¿A cuál super? ¿JSONProcessor o BaseProcessor?
        super().clean()  # Llama a JSONProcessor.clean → BaseProcessor.clean
        # Más limpieza específica...
```

**Problemas**:

- **Estado mutable compartido**: `self.data` se modifica en `load()`, `clean()`, `validate()` — cualquier método puede dejarlo en estado inconsistente
- **Template method frágil**: `process()` asume un flujo fijo. ¿Y si un formato no necesita `clean()`? ¿Y si necesita un paso extra?
- **`super().clean()` ambiguo**: En `NestedJSONProcessor`, `super()` llama a `JSONProcessor.clean()` que llama a `BaseProcessor.clean()`. ¿Es eso lo que quieres?
- **Rigidez**: Si quieres un procesador que lee CSV pero guarda en Parquet, no encaja en la jerarquía. ¿Heredas de CSV y overrideas `save()`?

### Qué Cambiar y Por Qué

1. Jerarquía profunda → objetos independientes compuestos (cada pieza hace una cosa)
2. Estado mutable compartido (`self.data`) → datos que fluyen entre funciones (input → output)
3. `NotImplementedError` → Protocol (contrato explícito que el type checker verifica)
4. Template method rígido → composición de pasos (puedes combinar como quieras)

---

## 2. Composición: Inyectar Comportamiento

### Por Qué Importa

La composición te permite construir comportamiento complejo combinando piezas simples e independientes. Cada pieza tiene una responsabilidad, se puede probar sola, y se puede reemplazar sin afectar al resto.

### Ejemplo Correcto: Composición

Vamos a refactorizar el ejemplo anterior. Primero, separemos **qué son datos** de **qué es comportamiento**, siguiendo lo de Day 3:

```python
from dataclasses import dataclass

import pandas as pd


# --- Estructuras de datos: solo datos, sin lógica de negocio ---

@dataclass(frozen=True)
class ProcessingResult:
    """Resultado del procesamiento — estructura de datos inmutable."""
    data: pd.DataFrame
    rows_original: int
    rows_after_cleaning: int
    source_path: str
```

Ahora, las piezas de comportamiento. Cada una es un **objeto** con una responsabilidad:

```python
class CSVLoader:
    """Carga datos desde CSV. Una responsabilidad."""

    def load(self, path: str) -> pd.DataFrame:
        return pd.read_csv(path)


class JSONLoader:
    """Carga datos desde JSON. Una responsabilidad."""

    def load(self, path: str) -> pd.DataFrame:
        return pd.read_json(path)


class DropNACleaner:
    """Elimina filas con valores nulos. Una responsabilidad."""

    def clean(self, data: pd.DataFrame) -> pd.DataFrame:
        return data.dropna()


class CSVSaver:
    """Guarda datos en CSV. Una responsabilidad."""

    def save(self, data: pd.DataFrame, path: str) -> None:
        data.to_csv(path, index=False)


class ParquetSaver:
    """Guarda datos en Parquet. Una responsabilidad."""

    def save(self, data: pd.DataFrame, path: str) -> None:
        data.to_parquet(path, index=False)
```

Y el pipeline **compone** estas piezas:

```python
class DataPipeline:
    """Pipeline que TIENE un loader, un cleaner y un saver (composición)."""

    def __init__(self, loader, cleaner, saver):
        self._loader = loader
        self._cleaner = cleaner
        self._saver = saver

    def run(self, source_path: str, output_path: str) -> ProcessingResult:
        data = self._loader.load(source_path)
        rows_original = len(data)
        cleaned = self._cleaner.clean(data)
        self._saver.save(cleaned, output_path)

        return ProcessingResult(
            data=cleaned,
            rows_original=rows_original,
            rows_after_cleaning=len(cleaned),
            source_path=source_path,
        )


# --- Uso: combina piezas como necesites ---

# CSV → limpiar → guardar en CSV
pipeline_csv = DataPipeline(
    loader=CSVLoader(),
    cleaner=DropNACleaner(),
    saver=CSVSaver(),
)

# JSON → limpiar → guardar en Parquet (¡sin nueva clase!)
pipeline_json_to_parquet = DataPipeline(
    loader=JSONLoader(),
    cleaner=DropNACleaner(),
    saver=ParquetSaver(),
)

result = pipeline_csv.run("data.csv", "output.csv")
print(f"Procesadas {result.rows_original} → {result.rows_after_cleaning} filas")
```

**Ventajas**:

- **Sin herencia**: Ninguna clase hereda de otra
- **Combinable**: CSV→Parquet, JSON→CSV, cualquier combinación sin nueva clase
- **Probable**: Cada pieza se prueba en aislamiento
- **Datos separados del comportamiento**: `ProcessingResult` es estructura de datos (Day 3), las piezas son objetos con comportamiento
- **Sin estado mutable compartido**: Los datos fluyen como argumentos y retornos, no como `self.data`

### Nota sobre la separación estructura vs objeto

Observa que hemos aplicado lo de Day 3:

- `ProcessingResult` es una **estructura de datos** (`@dataclass`, expone atributos, sin lógica)
- `CSVLoader`, `DropNACleaner`, etc. son **objetos** (podrían tener estado interno, exponen comportamiento via métodos)
- Los datos fluyen entre objetos como argumentos, no como estado mutado internamente

### Pero hay un problema...

¿Cómo sabe `DataPipeline` que el `loader` que recibe tiene un método `.load()`? ¿Y que el `cleaner` tiene `.clean()`? Ahora mismo, si alguien pasa un objeto sin esos métodos, el error llega en runtime. Necesitamos **contratos**. Eso nos lleva a Protocols.

---

## 3. Protocols: Contratos sin Herencia

### Por Qué Importa

Cuando usas composición, necesitas una forma de decir "este parámetro debe tener un método `.load()` que reciba un `str` y devuelva un `DataFrame`" — sin forzar herencia. `typing.Protocol` hace exactamente eso: define contratos estructurales que el type checker (pyright, mypy) verifica sin que la clase que cumple el contrato tenga que heredar de nada.

Es el enfoque que usan los frameworks modernos de Python. FastAPI, LangChain, Strands — todos trabajan con duck typing estructural, no con jerarquías de herencia.

### ABC vs Protocol

Antes de Protocol (PEP 544, Python 3.8+), la única forma de definir contratos era `abc.ABC` con `@abstractmethod`:

```python
from abc import ABC, abstractmethod

import pandas as pd


# Con ABC — requiere herencia explícita
class DataLoader(ABC):
    @abstractmethod
    def load(self, path: str) -> pd.DataFrame: ...


class CSVLoader(DataLoader):  # ← Forzado a heredar
    def load(self, path: str) -> pd.DataFrame:
        return pd.read_csv(path)
```

Funciona, pero tiene problemas:

- **Requiere herencia explícita**: `CSVLoader(DataLoader)` — si olvidas heredar, el contrato no se aplica
- **No funciona con clases de terceros**: No puedes hacer que `pd.read_csv` "implemente" tu ABC
- **Nominal subtyping**: La compatibilidad es por nombre (hereda de X), no por estructura (tiene los métodos)
- **Tentación de añadir lógica a la base**: Los ABCs tienden a acumular métodos concretos y convertirse en el `BaseProcessor` del ejemplo anterior

### Ejemplo Correcto: Protocol

```python
from typing import Protocol, runtime_checkable

import pandas as pd


# --- Contratos: definen QUÉ necesitas, no CÓMO heredar ---

class DataLoader(Protocol):
    """Contrato: cualquier cosa con un método load(str) → DataFrame."""

    def load(self, path: str) -> pd.DataFrame: ...


class DataCleaner(Protocol):
    """Contrato: cualquier cosa con un método clean(DataFrame) → DataFrame."""

    def clean(self, data: pd.DataFrame) -> pd.DataFrame: ...


class DataSaver(Protocol):
    """Contrato: cualquier cosa con un método save(DataFrame, str) → None."""

    def save(self, data: pd.DataFrame, path: str) -> None: ...
```

Las implementaciones **no heredan del Protocol**. Solo cumplen la firma:

```python
class CSVLoader:  # ← NO hereda de DataLoader
    """Cumple DataLoader por estructura, no por herencia."""

    def load(self, path: str) -> pd.DataFrame:
        return pd.read_csv(path)


class ParquetLoader:  # ← Tampoco hereda
    def load(self, path: str) -> pd.DataFrame:
        return pd.read_parquet(path)


class DropNACleaner:  # ← NO hereda de DataCleaner
    def clean(self, data: pd.DataFrame) -> pd.DataFrame:
        return data.dropna()


class FillNACleaner:
    """Alternativa: rellena nulos en vez de eliminar filas."""

    def __init__(self, fill_value: float = 0.0):
        self._fill_value = fill_value

    def clean(self, data: pd.DataFrame) -> pd.DataFrame:
        return data.fillna(self._fill_value)
```

El pipeline ahora usa los Protocols como type hints:

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class ProcessingResult:
    rows_original: int
    rows_after_cleaning: int
    source_path: str


class DataPipeline:
    """Pipeline tipado con Protocols — composición con contratos."""

    def __init__(
        self,
        loader: DataLoader,      # ← Protocol como type hint
        cleaner: DataCleaner,     # ← No fuerza herencia
        saver: DataSaver,
    ):
        self._loader = loader
        self._cleaner = cleaner
        self._saver = saver

    def run(self, source_path: str, output_path: str) -> ProcessingResult:
        data = self._loader.load(source_path)
        rows_original = len(data)

        cleaned = self._cleaner.clean(data)
        self._saver.save(cleaned, output_path)

        return ProcessingResult(
            rows_original=rows_original,
            rows_after_cleaning=len(cleaned),
            source_path=source_path,
        )


# pyright/mypy verifican que CSVLoader cumple DataLoader
# SIN que CSVLoader herede de nada
pipeline = DataPipeline(
    loader=CSVLoader(),
    cleaner=FillNACleaner(fill_value=-1),
    saver=ParquetSaver(),
)
```

### Qué Ganamos

```
CON HERENCIA (ABC):

BaseProcessor  ←──── CSVProcessor ←──── LargeCSVProcessor
      ↑
      └──────── JSONProcessor ←──── NestedJSONProcessor

→ Acoplamiento fuerte, jerarquía rígida, difícil de combinar


CON COMPOSICIÓN + PROTOCOLS:

DataLoader (Protocol)     DataCleaner (Protocol)     DataSaver (Protocol)
    ↓                         ↓                          ↓
CSVLoader                 DropNACleaner              CSVSaver
ParquetLoader             FillNACleaner              ParquetSaver
JSONLoader                                           JSONLSaver

DataPipeline(loader, cleaner, saver)  ← Combina cualquiera con cualquiera

→ Piezas independientes, combinables, sin acoplamiento
```

### runtime_checkable: Verificación en Runtime (Opcional)

Para debugging o validación dinámica, puedes marcar un Protocol como `@runtime_checkable`:

```python
@runtime_checkable
class DataLoader(Protocol):
    def load(self, path: str) -> pd.DataFrame: ...


# Ahora puedes usar isinstance()
loader = CSVLoader()
print(isinstance(loader, DataLoader))  # True — verifica que tiene .load()
```

Úsalo con moderación: la verificación real la hace el type checker (pyright). `@runtime_checkable` es útil para assertions o mensajes de error claros en desarrollo, no como mecanismo principal de validación.

---

## Aprendizaje Clave

### Puntos Críticos a Recordar

1. **Herencia solo para is-a real y estable** — excepciones custom, poco más en la práctica diaria
2. **Composición por defecto** — "tiene un" en vez de "es un" para la mayoría de los casos
3. **Protocol > ABC** — contratos estructurales sin forzar herencia, verificados por el type checker
4. **Datos fluyen, no se mutan** — los datos pasan como argumentos y retornos entre piezas, no como `self.data` compartido
5. **Coherencia con Day 3** — estructuras de datos para los datos, objetos para el comportamiento, funciones para la lógica

### Cómo Desarrollar Intuición

**¿Debería usar herencia?**

- ¿Es una relación "is-a" permanente? (no "se parece a" o "comparte código con") → Quizá sí
- ¿La jerarquía tiene más de 2 niveles? → Probablemente no, refactoriza a composición
- ¿Necesitas hacer `super()` en más de un nivel? → No, refactoriza
- ¿Es una excepción custom? → Sí, herencia es el patrón correcto aquí

**¿Debería usar Protocol o ABC?**

- ¿Las implementaciones son tuyas y de tu equipo? → Protocol (más flexible)
- ¿Necesitas que el type checker valide sin que la clase herede? → Protocol
- ¿Trabajas con clases de terceros que no puedes modificar? → Protocol (encajan si tienen los métodos)
- ¿Necesitas forzar la implementación en runtime (no solo type checking)? → ABC puede tener sentido

**¿Composición o herencia para reutilizar código?**

- ¿Quiero que la clase hija herede comportamiento del padre? → Probablemente composición — extrae el comportamiento a un objeto separado e inyéctalo
- ¿Quiero que varias clases compartan el mismo método? → Composición — pon ese método en un objeto que todas usen

### Anti-patterns Rápidos

| ❌ No hagas esto                                      | ✅ Haz esto                                       |
| ----------------------------------------------------- | ------------------------------------------------- |
| Jerarquía de 3+ niveles de herencia                   | Composición con piezas independientes             |
| `class CSVLoader(BaseLoader)` para cada formato       | `DataLoader` Protocol + clases independientes     |
| `self.data` mutado por múltiples métodos heredados    | Datos que fluyen como argumentos entre funciones   |
| `raise NotImplementedError` en la base                | `Protocol` con firma del método                   |
| Herencia para reutilizar código                       | Composición — extraer y delegar                   |
| `super().clean()` en cadena de 3 niveles              | Cada pieza hace su trabajo completo                |

---

## Resumen de Principios

La composición es la opción por defecto para combinar comportamiento. La herencia es apropiada solo para relaciones is-a genuinas y estables (como excepciones). Los Protocols de `typing` permiten definir contratos que el type checker verifica sin forzar herencia, lo que te da flexibilidad para combinar piezas independientes. Respeta la separación de Day 3: los datos son estructuras (`dataclass`/Pydantic), el comportamiento vive en objetos que se componen, y los datos fluyen entre ellos como argumentos — nunca como estado mutable compartido.

---

## Referencias

1. Gamma, E. et al. (1994). *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley. "Favor object composition over class inheritance."
2. PEP 544 – Protocols: Structural subtyping: <https://peps.python.org/pep-0544/>
3. Martin, R. C. (2008). *Clean Code*. Prentice Hall. Chapter 6: Objects and Data Structures.
4. Python `typing.Protocol` Documentation: <https://docs.python.org/3/library/typing.html#typing.Protocol>
5. Hynek Schlawack (2023). "Subclassing in Python Redux": <https://hynek.me/articles/python-subclassing-redux/>

---

## Ejercicio Individual

**Objetivo**: Refactorizar una jerarquía de herencia a composición con Protocols.

**Tiempo estimado**: 15 minutos

### Código a Refactorizar

```python
import pandas as pd


class BaseFeatureEngineer:
    """Clase base para feature engineering — herencia abusada."""

    def __init__(self, data: pd.DataFrame):
        self.data = data

    def add_features(self):
        raise NotImplementedError

    def remove_outliers(self):
        """Elimina outliers por z-score — ¿todos los hijos lo necesitan?"""
        for col in self.data.select_dtypes(include="number").columns:
            z_scores = (self.data[col] - self.data[col].mean()) / self.data[col].std()
            self.data = self.data[z_scores.abs() < 3]

    def run(self):
        self.add_features()
        self.remove_outliers()
        return self.data


class NumericalFeatureEngineer(BaseFeatureEngineer):
    def add_features(self):
        for col in self.data.select_dtypes(include="number").columns:
            self.data[f"{col}_squared"] = self.data[col] ** 2
            self.data[f"{col}_log"] = self.data[col].apply(
                lambda x: x if x <= 0 else pd.np.log(x)
            )


class TextFeatureEngineer(BaseFeatureEngineer):
    def add_features(self):
        for col in self.data.select_dtypes(include="object").columns:
            self.data[f"{col}_length"] = self.data[col].str.len()
            self.data[f"{col}_word_count"] = self.data[col].str.split().str.len()

    def remove_outliers(self):
        """Texto no tiene outliers numéricos — override vacío. Code smell."""
        pass
```

### Criterios de Éxito

- [ ] Ninguna clase hereda de otra (excepto si defines excepciones)
- [ ] Al menos un `Protocol` que defina el contrato de feature engineering
- [ ] Feature adders y outlier removal son piezas separadas (composición)
- [ ] Los datos fluyen como argumentos, no como `self.data` mutado
- [ ] El override vacío de `remove_outliers()` desaparece
- [ ] Puedes combinar features numéricos sin outlier removal

### Pistas

- `remove_outliers` vacío es un code smell clásico: la clase hija NO es-un `BaseFeatureEngineer` si no necesita todos sus métodos
- Piensa en una función `add_numerical_features(df) → df` y otra `add_text_features(df) → df` como piezas
- `self.data` mutado por varios métodos es exactamente lo que queremos eliminar
- El Protocol podría ser tan simple como: `def transform(self, data: DataFrame) -> DataFrame`

---

## Ejercicio Grupal

**Objetivo**: Refactorizar un sistema de ingestión de datos de herencia profunda a composición con Protocols.

**Contexto**: Tu equipo heredó un sistema de ingestión que conecta a diferentes fuentes (S3, base de datos, API REST) para alimentar un pipeline de ML. El código original usa herencia profunda y cada nueva fuente requiere entender toda la jerarquía. Quieren que añadir una nueva fuente sea tan simple como escribir una clase que cumpla un contrato.

**Tiempo estimado**: 45 minutos

### Dinámica

1. **Análisis** (10 min): Identifiquen los problemas de herencia en el código y dibujen la jerarquía actual
2. **Diseño** (10 min): Definan los Protocols necesarios y cómo se compondrán
3. **Implementación** (20 min): Refactoricen a composición
4. **Demo** (5 min): Muestren cómo añadir una nueva fuente sin tocar código existente

### Código a Refactorizar

```python
import logging
from datetime import datetime

import pandas as pd

logger = logging.getLogger(__name__)


class BaseDataIngester:
    """Base para toda ingestión de datos."""

    def __init__(self, source_name: str):
        self.source_name = source_name
        self.data = None
        self.metadata = {}

    def connect(self):
        raise NotImplementedError

    def extract(self):
        raise NotImplementedError

    def validate(self):
        """Validación genérica — ¿sirve para todas las fuentes?"""
        if self.data is None:
            raise ValueError("No data extracted")
        if len(self.data) == 0:
            logger.warning(f"Empty dataset from {self.source_name}")

        self.metadata["row_count"] = len(self.data)
        self.metadata["extracted_at"] = datetime.now().isoformat()

    def transform(self):
        """Transformación por defecto — drop duplicates."""
        self.data = self.data.drop_duplicates()

    def ingest(self) -> pd.DataFrame:
        """Template method."""
        self.connect()
        self.extract()
        self.validate()
        self.transform()
        return self.data


class FileIngester(BaseDataIngester):
    """Ingestión desde archivos."""

    def __init__(self, source_name: str, file_path: str):
        super().__init__(source_name)
        self.file_path = file_path

    def connect(self):
        """Archivos no necesitan conexión — override vacío."""
        logger.info(f"File source: {self.file_path}")


class S3Ingester(FileIngester):
    """Ingestión desde S3 — hereda de FileIngester."""

    def __init__(self, source_name: str, bucket: str, key: str):
        super().__init__(source_name, f"s3://{bucket}/{key}")
        self.bucket = bucket
        self.key = key

    def connect(self):
        logger.info(f"Connecting to S3: {self.bucket}/{self.key}")
        # Simula descarga
        self.file_path = f"/tmp/{self.key}"

    def extract(self):
        # Simula lectura del archivo descargado
        self.data = pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]})


class DatabaseIngester(BaseDataIngester):
    """Ingestión desde base de datos."""

    def __init__(self, source_name: str, connection_string: str, query: str):
        super().__init__(source_name)
        self.connection_string = connection_string
        self.query = query
        self.connection = None

    def connect(self):
        logger.info(f"Connecting to DB: {self.connection_string}")
        self.connection = "fake_connection"  # Simula conexión

    def extract(self):
        logger.info(f"Executing query: {self.query}")
        self.data = pd.DataFrame({"id": [1, 2], "value": [10, 20]})

    def transform(self):
        """Override: DB necesita transformación diferente."""
        super().transform()
        # Renombrar columnas de DB
        self.data.columns = [c.lower().replace(" ", "_") for c in self.data.columns]


class APIIngester(BaseDataIngester):
    """Ingestión desde API REST."""

    def __init__(self, source_name: str, base_url: str, endpoint: str):
        super().__init__(source_name)
        self.base_url = base_url
        self.endpoint = endpoint

    def connect(self):
        logger.info(f"API endpoint: {self.base_url}/{self.endpoint}")

    def extract(self):
        # Simula llamada a API
        self.data = pd.DataFrame({"name": ["Alice"], "score": [95]})

    def validate(self):
        """Override: API necesita validar status code también."""
        super().validate()
        # Validación específica de API
        if "error" in self.data.columns:
            raise ValueError("API returned error response")
```

### Instrucciones por Persona

- **Persona 1**: Definir los Protocols (`DataExtractor`, `DataTransformer`, `DataValidator`) y la estructura de datos `IngestionResult`
- **Persona 2**: Implementar extractores concretos (`S3Extractor`, `DatabaseExtractor`, `APIExtractor`) que cumplan el Protocol
- **Persona 3**: Implementar transformadores y validadores concretos como piezas independientes
- **Persona 4**: Crear la clase `IngestionPipeline` que compone las piezas y verificar que añadir un `LocalFileExtractor` nuevo no requiere tocar código existente

### Criterios de Éxito

- [ ] Cero herencia (excepto excepciones custom si las crean)
- [ ] Al menos 2 Protocols definidos
- [ ] Extractores, transformadores y validadores son piezas independientes
- [ ] Los datos fluyen como argumentos (no `self.data` mutado)
- [ ] El override vacío de `connect()` en `FileIngester` desaparece
- [ ] Añadir una nueva fuente = crear una clase nueva sin tocar las existentes
- [ ] Type hints usan Protocols, no clases concretas
- [ ] `ProcessingResult` / `IngestionResult` es un `@dataclass` o Pydantic, no un dict

### Pistas

**Para Persona 1 — Protocols**:

```python
class DataExtractor(Protocol):
    """Contrato: extrae datos de una fuente."""

    def extract(self) -> pd.DataFrame: ...
```

**Para Persona 2 — Un extractor concreto**:

```python
class S3Extractor:
    """Extrae datos de S3 — NO hereda de nada."""

    def __init__(self, bucket: str, key: str):
        self._bucket = bucket
        self._key = key

    def extract(self) -> pd.DataFrame:
        # Descarga y lee — todo en un método
        ...
```

**Para Persona 4 — Pipeline compuesto**:

```python
class IngestionPipeline:
    def __init__(
        self,
        extractor: DataExtractor,
        transformers: list[DataTransformer],  # ← Múltiples, en orden
        validator: DataValidator,
    ): ...
```

### Preguntas para Reflexión

1. ¿Cuántas clases tenían herencia antes vs después?
2. Si un nuevo miembro del equipo quiere añadir un extractor de Google Sheets, ¿cuántas clases existentes necesita leer?
3. ¿Qué pasa con el `connect()` vacío de `FileIngester` después de la refactorización?
4. ¿Cómo testearías un `IngestionPipeline` sin conectar a S3 real?
5. ¿En qué se diferencia esta separación de responsabilidades de lo que vimos en Day 3 con funciones?

---

## Aplicación al Proyecto de Equipo

- [ ] Revisa tu proyecto: ¿hay alguna jerarquía de herencia de más de 2 niveles? Si sí, evalúa refactorizar a composición
- [ ] Si tienes clases con `raise NotImplementedError`, reemplázalas por Protocols
- [ ] Verifica que los datos fluyen como argumentos entre piezas, no como `self.data` mutado en una clase base
- [ ] Si tienes overrides vacíos (métodos heredados que no necesitas), es señal de que la herencia no es apropiada