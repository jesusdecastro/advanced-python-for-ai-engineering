# Objetos y Estructuras de Datos

## Tabla de Contenidos

1. [Introducción](#introducción)
2. [La Distinción Fundamental](#1-la-distinción-fundamental)
3. [Estructuras de Datos: Data Transfer Objects](#2-estructuras-de-datos-data-transfer-objects)
4. [Objetos: Encapsulación y Comportamiento](#3-objetos-encapsulación-y-comportamiento)
5. [La Ley de Demeter](#4-la-ley-de-demeter)
6. [Tell, Don't Ask](#5-tell-dont-ask)
7. [Resumen](#resumen-de-principios)

---

## Introducción

La distinción entre objetos y estructuras de datos es uno de los conceptos más malentendidos en programación orientada a objetos. Esta confusión lleva a diseños híbridos que violan principios fundamentales y resultan en código difícil de mantener.

**Referencia principal**: Martin, R. C. (2008). *Clean Code: A Handbook of Agile Software Craftsmanship*. Prentice Hall. Chapter 6: Objects and Data Structures.

### Contexto: Por Qué Importa

**Problema real en Data/IA**:
Estás construyendo un sistema de ML que maneja configuraciones de modelos, resultados de experimentos, y métricas de evaluación. Si mezclas objetos (con comportamiento) y estructuras de datos (solo datos), terminas con código confuso donde no sabes si una clase debe tener lógica o solo almacenar información. Esto lleva a bugs sutiles y código difícil de mantener.

**Ejemplo concreto**:
Tienes una clase `ModelConfig` que almacena hiperparámetros. ¿Debería tener métodos para validar los parámetros? ¿O solo ser un contenedor de datos? Si agregas lógica, ¿dónde termina? Esta confusión hace que el código crezca de forma desorganizada.

**Consecuencias de NO entenderlo**:
- **Clases híbridas confusas**: Mezclan datos y comportamiento sin criterio claro
- **Violación de encapsulación**: Expones detalles internos que no deberías
- **Código frágil**: Cambios pequeños rompen múltiples partes del sistema
- **Testing difícil**: No sabes qué mockear ni cómo estructurar tests
- **Mantenimiento costoso**: Cada cambio requiere tocar muchas clases

### Principio Fundamental

> "Objects hide their data behind abstractions and expose functions that operate on that data. Data structures expose their data and have no meaningful functions."
>
> — Robert C. Martin, Clean Code

Esta distinción es absoluta: una clase es un objeto O una estructura de datos, nunca ambos.

---

### El Concepto

**Definición técnica**:
Los **objetos** ocultan sus datos detrás de abstracciones y exponen funciones que operan sobre esos datos. Las **estructuras de datos** exponen sus datos y no tienen funciones significativas. Son conceptos opuestos que sirven propósitos diferentes.

**Cómo funciona internalmente**:
1. **Objetos**: Encapsulan estado privado + comportamiento público
2. **Estructuras de datos**: Exponen estado público + sin comportamiento
3. **Ley de Demeter**: Los objetos no deben exponer su estructura interna
4. **Tell, Don't Ask**: Dile al objeto qué hacer, no le preguntes por sus datos

**Terminología clave**:
- **Encapsulación**: Ocultar detalles de implementación detrás de una interfaz
- **Abstracción**: Exponer solo lo esencial, ocultar lo accidental
- **Ley de Demeter**: Principio de "no hables con extraños" - limita dependencias
- **Data Transfer Object (DTO)**: Estructura de datos para transferir información entre capas
- **Tell, Don't Ask**: Principio de diseño OO que favorece comandos sobre queries

---

## 1. La Distinción Fundamental

### Por Qué Importa

La confusión entre objetos y estructuras de datos lleva a clases híbridas que violan principios de diseño y son difíciles de mantener. Entender la distinción te permite elegir la herramienta correcta para cada situación.

---

### Ejemplo Incorrecto: Clase Híbrida

```python
class ModelResult:
    """Clase híbrida confusa - mezcla datos y comportamiento."""
    
    def __init__(self):
        self.accuracy = 0.0
        self.precision = 0.0
        self.recall = 0.0
        self.model_name = ""
        self.timestamp = None
    
    def get_accuracy(self):
        """Getter innecesario."""
        return self.accuracy
    
    def set_accuracy(self, value):
        """Setter innecesario."""
        self.accuracy = value
    
    def calculate_f1(self):
        """Comportamiento mezclado con getters/setters."""
        return 2 * (self.precision * self.recall) / (self.precision + self.recall)
    
    def is_good_model(self):
        """Lógica de negocio en estructura de datos."""
        return self.accuracy > 0.8

# Uso - violando encapsulación
result = ModelResult()
result.accuracy = 0.85  # Acceso directo
result.precision = 0.9
result.recall = 0.8

# O usando getters innecesarios
result.set_accuracy(0.85)

# Lógica dispersa fuera de la clase
if result.accuracy > 0.8 and result.precision > 0.85:
    print("Good model")
```

**Problemas**:

- **Getters/setters innecesarios**: Si expones todo, ¿para qué métodos?
- **Mezcla responsabilidades**: ¿Es contenedor de datos o tiene lógica?
- **Violación de encapsulación**: Acceso directo a atributos
- **Lógica dispersa**: Reglas de negocio fuera de la clase
- **Difícil de cambiar**: Cambiar estructura afecta todo el código

---

## 2. Estructuras de Datos: Data Transfer Objects

### Por Qué Importa

Las estructuras de datos son contenedores de información sin comportamiento. Su propósito es transferir datos entre capas o componentes del sistema. No deben tener lógica de negocio.

**Referencia**: Fowler, M. (2002). *Patterns of Enterprise Application Architecture*. Addison-Wesley. Pattern: Data Transfer Object.

---

### Ejemplo Correcto: DTO con Dataclass

```python
from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class ModelMetrics:
    """
    Pure data structure for model metrics.
    
    No behavior, just data. Immutable for safety.
    
    :param accuracy: Model accuracy score
    :type accuracy: float
    :param precision: Model precision score
    :type precision: float
    :param recall: Model recall score
    :type recall: float
    :param model_name: Name of the model
    :type model_name: str
    :param timestamp: When metrics were calculated
    :type timestamp: datetime
    """
    accuracy: float
    precision: float
    recall: float
    model_name: str
    timestamp: datetime
    
    def __post_init__(self):
        """Validate data on creation - minimal logic."""
        if not 0 <= self.accuracy <= 1:
            raise ValueError(f"Invalid accuracy: {self.accuracy}")
        if not 0 <= self.precision <= 1:
            raise ValueError(f"Invalid precision: {self.precision}")
        if not 0 <= self.recall <= 1:
            raise ValueError(f"Invalid recall: {self.recall}")

# Uso - datos expuestos, sin comportamiento
metrics = ModelMetrics(
    accuracy=0.85,
    precision=0.9,
    recall=0.8,
    model_name="RandomForest",
    timestamp=datetime.now()
)

# Acceso directo está bien - es una estructura de datos
print(f"Accuracy: {metrics.accuracy}")
print(f"Precision: {metrics.precision}")
```

**Ventajas**:

- **Propósito claro**: Solo transferir datos
- **Inmutable**: `frozen=True` previene modificaciones accidentales
- **Validación mínima**: Solo verifica que los datos sean válidos
- **Sin comportamiento**: No tiene lógica de negocio
- **Fácil de serializar**: Puede convertirse a JSON, CSV, etc.

---

### Cuándo Usar Estructuras de Datos

**Usar cuando**:
- Transferir información entre capas (API → Service → Database)
- Serialización/deserialización (JSON, CSV, Parquet)
- Configuraciones simples
- Resultados de queries
- Sin lógica de negocio

**Características**:
- Atributos públicos
- Sin métodos (excepto validación mínima)
- Inmutables cuando sea posible
- Fáciles de serializar

---

## 3. Objetos: Encapsulación y Comportamiento

### Por Qué Importa

Los objetos encapsulan estado privado y exponen comportamiento público. Su propósito es proteger invariantes y proporcionar una interfaz clara para operaciones complejas.

---

### Ejemplo Correcto: Objeto con Comportamiento

```python
from datetime import datetime
from typing import Optional

class ModelEvaluator:
    """
    Object that encapsulates evaluation logic.
    
    Hides internal state, exposes behavior.
    """
    
    def __init__(
        self,
        model_name: str,
        accuracy: float,
        precision: float,
        recall: float
    ):
        """
        Initialize evaluator with metrics.
        
        :param model_name: Name of the model
        :type model_name: str
        :param accuracy: Accuracy score
        :type accuracy: float
        :param precision: Precision score
        :type precision: float
        :param recall: Recall score
        :type recall: float
        :raises ValueError: If metrics are out of valid range
        """
        # Validate inputs
        self._validate_metric("accuracy", accuracy)
        self._validate_metric("precision", precision)
        self._validate_metric("recall", recall)
        
        # Private attributes - encapsulated state
        self._model_name = model_name
        self._accuracy = accuracy
        self._precision = precision
        self._recall = recall
        self._timestamp = datetime.now()
        self._validated = False
    
    def _validate_metric(self, name: str, value: float) -> None:
        """Private helper for validation."""
        if not 0 <= value <= 1:
            raise ValueError(f"{name} must be in [0, 1], got {value}")
    
    def calculate_f1_score(self) -> float:
        """
        Calculate F1 score from internal metrics.
        
        :return: F1 score
        :rtype: float
        """
        if self._precision + self._recall == 0:
            return 0.0
        return 2 * (self._precision * self._recall) / \
               (self._precision + self._recall)
    
    def is_production_ready(self, threshold: float = 0.8) -> bool:
        """
        Determine if model meets production criteria.
        
        Encapsulates business logic.
        
        :param threshold: Minimum acceptable score
        :type threshold: float
        :return: True if model is production ready
        :rtype: bool
        """
        return (
            self._accuracy >= threshold and
            self._precision >= threshold and
            self.calculate_f1_score() >= threshold
        )
    
    def generate_report(self) -> str:
        """
        Generate evaluation report.
        
        :return: Formatted report string
        :rtype: str
        """
        f1 = self.calculate_f1_score()
        status = "READY" if self.is_production_ready() else "NOT READY"
        
        return f"""
Model Evaluation Report
=======================
Model: {self._model_name}
Status: {status}
Timestamp: {self._timestamp}

Metrics:
  Accuracy:  {self._accuracy:.4f}
  Precision: {self._precision:.4f}
  Recall:    {self._recall:.4f}
  F1 Score:  {f1:.4f}
        """.strip()
    
    # Only expose what's necessary - read-only access
    @property
    def model_name(self) -> str:
        """
        Get model name (read-only).
        
        :return: Model name
        :rtype: str
        """
        return self._model_name

# Uso - Tell, Don't Ask
evaluator = ModelEvaluator(
    model_name="RandomForest",
    accuracy=0.85,
    precision=0.9,
    recall=0.8
)

# No preguntamos por datos, le decimos qué hacer
if evaluator.is_production_ready():
    print(evaluator.generate_report())
```

**Ventajas**:

- **Encapsulación real**: Estado privado, comportamiento público
- **Tell, Don't Ask**: Invocamos comportamiento, no extraemos datos
- **Invariantes protegidos**: Validación en constructor
- **Fácil de cambiar**: Implementación interna puede cambiar sin afectar clientes
- **Testing simple**: Mock comportamiento, no estructura de datos

---

### Cuándo Usar Objetos

**Usar cuando**:
- Lógica de negocio compleja
- Estado que debe protegerse
- Comportamiento que puede cambiar
- Necesitas polimorfismo
- Invariantes que mantener

**Características**:
- Atributos privados (prefijo `_`)
- Métodos públicos ricos
- Validación de invariantes
- Comportamiento encapsulado

---

## 4. La Ley de Demeter

### Por Qué Importa

La Ley de Demeter (también conocida como "Principio del Mínimo Conocimiento") reduce el acoplamiento al limitar las interacciones entre objetos. Un objeto solo debe hablar con sus "amigos inmediatos", no con extraños.

**Referencia**: Lieberherr, K. J., & Holland, I. M. (1989). Assuring good style for object-oriented programs. *IEEE Software*, 6(5), 38-48.

---

### Ejemplo Incorrecto: Violación de la Ley de Demeter

```python
# Cadena de llamadas - "train wreck"
model_path = experiment.get_config().get_model_settings().get_path()

# Expone estructura interna
if user.get_account().get_balance() > 100:
    user.get_account().withdraw(50)

# Navegación profunda
output_dir = project.get_settings().get_output_config().get_directory()
```

**Problemas**:

- **Alto acoplamiento**: Código depende de la estructura interna de múltiples objetos
- **Frágil**: Cambios en la cadena rompen el código
- **Difícil de testear**: Necesitas mockear múltiples niveles
- **Violación de encapsulación**: Expone detalles de implementación

---

### Ejemplo Correcto: Respetando la Ley de Demeter

```python
# Tell, Don't Ask - método directo
model_path = experiment.get_model_path()

# Encapsula la lógica
if user.can_afford(100):
    user.withdraw(50)

# Método de conveniencia
output_dir = project.get_output_directory()
```

**Ventajas**:

- **Bajo acoplamiento**: Solo dependes de la interfaz inmediata
- **Fácil de cambiar**: Implementación interna puede cambiar
- **Testing simple**: Mock solo el objeto directo
- **Encapsulación preservada**: Detalles internos ocultos

---

### Regla Formal

Un método `M` de un objeto `O` solo puede invocar métodos de:

1. El propio objeto `O`
2. Parámetros de `M`
3. Objetos creados dentro de `M`
4. Atributos directos de `O`

**NO puede invocar métodos de objetos retornados por otros métodos.**

---

## 5. Tell, Don't Ask

### Por Qué Importa

El principio "Tell, Don't Ask" favorece comandos sobre queries. En vez de preguntar a un objeto por su estado y tomar decisiones basadas en eso, le dices al objeto qué hacer y dejas que él tome las decisiones.

**Referencia**: Alec Sharp, "Smalltalk by Example" (1997)

---

### Ejemplo Incorrecto: Ask, Then Tell

```python
# Preguntamos por el estado y decidimos afuera
if model.get_accuracy() > 0.8 and model.get_precision() > 0.85:
    model.save_to_disk()
    logger.info("Model saved")
else:
    logger.warning("Model not good enough")

# Extraemos datos para calcular
accuracy = evaluator.get_accuracy()
precision = evaluator.get_precision()
recall = evaluator.get_recall()
f1 = 2 * (precision * recall) / (precision + recall)
```

**Problemas**:

- **Lógica dispersa**: Reglas de negocio fuera del objeto
- **Duplicación**: Misma lógica repetida en múltiples lugares
- **Violación de encapsulación**: Dependemos de detalles internos
- **Difícil de cambiar**: Cambiar criterios requiere buscar todos los usos

---

### Ejemplo Correcto: Tell, Don't Ask

```python
# Le decimos qué hacer, él decide cómo
model.save_if_production_ready(threshold=0.8)

# El objeto encapsula el cálculo
f1 = evaluator.calculate_f1_score()

# Comando en vez de query + decisión
if evaluator.is_production_ready():
    evaluator.deploy()
```

**Ventajas**:

- **Lógica centralizada**: Reglas de negocio en un solo lugar
- **Sin duplicación**: Comportamiento reutilizable
- **Encapsulación preservada**: No dependemos de detalles internos
- **Fácil de cambiar**: Cambiar criterios en un solo lugar

---

### Implementación

```python
class ModelEvaluator:
    """Ejemplo de Tell, Don't Ask."""
    
    def save_if_production_ready(
        self,
        path: str,
        threshold: float = 0.8
    ) -> bool:
        """
        Save model if it meets production criteria.
        
        Encapsulates decision logic.
        
        :param path: Where to save the model
        :type path: str
        :param threshold: Minimum acceptable score
        :type threshold: float
        :return: True if model was saved
        :rtype: bool
        """
        if not self.is_production_ready(threshold):
            logger.warning(
                f"Model {self._model_name} not production ready. "
                f"Accuracy: {self._accuracy:.3f}, threshold: {threshold}"
            )
            return False
        
        try:
            self._save_model(path)
            logger.info(f"Model {self._model_name} saved to {path}")
            return True
        except IOError as e:
            logger.error(f"Failed to save model: {e}")
            raise
    
    def _save_model(self, path: str) -> None:
        """Private helper for saving."""
        # Implementation details hidden
        pass
```

---

## Aprendizaje Clave

### Puntos Críticos a Recordar

1. **Elige uno**: Estructura de datos O objeto, nunca ambos
2. **Estructuras de datos**: Exponen todo, sin comportamiento significativo
3. **Objetos**: Ocultan datos, exponen comportamiento
4. **No getters/setters**: Si expones todo, usa estructura de datos
5. **Tell, Don't Ask**: Invoca métodos, no extraigas datos para decidir
6. **Ley de Demeter**: Habla solo con amigos inmediatos

---

### Cómo Desarrollar Intuición

**Pregúntate**: "¿Esta clase tiene lógica de negocio?"
- NO → Usa estructura de datos (dataclass)
- SÍ → Usa objeto con encapsulación

**Pregúntate**: "¿Necesito acceder a estos datos directamente?"
- SÍ → Estructura de datos
- NO → Objeto con métodos

**Pregúntate**: "¿Estoy preguntando por estado para tomar decisiones?"
- SÍ → Violación de Tell, Don't Ask - mueve la lógica al objeto
- NO → Correcto

**Pregúntate**: "¿Esta cadena de llamadas es muy larga?"
- SÍ → Violación de Ley de Demeter - añade método de conveniencia
- NO → Correcto

---

### Cuándo Usar Cada Uno

**Estructura de datos cuando**:
- Transferir información entre capas (DTOs)
- Configuraciones simples
- Resultados de queries
- Sin lógica de negocio
- Necesitas serialización fácil

**Objeto cuando**:
- Lógica de negocio compleja
- Estado que debe protegerse
- Comportamiento que puede cambiar
- Necesitas polimorfismo
- Invariantes que mantener

**NO mezcles**:
- Getters/setters con lógica de negocio
- Atributos públicos con métodos complejos
- Acceso directo con encapsulación

---

## Resumen de Principios

La distinción entre objetos y estructuras de datos es fundamental para código limpio:

1. **Objetos**: Ocultan datos, exponen comportamiento
2. **Estructuras de datos**: Exponen datos, sin comportamiento
3. **No híbridos**: Elige uno u otro, no ambos
4. **Tell, Don't Ask**: Invoca métodos, no extraigas datos
5. **Ley de Demeter**: Habla solo con amigos inmediatos
6. **Encapsulación**: Protege invariantes con atributos privados

**Regla de oro**: Si una clase tiene lógica de negocio, debe ser un objeto con encapsulación. Si solo transfiere datos, debe ser una estructura de datos pura.

---

## Referencias

1. Martin, R. C. (2008). *Clean Code: A Handbook of Agile Software Craftsmanship*. Prentice Hall. Chapter 6: Objects and Data Structures.
2. Fowler, M. (2002). *Patterns of Enterprise Application Architecture*. Addison-Wesley. Pattern: Data Transfer Object.
3. Lieberherr, K. J., & Holland, I. M. (1989). Assuring good style for object-oriented programs. *IEEE Software*, 6(5), 38-48.
4. Python Dataclasses: <https://docs.python.org/3/library/dataclasses.html>
5. Martin Fowler - Tell Don't Ask: <https://martinfowler.com/bliki/TellDontAsk.html>
6. Law of Demeter: <https://en.wikipedia.org/wiki/Law_of_Demeter>

---

## Ejercicio Práctico Individual

Identifica si las siguientes clases deberían ser objetos o estructuras de datos, y refactoriza según corresponda:

```python
class TrainingConfig:
    def __init__(self):
        self.learning_rate = 0.001
        self.batch_size = 32
        self.epochs = 100
    
    def get_learning_rate(self):
        return self.learning_rate
    
    def validate(self):
        if self.learning_rate <= 0:
            raise ValueError("Invalid learning rate")

class DataProcessor:
    def __init__(self):
        self.data = None
        self.processed = False
    
    def get_data(self):
        return self.data
    
    def is_processed(self):
        return self.processed
```

**Pistas**:
- ¿Tiene lógica de negocio compleja?
- ¿Necesita proteger invariantes?
- ¿Solo transfiere datos?

---
