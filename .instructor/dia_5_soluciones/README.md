# Soluciones - Día 5: Testing para AI Engineers

Este directorio contiene las soluciones completas para los ejercicios del día 5.

## Archivos

- `SOLUCION_EJERCICIO_1.py` - Solución completa para Text Normalizer
- `SOLUCION_EJERCICIO_2.py` - Solución completa para Record Validator
- `SOLUCION_EJERCICIO_3.py` - Solución completa para Log Processor

## Uso

### Copiar soluciones al proyecto de ejercicios

```bash
# Desde la raíz del repositorio
cp .instructor/dia_5_soluciones/SOLUCION_EJERCICIO_1.py dia_5/exercises/tests/test_search_normalizer.py
cp .instructor/dia_5_soluciones/SOLUCION_EJERCICIO_2.py dia_5/exercises/tests/test_record_validator.py
cp .instructor/dia_5_soluciones/SOLUCION_EJERCICIO_3.py dia_5/exercises/tests/test_log_processor.py
```

### Ejecutar tests con soluciones

```bash
cd dia_5/exercises
uv sync
uv run pytest tests/ -v
uv run pytest tests/ -v --cov=src --cov-report=term-missing
```

## Cobertura Esperada

Con las soluciones completas, la cobertura debería ser:

- Ejercicio 1 (search_normalizer): ~95-100%
- Ejercicio 2 (record_validator): ~95-100%
- Ejercicio 3 (log_processor): ~95-100%

## Notas para Instructores

### Ejercicio 1: Text Normalizer

**Conceptos clave**:
- Patrón AAA (Arrange, Act, Assert)
- Nombres de test descriptivos
- Casos borde (empty string, solo espacios, etc.)

**Tiempo estimado**: 50 minutos

**Dificultades comunes**:
- Olvidar casos borde
- Nombres de test genéricos (test_1, test_2)
- No seguir el patrón AAA

### Ejercicio 2: Record Validator

**Conceptos clave**:
- `@pytest.mark.parametrize` para múltiples inputs
- Fixtures para datos reutilizables
- Mocks con `patch` y `mock_open`

**Tiempo estimado**: 50 minutos (25 min parte A + 25 min parte B)

**Dificultades comunes**:
- Sintaxis de `parametrize` (olvidar la lista de tuplas)
- Path correcto en `patch` (debe ser donde se importa, no donde se define)
- Olvidar `return_value` en mocks

### Ejercicio 3: Log Processor

**Conceptos clave**:
- Functional tests con `tmp_path`
- Verificación de I/O real (ficheros CSV)
- Fixtures reutilizables para ficheros de test

**Tiempo estimado**: 55 minutos (15 min parte A + 30 min parte B + 10 min review)

**Dificultades comunes**:
- Usar rutas fijas en vez de `tmp_path`
- No verificar el contenido del CSV, solo que existe
- Olvidar encoding UTF-8 para tests de Unicode

## Criterios de Evaluación

Para cada ejercicio, verificar:

- [ ] Tests siguen el patrón AAA
- [ ] Nombres descriptivos
- [ ] Cobertura ≥ 90%
- [ ] Todos los tests pasan
- [ ] Código pasa ruff sin errores

## Extensiones Opcionales

Si los estudiantes terminan antes, pueden:

1. **Ejercicio 1**: Añadir tests para caracteres Unicode exóticos (emojis, CJK)
2. **Ejercicio 2**: Añadir validaciones adicionales (phone, URL, etc.)
3. **Ejercicio 3**: Añadir soporte para múltiples formatos de salida (JSON, Parquet)

## Recursos Adicionales

- [pytest Documentation](https://docs.pytest.org/)
- [unittest.mock Documentation](https://docs.python.org/3/library/unittest.mock.html)
- [Working Effectively with Legacy Code](https://www.oreilly.com/library/view/working-effectively-with/0131177052/)
