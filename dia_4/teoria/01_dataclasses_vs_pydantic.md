# Modelado de Datos con Pydantic

## Tabla de Contenidos

1. [Objetivos de Aprendizaje](#objetivos-de-aprendizaje)
2. [Prerrequisitos](#prerrequisitos)
3. [Introducción](#introducción)
4. [Repaso Rápido: @property y dataclasses](#1-repaso-rápido-property-y-dataclasses)
5. [Pydantic v2: Modelos y Validación](#2-pydantic-v2-modelos-y-validación)
6. [Validadores: Field y Model](#3-validadores-field-y-model)
7. [Modelos Anidados y Discriminated Unions](#4-modelos-anidados-y-discriminated-unions)
8. [Aprendizaje Clave](#aprendizaje-clave)
9. [Resumen de Principios](#resumen-de-principios)
10. [Referencias](#referencias)
11. [Ejercicio Individual](#ejercicio-individual)
12. [Ejercicio Grupal](#ejercicio-grupal)

---

## Objetivos de Aprendizaje

Al completar esta lección serás capaz de:

- Elegir entre `dataclasses` y Pydantic según el caso de uso
- Crear modelos Pydantic v2 con validación automática de datos
- Implementar validadores a nivel de campo y de modelo
- Modelar estructuras complejas con modelos anidados y discriminated unions
- Aplicar Pydantic a casos reales de Data/IA: configs de pipelines, schemas de datos, structured outputs de LLMs

---

## Prerrequisitos

- Día 1-2: Proyecto Python con `uv`, estructura de módulos
- Día 3: Clean Code (naming, funciones, type hints)
- Familiaridad básica con type hints de Python (`str`, `int`, `list[str]`, `dict`, `Optional`)

---

## Introducción

### Contexto: Por Qué Importa

**Problema real en Data/IA**:

Tu pipeline de datos recibe configuraciones desde un JSON. Alguien cambia `"learning_rate": 0.01` por `"learning_rate": "alto"`. El código no falla inmediatamente — simplemente produce resultados basura después de 4 horas de entrenamiento. O peor: un LLM devuelve un JSON con un campo que debería ser una lista pero viene como string, y tu código downstream se rompe en producción a las 3 AM.

**Ejemplo concreto**:

Un equipo tiene un pipeline que acepta configuraciones por diccionario. Cada función accede a `config["model"]["hidden_size"]` con `[]`. Un día alguien renombra el campo a `hidden_dim`. No hay error de tipo, no hay validación — solo un `KeyError` en producción, 3 niveles de llamada profundo, sin contexto de qué salió mal.

**Consecuencias de NO modelar datos**:

- **Errores silenciosos**: Tipos incorrectos que no fallan pero producen resultados erróneos
- **Debugging doloroso**: `KeyError` sin contexto de qué campo falta ni por qué
- **Código frágil**: Cambiar un campo rompe cosas en lugares inesperados
- **Documentación inexistente**: El "schema" vive en la cabeza de quien escribió el código
- **LLM outputs impredecibles**: Sin validación, un JSON malformado de un LLM rompe toda la cadena

### Principio Fundamental

> "Make illegal states unrepresentable."
>
> — Yaron Minsky (Jane Street)

Si tu modelo de datos solo permite estados válidos, toda una categoría de bugs desaparece. No necesitas validar en 15 sitios diferentes — validas una vez, al crear el objeto, y el resto del código trabaja con datos que **sabes** que son correctos.

### El Concepto

**Definición técnica**:

El modelado de datos es definir estructuras tipadas que representan la información de tu dominio. En Python, las tres herramientas principales son `@property` (atributos calculados), `dataclasses` (estructuras de datos simples) y `Pydantic` (modelos con validación).

**Cómo funciona internamente**:

1. **`dataclasses`**: Generan `__init__`, `__repr__`, `__eq__` automáticamente. No validan tipos en runtime
2. **Pydantic**: Usa un core de validación escrito en Rust. Valida y coerce tipos en runtime. Serializa/deserializa nativamente
3. **`@property`**: Decorador que convierte un método en un atributo de solo lectura, útil para valores derivados

**Terminología clave**:

- **Schema**: Definición de la estructura y tipos de tus datos
- **Validación**: Verificar que los datos cumplen el schema en runtime
- **Serialización**: Convertir objeto → dict/JSON
- **Deserialización**: Convertir dict/JSON → objeto tipado
- **Coerción**: Conversión automática de tipos (`"42"` → `42`)

---

## 1. Repaso Rápido: @property y dataclasses

### @property: Atributos Calculados

`@property` convierte un método en un atributo de solo lectura. Es útil para valores que se derivan de otros atributos.

```python
class ModelMetrics:
    def __init__(self, true_positives: int, false_positives: int, false_negatives: int):
        self.true_positives = true_positives
        self.false_positives = false_positives
        self.false_negatives = false_negatives

    @property
    def precision(self) -> float:
        """Se calcula, no se almacena."""
        total = self.true_positives + self.false_positives
        return self.true_positives / total if total > 0 else 0.0

    @property
    def recall(self) -> float:
        total = self.true_positives + self.false_negatives
        return self.true_positives / total if total > 0 else 0.0

    @property
    def f1_score(self) -> float:
        p, r = self.precision, self.recall
        return 2 * (p * r) / (p + r) if (p + r) > 0 else 0.0


metrics = ModelMetrics(true_positives=80, false_positives=20, false_negatives=10)
print(metrics.precision)  # 0.8 — se accede como atributo, no como método()
print(metrics.f1_score)   # 0.842...
```

**Cuándo usar `@property`**: cuando un valor se calcula a partir de otros atributos y quieres que se acceda como si fuera un atributo normal. No para lógica compleja ni llamadas costosas.

### dataclasses: Estructuras Simples

```python
from dataclasses import dataclass, field


@dataclass
class TrainingConfig:
    """Configuración para entrenamiento — sin validación runtime."""
    model_name: str
    learning_rate: float = 0.001
    epochs: int = 10
    batch_size: int = 32
    tags: list[str] = field(default_factory=list)


# Funciona — dataclass no valida tipos
config = TrainingConfig(
    model_name="bert-base",
    learning_rate="esto no es un float",  # ← No falla. Debería.
    epochs=-5,                             # ← Tampoco falla.
)
```

**Ventajas de dataclasses**: generan `__init__`, `__repr__`, `__eq__` automáticamente. Ligeros, sin dependencias externas, parte de la stdlib.

**Limitación crítica**: NO validan tipos en runtime. Los type hints son solo documentación.

---

## 2. Pydantic v2: Modelos y Validación

### Por Qué Importa

Pydantic es la librería de modelado de datos más usada del ecosistema Python en IA. FastAPI, LangChain, Strands, OpenAI SDK, Instructor — todos usan Pydantic para definir schemas. Si trabajas en AI Engineering, vas a usar Pydantic todos los días.

### Ejemplo Incorrecto

```python
def create_pipeline_config(raw_config: dict) -> dict:
    """Configuración por diccionario — sin schema ni validación."""
    config = {
        "model_name": raw_config.get("model_name", "default"),
        "learning_rate": raw_config.get("lr", 0.001),
        "epochs": raw_config.get("epochs", 10),
        "output_dir": raw_config.get("output_dir", "./output"),
    }
    # ¿Es válido? ¿Quién sabe?
    return config


# Nadie sabe qué campos son obligatorios
config = create_pipeline_config({"lr": "rápido", "epochs": -1})
# config["learning_rate"] == "rápido"  ← Error silencioso
```

**Problemas**:

- Sin validación de tipos: `"rápido"` se acepta como learning_rate
- Sin documentación del schema: hay que leer el código para saber qué campos existen
- Keys como strings: un typo en `"lerning_rate"` pasa desapercibido
- Sin valores por defecto declarativos: la lógica de defaults está dispersa
- Sin serialización: hay que escribir manualmente la conversión a JSON/YAML

### Qué Cambiar y Por Qué

1. `dict` → `BaseModel` de Pydantic (schema explícito, autocompletado en IDE)
2. `raw_config.get()` → atributos tipados (error en construcción si falta algo obligatorio)
3. Sin validación → validadores automáticos (tipos incorrectos fallan inmediatamente)
4. Sin serialización → `.model_dump()` / `.model_dump_json()` gratis

### Ejemplo Correcto

```python
from pydantic import BaseModel, Field


class PipelineConfig(BaseModel):
    """Configuración del pipeline — validada automáticamente."""
    model_name: str
    learning_rate: float = Field(default=0.001, gt=0, lt=1)
    epochs: int = Field(default=10, ge=1, le=1000)
    output_dir: str = "./output"


# Validación automática al construir
config = PipelineConfig(model_name="bert-base", learning_rate=0.01)
print(config.learning_rate)  # 0.01 — acceso por atributo, no por key
print(config.model_dump())   # {'model_name': 'bert-base', 'learning_rate': 0.01, ...}

# Esto FALLA inmediatamente — no silenciosamente
try:
    bad_config = PipelineConfig(
        model_name="bert",
        learning_rate="rápido",  # ValidationError: valor no es float
    )
except Exception as e:
    print(e)  # Mensaje claro de qué campo falló y por qué

# Coerción automática — "42" → 42
config2 = PipelineConfig(model_name="bert", epochs="20")
print(type(config2.epochs))  # <class 'int'> — Pydantic lo convierte
```

**Ventajas**:

- Schema explícito y auto-documentado
- Validación automática al crear el objeto
- Restricciones declarativas (`gt=0`, `le=1000`)
- Coerción inteligente de tipos
- Serialización/deserialización gratis
- Mensajes de error claros con contexto

### Pydantic vs dataclasses: Cuándo Usar Cada Uno

| Criterio                  | `dataclasses`              | Pydantic                        |
| ------------------------- | -------------------------- | ------------------------------- |
| **Validación runtime**    | No                         | Sí, automática                  |
| **Dependencias**          | Ninguna (stdlib)           | `pydantic` (depende de Rust)    |
| **Performance creación**  | Más rápido (sin validación)| Más lento (valida todo)         |
| **Serialización JSON**    | Manual                     | `.model_dump_json()` incluido   |
| **Coerción de tipos**     | No                         | Sí (`"42"` → `42`)             |
| **Restricciones (gt, lt)**| Manual en `__post_init__`  | Declarativo con `Field()`       |
| **Uso típico en IA**      | DTOs internos simples      | Configs, APIs, schemas de LLM   |

**Regla práctica**: si los datos vienen de fuera (JSON, API, usuario, LLM), usa Pydantic. Si son estructuras internas que tú controlas, `dataclasses` puede bastar.

---

## 3. Validadores: Field y Model

### Por Qué Importa

Los campos con tipos básicos no siempre son suficientes. Necesitas reglas de negocio: "el learning rate debe estar entre 0 y 1", "el nombre del modelo no puede estar vacío", "si usas GPU, el batch size debe ser múltiplo de 8". Pydantic v2 ofrece validadores a nivel de campo y de modelo para esto.

### Ejemplo Incorrecto

```python
from pydantic import BaseModel


class ExperimentConfig(BaseModel):
    experiment_name: str
    learning_rate: float
    train_split: float
    val_split: float
    model_type: str
    num_layers: int


# Todo esto pasa validación pero es INVÁLIDO semánticamente
config = ExperimentConfig(
    experiment_name="",              # Nombre vacío
    learning_rate=-0.5,              # Negativo
    train_split=0.7,
    val_split=0.5,                   # 0.7 + 0.5 = 1.2 > 1.0
    model_type="TRANSFORMER",        # ¿Debería normalizarse?
    num_layers=0,                    # Cero capas no tiene sentido
)
```

**Problemas**:

- Pydantic valida tipos pero no reglas de negocio
- Valores semánticamente inválidos se aceptan silenciosamente
- No hay normalización de datos (mayúsculas, espacios, etc.)
- Relaciones entre campos no se validan (train + val > 1.0)

### Qué Cambiar y Por Qué

1. Añadir `Field()` con restricciones numéricas para validación declarativa
2. Añadir `@field_validator` para reglas de un campo individual
3. Añadir `@model_validator` para reglas que cruzan múltiples campos
4. Normalizar datos en validadores (strip, lowercase) para consistencia

### Ejemplo Correcto

```python
from pydantic import BaseModel, Field, field_validator, model_validator


class ExperimentConfig(BaseModel):
    """Configuración de experimento — con validación semántica."""
    experiment_name: str = Field(min_length=1, max_length=100)
    learning_rate: float = Field(gt=0, lt=1)
    train_split: float = Field(gt=0, lt=1)
    val_split: float = Field(gt=0, lt=1)
    model_type: str
    num_layers: int = Field(ge=1, le=200)

    @field_validator("experiment_name")
    @classmethod
    def clean_experiment_name(cls, v: str) -> str:
        """Normaliza nombre: sin espacios extra, lowercase."""
        cleaned = v.strip().lower().replace(" ", "_")
        if not cleaned.replace("_", "").isalnum():
            raise ValueError("experiment_name solo acepta alfanuméricos y guiones bajos")
        return cleaned

    @field_validator("model_type")
    @classmethod
    def normalize_model_type(cls, v: str) -> str:
        """Normaliza a lowercase para consistencia."""
        allowed = {"transformer", "lstm", "cnn", "mlp"}
        normalized = v.strip().lower()
        if normalized not in allowed:
            raise ValueError(f"model_type debe ser uno de: {allowed}")
        return normalized

    @model_validator(mode="after")
    def validate_splits(self) -> "ExperimentConfig":
        """Los splits deben sumar <= 1.0 para dejar espacio al test."""
        total = self.train_split + self.val_split
        if total >= 1.0:
            raise ValueError(
                f"train_split ({self.train_split}) + val_split ({self.val_split}) "
                f"= {total}, debe ser < 1.0 para dejar espacio al test split"
            )
        return self


# Ahora todo se valida y normaliza automáticamente
config = ExperimentConfig(
    experiment_name="  Mi Experimento 1  ",
    learning_rate=0.001,
    train_split=0.7,
    val_split=0.15,
    model_type="TRANSFORMER",
    num_layers=12,
)
print(config.experiment_name)  # "mi_experimento_1" — normalizado
print(config.model_type)       # "transformer" — normalizado

# Esto falla con mensaje CLARO
try:
    bad = ExperimentConfig(
        experiment_name="test",
        learning_rate=0.01,
        train_split=0.7,
        val_split=0.5,  # 0.7 + 0.5 > 1.0
        model_type="transformer",
        num_layers=6,
    )
except Exception as e:
    print(e)
    # train_split (0.7) + val_split (0.5) = 1.2, debe ser < 1.0 ...
```

**Ventajas**:

- Reglas de negocio declarativas junto al modelo, no dispersas por el código
- `@field_validator`: valida y transforma un campo individual
- `@model_validator`: valida relaciones entre campos
- Mensajes de error claros con los valores que fallaron
- La normalización es automática — el resto del código recibe datos limpios

---

## 4. Modelos Anidados y Discriminated Unions

### Por Qué Importa

Los sistemas reales tienen configuraciones anidadas: un pipeline tiene un modelo, el modelo tiene hiperparámetros, los hiperparámetros dependen del tipo de modelo. Además, en AI Engineering es muy común tener variantes: "si el tipo es `openai`, espero estos campos; si es `bedrock`, espero estos otros". Pydantic maneja todo esto nativamente.

### Ejemplo Incorrecto

```python
def build_pipeline(config: dict) -> None:
    """Pipeline configurado con dicts anidados — frágil."""
    model_config = config["model"]
    model_type = model_config["type"]

    if model_type == "openai":
        api_key = model_config["api_key"]          # ¿Existe?
        model_name = model_config["model_name"]     # ¿Existe?
    elif model_type == "bedrock":
        region = model_config["region"]             # ¿Existe?
        model_id = model_config["model_id"]         # ¿Existe?
    # Si alguien pasa type="huggingface", no falla — simplemente no hace nada
```

**Problemas**:

- Sin schema para las variantes: hay que leer if/elif para saber qué campos necesita cada tipo
- `KeyError` si falta un campo — sin contexto claro
- Nuevos tipos no fallan, simplemente se ignoran silenciosamente
- Imposible generar documentación o schema JSON automáticamente

### Qué Cambiar y Por Qué

1. Dicts anidados → modelos Pydantic anidados (schema explícito para cada nivel)
2. if/elif por tipo → discriminated union con `Literal` + `Discriminator` (Pydantic elige el modelo correcto automáticamente)
3. Campos opcionales implícitos → campos requeridos por variante (si falta algo, falla al crear)

### Ejemplo Correcto

```python
from typing import Annotated, Literal, Union

from pydantic import BaseModel, Field, SecretStr
from pydantic import Discriminator


# --- Modelos anidados para cada proveedor ---

class OpenAIModelConfig(BaseModel):
    """Configuración para modelos de OpenAI."""
    provider: Literal["openai"] = "openai"
    model_name: str = "gpt-4o"
    api_key: SecretStr  # SecretStr oculta el valor en logs/repr
    temperature: float = Field(default=0.7, ge=0, le=2)
    max_tokens: int = Field(default=1000, ge=1)


class BedrockModelConfig(BaseModel):
    """Configuración para modelos en AWS Bedrock."""
    provider: Literal["bedrock"] = "bedrock"
    model_id: str = "anthropic.claude-sonnet-4-20250514"
    region: str = "us-east-1"
    max_tokens: int = Field(default=1000, ge=1)


# --- Discriminated union: Pydantic elige el modelo según "provider" ---

ModelConfig = Annotated[
    Union[OpenAIModelConfig, BedrockModelConfig],
    Field(discriminator="provider"),
]


# --- Modelo principal del pipeline ---

class ChunkingConfig(BaseModel):
    chunk_size: int = Field(default=512, ge=100, le=8192)
    chunk_overlap: int = Field(default=50, ge=0)

    @model_validator(mode="after")
    def overlap_less_than_size(self) -> "ChunkingConfig":
        if self.chunk_overlap >= self.chunk_size:
            raise ValueError(
                f"chunk_overlap ({self.chunk_overlap}) debe ser menor "
                f"que chunk_size ({self.chunk_size})"
            )
        return self


class RAGPipelineConfig(BaseModel):
    """Configuración completa de un pipeline RAG."""
    pipeline_name: str = Field(min_length=1)
    model: ModelConfig                          # ← Discriminated union
    chunking: ChunkingConfig = ChunkingConfig() # ← Modelo anidado con defaults
    top_k: int = Field(default=5, ge=1, le=100)


# --- Uso: Pydantic valida TODO recursivamente ---

# Desde un dict (como vendría de un JSON/YAML)
config_dict = {
    "pipeline_name": "rag-produccion",
    "model": {
        "provider": "openai",
        "model_name": "gpt-4o",
        "api_key": "sk-abc123",
        "temperature": 0.3,
    },
    "chunking": {
        "chunk_size": 1024,
        "chunk_overlap": 100,
    },
    "top_k": 10,
}

config = RAGPipelineConfig(**config_dict)
print(type(config.model))       # OpenAIModelConfig — Pydantic eligió automáticamente
print(config.model.api_key)     # SecretStr('**********') — no se filtra en logs
print(config.chunking.chunk_size)  # 1024

# Serialización completa a JSON
print(config.model_dump_json(indent=2))

# Si el provider no es válido, falla con mensaje claro
try:
    bad = RAGPipelineConfig(
        pipeline_name="test",
        model={"provider": "huggingface", "model_id": "x"},  # No existe
    )
except Exception as e:
    print(e)  # Error claro: provider must be 'openai' or 'bedrock'
```

**Ventajas**:

- Schema completo y auto-documentado para estructuras complejas
- Discriminated union: Pydantic instancia el modelo correcto según el valor de `provider`
- Validación recursiva: cada nivel se valida independientemente
- `SecretStr` para campos sensibles — no se filtran en logs ni repr
- Un dict de JSON se convierte en objeto tipado con una línea

### Caso de Uso: Structured Outputs de LLMs

```python
from pydantic import BaseModel


class ExtractedEntity(BaseModel):
    """Schema para forzar al LLM a devolver datos estructurados."""
    entity_name: str
    entity_type: Literal["person", "organization", "location"]
    confidence: float = Field(ge=0, le=1)


class ExtractionResult(BaseModel):
    """Resultado completo de extracción de entidades."""
    entities: list[ExtractedEntity]
    source_text: str
    model_used: str


# Con frameworks como Instructor o el SDK de OpenAI:
# result = client.chat.completions.create(
#     model="gpt-4o",
#     response_model=ExtractionResult,  # ← Pydantic como schema
#     messages=[{"role": "user", "content": text}],
# )
# result es un ExtractionResult validado automáticamente
```

---

## Aprendizaje Clave

### Puntos Críticos a Recordar

1. **`dataclasses` no validan en runtime** — los type hints son solo documentación; Pydantic sí valida
2. **`Field()` para restricciones declarativas** — `gt`, `lt`, `ge`, `le`, `min_length`, `max_length` evitan validación manual
3. **`@field_validator` para un campo, `@model_validator` para relaciones** — siempre con `@classmethod` y `mode` explícito
4. **Discriminated unions para variantes** — `Literal` + `discriminator` reemplaza if/elif sobre tipos
5. **`SecretStr` para datos sensibles** — nunca almacenes API keys como `str` plano

### Cómo Desarrollar Intuición

**¿Debería usar Pydantic o dataclass?**

- ¿Los datos vienen de fuera (JSON, API, usuario, LLM)? → **Pydantic**
- ¿Son datos internos que solo mueve mi código? → **dataclass** puede bastar
- ¿Necesito serializar/deserializar? → **Pydantic**
- ¿Quiero máxima performance y los tipos son correctos por construcción? → **dataclass**

**¿Debería añadir un validador?**

- ¿El tipo solo (`float`) no captura la restricción (`> 0`)? → Sí, `Field(gt=0)`
- ¿La validación depende de OTRO campo? → Sí, `@model_validator`
- ¿Necesito transformar/normalizar el dato? → Sí, `@field_validator`
- ¿Solo verifico el tipo? → No, Pydantic ya lo hace

### Anti-patterns Rápidos

| ❌ No hagas esto                              | ✅ Haz esto                                        |
| --------------------------------------------- | -------------------------------------------------- |
| `config["learning_rate"]` con dict            | `config.learning_rate` con Pydantic                |
| Validar tipos manualmente con `isinstance()`  | Dejar que Pydantic valide automáticamente          |
| `api_key: str` en el modelo                   | `api_key: SecretStr` para no filtrarlo en logs     |
| if/elif para variantes de configuración       | Discriminated union con `Literal` + `discriminator`|
| `@field_validator` para validar entre campos  | `@model_validator(mode="after")` para relaciones   |
| Validación dispersa por el código             | Centralizada en el modelo Pydantic                 |

---

## Resumen de Principios

Pydantic convierte tu schema de datos en código que se auto-valida y auto-documenta. Los datos de fuera (JSON, APIs, LLMs) siempre deben pasar por un modelo Pydantic antes de entrar a tu lógica de negocio. Usa `Field()` para restricciones simples, `@field_validator` para transformar campos individuales, `@model_validator` para reglas que cruzan campos, y discriminated unions para configuraciones con variantes. `dataclasses` sigue siendo válido para estructuras internas simples donde no necesitas validación runtime.

---

## Referencias

1. Pydantic v2 Documentation: <https://docs.pydantic.dev/latest/>
2. Pydantic v2 — Validators: <https://docs.pydantic.dev/latest/concepts/validators/>
3. Pydantic v2 — Discriminated Unions: <https://docs.pydantic.dev/latest/concepts/unions/#discriminated-unions>
4. Python `dataclasses` Documentation: <https://docs.python.org/3/library/dataclasses.html>
5. Samuel Colvin (2023). "Pydantic V2 Plan": <https://docs.pydantic.dev/latest/concepts/v1-vs-v2/>

---

## Ejercicio Individual

**Objetivo**: Crear un modelo Pydantic para validar la configuración de un dataset de entrenamiento.

### Código Base

Tienes esta función que carga configuración desde un diccionario. Refactorízala usando Pydantic:

```python
def prepare_dataset(config: dict) -> dict:
    name = config["dataset_name"]
    path = config["file_path"]
    fmt = config.get("format", "csv")
    sample_pct = config.get("sample_percentage", 100)
    seed = config.get("random_seed", 42)
    columns = config.get("selected_columns")  # None si no está

    if fmt not in ("csv", "parquet", "jsonl"):
        raise ValueError(f"Formato no soportado: {fmt}")

    if sample_pct <= 0 or sample_pct > 100:
        raise ValueError(f"Porcentaje inválido: {sample_pct}")

    return {
        "name": name,
        "path": path,
        "format": fmt,
        "sample_pct": sample_pct,
        "seed": seed,
        "columns": columns,
    }
```

### Criterios de Éxito

- [ ] Modelo Pydantic con todos los campos tipados
- [ ] `format` validado con `Literal["csv", "parquet", "jsonl"]`
- [ ] `sample_percentage` con restricciones numéricas via `Field()`
- [ ] `selected_columns` como `list[str] | None` con default `None`
- [ ] `dataset_name` con `min_length=1`
- [ ] Un `@field_validator` para normalizar o validar al menos un campo
- [ ] Test: crear un `DatasetConfig` válido e intentar crear uno inválido

### Pistas

- Empieza definiendo la clase con los campos y sus tipos
- `Literal["csv", "parquet", "jsonl"]` reemplaza la validación manual del `if fmt not in ...`
- `Field(gt=0, le=100)` reemplaza la validación manual del porcentaje
- Piensa: ¿qué campo se beneficiaría de normalización? (hint: `file_path` podría expandir `~`)

---

## Ejercicio Grupal

**Objetivo**: Modelar con Pydantic la configuración completa de un pipeline RAG, aplicando modelos anidados, discriminated unions y validadores.

**Contexto**: Tu equipo está construyendo un framework RAG que soporta múltiples proveedores de embeddings y LLMs. Hasta ahora la configuración se pasa como un diccionario anidado y cada parte del código valida (o no) lo que necesita. Quieren migrar a Pydantic para tener un schema centralizado.

### Dinámica

1. **Diseño del schema** (10 min): Dibujen en papel/pizarra la estructura de modelos anidados
2. **Implementación** (25 min): Codifiquen los modelos Pydantic según la distribución de trabajo
3. **Integración y test** (10 min): Junten las partes, creen configs válidas e inválidas

### Configuración a Modelar

Este es el dict que actualmente se pasa al pipeline. Conviértanlo a modelos Pydantic:

```python
raw_config = {
    "pipeline_name": "rag-production-v2",
    "embedding": {
        "provider": "openai",            # openai o sentence-transformers
        "model_name": "text-embedding-3-small",
        "dimensions": 256,
        # si provider es sentence-transformers:
        # "model_name": "all-MiniLM-L6-v2",
        # "device": "cpu",  # o "cuda"
    },
    "llm": {
        "provider": "bedrock",            # openai o bedrock
        "model_id": "anthropic.claude-sonnet-4-20250514",
        "region": "us-east-1",
        "temperature": 0.3,
        "max_tokens": 2000,
        # si provider es openai:
        # "model_name": "gpt-4o",
        # "api_key": "sk-...",
    },
    "retriever": {
        "top_k": 5,
        "score_threshold": 0.7,          # 0.0 a 1.0
        "reranker_enabled": True,
    },
    "chunking": {
        "strategy": "recursive",          # fixed, recursive, semantic
        "chunk_size": 1024,
        "chunk_overlap": 100,
    },
}
```

### Instrucciones por Persona

- **Persona 1**: Modelos de `embedding` — discriminated union `OpenAIEmbeddingConfig` / `STEmbeddingConfig`
- **Persona 2**: Modelos de `llm` — discriminated union `OpenAILLMConfig` / `BedrockLLMConfig`
- **Persona 3**: Modelos de `retriever` y `chunking` — con validadores (overlap < size, threshold 0-1)
- **Persona 4**: Modelo raíz `RAGPipelineConfig` — ensambla todo, añade `@model_validator` si hace falta

### Criterios de Éxito

- [ ] Cada sub-config es un `BaseModel` independiente con tipos correctos
- [ ] `embedding` y `llm` usan discriminated unions con `Literal` + `discriminator`
- [ ] Al menos 3 `Field()` con restricciones numéricas
- [ ] Al menos 1 `@field_validator` (normalización o validación custom)
- [ ] Al menos 1 `@model_validator` (validación cruzada entre campos)
- [ ] `SecretStr` para API keys
- [ ] Config válida se crea sin error desde el dict
- [ ] Config inválida falla con mensaje claro indicando qué campo y por qué
- [ ] `.model_dump_json()` produce JSON válido

### Pistas

**Para Persona 1 — Embeddings**:

```python
class OpenAIEmbeddingConfig(BaseModel):
    provider: Literal["openai"] = "openai"
    model_name: str = "text-embedding-3-small"
    dimensions: int = Field(default=256, ge=64, le=3072)
```

**Para Persona 3 — Chunking con validador**:

```python
class ChunkingConfig(BaseModel):
    strategy: Literal["fixed", "recursive", "semantic"]
    chunk_size: int = Field(ge=100, le=8192)
    chunk_overlap: int = Field(ge=0)

    @model_validator(mode="after")
    def overlap_must_be_less_than_size(self) -> "ChunkingConfig":
        # ...
```

**Para Persona 4 — Ensamblaje**:

```python
EmbeddingConfig = Annotated[
    Union[OpenAIEmbeddingConfig, STEmbeddingConfig],
    Field(discriminator="provider"),
]
```

### Preguntas para Reflexión

1. ¿Cuántas líneas de validación manual reemplazó Pydantic?
2. ¿Qué pasa si un equipo nuevo quiere añadir un proveedor de embeddings (por ejemplo, Cohere)? ¿Cuánto código hay que cambiar?
3. ¿Cómo generarían documentación automática del schema para el equipo de infraestructura?
4. ¿Qué validaciones son "de tipo" (Pydantic las hace gratis) vs "de negocio" (necesitan validadores)?
5. Si este config se guarda en un JSON en S3, ¿cómo lo cargarían con una línea? (hint: `model_validate_json`)

---

## Aplicación al Proyecto de Equipo

- [ ] Identifica al menos 2 estructuras de datos en tu proyecto que deberían ser modelos Pydantic
- [ ] Reemplaza al menos 1 dict de configuración por un `BaseModel` con validación
- [ ] Si tu proyecto tiene variantes (diferentes modelos, diferentes fuentes), evalúa si una discriminated union aplica
- [ ] Asegúrate de que ningún API key o secreto está como `str` plano — usa `SecretStr`