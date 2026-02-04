# Proyectos Integradores - Python Avanzado para IA

Este directorio contiene las guías detalladas para los proyectos integradores del curso. Cada proyecto está diseñado para aplicar todos los conceptos aprendidos durante la semana.

---

## Proyectos Disponibles

### Nivel Básico (⭐⭐)

1. **[Data Pipeline Package](01_data_pipeline_guia.md)**
   - Sistema ETL configurable
   - Ideal para: Principiantes en arquitectura de software
   - Conceptos: Streaming, transformaciones, validación

2. **[Log Analyzer Tool](02_log_analyzer_guia.md)**
   - Análisis de logs con métricas y reportes
   - Ideal para: Interesados en observabilidad/DevOps
   - Conceptos: Parsing, análisis de texto, agregaciones

3. **[CSV Data Cleaner](03_csv_cleaner_guia.md)**
   - Limpieza y validación de datos CSV
   - Ideal para: Enfoque en data quality
   - Conceptos: Validación, transformación, reporting

4. **[Config File Manager](04_config_manager_guia.md)**
   - Gestión de configuraciones multi-formato
   - Ideal para: Enfoque en robustez y testing
   - Conceptos: Parsing, validación, conversión

### Nivel Medio (⭐⭐⭐)

5. **[Data Validator Library](05_data_validator_guia.md)**
   - Framework de validación de datos tabulares
   - Ideal para: Interesados en data engineering
   - Conceptos: Validación, reglas, data quality

6. **[Text Processing Toolkit](06_text_processing_guia.md)**
   - Procesamiento y análisis de texto
   - Ideal para: Interesados en NLP básico
   - Conceptos: Regex, análisis, transformaciones

---

## Estructura de las Guías

Cada guía incluye:

- **Visión General**: Qué vas a construir y por qué
- **Objetivos de Aprendizaje**: Qué principios aplicarás
- **Estructura Sugerida**: Organización de carpetas y módulos
- **Roadmap Día a Día**: Qué hacer cada día del curso
- **Funcionalidades Mínimas**: Checklist de lo que debe funcionar
- **Criterios de Evaluación**: Cómo se evaluará tu proyecto
- **Errores Comunes**: Qué evitar
- **Preguntas Frecuentes**: Respuestas a dudas comunes
- **Checklist Final**: Verificación antes de entregar

---

## Cómo Elegir un Proyecto

### Si eres nuevo en arquitectura de software:
Elige un proyecto de nivel básico (⭐⭐). Todos son completables en 6 días con guía.

### Si tienes experiencia con Python:
Considera un proyecto de nivel medio (⭐⭐⭐). Más funcionalidades pero guiadas.

### Considera tus intereses:
- **DevOps/Observabilidad**: Log Analyzer
- **Data Engineering**: Data Pipeline, CSV Cleaner, Data Validator
- **Configuración/Tooling**: Config Manager
- **NLP/Texto**: Text Processing

---

## Principios Aplicados en Todos los Proyectos

Independientemente del proyecto que elijas, aplicarás:

### Día 1: Fundamentos
- Estructura de paquetes con src layout
- Configuración de pyproject.toml
- Herramientas de calidad (ruff, pyright)

### Día 2: Código Pythónico
- Generadores e iteradores
- Comprehensions
- Decoradores
- Context managers

### Día 3: Código Limpio
- Funciones pequeñas y enfocadas
- Meaningful names
- Type hints
- Error handling robusto
- Docstrings completos

### Día 4: Diseño
- Abstract Base Classes (ABCs)
- Herencia vs composición
- Modelos Pydantic
- Principios SOLID

### Día 5: Testing y Optimización
- Unit testing con pytest
- Fixtures y mocking
- Cobertura 80%+
- Optimización con pandas/numpy

### Día 6: Integración
- CLI funcional
- Documentación completa
- Ejemplos de uso
- Paquete distribuible

---

## Criterios de Evaluación Generales

Todos los proyectos se evalúan en:

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

## Entregables

Al finalizar el proyecto, debes entregar:

- [ ] Repositorio con código completo
- [ ] Estructura src layout correcta
- [ ] Tests pasando con cobertura 80%+
- [ ] README con:
  - Descripción del proyecto
  - Instrucciones de instalación
  - Ejemplos de uso
  - Documentación de API
- [ ] Ejemplos funcionales en carpeta examples/
- [ ] Paquete distribuible (wheel)
- [ ] Código que pasa ruff sin errores

---

## Recursos Adicionales

- [Plan de Formación](../plan_de_formacion.md): Contenido detallado de cada día
- [Proyectos Integradores](../proyectos_integradores.md): Descripción completa de cada proyecto
- [Estándares del Curso](../.kiro/steering/course-standards.md): Convenciones de código

---

## Preguntas Frecuentes Generales

**P: ¿Puedo cambiar de proyecto a mitad de semana?**
R: No es recomendable. Elige bien desde el principio.

**P: ¿Puedo trabajar solo en lugar de en grupo?**
R: Sí, pero se recomienda trabajar en grupos de 3 para aprender colaboración.

**P: ¿Qué pasa si no termino todas las funcionalidades?**
R: Prioriza calidad sobre cantidad. Es mejor tener menos funcionalidades bien hechas.

**P: ¿Puedo usar librerías externas?**
R: Sí, pero con moderación. No uses librerías que hagan todo el trabajo por ti.

**P: ¿Cómo sé si mi diseño OOP es bueno?**
R: Pregúntate: ¿Puedo añadir nueva funcionalidad sin modificar código existente? Si sí, vas bien.

**P: ¿Debo seguir la estructura sugerida exactamente?**
R: Es una guía, no una regla estricta. Pero debe tener sentido y estar bien organizada.

---

## Consejos Finales

1. **Lee la guía completa antes de empezar**: Entiende el proyecto completo
2. **Sigue el roadmap día a día**: No te adelantes ni te atrases
3. **Prioriza calidad sobre cantidad**: Mejor poco y bien hecho
4. **Haz commits frecuentes**: Facilita el trabajo en equipo
5. **Pide ayuda cuando la necesites**: Los instructores están para ayudar
6. **Testea continuamente**: No dejes los tests para el final
7. **Documenta mientras programas**: No lo dejes para el último día

---

¡Buena suerte con tu proyecto! Recuerda: el objetivo es aplicar principios, no crear el software perfecto.
