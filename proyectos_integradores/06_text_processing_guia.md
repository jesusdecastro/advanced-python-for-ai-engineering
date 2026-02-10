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

## Diseñando la Estructura del Proyecto

### Preguntas Clave para Diseñar tu Estructura

Antes de crear carpetas, piensa en estas preguntas:

**1. ¿Qué hace mi toolkit de procesamiento de texto?**
- Lee archivos de texto (TXT, Markdown, etc.)
- Analiza el texto (frecuencias, estadísticas, sentimiento básico)
- Transforma el texto (normalización, limpieza, tokenización)
- Extrae información (emails, URLs, fechas, entidades)

**2. ¿Cuáles son las operaciones principales?**
- **Leer**: Cargar texto desde archivos
- **Analizar**: Calcular métricas (palabras más frecuentes, longitud promedio)
- **Transformar**: Modificar el texto (lowercase, quitar puntuación, tokenizar)
- **Extraer**: Encontrar patrones específicos (emails, URLs)
- Cada operación es una responsabilidad diferente

**3. ¿Cómo represento un documento?**
- ¿Solo el texto crudo?
- ¿Texto + metadata (autor, fecha, fuente)?
- ¿Texto + análisis pre-calculado?
- Hint: Un modelo de datos (clase o Pydantic) es útil

### Pistas de Organización

**Sobre lectura:**
- Diferentes formatos de texto: TXT plano, Markdown, HTML
- Todos devuelven texto, pero el parsing es diferente
- Hint: Clase base abstracta con método `read()`
- ¿Cómo manejas diferentes encodings (UTF-8, Latin-1)?

**Sobre análisis:**
- Contar palabras es diferente a calcular frecuencias
- Calcular estadísticas (promedio de palabras por oración) es otra cosa
- Análisis de sentimiento básico (positivo/negativo) es otra
- ¿Cada análisis es una clase o una función?
- Hint: Si el análisis tiene estado o configuración → clase

**Sobre transformaciones:**
- Normalizar: lowercase, quitar acentos, trim
- Limpiar: quitar puntuación, números, stopwords
- Tokenizar: dividir en palabras, oraciones, n-gramas
- Todas transforman texto → texto (o texto → lista)
- ¿Necesitas una interfaz común?

**Sobre extracción:**
- Emails: regex `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b`
- URLs: regex para http/https
- Fechas: múltiples formatos posibles
- Cada extractor busca un patrón específico
- Hint: Todos devuelven lista de matches

**Sobre eficiencia:**
- Archivos de texto pueden ser enormes (logs, libros, datasets)
- ¿Cargas todo en memoria o usas generadores?
- Hint: `yield` línea por línea o token por token

**Sobre modelos de datos:**
- Un documento tiene: texto, metadata, análisis
- ¿Cómo estructuras esto?
- Hint: Pydantic o dataclass

### Checklist de Estructura

Antes de empezar a programar, asegúrate de tener:
- [ ] Carpeta `src/` con tu paquete principal
- [ ] Módulo/paquete para readers (lectura de archivos)
- [ ] Módulo/paquete para analyzers (análisis estadístico)
- [ ] Módulo/paquete para transformers (modificación de texto)
- [ ] Módulo/paquete para extractors (extracción de patrones)
- [ ] Módulo/paquete para modelos de datos (Document, AnalysisResult)
- [ ] Carpeta `tests/` con fixtures de textos de ejemplo
- [ ] Carpeta `examples/` con scripts de uso
- [ ] `pyproject.toml` (solo stdlib, pandas opcional)
- [ ] `README.md`

### Enfoque Recomendado

1. **Empieza con lectura**: Implementa un reader básico para TXT
2. **Añade análisis simple**: Cuenta palabras, calcula frecuencias
3. **Añade transformaciones**: Normalización, tokenización
4. **Añade extracción**: Implementa extractor de emails con regex
5. **Generaliza**: Crea abstracciones cuando tengas 2+ implementaciones
6. **Optimiza**: Usa generadores para archivos grandes

**Pregunta guía**: "Si necesito añadir extracción de números de teléfono, ¿dónde va ese código?"

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
