# Guía del Proyecto: Data Validator Library

## Visión General

Construirás un framework de validación de datos tabulares con reglas custom, reporting detallado y corrección automática opcional. Ideal para data quality en pipelines de ML.

---

## Objetivos de Aprendizaje

Al finalizar este proyecto, habrás aplicado:
- Sistema extensible de validadores
- Rule engine para reglas custom
- Integración con pandas
- Reporting detallado de errores
- Testing con datos problemáticos
- Corrección automática opcional

---

## Estructura Sugerida del Proyecto

```
dataval/
├── src/
│   └── dataval/
│       ├── __init__.py
│       ├── validators/
│       │   ├── __init__.py
│       │   ├── base.py
│       │   ├── type_validator.py
│       │   ├── range_validator.py
│       │   ├── format_validator.py
│       │   └── custom_validator.py
│       ├── rules/
│       │   ├── __init__.py
│       │   └── rule_engine.py
│       ├── reporters/
│       │   ├── __init__.py
│       │   ├── report.py
│       │   └── html_reporter.py
│       ├── correctors/
│       │   ├── __init__.py
│       │   ├── type_coercer.py
│       │   └── imputer.py
│       ├── models/
│       │   ├── __init__.py
│       │   └── validation_result.py
│       └── cli.py
├── tests/
│   ├── conftest.py
│   ├── fixtures/
│   │   ├── invalid_data.csv
│   │   └── rules.yaml
│   ├── test_validators.py
│   ├── test_rules.py
│   ├── test_correctors.py
│   └── test_reporters.py
├── examples/
│   ├── sample_data.csv
│   ├── validation_rules.yaml
│   └── validate_example.py
├── pyproject.toml
└── README.md
```

---

## Roadmap Día a Día

### Día 1: Fundamentos
**Objetivo:** Validadores básicos

**Tareas:**
- Crear estructura de carpetas con src layout
- Configurar pyproject.toml (pandas, pydantic)
- Implementar validadores básicos: tipo, rango, nulos
- Validar DataFrames de pandas

**Checkpoint:** Puedes validar tipos y rangos en un DataFrame

---

### Día 2: Código Pythónico
**Objetivo:** Procesamiento eficiente

**Tareas:**
- Generadores para validar DataFrames fila por fila (yield validation_result)
- Comprehensions para filtrar errores por tipo
- Decorador @validate_input para funciones
- Lazy evaluation de reglas complejas

**Tips:**
- Para DataFrames grandes, valida por chunks
- El generador debe hacer yield de ValidationResult por fila
- El decorador @validate_input aplica validación automática

**Checkpoint:** Puedes validar DataFrames grandes eficientemente

---

### Día 3: Código Limpio
**Objetivo:** Validación robusta y reporting

**Tareas:**
- Funciones pequeñas: validate_dataframe → check_types, check_ranges, check_nulls
- Excepciones custom: ValidationError, RuleError, CorrectionError
- Docstrings completos con ejemplos
- Reporting detallado: qué, dónde, por qué

**Tips:**
- Cada validador debe reportar errores claramente
- Los reportes deben ser accionables
- Documenta qué valida cada validador y cómo

**Checkpoint:** Los reportes indican exactamente qué está mal y dónde

---

### Día 4: Diseño
**Objetivo:** Sistema extensible de validadores

**Tareas:**
- ABC BaseValidator con método abstracto validate()
- Implementar TypeValidator, RangeValidator, FormatValidator
- Modelos Pydantic: ValidationResult(is_valid, errors, warnings)
- Rule engine para reglas custom

**Tips:**
- Cada validador es independiente y reutilizable
- Pydantic valida la configuración de reglas
- El rule engine permite expresiones como "age > 18 AND age < 100"
- Composición: DataValidator compone múltiples Validators

**Checkpoint:** Puedes añadir un nuevo validador sin modificar código existente

---

### Día 5: Testing y Optimización
**Objetivo:** Tests exhaustivos y optimización

**Tareas:**
- Crear fixtures con DataFrames inválidos (todos los tipos de errores)
- Tests para cada validador
- Tests de corrección automática
- Optimizar validación con pandas vectorización

**Tips:**
- Los fixtures deben cubrir todos los casos edge
- Tests de corrección: verifica que los datos corregidos son válidos
- pandas permite validar columnas completas de una vez
- Verifica que el reporting es correcto

**Checkpoint:** 80%+ cobertura y validación correcta

---

### Día 6: Integración
**Objetivo:** CLI y reportes HTML

**Tareas:**
- CLI: dataval validate --input data.csv --rules rules.yaml
- CLI: dataval correct --input data.csv --output clean.csv --rules rules.yaml
- Generar reportes HTML con errores detallados
- README con ejemplos

**Tips:**
- El CLI debe soportar validación y corrección
- Los reportes HTML deben ser legibles y útiles
- Incluye ejemplos de reglas en YAML

**Checkpoint:** Puedes validar datos y obtener un reporte útil

---

## Funcionalidades Mínimas Requeridas

### Validadores
- [ ] TypeValidator (int, float, string, date)
- [ ] RangeValidator (min, max para numéricos)
- [ ] FormatValidator (regex para strings)
- [ ] NullValidator (columnas requeridas)
- [ ] UniqueValidator (valores únicos)

### Rule Engine
- [ ] Reglas desde YAML/JSON
- [ ] Expresiones lógicas (AND, OR, NOT)
- [ ] Comparaciones (>, <, ==, !=, in)
- [ ] Reglas por columna

### Reporting
- [ ] Errores por tipo
- [ ] Errores por fila
- [ ] Estadísticas de validación
- [ ] Reporte HTML legible

### Corrección (Opcional)
- [ ] Coerción de tipos
- [ ] Imputación de nulos (media, mediana, moda)
- [ ] Corrección de formatos
- [ ] Eliminación de duplicados

### Integración pandas
- [ ] Validar DataFrames
- [ ] Validar Series
- [ ] Retornar DataFrame con errores marcados
- [ ] Optimización vectorizada

---

## Criterios de Evaluación

1. **Estructura y Organización** (20%)
   - Src layout correcto
   - Módulos bien separados
   - Configuración de herramientas

2. **Calidad del Código** (30%)
   - Validadores robustos
   - Funciones pequeñas
   - Docstrings completos
   - Manejo de errores

3. **Diseño OOP** (20%)
   - ABCs para validadores
   - Modelos Pydantic
   - Rule engine extensible
   - Composición

4. **Testing** (20%)
   - Fixtures con datos inválidos
   - Tests de validación
   - Tests de corrección
   - 80%+ cobertura

5. **Documentación y Usabilidad** (10%)
   - README completo
   - CLI intuitivo
   - Reportes útiles

---

## Errores Comunes a Evitar

❌ **Validadores que modifican datos**
✅ Separa validación de corrección

❌ **Reportes genéricos: "hay errores"**
✅ Reportes específicos: "fila 5, columna 'age': valor -10 fuera de rango [0, 120]"

❌ **Validación lenta fila por fila**
✅ Usa pandas vectorización cuando sea posible

❌ **Rule engine inflexible**
✅ Permite reglas custom con expresiones

❌ **Corrección sin reportar qué se cambió**
✅ Reporta todas las correcciones aplicadas

❌ **No manejar tipos de pandas (datetime64, category)**
✅ Soporta todos los tipos de pandas

---

## Recursos Útiles

- Documentación de pandas para validación
- Patrones de validación de datos
- Documentación de Pydantic
- Ejemplos de rule engines
- Técnicas de imputación de datos

---

## Preguntas Frecuentes

**P: ¿Debo implementar corrección automática?**
R: Es opcional pero recomendado. Al menos coerción de tipos e imputación básica.

**P: ¿Cómo implemento el rule engine?**
R: Parsea expresiones simples o usa eval con cuidado. Alternativamente, usa una librería como `simpleeval`.

**P: ¿Qué formato usar para reglas?**
R: YAML es intuitivo. JSON también funciona. Lo importante es que sea legible.

**P: ¿Cómo optimizo validación de DataFrames grandes?**
R: Usa pandas vectorización. Valida columnas completas, no fila por fila.

**P: ¿Los reportes deben ser HTML?**
R: No necesariamente. JSON o texto plano está bien. Lo importante es que sean útiles.

---

## Checklist Final

- [ ] Estructura src layout
- [ ] pyproject.toml configurado
- [ ] Validadores básicos implementados
- [ ] ABCs para validadores
- [ ] Modelos Pydantic
- [ ] Rule engine funcional
- [ ] Reporting detallado
- [ ] Corrección automática (opcional)
- [ ] Tests con fixtures
- [ ] 80%+ cobertura
- [ ] CLI funcional
- [ ] Integración con pandas
- [ ] README con ejemplos
- [ ] Código pasa ruff

---

¡Adelante! La validación de datos es crítica para ML de calidad.
