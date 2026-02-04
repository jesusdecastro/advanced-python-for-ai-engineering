# Guía del Proyecto: Log Analyzer Tool

## Visión General

Construirás una herramienta para analizar archivos de logs, extraer métricas y generar reportes. El objetivo es aplicar todos los principios del curso mientras creas algo útil para DevOps/observabilidad.

---

## Objetivos de Aprendizaje

Al finalizar este proyecto, habrás aplicado:
- Parsing de texto con expresiones regulares
- Generadores para archivos grandes
- Análisis de datos con pandas
- Diseño extensible con ABCs
- Testing con fixtures y mocking
- Generación de reportes

---

## Estructura Sugerida del Proyecto

```
loglyzer/
├── src/
│   └── loglyzer/
│       ├── __init__.py
│       ├── parsers/
│       │   ├── __init__.py
│       │   ├── base.py
│       │   ├── nginx.py
│       │   └── apache.py
│       ├── analyzers/
│       │   ├── __init__.py
│       │   ├── metrics.py
│       │   └── anomaly.py
│       ├── models/
│       │   ├── __init__.py
│       │   └── log_entry.py
│       ├── reporters/
│       │   ├── __init__.py
│       │   ├── json_reporter.py
│       │   └── html_reporter.py
│       ├── filters.py
│       └── cli.py
├── tests/
│   ├── conftest.py
│   ├── fixtures/
│   │   ├── sample_nginx.log
│   │   └── sample_apache.log
│   ├── test_parsers.py
│   ├── test_analyzers.py
│   └── test_reporters.py
├── templates/
│   └── report.html
├── examples/
│   └── analyze_logs.py
├── pyproject.toml
└── README.md
```

---

## Roadmap Día a Día

### Día 1: Fundamentos
**Objetivo:** Estructura y parsing básico

**Tareas:**
- Crear estructura de carpetas con src layout
- Configurar pyproject.toml (pandas, jinja2 para HTML)
- Crear módulos base
- Implementar un parser simple que lea líneas de un log

**Checkpoint:** Puedes leer un archivo de log línea por línea

---

### Día 2: Código Pythónico
**Objetivo:** Streaming eficiente de logs

**Tareas:**
- Implementar generadores para leer logs grandes (yield por línea)
- Usar comprehensions para filtrar logs por criterios
- Crear decorador @timed para medir performance de parsers
- Context manager para abrir archivos de log

**Tips:**
- Los logs pueden ser enormes: nunca cargues todo en memoria
- Un generador que hace yield de LogEntry por línea es perfecto
- El decorador @timed ayuda a identificar cuellos de botella

**Checkpoint:** Puedes procesar un log de 1GB sin problemas de memoria

---

### Día 3: Código Limpio
**Objetivo:** Parsing robusto y legible

**Tareas:**
- Dividir parsing en funciones pequeñas: extract_timestamp, extract_ip, extract_status
- Crear excepciones custom: InvalidLogFormatError, ParsingError
- Añadir docstrings completos con ejemplos de formato de log
- Validar cada línea parseada

**Tips:**
- Cada formato de log (nginx, apache) tiene su estructura: usa regex
- Las funciones pequeñas facilitan testing
- Los nombres deben ser claros: `parsed_log_entries` no `data`

**Checkpoint:** El código maneja logs malformados sin crashear

---

### Día 4: Diseño
**Objetivo:** Sistema extensible de parsers y analyzers

**Tareas:**
- Crear ABC BaseParser con método abstracto parse()
- Implementar NginxParser, ApacheParser heredando de BaseParser
- Crear modelos Pydantic: LogEntry(timestamp, ip, status, latency)
- Implementar analyzers que calculen métricas

**Tips:**
- Cada parser conoce el formato de su tipo de log
- Pydantic valida automáticamente tipos y formatos
- Los analyzers reciben LogEntry, no strings
- Composición: LogAnalyzer compone múltiples Analyzers

**Checkpoint:** Puedes añadir un nuevo formato de log sin modificar código existente

---

### Día 5: Testing y Optimización
**Objetivo:** Tests completos y análisis eficiente

**Tareas:**
- Crear fixtures con logs de ejemplo (nginx, apache)
- Tests para cada parser con logs válidos e inválidos
- Tests de métricas (requests/sec, percentiles)
- Optimizar agregaciones con pandas

**Tips:**
- Los fixtures deben incluir casos edge: logs malformados, vacíos
- Mock filesystem para no crear archivos reales
- pandas es excelente para groupby y resample temporal
- Verifica que las métricas son correctas

**Checkpoint:** 80%+ cobertura y métricas correctas

---

### Día 6: Integración
**Objetivo:** CLI y reportes

**Tareas:**
- CLI: loglyzer analyze --format nginx --output html access.log
- Generar reportes HTML con jinja2
- Reportes deben incluir: métricas, gráficos básicos, anomalías
- README con ejemplos de uso

**Tips:**
- El CLI debe ser intuitivo: formato, input, output
- Los reportes HTML deben ser legibles
- Incluye ejemplos de logs en examples/

**Checkpoint:** Puedes analizar un log y obtener un reporte útil

---

## Funcionalidades Mínimas Requeridas

### Parsers
- [ ] Parser para formato nginx
- [ ] Parser para formato apache (o JSON logs)
- [ ] Detección automática de formato
- [ ] Manejo de líneas malformadas

### Análisis
- [ ] Conteo de requests por status code
- [ ] Requests por segundo (promedio)
- [ ] Top IPs más activas
- [ ] Latencias (percentiles p50, p95, p99)
- [ ] Detección de errores 5xx

### Filtrado
- [ ] Filtrar por rango de tiempo
- [ ] Filtrar por status code
- [ ] Filtrar por IP
- [ ] Filtrar por path/URL

### Reportes
- [ ] Reporte JSON con métricas
- [ ] Reporte HTML legible
- [ ] Incluir timestamp del análisis
- [ ] Resumen ejecutivo

---

## Criterios de Evaluación

1. **Estructura y Organización** (20%)
   - Src layout correcto
   - Módulos bien organizados
   - Configuración de herramientas

2. **Calidad del Código** (30%)
   - Parsing robusto con regex
   - Funciones pequeñas
   - Docstrings completos
   - Manejo de errores

3. **Diseño OOP** (20%)
   - ABCs para parsers
   - Modelos Pydantic
   - Composición de analyzers
   - Extensibilidad

4. **Testing** (20%)
   - Fixtures con logs reales
   - Tests de parsing
   - Tests de métricas
   - 80%+ cobertura

5. **Documentación y Usabilidad** (10%)
   - README completo
   - CLI intuitivo
   - Reportes útiles

---

## Errores Comunes a Evitar

❌ **Cargar todo el log en memoria**
✅ Usa generadores para streaming

❌ **Regex complejas e ilegibles**
✅ Usa regex con nombres de grupos y comenta

❌ **Parser monolítico de 200 líneas**
✅ Divide en funciones pequeñas

❌ **Ignorar líneas malformadas silenciosamente**
✅ Logea warnings y cuenta líneas problemáticas

❌ **Métricas incorrectas**
✅ Verifica con logs de ejemplo conocidos

❌ **Reportes ilegibles**
✅ Formato claro con secciones bien definidas

---

## Recursos Útiles

- Documentación de expresiones regulares en Python
- Ejemplos de formatos de logs nginx/apache
- Documentación de pandas para análisis temporal
- Jinja2 para templates HTML
- Ejemplos de logs reales para testing

---

## Preguntas Frecuentes

**P: ¿Qué formatos de log debo soportar?**
R: Mínimo 2: nginx y apache (o JSON). Prioriza que funcionen bien sobre soportar muchos formatos.

**P: ¿Cómo manejo logs de varios GB?**
R: Generadores. Nunca cargues todo en memoria. Procesa línea por línea.

**P: ¿Debo hacer gráficos en los reportes?**
R: No es obligatorio. Si lo haces, usa matplotlib o plotly, pero prioriza métricas correctas.

**P: ¿Qué métricas son más importantes?**
R: Requests/sec, status codes, latencias, top IPs. Enfócate en lo útil para debugging.

**P: ¿Cómo testeo con logs grandes?**
R: Usa fixtures pequeños pero representativos. No necesitas logs de GB para tests.

---

## Checklist Final

- [ ] Estructura src layout
- [ ] pyproject.toml configurado
- [ ] Parsers con generadores
- [ ] ABCs implementadas
- [ ] Modelos Pydantic
- [ ] Métricas correctas
- [ ] Tests con fixtures
- [ ] 80%+ cobertura
- [ ] CLI funcional
- [ ] Reportes legibles
- [ ] README con ejemplos
- [ ] Código pasa ruff

---

¡Éxito! Recuerda: un buen log analyzer es simple pero robusto.
