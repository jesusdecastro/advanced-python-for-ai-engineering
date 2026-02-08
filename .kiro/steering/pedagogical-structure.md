# Estructura Pedagógica del Curso

## Filosofía de Enseñanza

**Objetivo Principal**: Desarrollar intuición profunda, no memorización superficial.

**Principios Fundamentales**:
1. **Contexto antes de sintaxis**: Siempre empezar con problema real de Data/IA
2. **Profundidad sobre amplitud**: Mejor entender bien 5 conceptos que superficialmente 20
3. **Contraste para criterio**: Mostrar MAL vs BIEN para desarrollar juicio
4. **Autodescubrimiento guiado**: Ejercicios con soluciones ocultas

## Estructura OBLIGATORIA para Cada Concepto

### 1. CONTEXTO (Por qué importa)

```markdown
#### 🎯 Contexto: Por Qué Importa

**Problema real en Data/IA**: 
[Descripción específica del problema que resuelve este concepto en el contexto de ML/Data Science]

**Ejemplo concreto para juniors**:
[Situación específica que un desarrollador junior puede entender y relacionar]

**Consecuencias de NO usarlo**:
- Consecuencia técnica 1 (con impacto medible)
- Consecuencia de negocio 2
- Consecuencia de escalabilidad 3
```

**Ejemplo**:
```markdown
#### 🎯 Contexto: Por Qué Importa

**Problema real en Data/IA**: 
Estás procesando un dataset de 10 millones de registros de transacciones. 
Necesitas filtrar, transformar y agregar datos constantemente.

**Ejemplo concreto para juniors**:
Tienes una lista de 10,000 precios de productos. Necesitas:
1. Filtrar solo productos > $100
2. Aplicar 20% descuento
3. Crear diccionario producto → precio_final

**Consecuencias de NO usarlo**:
- Código 3-5x más largo (más lugares para bugs)
- 20-30% más lento en ejecución
- Difícil de leer y mantener
```

### 2. CONCEPTO PURO

```markdown
#### 📚 El Concepto

**Definición técnica**:
[Definición precisa y técnica del concepto]

**Cómo funciona internamente**:
1. Paso 1 del proceso interno
2. Paso 2 del proceso interno
3. Paso 3 del proceso interno

**Terminología clave**:
- **Término 1**: Explicación clara
- **Término 2**: Explicación clara
```

**Ejemplo**:
```markdown
#### 📚 El Concepto

**Definición técnica**:
Sintaxis compacta para crear listas/dicts/sets a partir de iterables, 
con transformación y filtrado opcional en una sola expresión.

**Cómo funciona internamente**:
1. Python crea estructura vacía (lista/dict/set)
2. Itera sobre el iterable
3. Aplica filtro (if) si existe
4. Aplica transformación a cada elemento
5. Añade resultado a la estructura

**Terminología clave**:
- **Expresión**: La transformación aplicada a cada elemento
- **Iterable**: La fuente de datos (lista, range, etc.)
- **Condición**: Filtro opcional con if
```

### 3. EJEMPLOS MAL vs BIEN

```markdown
#### ❌ Ejemplo Incorrecto

**Código**:
```python
# Código que NO debes hacer
[código mal implementado]
```

**Problemas**:
- Problema específico 1
- Problema específico 2
- Problema específico 3

#### ✅ Ejemplo Correcto

**Código**:
```python
# Código que SÍ debes hacer
[código bien implementado]
```

**Ventajas**:
- Ventaja específica 1
- Ventaja específica 2
- Ventaja específica 3

#### 📊 Comparación Lado a Lado

| Aspecto | Incorrecto | Correcto |
|---------|-----------|----------|
| Líneas de código | X | Y |
| Legibilidad | Baja | Alta |
| Performance | Lenta | Rápida |
```

### 4. APRENDIZAJE CLAVE

```markdown
#### 💡 Aprendizaje Clave

**Puntos críticos a recordar**:
1. Punto esencial 1
2. Punto esencial 2
3. Punto esencial 3

**Cómo desarrollar intuición**:
- **Pregúntate**: "[Pregunta clave para tomar decisión]"
  - Si [condición] → [acción recomendada]
  - Si [condición] → [acción alternativa]

**Cuándo usar / NO usar**:
- ✅ **Usar cuando**:
  - Caso de uso 1
  - Caso de uso 2
- ❌ **NO usar cuando**:
  - Caso donde no aplica 1
  - Caso donde no aplica 2

**Referencia oficial**: [Nombre del recurso](URL)
```

## Estructura de Ejercicios

### Formato OBLIGATORIO

**1. Celda Markdown - Instrucciones**:
```markdown
## 🏋️ Ejercicio [N]: [Título Descriptivo]

**Objetivo**: [Qué concepto específico van a practicar]

**Contexto real**: 
[Situación del mundo real donde aplicarían esto en Data/IA]

**Instrucciones**:
1. Paso específico 1
2. Paso específico 2
3. Paso específico 3

**Criterios de éxito**:
- [ ] Criterio 1
- [ ] Criterio 2
```

**2. Celda Python - Para Completar**:
```python
# TODO: Completa esta función
def exercise_function(param: type) -> return_type:
    """
    [Docstring completo en formato Sphinx]
    
    :param param: [Descripción]
    :type param: [Tipo]
    :return: [Descripción]
    :rtype: [Tipo]
    
    Example:
        >>> exercise_function(input)
        expected_output
    """
    # Tu código aquí
    pass

# Tests de validación
assert exercise_function(test_input_1) == expected_output_1
assert exercise_function(test_input_2) == expected_output_2
print("✅ Todos los tests pasaron!")
```

**3. Celda Markdown - Solución Oculta**:
```markdown
<details>
<summary><b>💡 Pista 1</b></summary>

[Pista general sobre el enfoque]

</details>

<details>
<summary><b>💡 Pista 2</b></summary>

[Pista más específica sobre la implementación]

</details>

<details>
<summary><b>✅ Ver Solución Completa</b></summary>

```python
def exercise_function(param: type) -> return_type:
    """[Docstring completo]"""
    # Solución implementada
    return result
```

**Explicación paso a paso**:
1. Por qué este enfoque funciona
2. Conceptos clave aplicados
3. Alternativas posibles y trade-offs

**Conexión con conceptos**:
- Concepto 1: Cómo se aplica aquí
- Concepto 2: Cómo se aplica aquí

</details>
```

## Preguntas para Desarrollar Intuición

Cada concepto debe incluir una "pregunta clave" que ayude a tomar decisiones:

### Ejemplos de Preguntas Clave

**Comprehensions**:
- "¿Puedo leer esto en voz alta naturalmente?"
  - SÍ → usa comprehension
  - NO → usa loop tradicional

**Generators**:
- "¿Los datos caben en RAM?"
  - NO → generator obligatorio
  - SÍ → lista está bien

**Context Managers**:
- "¿Este recurso necesita cerrarse?"
  - SÍ → usa `with`
  - NO → no necesario

**Decorators**:
- "¿Este código se repite en múltiples funciones?"
  - SÍ → considera decorator
  - NO → déjalo en la función

**`__init__.py`**:
- "¿Otros van a usar este paquete?"
  - SÍ → configura `__init__.py` bien
  - NO → puede estar vacío (pero úsalo igual)

## Niveles de Profundidad

### Nivel 1: Superficial (❌ Evitar)
- Solo sintaxis
- Sin contexto
- Sin explicar por qué

### Nivel 2: Funcional (⚠️ Mínimo aceptable)
- Sintaxis + ejemplo
- Contexto básico
- Cuándo usar

### Nivel 3: Profundo (✅ Objetivo)
- Sintaxis + cómo funciona internamente
- Contexto real de Data/IA
- Por qué existe
- Cuándo usar / NO usar
- Cómo desarrollar intuición
- Ejemplos contrastantes (MAL vs BIEN)

## Checklist para Cada Concepto

Antes de considerar un concepto "completo", verificar:

- [ ] Tiene sección de CONTEXTO con problema real de Data/IA
- [ ] Tiene ejemplo concreto que juniors entienden
- [ ] Explica consecuencias de NO usarlo
- [ ] Define el concepto técnicamente
- [ ] Explica cómo funciona internamente
- [ ] Tiene ejemplo INCORRECTO con explicación
- [ ] Tiene ejemplo CORRECTO con explicación
- [ ] Tiene comparación lado a lado
- [ ] Tiene "pregunta clave" para desarrollar intuición
- [ ] Tiene criterios claros de cuándo usar/no usar
- [ ] Tiene referencia oficial
- [ ] Tiene al menos 1 ejercicio práctico
- [ ] Ejercicio tiene solución oculta con HTML details
- [ ] Ejercicio tiene explicación paso a paso en solución

## Errores Comunes a Evitar

### ❌ NO Hacer

1. **Empezar con sintaxis**: "List comprehensions se escriben así: [x for x in...]"
2. **Solo mostrar código correcto**: Sin contraste, no desarrollan criterio
3. **Ejemplos triviales**: `[x*2 for x in range(10)]` no muestra valor real
4. **Soluciones visibles**: Quita oportunidad de autodescubrimiento
5. **Sin conexión con Data/IA**: Ejemplos genéricos que no resuenan

### ✅ SÍ Hacer

1. **Empezar con problema**: "Tienes 10M de registros y necesitas..."
2. **Mostrar MAL y BIEN**: Desarrolla criterio por contraste
3. **Ejemplos realistas**: Casos que encontrarán en trabajo real
4. **Soluciones ocultas**: Permite intentar antes de ver respuesta
5. **Contexto de Data/IA**: Ejemplos con datasets, modelos, APIs

## Medición de Éxito

Un concepto está bien enseñado cuando el alumno puede:

1. **Explicar por qué existe**: No solo qué es, sino por qué lo necesitamos
2. **Identificar cuándo usarlo**: Dado un problema, sabe si aplica
3. **Reconocer mal uso**: Puede ver código y decir "esto está mal porque..."
4. **Aplicar en contexto nuevo**: No solo reproduce ejemplos, sino adapta
5. **Desarrollar intuición**: Toma decisiones correctas sin memorizar reglas

## Recursos para Instructores

### Preparación de Conceptos

Antes de enseñar un concepto, prepara:

1. **3 problemas reales** donde se usa en Data/IA
2. **2 ejemplos incorrectos** comunes que juniors hacen
3. **1 pregunta clave** para desarrollar intuición
4. **5 criterios** de cuándo usar/no usar
5. **2 referencias oficiales** (PEP, docs, artículos)

### Durante la Clase

1. **Empieza con problema**: Nunca con sintaxis
2. **Muestra código malo primero**: Genera empatía
3. **Pregunta antes de responder**: "¿Por qué creen que esto es problema?"
4. **Conecta con experiencia**: "¿Han visto esto en su código?"
5. **Valida intuición**: "Su instinto es correcto porque..."

### Después de Enseñar

1. **Verifica comprensión profunda**: No solo "¿entendieron?" sino "¿cuándo NO usarían esto?"
2. **Pide que expliquen a compañero**: La mejor forma de verificar entendimiento
3. **Revisa ejercicios**: Busca patrones de errores comunes
4. **Ajusta ejemplos**: Si muchos fallan, el ejemplo no es claro
5. **Documenta preguntas**: Las preguntas frecuentes mejoran el material

## Mantenimiento del Material

### Señales de que un concepto necesita mejora:

- Muchos alumnos fallan el ejercicio
- Preguntas repetidas sobre lo mismo
- Alumnos memorizan sin entender
- No pueden aplicar en contexto diferente
- Dicen "entiendo pero no sé cuándo usarlo"

### Cómo mejorar:

1. Añadir más contexto real
2. Mejorar ejemplo incorrecto (más realista)
3. Añadir más pistas en ejercicio
4. Clarificar pregunta clave para intuición
5. Añadir más criterios de cuándo usar/no usar
