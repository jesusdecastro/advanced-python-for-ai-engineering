# Ejercicios Día 4: Arquitectura de Software y Principios SOLID

Ejercicios prácticos organizados en 4 bloques temáticos para dominar modelado de datos, composición, separación de responsabilidades y principios SOLID.

## Inicio Rápido

El proyecto ya está configurado con `pyproject.toml`. Solo necesitas:

### 1. Configurar el Entorno

```bash
# Navega al directorio de ejercicios
cd dia_4/exercises

# Sincroniza dependencias (crea .venv e instala todo automáticamente)
uv sync
```

**¿Qué hace `uv sync`?**
- Crea el entorno virtual `.venv/` si no existe
- Lee `pyproject.toml` y `uv.lock`
- Instala todas las dependencias del proyecto (incluyendo Pydantic)
- Instala las dependencias de desarrollo (pytest, pytest-cov, ruff, pyright) automáticamente
- Instala tu paquete `exercises` en modo editable
- Todo en un solo comando, sin necesidad de activar el entorno

### 2. Ejecutar Tests

```bash
# Ejecutar todos los tests de un bloque
uv run pytest tests/bloque_1/ -v

# Ejecutar todos los tests
uv run pytest

# Ejecutar un test individual (función)
uv run pytest tests/bloque_1/test_models.py::test_valid_local_source_config_creates_successfully

# Ejecutar tests de un concepto específico
uv run pytest tests/bloque_1/ -k "discriminated" -v

# Con coverage
uv run pytest --cov=exercises --cov-report=term-missing
```

**¿Por qué `uv run`?**
- Ejecuta comandos dentro del entorno virtual automáticamente
- No necesitas activar/desactivar el entorno manualmente
- Más rápido y conveniente

**Nota sobre dependencias de desarrollo:**
El proyecto usa `[dependency-groups]` en lugar de `[project.optional-dependencies]`. Esto significa que `uv sync` instala automáticamente las herramientas de desarrollo (pytest, ruff, pyright) sin necesidad de flags adicionales.

## Estructura del Proyecto

```
dia_4/exercises/
├── .venv/                  # Entorno virtual (creado por uv sync)
├── src/
│   └── exercises/          # Tu paquete
│       ├── __init__.py
│       ├── bloque_1/       # Modelado de Datos con Pydantic
│       │   ├── models.py
│       │   ├── helpers.py
│       │   ├── conftest.py
│       │   └── README.md
│       ├── bloque_2/       # Composición sobre Herencia
│       │   ├── preprocessing.py
│       │   ├── protocols.py
│       │   ├── helpers.py
│       │   ├── conftest.py
│       │   └── README.md
│       ├── bloque_3/       # SRP + DIP
│       │   ├── scoring.py
│       │   ├── protocols.py
│       │   ├── helpers.py
│       │   ├── conftest.py
│       │   └── README.md
│       └── bloque_4/       # OCP, LSP, ISP
│           ├── evaluation.py
│           ├── protocols.py
│           ├── helpers.py
│           ├── conftest.py
│           └── README.md
├── tests/
│   ├── __init__.py
│   ├── bloque_1/
│   │   ├── __init__.py
│   │   └── test_models.py
│   ├── bloque_2/
│   │   ├── __init__.py
│   │   └── test_preprocessing.py
│   ├── bloque_3/
│   │   ├── __init__.py
│   │   └── test_scoring.py
│   └── bloque_4/
│       ├── __init__.py
│       └── test_evaluation.py
├── pyproject.toml          # Ya configurado
├── uv.lock                 # Lock file con versiones exactas
└── README.md
```

## Flujo de Trabajo

### 1. Leer el Ejercicio

Revisa el archivo correspondiente en `src/exercises/` y el material de referencia en `dia_4/teoria/`.

### 2. Implementar la Solución

Completa las funciones marcadas con `TODO` o `pass`.

### 3. Ejecutar Tests

```bash
# Test específico del bloque que estás haciendo
uv run pytest tests/bloque_1/ -v

# Todos los tests
uv run pytest

# Un test individual
uv run pytest tests/bloque_1/test_models.py::test_cleaning_step_with_valid_operation

# Con más detalle
uv run pytest -v
```

### 4. Verificar Calidad del Código

```bash
# Verificar estilo
uv run ruff check src/

# Formatear código automáticamente
uv run ruff format src/
```

## Cómo Funcionan los Imports

**El problema original:**
```python
from exercises.bloque_1.models import CleaningJobConfig
# ModuleNotFoundError: No module named 'exercises'
```

**Después de `uv sync`:**
```python
from exercises.bloque_1.models import CleaningJobConfig
# Funciona porque el paquete está instalado en modo editable
```

**¿Por qué funciona?**

1. `uv sync` instala el paquete en modo editable (`-e`)
2. Crea un link en `.venv/lib/site-packages/` que apunta a `src/exercises/`
3. Python encuentra el módulo cuando lo importas
4. Los cambios en tu código se reflejan inmediatamente (no necesitas reinstalar)

## Comandos Rápidos

```bash
# Configuración inicial (una vez)
cd dia_4/exercises
uv sync

# Ejecutar tests mientras trabajas
uv run pytest tests/bloque_1/ -v                                             # Bloque completo
uv run pytest tests/bloque_1/test_models.py::test_valid_local_source_config_creates_successfully  # Test específico
uv run pytest tests/bloque_2/ -k "normalizer" -v                            # Tests de un concepto
uv run pytest                                                                # Todos los tests

# Verificar código
uv run ruff check src/                           # Verificar estilo
uv run ruff format src/                          # Formatear código

# Coverage
uv run pytest --cov=exercises --cov-report=term-missing
```

## Bloques de Ejercicios

### Bloque 1: Modelado de Datos con Pydantic

**Directorio**: `src/exercises/bloque_1/`  
**Material de referencia**: `dia_4/teoria/01_dataclasses_vs_pydantic.md`

**Ejercicio**: Modelar configuración de un pipeline de limpieza de CSV

**Conceptos que se practican**:
- Pydantic BaseModel
- Field con restricciones (min_length, ge, le)
- Discriminated unions
- @field_validator para normalización
- @model_validator para reglas de negocio
- SecretStr para datos sensibles

**Tests**: 15 tests que verifican validación, discriminated unions, normalización y serialización

### Bloque 2: Composición sobre Herencia

**Directorio**: `src/exercises/bloque_2/`  
**Material de referencia**: `dia_4/teoria/02_protocols_structural_typing.md`

**Ejercicio**: Pipeline de preprocesamiento de texto para NLP

**Conceptos que se practican**:
- Composición sobre herencia
- Protocols como contratos
- Datos como argumentos (no self.data mutable)
- @dataclass(frozen=True) para resultados inmutables
- Separación de lógica en componentes reutilizables

**Tests**: 12 tests que verifican composición, protocols y flujo de datos

### Bloque 3: SRP + DIP

**Directorio**: `src/exercises/bloque_3/`  
**Material de referencia**: `dia_4/teoria/03_solid_principles.md`

**Ejercicio**: Sistema de scoring de reviews de productos

**Conceptos que se practican**:
- Single Responsibility Principle (SRP)
- Dependency Inversion Principle (DIP)
- Inyección de dependencias
- Testing con fakes
- Separación de responsabilidades (carga, análisis, guardado)

**Tests**: 11 tests que verifican SRP, DIP y separación de responsabilidades

### Bloque 4: OCP, LSP, ISP

**Directorio**: `src/exercises/bloque_4/`  
**Material de referencia**: `dia_4/teoria/03_solid_principles.md`

**Ejercicio**: Sistema extensible de métricas para evaluación de modelos

**Conceptos que se practican**:
- Open-Closed Principle (OCP): añadir métricas sin modificar evaluador
- Liskov Substitution Principle (LSP): métricas intercambiables
- Interface Segregation Principle (ISP): protocols segregados
- Composición de métricas
- Extensibilidad sin modificación

**Tests**: 15 tests que verifican OCP, LSP, ISP y extensibilidad

## Solución de Problemas

**Error: `ModuleNotFoundError: No module named 'exercises'`**
- Solución: Ejecuta `uv sync` desde `dia_4/exercises/`

**Error: `ModuleNotFoundError: No module named 'pydantic'`**
- Solución: Ejecuta `uv sync` para instalar Pydantic

**Error: `uv: command not found`**
- Solución: Instala UV siguiendo las instrucciones en el README principal del curso

**Los tests no se ejecutan**
- Verifica que estás en el directorio correcto: `cd dia_4/exercises`
- Ejecuta: `uv sync` para asegurar que todo está instalado

**Quiero usar el entorno virtual manualmente**
```bash
# Activar entorno (opcional, uv run lo hace automáticamente)
# Windows (CMD)
.venv\Scripts\activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate

# Luego puedes usar pytest directamente
pytest tests/test_dataclasses.py
```

## Filosofía de los Ejercicios

Los ejercicios están diseñados para que te concentres en la arquitectura, no en implementar lógica de dominio:

- **helpers.py**: Lógica de dominio ya implementada (no modificar)
- **protocols.py**: Contratos que tus clases deben cumplir (no modificar)
- **<modulo>.py**: Esqueleto con hints en docstrings para implementar
- **conftest.py**: Fixtures con datos de prueba
- **test_<modulo>.py**: Tests completos ordenados de simple a complejo

Cada bloque tiene su propio README con tips paso a paso.

## Recursos

- **UV**: https://docs.astral.sh/uv/
- **pytest**: https://docs.pytest.org/
- **Pydantic**: https://docs.pydantic.dev/
- **Dataclasses**: https://docs.python.org/3/library/dataclasses.html
- **Protocols (PEP 544)**: https://peps.python.org/pep-0544/
- **SOLID Principles**: https://en.wikipedia.org/wiki/SOLID
- **Material de referencia**: `dia_4/teoria/`

## Soluciones

Las soluciones están en `.instructor/DIA_4_SOLUCIONES_*.py` para referencia del instructor.

## Criterios de Éxito

- [ ] Todos los tests pasan
- [ ] Código pasa ruff sin warnings
- [ ] Type hints correctos en todas las funciones
- [ ] Uso apropiado de Pydantic con Field y validators (Bloque 1)
- [ ] Composición sin herencia (Bloque 2)
- [ ] Separación de responsabilidades clara (Bloque 3)
- [ ] Sistema extensible sin modificar código existente (Bloque 4)
- [ ] Protocols usados como contratos
- [ ] Inyección de dependencias correcta
- [ ] Dataclasses inmutables donde corresponde

## Notas sobre Dificultad

Los ejercicios del día 4 están diseñados para ser progresivos:

- **Bloque 1**: Nivel básico-medio (Pydantic con validación)
- **Bloque 2**: Nivel medio (Composición y Protocols)
- **Bloque 3**: Nivel medio (SRP y DIP)
- **Bloque 4**: Nivel medio-avanzado (OCP, LSP, ISP)

Cada bloque es independiente pero los conceptos se acumulan. Se recomienda completarlos en orden.

Si encuentras dificultades, revisa primero el README del bloque y luego el material de referencia en `dia_4/teoria/`.
