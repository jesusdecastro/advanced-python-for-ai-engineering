# Template Pedagógico para Notebooks

## Estructura OBLIGATORIA para Cada Concepto

### 1. 🎯 Contexto: Por Qué Importa

```markdown
### 🎯 Contexto: Por Qué Importa

**Problema real en Data/IA**: 
[Descripción específica del problema que resuelve este concepto en ML/Data Science]

**Ejemplo concreto para juniors**:
[Situación específica que un desarrollador junior puede entender]

**Consecuencias de NO usarlo**:
- [Consecuencia técnica 1 con impacto medible]
- [Consecuencia de negocio 2]
- [Consecuencia de escalabilidad 3]
```

### 2. 📚 El Concepto

```markdown
### 📚 El Concepto

**Definición técnica**:
[Definición precisa y técnica del concepto]

**Cómo funciona internamente**:
1. [Paso 1 del proceso interno]
2. [Paso 2 del proceso interno]
3. [Paso 3 del proceso interno]

**Terminología clave**:
- **Término 1**: Explicación clara
- **Término 2**: Explicación clara
```

### 3. ❌ Ejemplo Incorrecto

```markdown
### ❌ Ejemplo Incorrecto

**Código que NO debes hacer**:
```

### 4. ✅ Ejemplo Correcto

```markdown
### ✅ Ejemplo Correcto

**Código que SÍ debes hacer**:
```

### 5. 📊 Comparación

```markdown
### 📊 Comparación Lado a Lado

| Aspecto | Incorrecto | Correcto |
|---------|-----------|----------|
| [Aspecto 1] | [Valor] | [Valor] |
| [Aspecto 2] | [Valor] | [Valor] |
```

### 6. 💡 Aprendizaje Clave

```markdown
### 💡 Aprendizaje Clave

**Puntos críticos a recordar**:
1. [Punto esencial 1]
2. [Punto esencial 2]
3. [Punto esencial 3]

**Cómo desarrollar intuición**:
- **Pregúntate**: "[Pregunta clave para tomar decisión]"
  - Si [condición] → [acción recomendada]
  - Si [condición] → [acción alternativa]

**Cuándo usar / NO usar**:
- ✅ **Usar cuando**:
  - [Caso de uso 1]
  - [Caso de uso 2]
- ❌ **NO usar cuando**:
  - [Caso donde no aplica 1]
  - [Caso donde no aplica 2]

**Referencia oficial**: [Nombre del recurso](URL)
```

### 7. 🏋️ Ejercicio

```markdown
### 🏋️ Ejercicio [N]: [Título]

**Objetivo**: [Qué concepto específico van a practicar]

**Contexto real**: 
[Situación del mundo real donde aplicarían esto en Data/IA]

**Instrucciones**:
1. [Paso específico 1]
2. [Paso específico 2]

**Criterios de éxito**:
- [ ] [Criterio 1]
- [ ] [Criterio 2]
```

### 8. Solución Oculta

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

\```python
[Código de la solución]
\```

**Explicación paso a paso**:
1. [Por qué este enfoque funciona]
2. [Conceptos clave aplicados]
3. [Alternativas posibles y trade-offs]

**Conexión con conceptos**:
- [Concepto 1]: Cómo se aplica aquí
- [Concepto 2]: Cómo se aplica aquí

</details>
```

## Preguntas Clave por Concepto

### Comprehensions
"¿Puedo leer esto en voz alta naturalmente?"

### Generators
"¿Los datos caben en RAM?"

### Context Managers
"¿Este recurso necesita cerrarse?"

### Decorators
"¿Este código se repite en múltiples funciones?"

### Type Hints
"¿Este código será usado por otros?"

### Módulos/Imports
"¿Otros van a usar este paquete?"

### Clean Code
"¿Puedo entender esto en 30 segundos?"

### SOLID
"¿Esta clase tiene una sola responsabilidad?"

### Testing
"¿Cómo sé que esto funciona?"

## Checklist por Notebook

- [ ] Título y descripción en castellano
- [ ] Objetivos de aprendizaje claros (3-5)
- [ ] Cada concepto tiene 🎯 Contexto
- [ ] Cada concepto tiene 📚 Definición técnica
- [ ] Cada concepto tiene ❌ Ejemplo incorrecto
- [ ] Cada concepto tiene ✅ Ejemplo correcto
- [ ] Cada concepto tiene 📊 Comparación
- [ ] Cada concepto tiene 💡 Aprendizaje clave
- [ ] Cada concepto tiene pregunta para intuición
- [ ] Al menos 1 ejercicio 🏋️ por concepto
- [ ] Ejercicios tienen soluciones ocultas con `<details>`
- [ ] Referencias oficiales (PEPs, docs)
- [ ] Resumen al final
- [ ] Preguntas de autoevaluación (5+)
- [ ] Recursos y referencias oficiales

## Nivel de Profundidad Objetivo

**Nivel 3 (Profundo)**:
- Sintaxis + cómo funciona internamente
- Contexto real de Data/IA
- Por qué existe
- Cuándo usar / NO usar
- Cómo desarrollar intuición
- Ejemplos contrastantes (MAL vs BIEN)
