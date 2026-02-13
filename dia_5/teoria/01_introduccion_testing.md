# Introducción al Testing

## Contexto: Por Qué Importa

**Problema real en Data/IA**:

Tu pipeline de limpieza de datos funciona correctamente con el CSV de desarrollo. Lo despliegas a producción el viernes por la tarde. El lunes descubres que el CSV de producción tenía una columna con valores vacíos que tu función `parse_float` no manejaba — no lanzó error, simplemente convirtió `""` a `0.0`. Tu modelo se entrenó con ceros donde debería haber NaN. Los resultados del fin de semana son basura. Tres días de cómputo perdidos.

**Ejemplo concreto**:

Un equipo desarrolla un procesador de texto para NLP. La función `normalize_text` hace lowercase, elimina acentos y colapsa espacios. Funciona con los 20 ejemplos del notebook. En producción recibe un documento con caracteres Unicode exóticos (emojis, caracteres CJK, zero-width spaces). La función no falla — simplemente produce texto corrupto que contamina el embedding store. Sin tests, nadie se entera hasta que los usuarios reportan resultados irrelevantes semanas después.

**Consecuencias de NO testear**:

- **Errores silenciosos**: Funciones que no fallan pero producen resultados incorrectos — el peor tipo de bug en data pipelines
- **Miedo a refactorizar**: Sin tests, cada cambio es una ruleta rusa. El código se vuelve legacy en semanas
- **Debugging en producción**: Sin tests locales, el primer lugar donde descubres bugs es en producción, a las 3 AM
- **Regresiones**: Arreglas un bug hoy, introduces otro mañana en la misma función. Sin tests, no lo sabes
- **Onboarding lento**: Un nuevo miembro del equipo no puede verificar que sus cambios no rompen nada

## El Concepto

### Principio Fundamental

> "Legacy code is simply code without tests."
>
> — Michael Feathers, *Working Effectively with Legacy Code* (Prentice Hall, 2004), Preface

Si tu código no tiene tests, ya es legacy — aunque lo hayas escrito ayer. Los tests no son un lujo ni una tarea para "cuando haya tiempo". Son la herramienta que te permite cambiar código con confianza, detectar bugs antes de que lleguen a producción, y dormir tranquilo sabiendo que tu pipeline hace lo que debe.

### Definición técnica

El **testing de software** es la práctica de verificar automáticamente que tu código se comporta como esperas. Un test es una función que ejecuta tu código con inputs conocidos y verifica que los outputs son correctos. En Python, el framework estándar de facto es **pytest**.

### Cómo funciona

1. Escribes una función de test que llama a tu código con inputs específicos
2. Usas `assert` para verificar que el resultado es el esperado
3. Ejecutas `pytest` que descubre y ejecuta todos los tests automáticamente
4. pytest reporta qué tests pasaron (verde) y cuáles fallaron (rojo) con detalle del error

### Terminología clave

- **Unit test**: Test que verifica una función o clase aislada, sin dependencias externas
- **Functional test**: Test que verifica un flujo completo de entrada → salida, con I/O real
- **Test fixture**: Código de preparación que configura el estado necesario para un test (datos, ficheros, objetos)
- **Mock**: Objeto falso que simula una dependencia externa (fichero, API, BD) para aislar lo que quieres testear
- **Cobertura (coverage)**: Porcentaje de líneas de tu código que son ejecutadas por al menos un test
- **Patrón AAA**: Arrange (preparar datos), Act (ejecutar código), Assert (verificar resultado)
- **Regresión**: Bug que aparece en código que antes funcionaba, típicamente al hacer cambios

## La Pirámide de Testing

### Por Qué Importa

Sin una estrategia clara de qué testear y cómo, los equipos tienden a dos extremos: no testear nada ("no hay tiempo") o testear todo con tests E2E lentos y frágiles que nadie mantiene. La pirámide de testing es un modelo mental que te dice cuántos tests de cada tipo necesitas.

En data engineering y AI, la base de la pirámide (unit tests) es especialmente importante porque las funciones de transformación de datos son puras y fáciles de testear — y son exactamente donde los bugs silenciosos causan más daño.

### La Pirámide Visual

```
        /‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\
       /     E2E Tests       \        Pocos, lentos, frágiles
      /   (pipeline entero)   \       Solo camino crítico
     /‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\
    /   Integration Tests       \     Algunos, velocidad media
   /   (componentes juntos)      \    Con mocks parciales
  /‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\
 /   Functional Tests (I/O)        \  Varios por flujo I/O
/   (fichero entra → fichero sale)  \ Con tmp_path, sin mocks
/‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\
/         Unit Tests                    \ Muchos, rápidos, estables
/ (una función aislada, sin I/O)         \ La base de todo
/‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\
```

### Tabla Comparativa

| Tipo | ¿Qué prueba? | Ejemplo en AI/Data | Velocidad | Cantidad |
|------|--------------|-------------------|-----------|----------|
| Unit | Una función aislada | `clean_text(" Hello ")` → `"hello"` | Rápido (ms) | Muchos (70-80%) |
| Functional | Entrada → Salida real | Fichero CSV entra → fichero JSON sale | Medio (ms-seg) | Varios (15-20%) |
| Integration | Componentes juntos | Leer CSV + limpiar + validar schema | Medio (segundos) | Pocos (5-10%) |
| E2E | Flujo completo | Pipeline entero desde API hasta output | Lento (minutos) | Mínimos (1-5%) |

## Ejemplo Incorrecto

```python
# test_pipeline.py — Un solo test E2E gigante que intenta probarlo todo
import subprocess

def test_entire_pipeline():
    """Test que ejecuta el pipeline entero y verifica el output."""
    # Requiere: BD Postgres levantada, S3 con datos, modelo descargado...
    result = subprocess.run(
        ["python", "run_pipeline.py", "--config", "prod_config.yaml"],
        capture_output=True,
    )
    assert result.returncode == 0
    # ¿Qué falló exactamente si returncode != 0? No sabemos.
    # ¿Cuánto tarda? 15 minutos.
    # ¿Funciona en el portátil de un nuevo dev? No.
```

**Problemas**:

- Test lento (minutos): nadie lo ejecuta durante el desarrollo
- Frágil: falla si la BD no está levantada, si S3 está caído, si cambió el schema...
- Sin diagnóstico: si falla, solo sabes que "algo" no funcionó — no qué
- No aislado: un error en la función `clean_text` y un error en la conexión a BD producen el mismo síntoma
- Imposible de ejecutar en CI sin infraestructura completa

## Ejemplo Correcto

```python
# La pirámide en la práctica:

# ======== UNIT TESTS (muchos, rápidos, aislados) ========

def test_clean_text_removes_extra_spaces():
    """Una función, un comportamiento, un assert."""
    assert clean_text("hello   world") == "hello world"

def test_clean_text_handles_empty_string():
    assert clean_text("") == ""

def test_validate_email_rejects_missing_at():
    assert validate_email("invalidemail.com") is False

# ======== FUNCTIONAL TESTS (algunos, I/O real) ========

def test_csv_processing_produces_valid_output(tmp_path):
    """Entrada real → proceso → salida real."""
    input_file = tmp_path / "input.csv"
    input_file.write_text("name,age\nAlice,30\n")
    
    output_file = tmp_path / "output.csv"
    process_csv(str(input_file), str(output_file))
    
    result = output_file.read_text()
    assert "Alice" in result

# ======== INTEGRATION TESTS (pocos, componentes juntos) ========

def test_pipeline_reads_and_transforms(mock_db, tmp_path):
    """Dos componentes reales trabajando juntos."""
    # mock_db simula la BD, pero el CSV es real
    ...

# ======== E2E (mínimos, solo camino crítico) ========
# Se ejecutan solo en CI, no en cada commit
```

**Ventajas**:

- Los unit tests se ejecutan en milisegundos — los corres constantemente
- Si falla `test_clean_text_removes_extra_spaces`, sabes exactamente qué se rompió
- No necesitas infraestructura para el 80% de tus tests
- Cada test es independiente — un fallo no contamina otros
- Los nuevos miembros del equipo pueden ejecutar tests desde el primer día

## Aprendizaje Clave

**Puntos críticos a recordar**:

1. Los tests no son opcionales — son la red de seguridad que te permite cambiar código con confianza
2. La pirámide de testing te guía: muchos unit tests rápidos en la base, pocos E2E en la cima
3. En data/AI, los bugs silenciosos (resultados incorrectos sin error) son los más peligrosos

**Cómo desarrollar intuición**:

- **Pregúntate**: "¿Qué tipo de test necesita este código?"
  - Si es una función pura (input → output, sin I/O) → Unit test
  - Si lee/escribe ficheros → Functional test con `tmp_path`
  - Si llama a API externa → Unit test con mock
  - Si es el flujo completo → E2E (solo para camino crítico)

**Cuándo usar / NO usar**:

- **Usar tests cuando**:
  - Escribes funciones de transformación de datos
  - Implementas validaciones o parsers
  - Tienes lógica de negocio que puede cambiar
  - Quieres refactorizar sin miedo
  
- **NO necesitas tests para**:
  - Wrappers triviales de una línea sin lógica
  - Código de configuración estático
  - Scripts de un solo uso

**Referencia oficial**: [pytest Documentation - Getting Started](https://docs.pytest.org/en/stable/getting-started.html)

## Resumen

Los tests son tu primera línea de defensa contra bugs en producción. La pirámide de testing te dice que la mayoría de tus tests deben ser unit tests rápidos y aislados (70-80%), complementados con functional tests para I/O (15-20%), algunos integration tests (5-10%), y mínimos E2E (1-5%). En data engineering y AI, donde los bugs silenciosos pueden contaminar datasets enteros, los tests no son un lujo — son esenciales.
