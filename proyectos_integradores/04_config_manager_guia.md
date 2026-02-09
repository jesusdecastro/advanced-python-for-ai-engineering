# Guía del Proyecto: Config File Manager

## Visión General

Construirás una librería para gestionar archivos de configuración en múltiples formatos (JSON, YAML, TOML, INI) con validación, conversión y acceso intuitivo. Perfecto para aplicar OOP, validación y métodos mágicos.

---

## Objetivos de Aprendizaje

Al finalizar este proyecto, habrás aplicado:
- Parsing de múltiples formatos
- Métodos mágicos para acceso intuitivo
- Validación de esquemas con Pydantic
- Merge de configuraciones
- Testing con múltiples formatos
- Conversión entre formatos

---

## Estructura Sugerida del Proyecto

```
configman/
 src/
    configman/
        __init__.py
        parsers/
           __init__.py
           base.py
           json_parser.py
           yaml_parser.py
           toml_parser.py
           ini_parser.py
        validators/
           __init__.py
           schema_validator.py
        converters/
           __init__.py
           format_converter.py
        models/
           __init__.py
           config.py
        merger.py
        cli.py
 tests/
    conftest.py
    fixtures/
       config.json
       config.yaml
       config.toml
       config.ini
    test_parsers.py
    test_validators.py
    test_converters.py
    test_merger.py
 examples/
    configs/
       defaults.yaml
       user.yaml
    usage_example.py
 pyproject.toml
 README.md
```

---

## Roadmap Día a Día

### Día 1: Fundamentos
**Objetivo:** Parsing básico de formatos

**Tareas:**
- Crear estructura de carpetas con src layout
- Configurar pyproject.toml (pyyaml, toml)
- Implementar parsers básicos para JSON y YAML
- Cargar configuraciones en diccionarios

**Checkpoint:** Puedes leer JSON y YAML correctamente

---

### Día 2: Código Pythónico
**Objetivo:** Acceso intuitivo con dot notation

**Tareas:**
- Implementar __getattr__ para acceso con dot notation (config.database.host)
- Implementar __setattr__ para modificación
- Decorador @validate_on_load para validación automática
- Context manager para cargar/guardar configs
- Usar functools.lru_cache para cachear configs

**Tips:**
- __getattr__ permite config.db.host en lugar de config['db']['host']
- El context manager debe manejar carga y guardado automático
- lru_cache evita recargar el mismo archivo múltiples veces

**Checkpoint:** Puedes acceder a config.database.host naturalmente

---

### Día 3: Código Limpio
**Objetivo:** Validación y error handling robusto

**Tareas:**
- Funciones pequeñas: load_config → parse_file, validate_schema, merge_defaults
- Excepciones custom: InvalidConfigError, SchemaValidationError, FormatError
- Docstrings completos con ejemplos de uso
- Validación de esquemas antes de usar

**Tips:**
- Cada parser debe manejar su formato específico
- Las excepciones deben indicar QUÉ está mal y DÓNDE
- Valida tipos, valores requeridos, rangos

**Checkpoint:** El código maneja configs inválidos sin crashear

---

### Día 4: Diseño
**Objetivo:** Sistema extensible de parsers

**Tareas:**
- ABC BaseParser con método abstracto parse()
- Implementar JSONParser, YAMLParser, TOMLParser, INIParser
- Modelos Pydantic para esquemas de configuración
- Implementar merge de configuraciones (defaults + user)

**Tips:**
- Cada parser conoce su formato
- Pydantic valida automáticamente el esquema
- El merge debe ser inteligente: deep merge de diccionarios
- Composición: ConfigManager compone Parser + Validator + Merger

**Checkpoint:** Puedes añadir un nuevo formato sin modificar código existente

---

### Día 5: Testing y Optimización
**Objetivo:** Tests exhaustivos para todos los formatos

**Tareas:**
- Crear fixtures con configs en todos los formatos
- Tests de parsing para cada formato
- Tests de validación de esquemas
- Tests de merge de configuraciones
- Tests de conversión entre formatos

**Tips:**
- Los fixtures deben incluir casos edge: configs vacíos, anidados, inválidos
- Verifica que el merge funciona correctamente
- Tests de conversión: JSON → YAML → TOML → JSON debe ser idempotente

**Checkpoint:** 80%+ cobertura y todos los formatos funcionan

---

### Día 6: Integración
**Objetivo:** CLI y conversión entre formatos

**Tareas:**
- CLI: configman convert --input config.json --output config.yaml
- CLI: configman validate --input config.yaml --schema schema.json
- CLI: configman merge --defaults defaults.yaml --user user.yaml --output final.yaml
- README con ejemplos de uso

**Tips:**
- El CLI debe soportar todos los formatos
- La conversión debe preservar la estructura
- Incluye ejemplos de configs en examples/

**Checkpoint:** Puedes convertir entre formatos y validar configs

---

## Funcionalidades Mínimas Requeridas

### Parsing
- [ ] Leer JSON
- [ ] Leer YAML
- [ ] Leer TOML
- [ ] Leer INI (opcional)
- [ ] Detección automática de formato por extensión

### Acceso
- [ ] Dot notation para lectura (config.db.host)
- [ ] Dot notation para escritura (config.db.host = "localhost")
- [ ] Acceso por diccionario (config['db']['host'])
- [ ] Manejo de claves inexistentes

### Validación
- [ ] Validar esquema con Pydantic
- [ ] Validar tipos de datos
- [ ] Validar valores requeridos
- [ ] Validar rangos/opciones

### Merge
- [ ] Merge de dos configuraciones
- [ ] Deep merge de diccionarios anidados
- [ ] Prioridad configurable (defaults vs user)
- [ ] Manejo de conflictos

### Conversión
- [ ] JSON → YAML
- [ ] YAML → TOML
- [ ] TOML → JSON
- [ ] Preservar estructura

---

## Criterios de Evaluación

1. **Estructura y Organización** (20%)
   - Src layout correcto
   - Módulos bien separados
   - Configuración de herramientas

2. **Calidad del Código** (30%)
   - Parsing robusto
   - Métodos mágicos bien implementados
   - Docstrings completos
   - Manejo de errores

3. **Diseño OOP** (20%)
   - ABCs para parsers
   - Modelos Pydantic
   - Composición
   - Extensibilidad

4. **Testing** (20%)
   - Fixtures para todos los formatos
   - Tests de parsing
   - Tests de validación
   - 80%+ cobertura

5. **Documentación y Usabilidad** (10%)
   - README completo
   - CLI intuitivo
   - Ejemplos claros

---

## Errores Comunes a Evitar

 **Parsers que modifican la estructura**
 Preserva la estructura original

 **Dot notation que no maneja anidamiento**
 Soporta config.db.connection.host

 **Merge que sobrescribe todo**
 Deep merge inteligente

 **Validación que no indica QUÉ está mal**
 Mensajes de error descriptivos

 **Conversión que pierde información**
 Conversión lossless cuando sea posible

 **No manejar configs vacíos**
 Maneja todos los casos edge

---

## Recursos Útiles

- Documentación de json (stdlib)
- Documentación de PyYAML
- Documentación de toml
- Documentación de configparser (INI)
- Ejemplos de esquemas de configuración

---

## Preguntas Frecuentes

**P: ¿Qué formatos son obligatorios?**
R: JSON, YAML, TOML. INI es opcional pero recomendado.

**P: ¿Cómo implemento dot notation?**
R: Usa __getattr__ y __setattr__. Devuelve un objeto Config para anidamiento.

**P: ¿Cómo hago el merge?**
R: Recursivamente. Si ambos son dicts, mergea keys. Si no, el user override defaults.

**P: ¿Debo soportar comentarios?**
R: YAML y TOML los soportan nativamente. JSON no. Preserva cuando sea posible.

**P: ¿Cómo valido esquemas?**
R: Usa Pydantic. Define un modelo con los campos esperados y sus tipos.

---

## Checklist Final

- [ ] Estructura src layout
- [ ] pyproject.toml configurado
- [ ] Parsers para JSON, YAML, TOML
- [ ] Dot notation funcionando
- [ ] ABCs implementadas
- [ ] Modelos Pydantic
- [ ] Merge de configs
- [ ] Conversión entre formatos
- [ ] Tests para todos los formatos
- [ ] 80%+ cobertura
- [ ] CLI funcional
- [ ] README con ejemplos
- [ ] Código pasa ruff

---

¡Éxito! Un buen config manager hace la vida más fácil a todos los desarrolladores.
