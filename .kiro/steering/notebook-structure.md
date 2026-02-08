# Estructura de Notebooks para el Curso

## Propósito

Este documento define el estándar para crear notebooks educativos en el curso de Python Avanzado para IA. Asegura consistencia, calidad y efectividad en la retención de conceptos.

## Filosofía Pedagógica

**Objetivo**: Que los alumnos desarrollen intuición profunda, no solo memoricen sintaxis.

**Principios**:
1. **Contexto primero**: Siempre empezar con problema real de Data/IA
2. **Profundidad sobre amplitud**: Mejor entender bien 5 conceptos que superficialmente 20
3. **Ejemplos contrastantes**: Mostrar MAL vs BIEN para desarrollar criterio
4. **Práctica guiada**: Ejercicios con soluciones ocultas para autodescubrimiento

## Estructura General del Notebook

Cada notebook debe seguir esta estructura en orden:

### 1. Título y Descripción (Markdown)
- Título principal con formato `# Día X: Tema Principal`
- Breve descripción del contenido (1-2 párrafos)
- **Conexión con Data/IA**: Por qué este tema importa en el contexto real

### 2. Objetivos de Aprendizaje (Markdown)
- Lista de 3-5 objetivos claros y medibles
- Usar formato: "Al finalizar este notebook, serás capaz de..."
- Cada objetivo debe ser verificable
- **Incluir**: Qué intuición desarrollarán

### 3. Contenido Teórico (Markdown + Código)

#### Estructura OBLIGATORIA para Cada Concepto:

##### A. CONTEXTO (Por qué importa)
```markdown
### [Nombre del Concepto]

#### 🎯 Contexto: Por Qué Importa

**Problema real en Data/IA**: [Descripción del problema que resuelve]

**Ejemplo concreto**: [Situación que un junior puede entender]

**Consecuencias de NO usarlo**:
- Consecuencia 1
- Consecuencia 2
- Consecuencia 3
```

##### B. CONCEPTO PURO
```markdown
#### 📚 El Concepto

**Definición**: [Definición técnica clara]

**Cómo funciona internamente**:
1. Paso 1
2. Paso 2
3. Paso 3

**Terminología clave**:
- Término 1: Explicación
- Término 2: Explicación
```

##### C. EJEMPLOS MAL vs BIEN
```markdown
#### ❌ Ejemplo Incorrecto

```python
# Código que NO debes hacer
# Explicación de por qué está mal
```

**Problemas**:
- Problema 1
- Problema 2

#### ✅ Ejemplo Correcto

```python
# Código que SÍ debes hacer
# Explicación de por qué está bien
```

**Ventajas**:
- Ventaja 1
- Ventaja 2
```

##### D. APRENDIZAJE CLAVE
```markdown
#### 💡 Aprendizaje Clave

**Puntos críticos a recordar**:
1. Punto 1
2. Punto 2
3. Punto 3

**Cómo desarrollar intuición**:
- Pregúntate: "[Pregunta clave]"
- Si [condición] → [acción]
- Si [condición] → [acción]

**Cuándo usar / NO usar**:
- ✅ Usar cuando: [casos]
- ❌ NO usar cuando: [casos]

**Referencia oficial:** [Nombre](URL)
```

### 4. Ejemplos Prácticos (Código)

- Código ejecutable que demuestre los conceptos
- Incluir docstrings en formato Sphinx
- Type hints en todas las funciones
- Comentarios explicativos en inglés
- Output esperado visible en las celdas

### 5. Ejercicios Prácticos (Código + Markdown)

#### Estructura OBLIGATORIA:

**Celda Markdown - Instrucciones**:
```markdown
## 🏋️ Ejercicio [N]: [Título]

**Objetivo**: [Qué van a practicar]

**Contexto**: [Situación real donde aplicarían esto]

**Instrucciones**:
1. Paso 1
2. Paso 2
3. Paso 3

**Pistas**:
- Pista 1
- Pista 2
```

**Celda Python - Para Completar**:
```python
# TODO: Completa esta función
def exercise_function(param):
    """
    [Docstring con descripción]
    
    :param param: [Descripción]
    :type param: [Tipo]
    :return: [Descripción]
    :rtype: [Tipo]
    """
    # Tu código aquí
    pass

# Test
assert exercise_function(input) == expected_output
print("✅ Test pasado!")
```

**Celda Markdown - Solución Oculta**:
```markdown
<details>
<summary><b>💡 Ver Pista Adicional</b></summary>

[Pista más específica]

</details>

<details>
<summary><b>✅ Ver Solución</b></summary>

```python
def exercise_function(param):
    """[Docstring]"""
    # Solución completa
    return result
```

**Explicación**:
- Por qué funciona esta solución
- Conceptos clave aplicados
- Alternativas posibles

</details>
```

#### Niveles de Dificultad:
- **Básico**: Aplicación directa de conceptos (1 concepto)
- **Intermedio**: Combinación de conceptos (2-3 conceptos)
- **Avanzado**: Problemas abiertos que requieren creatividad (3+ conceptos)

### 6. Resumen (Markdown)

- Recapitulación de puntos clave (3-5 puntos)
- Próximos pasos o conexión con el siguiente tema
- Motivación para continuar

### 7. Preguntas de Autoevaluación (Markdown)

#### Estructura:
```markdown
## Preguntas de Autoevaluación

### 1. [Pregunta sobre concepto clave]

**Respuesta:** [Respuesta esperada clara y concisa]

### 2. [Siguiente pregunta]

**Respuesta:** [Respuesta esperada]
```

- Mínimo 5 preguntas
- Cubrir conceptos principales
- Incluir respuestas esperadas
- Invitar a discusión con compañeros

### 8. Recursos y Referencias Oficiales (Markdown)

#### Estructura:
```markdown
## Recursos y Referencias Oficiales

### Documentación Oficial
- **[Nombre]**: [URL](URL)
  - Breve descripción de qué contiene

### Estándares/PEPs
- **[PEP XXX - Nombre]**: [URL](URL)
  - Descripción

### Herramientas Relacionadas
- **[Nombre]**: [URL](URL)
  - Descripción

### Mejores Prácticas
- **[Nombre]**: [URL](URL)
  - Descripción

### Notas Importantes
- Todos los enlaces están actualizados a partir de [AÑO]
- Se recomienda revisar la documentación oficial regularmente
```

## Estándares de Código en Notebooks

### Docstrings (Sphinx Format)
```python
def example_function(param1: str, param2: int) -> bool:
    """
    Brief description of what the function does.
    
    Longer description if needed, explaining the purpose
    and behavior in detail.
    
    :param param1: Description of param1
    :type param1: str
    :param param2: Description of param2
    :type param2: int
    :return: Description of return value
    :rtype: bool
    :raises ValueError: When something is invalid
    
    Example:
        >>> example_function("test", 42)
        True
    """
    pass
```

### Type Hints
- Usar type hints en todas las funciones
- Importar tipos de `typing` cuando sea necesario
- Usar tipos built-in cuando sea posible (Python 3.10+)

### Comentarios
- En inglés
- Explicar el "por qué", no el "qué"
- Evitar comentarios obvios

### Imports
Organizar en este orden:
1. Standard library
2. Third-party packages
3. Local modules

## Elementos Visuales

### Diagramas ASCII
Usar para visualizar conceptos complejos:
```
Proyecto A (Aislado)          Proyecto B (Aislado)
├── numpy 1.21.0              ├── numpy 1.24.0
├── pandas 1.3.0              ├── pandas 2.0.0
└── SIN CONFLICTO             └── SIN CONFLICTO
```

### Recuadros de Énfasis
Usar markdown para destacar información importante:
```markdown
### Aprendizaje Clave

[Contenido importante]

**Referencia oficial:** [Enlace](URL)
```

## Longitud y Ritmo

- **Notebooks cortos**: 30-45 minutos de lectura/práctica
- **Secciones teóricas**: 5-10 minutos cada una
- **Ejercicios**: 10-15 minutos
- **Máximo 100 celdas**: Mantener el notebook manejable

## Lenguaje

- **Documentación**: Castellano
- **Código**: Inglés
- **Comentarios en código**: Inglés
- **Docstrings**: Inglés
- **Nombres de variables/funciones**: Inglés

## Checklist para Crear un Notebook

- [ ] Título y descripción claros
- [ ] 3-5 objetivos de aprendizaje medibles
- [ ] Contenido teórico con "Aprendizaje Clave" en cada sección
- [ ] Preguntas intercaladas para mantener engagement
- [ ] Ejemplos prácticos ejecutables con docstrings
- [ ] 2-3 ejercicios progresivos
- [ ] Resumen de puntos clave
- [ ] Mínimo 5 preguntas de autoevaluación con respuestas
- [ ] Sección de recursos con enlaces oficiales actualizados
- [ ] Código pasa Ruff sin errores
- [ ] Type hints en todas las funciones
- [ ] Máximo 100 celdas
- [ ] Tiempo estimado: 45-60 minutos

## Búsqueda de Enlaces Oficiales

Para cada concepto principal:
1. Buscar documentación oficial del lenguaje/librería
2. Buscar PEPs relevantes (Python Enhancement Proposals)
3. Buscar guías de mejores prácticas
4. Verificar que los enlaces estén actualizados
5. Incluir fecha de última verificación

## Ejemplo de Sección Completa

```markdown
## Concepto Principal

Explicación clara del concepto en 2-3 párrafos.

### El Problema que Resuelve

Contexto real con ejemplo concreto.

### Visualización

```
Diagrama ASCII si es necesario
```

### Solución

Cómo el concepto resuelve el problema.

### Aprendizaje Clave

Punto más importante a recordar.

**Referencia oficial:** [Documentación](URL)

### Pregunta de Comprensión

¿Pregunta para verificar comprensión?
```

Luego en la sección de autoevaluación:

```markdown
### Respuesta a la Pregunta Anterior

**Respuesta:** Respuesta clara y concisa.
```

## Notas Finales

- La consistencia es clave para la experiencia del estudiante
- Cada notebook debe ser independiente pero conectado con los anteriores
- Priorizar la claridad sobre la brevedad
- Mantener un tono amigable y accesible
- Recordar que el objetivo es la retención de conceptos clave
