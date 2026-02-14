# Guía de Evaluación — Proyecto Integrador

## Módulo: Advanced Python para AI Engineering

---

## Qué se Evalúa (y Qué No)

Este proyecto evalúa que sabéis **diseñar y estructurar código Python profesional**. No se evalúa que el pipeline haga algo espectacular — se evalúa **cómo** está construido.

Un proyecto sencillo con arquitectura limpia puntúa más que un proyecto ambicioso con código desordenado.

---

## Distribución de la Nota

| Categoría | Peso | En una frase |
|---|---|---|
| Código y arquitectura | 35% | ¿Aplicáis lo aprendido en el código? |
| Calidad y tooling | 20% | ¿Ruff, Pyright y tests pasan? |
| Defensa en equipo | 25% | ¿Cada persona entiende lo que hizo y por qué? |
| Documentación | 10% | ¿README claro, docstrings, entrega correcta? |
| Ejecución funcional | 10% | ¿Funciona al primer intento? |

---

## 1. Código y Arquitectura (35%)

Esta es la categoría más importante. Se evalúa que el código refleje los conceptos de los 5 días del módulo.

### 1.1 Estructura de proyecto y tooling (Día 1)

**Pregunta clave**: ¿El proyecto está montado como un paquete Python profesional?

- `src/` layout con `pyproject.toml` correctamente configurado
- Gestión de dependencias con `uv`
- Módulos e imports limpios (no imports circulares, no `import *`)
- Type hints en todas las firmas públicas

**Lo que resta puntos**: scripts sueltos sin estructura de paquete, imports desordenados, `requirements.txt` en vez de `pyproject.toml`.

### 1.2 Clean Code y naming (Días 2-3)

**Pregunta clave**: ¿Un compañero nuevo entendería este código sin que se lo expliquéis?

- Nombres descriptivos en variables, funciones y clases
- Funciones cortas con una responsabilidad (idealmente < 20 líneas)
- DRY: sin bloques de código duplicados
- Error handling con excepciones específicas y logging con contexto
- Magic numbers extraídos a constantes con nombre
- Defensive programming: validación de inputs en puntos de entrada

**Lo que resta puntos**: variables de una letra, funciones de 50+ líneas, bloques `except Exception`, `print()` en vez de logging, código duplicado, números mágicos sueltos.

### 1.3 Modelado de datos (Día 4 — Bloque 1)

**Pregunta clave**: ¿Los datos que vienen de fuera pasan por Pydantic?

- Configuraciones, inputs de usuario, JSONs → `BaseModel` con validación
- Datos internos simples (resultados, DTOs) → `@dataclass(frozen=True)`
- Usáis `Field()` con restricciones donde tiene sentido (`gt=0`, `min_length=1`)
- Si hay variantes (ej: fuente local vs URL), usáis discriminated unions
- Los API keys o secretos usan `SecretStr`, no `str` plano

**Lo que resta puntos**: dicts sueltos por todo el código sin schema, validación manual con if/elif dispersa, mezclar Pydantic y dataclass sin criterio.

### 1.4 Separación estructura de datos vs objeto (Días 3-4)

**Pregunta clave**: ¿Las estructuras de datos solo tienen datos, y los objetos solo tienen comportamiento?

- Las estructuras de datos (`dataclass`, Pydantic) exponen atributos y no tienen lógica de negocio
- Los objetos (clases con comportamiento) ocultan estado interno y exponen métodos
- Los datos fluyen como argumentos entre funciones/objetos — no como `self.data` mutado

**Lo que resta puntos**: clases que son mitad datos mitad lógica, `self.data` que se modifica en 5 métodos diferentes, `@property` con cálculos de negocio en un dataclass.

### 1.5 Composición, Protocols y SOLID (Día 4 — Bloques 2, 3, 4)

**Pregunta clave**: Si mañana quiero cambiar UNA pieza, ¿cuántas clases toco?

- El pipeline se construye combinando piezas independientes (composición)
- Los contratos entre piezas se definen con `typing.Protocol`
- Cada clase tiene una responsabilidad — una razón para cambiar (SRP)
- Las dependencias se inyectan como Protocols, no se instancian dentro (DIP)
- Añadir un nuevo formato/fuente/estrategia no requiere modificar código existente (OCP)
- No hay herencia de más de 2 niveles, no hay `raise NotImplementedError` (LSP/ISP)

**Lo que resta puntos**: God class que hace ingestión + procesamiento + guardado, jerarquías de herencia profundas, dependencias hardcoded, `raise NotImplementedError` en clases base.

### 1.6 Testing (Día 5)

**Pregunta clave**: ¿Los tests verifican comportamiento real o solo que "no falla"?

- Tests unitarios para cada pieza individual
- Estructura Arrange-Act-Assert clara en cada test
- Fixtures para datos reutilizables
- `@pytest.mark.parametrize` para probar múltiples casos
- Mocking/fakes para dependencias externas (archivos, APIs)
- Tests de casos de error: datos inválidos, archivos que no existen, etc.

**Lo que resta puntos**: tests sin asserts, tests que dependen de archivos del disco duro del autor, un solo test "que corre todo", sin tests de error.

---

## 2. Calidad y Tooling (20%)

Esto es lo más mecánico y lo más fácil de aprobar. No hay excusa para perder puntos aquí.

### Lo que tiene que pasar

```bash
uv run ruff check .                              # 0 errores
uv run pyright                                   # 0 errores
uv run pytest --cov --cov-fail-under=80          # Tests pasan, ≥80% cobertura
```

### Ruff

Usad la configuración que os proporcionamos en el `pyproject.toml`. No la modifiquéis para quitar reglas. Si ruff se queja, arreglad el código.

### Pyright

Todas las funciones y métodos públicos deben tener type hints. Pyright en modo `basic` no debería dar errores. Si os sale un error que no entendéis, preguntad antes de ignorarlo.

### Tests y cobertura

**El 80% de cobertura es el mínimo para aprobar.** Intentad llegar lo más lejos que podáis — un proyecto con 90%+ demuestra que habéis testeado en serio, no solo para cumplir el número.

Pero cobertura no es todo. Los tests deben verificar algo real:

```python
# ❌ Esto pasa cobertura pero no verifica NADA
def test_pipeline_runs():
    pipeline.run("data.csv")  # Sin assert

# ✅ Esto verifica comportamiento real
def test_pipeline_returns_cleaned_data():
    result = pipeline.run("data.csv")
    assert result.rows_after_cleaning <= result.rows_original
    assert result.rows_after_cleaning > 0
```

**Tipos de tests que deberíais tener**:

- Tests de modelos Pydantic: validación correcta e incorrecta
- Tests de cada pieza individual: el loader carga, el cleaner limpia, etc.
- Tests del pipeline completo: las piezas trabajan juntas
- Tests con fakes inyectados: verificar que la composición y DIP funcionan
- Tests de error: datos inválidos, archivos que no existen, campos que faltan

**Un buen indicador**: si al romper una función a propósito (cambiar un `>` por un `<`), algún test falla. Si ninguno falla, vuestros tests no están verificando nada útil.

---

## 3. Defensa en Equipo (25%)

### Formato

Cada equipo tiene 20-25 minutos:

| Fase | Tiempo | Qué hacéis |
|---|---|---|
| Presentación | 8 min | El equipo presenta: qué hace el proyecto, cómo está estructurado, decisiones de diseño |
| Demo en vivo | 4 min | Ejecutáis: `uv sync`, `ruff`, `pyright`, `pytest`, y corréis el pipeline |
| Preguntas individuales | 8-10 min | Cada persona responde sobre su parte |

### Cómo prepararse

Cada persona debe poder:

1. **Explicar qué hizo y por qué** — no solo "qué" sino "por qué esta decisión y no otra"
2. **Nombrar los conceptos del curso** — si usaste composición, saberlo decir. Si aplicaste SRP, identificarlo
3. **Responder a un escenario** — "Si mañana quiero añadir soporte para Parquet, ¿qué cambio?" Demostrar que la arquitectura lo permite

### Ejemplos de preguntas que se harán

**Sobre Día 1-2 (estructura y setup)**:
- "¿Por qué usáis `src/` layout y no poner el código directamente en la raíz?"
- "¿Qué pasa si alguien clona el repo y hace `uv sync`? ¿Funciona sin más pasos?"

**Sobre Día 3 (Clean Code)**:
- "¿Por qué esta excepción es custom y no usáis `ValueError` directamente?"
- "¿Qué nivel de logging usáis aquí y por qué?"
- "¿Qué información tendríais en los logs si esto falla a las 3 AM?"

**Sobre Día 4 (arquitectura)**:
- "¿Por qué esta clase es un `BaseModel` y esta otra un `dataclass`?"
- "¿Cuántas razones de cambio tiene esta clase? ¿Cuáles son?"
- "¿Qué principio SOLID aplicáis aquí?"
- "Si sustituyo este loader por otro que lee de una API, ¿qué clases tengo que modificar?"

**Sobre Día 5 (testing)**:
- "Enséñame un test que verifique que tu pieza funciona en aislamiento"
- "¿Por qué usáis un fake aquí en vez del componente real?"
- "¿Qué pasa si comento este assert? ¿El test sigue siendo útil?"

**Pregunta transversal**:
- "¿Qué mejorarías de este trozo de código si tuvieras más tiempo?"

### Lo que resta puntos en la defensa

- No poder explicar código que supuestamente escribiste
- Usar solo lenguaje genérico ("está bien estructurado") sin nombrar conceptos concretos (SRP, composición, Protocol, DIP)
- No poder responder qué cambiarías ante un escenario nuevo

---

## 4. Documentación (10%)

### README.md

Mínimo que debe tener:

```markdown
# Nombre del Proyecto

Breve descripción de qué hace.

## Instalación

uv sync

## Uso

uv run python -m nombre_paquete [argumentos]

## Estructura del Proyecto

src/
├── nombre_paquete/
│   ├── models.py        # Modelos de datos (Pydantic/dataclass)
│   ├── loaders.py       # Carga de datos
│   ├── processors.py    # Lógica de procesamiento
│   └── pipeline.py      # Orquestador
tests/
└── ...

## Decisiones de Diseño

- Usamos Pydantic para X porque...
- Separamos loader y processor porque... (SRP)
- El pipeline recibe las piezas por inyección porque... (DIP)

## Tests

uv run pytest --cov
```

La sección de "Decisiones de Diseño" es la más importante. Demuestra que las decisiones fueron conscientes.

### Docstrings

Todas las clases y funciones públicas deben tener docstring en formato Sphinx. No hace falta que sean largos:

```python
class CSVLoader:
    """Carga datos desde archivos CSV. Cumple el Protocol DataLoader."""

    def load(self, path: str) -> pd.DataFrame:
        """Lee un CSV y devuelve un DataFrame validado.

        :param path: Ruta al archivo CSV.
        :raises FileNotFoundError: Si el archivo no existe.
        :raises ValueError: Si el archivo está vacío.
        """
```

### Entrega

- **Preferido**: Repositorio en GitHub con commits descriptivos (no un solo commit con todo)
- **Alternativa**: ZIP con la estructura de proyecto completa

---

## 5. Ejecución Funcional (10%)

El proyecto debe funcionar al ejecutar estos comandos, en este orden, sin intervención manual:

```bash
uv sync                                  # Instala dependencias
uv run ruff check .                      # Linting
uv run pyright                           # Type checking
uv run pytest                            # Tests
uv run python -m nombre_paquete [args]   # Ejecución
```

Si alguno falla, se pierde ese punto. **Verificadlo antes de entregar.**

---

## Checklist Pre-Entrega

Antes de entregar, verificad que podéis marcar todo:

### Estructura y setup (Día 1)
- [ ] `src/` layout con `pyproject.toml` configurado
- [ ] `uv sync` instala sin errores
- [ ] Imports limpios, sin circulares ni `import *`

### Clean Code (Días 2-3)
- [ ] Nombres descriptivos en variables, funciones y clases
- [ ] Funciones cortas con una responsabilidad
- [ ] Excepciones específicas con contexto, no `except Exception`
- [ ] Logging con niveles apropiados, no `print()`
- [ ] Sin magic numbers — extraídos a constantes
- [ ] Sin código duplicado

### Arquitectura (Día 4)
- [ ] Datos de fuera (configs, inputs) validados con Pydantic `BaseModel`
- [ ] Resultados internos como `@dataclass(frozen=True)` o Pydantic
- [ ] Cada clase una responsabilidad clara
- [ ] Piezas compuestas con inyección de dependencias, no herencia
- [ ] Al menos un Protocol que define un contrato
- [ ] Datos fluyen como argumentos, no como `self.data` mutado

### Testing (Día 5)
- [ ] `uv run pytest --cov` → todos pasan, ≥80% cobertura
- [ ] Tests con asserts significativos
- [ ] Tests de cada pieza individual + pipeline completo
- [ ] Al menos un test con datos inválidos

### Tooling
- [ ] `uv run ruff check .` → 0 errores
- [ ] `uv run pyright` → 0 errores

### Documentación
- [ ] README con instalación, uso, estructura y decisiones de diseño
- [ ] Docstrings en clases y funciones públicas (formato Sphinx)
- [ ] Entregado en GitHub o ZIP limpio

### Defensa
- [ ] Cada persona sabe explicar su parte con vocabulario técnico
- [ ] Cada persona puede conectar su código con conceptos del curso
- [ ] Habéis practicado la demo en vivo al menos una vez

---

## Dónde Concentrar el Esfuerzo

Si tenéis poco tiempo, priorizad en este orden:

1. **Que funcione** (10%) — Si no arranca, todo lo demás no se puede evaluar
2. **Ruff + Pyright + Tests** (20%) — Son puntos "gratis" si los corréis durante el desarrollo, no al final. Acostumbraos a ejecutar `ruff` y `pyright` después de cada cambio
3. **Arquitectura** (35%) — Es el grueso de la nota. Un proyecto sencillo bien diseñado supera a uno complejo mal estructurado
4. **Defensa** (25%) — Practicad explicar vuestro código. Si no podéis explicar por qué hicisteis algo, la nota baja aunque el código sea bueno
5. **Documentación** (10%) — README + docstrings. No os costará más de 30 minutos si lo hacéis al final