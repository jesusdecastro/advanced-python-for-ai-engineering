# Guía del Proyecto: Text Processing Toolkit

## Visión General

Construirás una librería para procesamiento de texto con análisis básico, transformaciones y extracción de información. Perfecto para aplicar todos los principios sin dependencias complejas (solo stdlib).

---

## Objetivos de Aprendizaje

Al finalizar este proyecto, habrás aplicado:
- Procesamiento de texto con regex
- Análisis estadístico de texto
- Generadores para archivos grandes
- Diseño extensible con ABCs
- Testing exhaustivo
- Optimización con pandas (opcional)

---

## Estructura Sugerida del Proyecto

```
textkit/
 src/
    textkit/
        __init__.py
        readers/
           __init__.py
           base.py
           txt_reader.py
           markdown_reader.py
        analyzers/
           __init__.py
           word_counter.py
           frequency_analyzer.py
           statistics.py
        transformers/
           __init__.py
           normalizer.py
           cleaner.py
           tokenizer.py
        extractors/
           __init__.py
           email_extractor.py
           url_extractor.py
           date_extractor.py
        models/
           __init__.py
           text_document.py
        cli.py
 tests/
    conftest.py
    fixtures/
       sample_text.txt
       sample_markdown.md
    test_analyzers.py
    test_transformers.py
    test_extractors.py
 examples/
    sample_document.txt
    analyze_example.py
 pyproject.toml
 README.md
```

---

## Roadmap Día a Día

### Día 1: Fundamentos
**Objetivo:** Lectura y estructura básica

**Tareas:**
- Crear estructura de carpetas con src layout
- Configurar pyproject.toml (solo stdlib, pandas opcional)
- Implementar readers básicos para TXT y Markdown
- Lectura de archivos con diferentes encodings

**Checkpoint:** Puedes leer archivos de texto correctamente

---

### Día 2: Código Pythónico
**Objetivo:** Procesamiento eficiente con generadores

**Tareas:**
- Generadores para leer archivos grandes línea por línea
- Generadores para tokenización (yield token por token)
- Comprehensions para filtrar palabras
- Decorador @cache_analysis para cachear resultados costosos

**Tips:**
- Para archivos grandes, nunca cargues todo en memoria
- El tokenizador debe hacer yield de cada token
- Comprehensions son perfectas para filtrado de stopwords
- El decorador debe cachear análisis costosos (frecuencias, estadísticas)

**Checkpoint:** Procesas archivos grandes sin problemas de memoria

---

### Día 3: Código Limpio
**Objetivo:** Análisis y transformación robusta

**Tareas:**
- Funciones pequeñas: analyze_text → count_words, calculate_frequencies, extract_stats
- Excepciones custom: InvalidTextError, ExtractionError, EncodingError
- Docstrings completos con ejemplos
- Validación de inputs

**Tips:**
- Cada función de análisis debe hacer UNA cosa
- Las excepciones deben ser descriptivas
- Documenta qué regex usa cada extractor

**Checkpoint:** El código maneja textos problemáticos sin crashear

---

### Día 4: Diseño
**Objetivo:** Sistema extensible de analyzers y extractors

**Tareas:**
- ABC BaseAnalyzer con método abstracto analyze()
- Implementar WordCounter, FrequencyAnalyzer, StatisticsAnalyzer
- ABC BaseExtractor con método abstracto extract()
- Implementar EmailExtractor, URLExtractor, DateExtractor
- Modelos Pydantic: TextDocument(content, metadata, statistics)

**Tips:**
- Cada analyzer produce un tipo específico de resultado
- Los extractors usan regex para encontrar patrones
- Pydantic valida la estructura del documento
- Composición: TextProcessor compone múltiples Analyzers y Extractors

**Checkpoint:** Puedes añadir un nuevo analyzer sin modificar código existente

---

### Día 5: Testing y Optimización
**Objetivo:** Tests exhaustivos y optimización

**Tareas:**
- Crear fixtures con textos de ejemplo (diferentes idiomas, formatos)
- Tests para cada analyzer y extractor
- Tests de regex para extracción
- Optimizar conteos con pandas para textos grandes (opcional)

**Tips:**
- Los fixtures deben incluir casos edge: textos vacíos, solo puntuación, unicode
- Verifica que las regex funcionan correctamente
- Tests de frecuencias: verifica que los conteos son correctos
- pandas puede acelerar análisis de frecuencias

**Checkpoint:** 80%+ cobertura y análisis correctos

---

### Día 6: Integración
**Objetivo:** CLI y reportes de análisis

**Tareas:**
- CLI: textkit analyze --input document.txt --output report.json
- CLI: textkit extract --input document.txt --type emails
- CLI: textkit transform --input document.txt --operation normalize
- README con ejemplos

**Tips:**
- El CLI debe soportar análisis, extracción y transformación
- Los reportes deben ser útiles: estadísticas, frecuencias, extracciones
- Incluye ejemplos de textos en examples/

**Checkpoint:** Puedes analizar un texto y obtener insights útiles

---

## Funcionalidades Mínimas Requeridas

### Lectura
- [ ] Leer archivos TXT
- [ ] Leer archivos Markdown
- [ ] Detectar encoding automáticamente
- [ ] Manejo de archivos grandes (generadores)

### Análisis
- [ ] Conteo de palabras
- [ ] Conteo de caracteres
- [ ] Análisis de frecuencias (palabras más comunes)
- [ ] Estadísticas (promedio palabras por oración, etc.)
- [ ] Detección de idioma (básico)

### Transformaciones
- [ ] Normalización (lowercase, trim)
- [ ] Limpieza (eliminar puntuación, números)
- [ ] Tokenización (palabras, oraciones)
- [ ] Eliminación de stopwords

### Extracción
- [ ] Extraer emails con regex
- [ ] Extraer URLs con regex
- [ ] Extraer fechas con regex
- [ ] Extraer números de teléfono (opcional)

### Reportes
- [ ] Estadísticas generales
- [ ] Top N palabras más frecuentes
- [ ] Información extraída
- [ ] Exportar a JSON/CSV

---

## Criterios de Evaluación

1. **Estructura y Organización** (20%)
   - Src layout correcto
   - Módulos bien separados
   - Configuración de herramientas

2. **Calidad del Código** (30%)
   - Regex bien documentadas
   - Funciones pequeñas
   - Docstrings completos
   - Manejo de errores

3. **Diseño OOP** (20%)
   - ABCs para analyzers y extractors
   - Modelos Pydantic
   - Composición
   - Extensibilidad

4. **Testing** (20%)
   - Fixtures con textos variados
   - Tests de análisis
   - Tests de regex
   - 80%+ cobertura

5. **Documentación y Usabilidad** (10%)
   - README completo
   - CLI intuitivo
   - Ejemplos claros

---

## Errores Comunes a Evitar

 **Cargar archivos completos en memoria**
 Usa generadores para streaming

 **Regex complejas sin documentar**
 Documenta qué busca cada regex

 **No manejar unicode**
 Soporta textos en diferentes idiomas

 **Análisis que no maneja casos edge**
 Maneja textos vacíos, solo puntuación, etc.

 **Extracción con regex incorrectas**
 Testa las regex exhaustivamente

 **No normalizar antes de analizar**
 Normaliza (lowercase, trim) antes de contar

---

## Recursos Útiles

- Documentación de re (regex en Python)
- Documentación de collections (Counter, defaultdict)
- Patrones de regex para emails, URLs, fechas
- Listas de stopwords en diferentes idiomas
- Documentación de unicodedata

---

## Preguntas Frecuentes

**P: ¿Debo usar librerías de NLP como NLTK o spaCy?**
R: No. El objetivo es usar solo stdlib (y pandas opcional). Implementa lo básico tú mismo.

**P: ¿Cómo manejo diferentes idiomas?**
R: Enfócate en inglés y español. Usa listas de stopwords y normalización básica.

**P: ¿Qué tan complejas deben ser las regex?**
R: Básicas pero funcionales. No necesitas regex perfectas, pero deben funcionar en casos comunes.

**P: ¿Debo implementar stemming o lemmatization?**
R: No es necesario. Enfócate en análisis básico y extracción.

**P: ¿Cómo optimizo el análisis de frecuencias?**
R: Usa collections.Counter. Para textos muy grandes, considera pandas.

---

## Checklist Final

- [ ] Estructura src layout
- [ ] pyproject.toml configurado
- [ ] Readers con generadores
- [ ] ABCs para analyzers y extractors
- [ ] Modelos Pydantic
- [ ] Análisis de frecuencias
- [ ] Extracción con regex
- [ ] Transformaciones básicas
- [ ] Tests con fixtures
- [ ] 80%+ cobertura
- [ ] CLI funcional
- [ ] README con ejemplos
- [ ] Código pasa ruff

---

¡Adelante! El procesamiento de texto es fundamental para NLP y análisis de datos.
