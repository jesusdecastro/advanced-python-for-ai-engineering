# Guía del Proyecto: Data Pipeline Package

## Visión General

Construirás un sistema ETL (Extract, Transform, Load) que lee datos de diferentes fuentes, aplica transformaciones y escribe resultados. El objetivo es aplicar todos los principios aprendidos en el curso, no crear el ETL más complejo del mundo.

---

## Objetivos de Aprendizaje

Al finalizar este proyecto, habrás aplicado:
- Estructura de paquetes profesional
- Programación orientada a objetos con herencia y composición
- Generadores para procesamiento eficiente
- Validación de datos robusta
- Testing exhaustivo
- Documentación completa

---

## Estructura Sugerida del Proyecto

```
datapipe/
 src/
    datapipe/
        __init__.py
        readers/
           __init__.py
           base.py
           csv_reader.py
           json_reader.py
        transformers/
           __init__.py
           base.py
           filter.py
           aggregate.py
        writers/
           __init__.py
           base.py
           csv_writer.py
        validators/
           __init__.py
           schema.py
        pipeline.py
        cli.py
 tests/
    conftest.py
    test_readers.py
    test_transformers.py
    test_writers.py
    test_pipeline.py
 examples/
    sample_data.csv
    example_pipeline.py
 pyproject.toml
 README.md
```

---

## Roadmap Día a Día

### Día 1: Fundamentos
**Objetivo:** Estructura del proyecto funcionando

**Tareas:**
- Crear estructura de carpetas con src layout
- Configurar pyproject.toml con dependencias básicas
- Crear módulos vacíos con __init__.py
- Configurar herramientas de calidad (ruff, pyright)
- Verificar que los imports funcionan entre módulos

**Checkpoint:** Puedes importar módulos entre sí sin errores

---

### Día 2: Código Pythónico
**Objetivo:** Implementar lectura eficiente de datos

**Tareas:**
- Implementar un reader básico para CSV que use generadores
- El reader debe hacer yield de cada fila, no cargar todo en memoria
- Crear un context manager para abrir/cerrar archivos automáticamente
- Usar comprehensions para filtrado básico
- Añadir un decorador simple para logging de operaciones

**Tips:**
- Piensa en archivos grandes: ¿cómo procesarías un CSV de 10GB?
- Los generadores son tu mejor amigo para streaming
- El context manager debe garantizar que los archivos se cierran

**Checkpoint:** Puedes leer un CSV grande línea por línea sin problemas de memoria

---

### Día 3: Código Limpio
**Objetivo:** Código legible y robusto

**Tareas:**
- Refactorizar funciones grandes en funciones pequeñas y específicas
- Cada función debe hacer UNA cosa bien
- Renombrar variables con nombres descriptivos (nada de `data`, `tmp`, `x`)
- Crear excepciones custom para errores específicos
- Añadir docstrings en formato Sphinx a todas las funciones públicas
- Implementar validación de inputs con error handling

**Tips:**
- Si una función tiene más de 20 líneas, probablemente hace demasiado
- Los nombres deben explicar QUÉ es, no CÓMO se usa
- Las excepciones custom ayudan a debuggear: `InvalidSchemaError` vs `ValueError`

**Checkpoint:** Otro desarrollador puede leer tu código y entenderlo sin preguntar

---

### Día 4: Diseño
**Objetivo:** Arquitectura extensible con OOP

**Tareas:**
- Crear clases base abstractas (ABC) para Reader, Transformer, Writer
- Implementar clases concretas que hereden de las ABCs
- Usar Pydantic para modelos de datos y validación automática
- Aplicar composición: Pipeline compone múltiples Transformers
- Cada clase debe tener una sola responsabilidad (SRP)

**Tips:**
- Las ABCs definen el contrato: qué métodos DEBEN implementar las subclases
- Pydantic valida automáticamente: aprovéchalo para schemas de datos
- Composición > Herencia: un Pipeline "tiene" Transformers, no "es" un Transformer
- Si una clase hace muchas cosas, divídela

**Checkpoint:** Puedes añadir un nuevo Reader sin modificar código existente

---

### Día 5: Testing y Optimización
**Objetivo:** Código confiable y eficiente

**Tareas:**
- Escribir tests para cada componente (readers, transformers, writers)
- Crear fixtures con datos de prueba
- Usar mocking para filesystem (no crear archivos reales en tests)
- Alcanzar 80%+ de cobertura de código
- Optimizar transformaciones con pandas cuando sea apropiado

**Tips:**
- Un test debe probar UNA cosa
- Los fixtures evitan duplicar código de setup
- Mock filesystem: usa pytest-mock o unittest.mock
- pandas es excelente para agregaciones, pero no siempre necesario

**Checkpoint:** Todos los tests pasan y tienes 80%+ de cobertura

---

### Día 6: Integración
**Objetivo:** Paquete production-ready

**Tareas:**
- Implementar CLI con argparse o typer
- El CLI debe permitir ejecutar pipelines desde línea de comandos
- Escribir README completo con ejemplos de uso
- Crear ejemplos funcionales en carpeta examples/
- Preparar el paquete para distribución (build)

**Tips:**
- El CLI es la cara de tu paquete: hazlo intuitivo
- El README debe tener: instalación, quick start, ejemplos, API reference
- Los ejemplos deben ser copy-paste y funcionar
- Prueba instalar tu paquete en un entorno limpio

**Checkpoint:** Alguien puede instalar tu paquete y usarlo sin ayuda

---

## Funcionalidades Mínimas Requeridas

### Readers
- [ ] Leer CSV con generadores (yield por fila)
- [ ] Leer JSON (puede cargar todo, archivos pequeños)
- [ ] Manejo de errores de archivo no encontrado
- [ ] Detección automática de delimitadores (CSV)

### Transformers
- [ ] Filtrar filas por condición
- [ ] Seleccionar columnas específicas
- [ ] Transformar valores (ej: normalizar strings)
- [ ] Agregaciones básicas (suma, promedio por grupo)

### Writers
- [ ] Escribir CSV
- [ ] Escribir JSON
- [ ] Crear archivo si no existe
- [ ] Manejo de errores de escritura

### Pipeline
- [ ] Componer Reader + Transformers + Writer
- [ ] Ejecutar pipeline completo
- [ ] Logging de operaciones
- [ ] Manejo de errores en cualquier etapa

### Validación
- [ ] Validar schema de datos con Pydantic
- [ ] Validar tipos de columnas
- [ ] Reportar errores de validación claramente

---

## Criterios de Evaluación

Tu proyecto será evaluado en:

1. **Estructura y Organización** (20%)
   - Uso correcto de src layout
   - Organización lógica de módulos
   - Configuración de herramientas

2. **Calidad del Código** (30%)
   - Nombres descriptivos
   - Funciones pequeñas y enfocadas
   - Docstrings completos
   - Manejo de errores

3. **Diseño OOP** (20%)
   - Uso correcto de ABCs
   - Herencia vs composición
   - Principios SOLID
   - Modelos de datos con Pydantic

4. **Testing** (20%)
   - Cobertura 80%+
   - Tests significativos
   - Uso de fixtures y mocking

5. **Documentación y Usabilidad** (10%)
   - README completo
   - Ejemplos funcionales
   - CLI intuitivo

---

## Errores Comunes a Evitar

 **Cargar archivos completos en memoria**
 Usa generadores para streaming

 **Funciones de 100+ líneas**
 Divide en funciones pequeñas

 **Variables llamadas `data`, `tmp`, `x`**
 Nombres descriptivos: `validated_records`, `filtered_rows`

 **Excepciones genéricas: `except Exception`**
 Excepciones específicas y custom

 **Sin tests o tests que no prueban nada**
 Tests significativos con buenos fixtures

 **README vacío o sin ejemplos**
 Documentación completa con quick start

 **Código que solo funciona en tu máquina**
 Paquete instalable y portable

---

## Recursos Útiles

- Documentación oficial de Python sobre paquetes
- PEP 8: Style Guide for Python Code
- Documentación de Pydantic
- Documentación de pytest
- Ejemplos de src layout en proyectos open source

---

## Preguntas Frecuentes

**P: ¿Cuántos readers/transformers/writers debo implementar?**
R: Mínimo 2 readers (CSV, JSON), 3 transformers (filter, select, aggregate), 1 writer (CSV). Más es mejor, pero prioriza calidad sobre cantidad.

**P: ¿Debo usar pandas para todo?**
R: No. Usa pandas cuando tenga sentido (agregaciones, análisis), pero los readers deben usar generadores para eficiencia.

**P: ¿Qué tan complejo debe ser el CLI?**
R: Básico pero funcional. Debe permitir especificar input, output y transformaciones. No necesitas un CLI súper avanzado.

**P: ¿Puedo usar librerías externas?**
R: Sí, pero con moderación. pandas, pydantic, typer están bien. No uses librerías que hagan todo el trabajo por ti.

**P: ¿Cómo sé si mi diseño OOP es bueno?**
R: Pregúntate: ¿Puedo añadir un nuevo Reader sin modificar código existente? Si sí, vas bien.

---

## Checklist Final

Antes de entregar, verifica:

- [ ] Estructura src layout correcta
- [ ] pyproject.toml configurado
- [ ] Todos los módulos tienen __init__.py
- [ ] Código pasa ruff sin errores
- [ ] Todas las funciones públicas tienen docstrings
- [ ] ABCs implementadas correctamente
- [ ] Modelos Pydantic para validación
- [ ] Tests con 80%+ cobertura
- [ ] README completo con ejemplos
- [ ] CLI funcional
- [ ] Ejemplos en carpeta examples/
- [ ] Paquete se puede instalar con pip

---

¡Buena suerte! Recuerda: el objetivo es aplicar principios, no crear el ETL perfecto.
