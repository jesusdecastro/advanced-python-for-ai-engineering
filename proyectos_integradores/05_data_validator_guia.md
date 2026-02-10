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

## Diseñando la Estructura del Proyecto

### 🤔 Preguntas Clave para Diseñar tu Estructura

Antes de crear carpetas, piensa en estas preguntas:

**1. ¿Qué hace mi framework de validación?**
- Valida datos tabulares (DataFrames de pandas)
- Aplica reglas de validación (tipo, rango, formato, custom)
- Genera reportes detallados de errores
- Opcionalmente corrige errores automáticamente
- Permite definir reglas custom por el usuario

**2. ¿Qué tipos de validaciones necesito?**
- **Tipo**: ¿Esta columna es int/float/str?
- **Rango**: ¿Los valores están entre min y max?
- **Formato**: ¿Los emails son válidos? ¿Las fechas tienen el formato correcto?
- **Nulos**: ¿Hay valores faltantes donde no deberían?
- **Custom**: Reglas específicas del negocio
- Cada tipo necesita su propia lógica

**3. ¿Cómo quiero que se use?**
```python
# ¿Así?
validator = DataValidator()
validator.add_rule(TypeRule("age", int))
validator.add_rule(RangeRule("age", 0, 120))
result = validator.validate(df)

# ¿O así?
rules = load_rules("rules.yaml")
result = validate(df, rules)
```

### 💡 Pistas de Organización

**Sobre validadores:**
- Cada validador verifica UNA cosa (tipo, rango, formato)
- Todos devuelven el mismo tipo de resultado: ValidationResult(is_valid, errors)
- Hint: Clase base abstracta con método `validate(data)`
- ¿Cómo pasas parámetros a cada validador? (ej: RangeValidator necesita min/max)

**Sobre reglas:**
- Una regla combina: columna + validador + parámetros
- Ejemplo: "La columna 'age' debe ser int entre 0 y 120"
- ¿Cómo representas esto? ¿Clase? ¿Diccionario? ¿Pydantic model?
- El usuario debe poder definir reglas en YAML/JSON

**Sobre el rule engine:**
- Aplica múltiples reglas a un DataFrame
- Recolecta todos los errores
- ¿Validas todas las reglas o paras en el primer error?
- ¿Validas fila por fila o columna por columna?

**Sobre reportes:**
- El reporte debe mostrar: qué regla falló, en qué fila, qué valor, por qué
- Formatos: texto, JSON, HTML
- Hint: Un modelo Pydantic para ValidationResult
- ¿Cómo agregas errores por tipo?

**Sobre corrección automática:**
- Algunos errores son corregibles: tipo incorrecto → convertir, null → imputar
- Otros no: valor fuera de rango → ¿qué haces?
- Hint: Patrón Strategy para diferentes estrategias de corrección
- ¿Cómo relacionas un validador con su corrector?

**Sobre integración con pandas:**
- Trabajas con DataFrames, no con listas
- pandas tiene métodos útiles: `df.dtypes`, `df.isnull()`, `df.apply()`
- ¿Validas el DataFrame completo o por chunks para eficiencia?

### 🎯 Checklist de Estructura

Antes de empezar a codear, asegúrate de tener:
- [ ] Carpeta `src/` con tu paquete principal
- [ ] Módulo/paquete para validadores (uno por tipo de validación)
- [ ] Módulo/paquete para el rule engine (aplica reglas)
- [ ] Módulo/paquete para modelos de datos (ValidationResult, Rule)
- [ ] Módulo/paquete para reportes (diferentes formatos)
- [ ] Módulo/paquete para correctores (opcional)
- [ ] Carpeta `tests/` con fixtures de datos inválidos
- [ ] Carpeta `examples/` con reglas de ejemplo en YAML
- [ ] `pyproject.toml` con pandas, pydantic
- [ ] `README.md`

### 🚀 Enfoque Recomendado

1. **Empieza con un validador**: Implementa TypeValidator
2. **Define tu modelo de resultado**: ValidationResult con Pydantic
3. **Añade más validadores**: Range, Format, Null
4. **Crea el rule engine**: Aplica múltiples reglas a un DataFrame
5. **Añade reportes**: Genera reportes legibles
6. **Añade corrección**: Implementa correctores automáticos

**Pregunta guía**: "Si necesito validar que una columna 'email' contiene emails válidos, ¿dónde va ese código?"

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

 **Validadores que modifican datos**
 Separa validación de corrección

 **Reportes genéricos: "hay errores"**
 Reportes específicos: "fila 5, columna 'age': valor -10 fuera de rango [0, 120]"

 **Validación lenta fila por fila**
 Usa pandas vectorización cuando sea posible

 **Rule engine inflexible**
 Permite reglas custom con expresiones

 **Corrección sin reportar qué se cambió**
 Reporta todas las correcciones aplicadas

 **No manejar tipos de pandas (datetime64, category)**
 Soporta todos los tipos de pandas

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
