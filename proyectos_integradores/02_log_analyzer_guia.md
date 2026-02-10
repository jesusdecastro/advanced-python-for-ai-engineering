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

## Diseñando la Estructura del Proyecto

### Preguntas Clave para Diseñar tu Estructura

Antes de crear carpetas, piensa en estas preguntas:

**1. ¿Qué responsabilidades tiene mi sistema?**
- Parsear diferentes formatos de logs (nginx, apache, custom)
- Analizar logs para extraer métricas
- Generar reportes en diferentes formatos
- Filtrar logs por criterios
- Representar una entrada de log

**2. ¿Cómo organizo código que hace cosas similares?**
- Si tengo múltiples parsers (nginx, apache), ¿los pongo juntos?
- Si tengo múltiples tipos de análisis (métricas, anomalías), ¿cómo los agrupo?
- ¿Los reportes JSON y HTML van en el mismo lugar?

**3. ¿Qué patrones de diseño necesito?**
- Cada formato de log necesita su propio parser → Piensa en herencia/ABCs
- Los reportes pueden ser de varios tipos → Piensa en estrategia
- Las entradas de log tienen estructura → Piensa en modelos de datos

### Pistas de Organización

**Sobre parsers:**
- Cada formato de log (nginx, apache) tiene su propia lógica de parsing
- Pero todos los parsers hacen lo mismo: convertir texto → objeto estructurado
- Hint: Una clase base abstracta define el contrato, las subclases implementan

**Sobre modelos de datos:**
- Una entrada de log tiene: timestamp, IP, status code, latency, etc.
- ¿Dónde defines esta estructura?
- Hint: Pydantic es perfecto para validar y estructurar datos

**Sobre análisis:**
- Calcular métricas (requests/sec, percentiles) es una responsabilidad
- Detectar anomalías es otra responsabilidad
- ¿Van en el mismo módulo o separados?

**Sobre reportes:**
- Generar JSON es diferente a generar HTML
- Pero ambos toman los mismos datos de entrada
- Hint: Piensa en una interfaz común con implementaciones específicas

### Checklist de Estructura

Antes de empezar a programar, asegúrate de tener:
- [ ] Carpeta `src/` con tu paquete principal dentro
- [ ] Módulo/paquete para parsers de logs
- [ ] Módulo/paquete para modelos de datos
- [ ] Módulo/paquete para análisis/métricas
- [ ] Módulo/paquete para generación de reportes
- [ ] Carpeta `tests/` con fixtures de logs de ejemplo
- [ ] Carpeta `examples/` con scripts de uso
- [ ] `pyproject.toml` configurado
- [ ] `README.md` con descripción

### Enfoque Recomendado

1. **Empieza con un parser**: Implementa parsing de un formato (nginx o apache)
2. **Define tu modelo**: Crea la estructura de LogEntry
3. **Añade análisis básico**: Cuenta requests, calcula promedios
4. **Extiende**: Añade más parsers, más métricas, más reportes

**Pregunta guía**: "Si necesito añadir soporte para logs de PostgreSQL, ¿dónde va ese código?"

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

 **Cargar todo el log en memoria**
 Usa generadores para streaming

 **Regex complejas e ilegibles**
 Usa regex con nombres de grupos y comenta

 **Parser monolítico de 200 líneas**
 Divide en funciones pequeñas

 **Ignorar líneas malformadas silenciosamente**
 Logea warnings y cuenta líneas problemáticas

 **Métricas incorrectas**
 Verifica con logs de ejemplo conocidos

 **Reportes ilegibles**
 Formato claro con secciones bien definidas

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
