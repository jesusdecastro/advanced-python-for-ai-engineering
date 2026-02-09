# Guía del Proyecto: CSV Data Cleaner

## Visión General

Construirás una herramienta para limpiar y validar archivos CSV, detectando problemas y aplicando correcciones automáticas. Perfecto para aplicar validación, transformaciones y reporting.

---

## Objetivos de Aprendizaje

Al finalizar este proyecto, habrás aplicado:
- Validación de datos con múltiples estrategias
- Transformaciones de datos limpias
- Generación de reportes detallados
- Testing exhaustivo con datos problemáticos
- Diseño extensible con validadores

---

## Estructura Sugerida del Proyecto

```
csvclean/
 src/
    csvclean/
        __init__.py
        readers/
           __init__.py
           csv_reader.py
        validators/
           __init__.py
           base.py
           null_validator.py
           type_validator.py
           duplicate_validator.py
        cleaners/
           __init__.py
           base.py
           null_cleaner.py
           duplicate_cleaner.py
        transformers/
           __init__.py
           normalizer.py
           type_converter.py
        reporters/
           __init__.py
           cleaning_report.py
        models/
           __init__.py
           config.py
        cli.py
 tests/
    conftest.py
    fixtures/
       dirty_data.csv
       expected_clean.csv
    test_validators.py
    test_cleaners.py
    test_transformers.py
 examples/
    sample_dirty.csv
    clean_example.py
 pyproject.toml
 README.md
```

---

## Roadmap Día a Día

### Día 1: Fundamentos
**Objetivo:** Lectura y estructura básica

**Tareas:**
- Crear estructura de carpetas con src layout
- Configurar pyproject.toml (pandas)
- Implementar lectura básica de CSV
- Detectar automáticamente delimitadores (`,` `;` `\t`)

**Checkpoint:** Puedes leer CSVs con diferentes delimitadores

---

### Día 2: Código Pythónico
**Objetivo:** Procesamiento eficiente

**Tareas:**
- Implementar generador para procesar filas una por una
- Usar comprehensions para filtrar filas problemáticas
- Decorador @track_changes para logging de transformaciones
- Context manager para archivos

**Tips:**
- Para CSVs grandes, procesa línea por línea
- El decorador debe registrar qué cambios se hicieron
- Comprehensions son perfectas para filtrado rápido

**Checkpoint:** Procesas CSVs grandes sin problemas de memoria

---

### Día 3: Código Limpio
**Objetivo:** Validación y limpieza robusta

**Tareas:**
- Funciones pequeñas: detect_nulls, fix_types, remove_duplicates
- Excepciones custom: InvalidCSVError, ValidationError, CleaningError
- Docstrings completos con ejemplos
- Validación de cada transformación

**Tips:**
- Cada función de limpieza debe hacer UNA cosa
- Las excepciones deben ser descriptivas
- Documenta qué problemas detecta cada validador

**Checkpoint:** El código maneja CSVs problemáticos sin crashear

---

### Día 4: Diseño
**Objetivo:** Sistema extensible de validadores y cleaners

**Tareas:**
- ABC BaseValidator con método abstracto validate()
- Implementar NullValidator, TypeValidator, DuplicateValidator
- ABC BaseCleaner con método abstracto clean()
- Modelos Pydantic: CleaningConfig(required_columns, type_mapping)

**Tips:**
- Cada validador detecta UN tipo de problema
- Los cleaners aplican correcciones específicas
- Pydantic valida la configuración de limpieza
- Composición: DataCleaner compone múltiples Validators y Cleaners

**Checkpoint:** Puedes añadir un nuevo validador sin modificar código existente

---

### Día 5: Testing y Optimización
**Objetivo:** Tests exhaustivos y optimización

**Tareas:**
- Crear fixtures con CSVs problemáticos (nulls, duplicados, tipos incorrectos)
- Tests para cada validador y cleaner
- Tests de transformaciones
- Optimizar con pandas para operaciones vectorizadas

**Tips:**
- Los fixtures deben cubrir todos los casos edge
- Verifica que las transformaciones son correctas
- pandas es excelente para operaciones en columnas completas
- Tests deben verificar que el reporte es correcto

**Checkpoint:** 80%+ cobertura y transformaciones correctas

---

### Día 6: Integración
**Objetivo:** CLI y reportes detallados

**Tareas:**
- CLI: csvclean clean --input dirty.csv --output clean.csv --report
- Generar reporte de limpieza (qué se cambió y por qué)
- El reporte debe incluir: problemas detectados, correcciones aplicadas, estadísticas
- README con ejemplos

**Tips:**
- El CLI debe ser simple pero completo
- El reporte debe ser útil: qué filas tenían problemas, qué se corrigió
- Incluye ejemplos de CSVs problemáticos

**Checkpoint:** Puedes limpiar un CSV y entender qué se cambió

---

## Funcionalidades Mínimas Requeridas

### Lectura
- [ ] Leer CSV con detección automática de delimitador
- [ ] Detectar encoding automáticamente
- [ ] Manejo de headers
- [ ] Soporte para archivos grandes (generadores)

### Validación
- [ ] Detectar valores nulos/vacíos
- [ ] Detectar tipos incorrectos
- [ ] Detectar duplicados (filas completas)
- [ ] Validar columnas requeridas

### Limpieza
- [ ] Eliminar/imputar valores nulos
- [ ] Convertir tipos de datos
- [ ] Eliminar duplicados
- [ ] Normalizar strings (trim, lowercase)

### Transformaciones
- [ ] Normalización de texto
- [ ] Conversión de tipos
- [ ] Formateo de fechas
- [ ] Eliminación de caracteres especiales

### Reportes
- [ ] Problemas detectados por tipo
- [ ] Correcciones aplicadas
- [ ] Estadísticas antes/después
- [ ] Filas problemáticas (sample)

---

## Criterios de Evaluación

1. **Estructura y Organización** (20%)
   - Src layout correcto
   - Módulos bien separados
   - Configuración de herramientas

2. **Calidad del Código** (30%)
   - Validación robusta
   - Funciones pequeñas
   - Docstrings completos
   - Manejo de errores

3. **Diseño OOP** (20%)
   - ABCs para validators y cleaners
   - Modelos Pydantic
   - Composición
   - Extensibilidad

4. **Testing** (20%)
   - Fixtures con datos problemáticos
   - Tests de validación
   - Tests de limpieza
   - 80%+ cobertura

5. **Documentación y Usabilidad** (10%)
   - README completo
   - CLI intuitivo
   - Reportes útiles

---

## Errores Comunes a Evitar

 **Modificar el CSV original**
 Siempre escribe en un archivo nuevo

 **Perder datos sin avisar**
 Reporta qué se eliminó y por qué

 **Validadores que hacen limpieza**
 Separa detección de corrección

 **Limpieza sin configuración**
 Permite configurar qué limpiar y cómo

 **Reportes vacíos o inútiles**
 Reportes detallados y accionables

 **No manejar encodings**
 Detecta y maneja diferentes encodings

---

## Recursos Útiles

- Documentación de pandas para CSV
- Documentación de csv module (stdlib)
- Patrones de validación de datos
- Ejemplos de CSVs problemáticos
- Técnicas de imputación de datos

---

## Preguntas Frecuentes

**P: ¿Debo usar pandas o csv module?**
R: Ambos. csv module para lectura línea por línea, pandas para operaciones vectorizadas.

**P: ¿Cómo manejo valores nulos?**
R: Depende del contexto. Ofrece opciones: eliminar fila, imputar con media/mediana, valor por defecto.

**P: ¿Qué hago con duplicados?**
R: Detecta y reporta. Permite configurar: eliminar todos, mantener primero, mantener último.

**P: ¿Cómo valido tipos?**
R: Intenta convertir. Si falla, es tipo incorrecto. Reporta y permite configurar acción.

**P: ¿El reporte debe ser HTML?**
R: No necesariamente. JSON o texto plano está bien. Lo importante es que sea útil.

---

## Checklist Final

- [ ] Estructura src layout
- [ ] pyproject.toml configurado
- [ ] Detección automática de delimitador
- [ ] ABCs para validators y cleaners
- [ ] Modelos Pydantic
- [ ] Validación completa
- [ ] Limpieza configurable
- [ ] Tests con fixtures
- [ ] 80%+ cobertura
- [ ] CLI funcional
- [ ] Reporte detallado
- [ ] README con ejemplos
- [ ] Código pasa ruff

---

¡Adelante! Un buen data cleaner es la base de cualquier análisis de calidad.
