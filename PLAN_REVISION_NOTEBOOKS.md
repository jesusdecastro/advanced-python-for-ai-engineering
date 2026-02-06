# Plan de Revisión de Notebooks - Day 1

## Estado Actual vs Objetivo

### Problemas Identificados en Notebooks Actuales:
1. ❌ Empiezan con sintaxis, no con problema
2. ❌ No explican consecuencias de NO usar
3. ❌ Solo muestran código correcto (sin contraste)
4. ❌ Ejemplos triviales sin contexto Data/IA
5. ❌ No desarrollan intuición
6. ❌ Ejercicios sin soluciones ocultas
7. ❌ Superficiales (Nivel 1-2, necesitamos Nivel 3)

### Objetivo:
Aplicar estructura pedagógica completa a TODOS los notebooks.

---

## 01_python_idioms_intro.ipynb

### Cambios Necesarios:

#### COMPREHENSIONS

**ANTES** (Actual):
```markdown
## 1. Comprehensions - Elegancia en una Línea
### El Problema
Necesitas transformar una lista de números...
```

**DESPUÉS** (Mejorado):
```markdown
## 1. List Comprehensions

#### 🎯 Contexto: Por Qué Importa

**Problema real en Data/IA**: 
Estás procesando un dataset de 10 millones de registros de transacciones bancarias.
Necesitas filtrar transacciones sospechosas (>$10,000), aplicar normalización,
y crear un diccionario cliente → total_transacciones. Esto lo haces 100 veces al día.

**Ejemplo concreto para juniors**:
Tienes una lista de 10,000 precios de productos de un e-commerce. Necesitas:
1. Filtrar solo productos caros (> $100)
2. Aplicar 20% descuento
3. Crear diccionario producto → precio_final

Sin comprehensions: 15 líneas, 4 lugares para bugs, difícil de leer.
Con comprehensions: 1 línea, intención clara.

**Consecuencias de NO usarlo**:
- Código 3-5x más largo → más tiempo de desarrollo
- 20-30% más lento en ejecución → impacta en producción
- Más lugares para bugs → más tiempo debugging
- Difícil de mantener → otros desarrolladores sufren
- No es idiomático → code reviews negativas

#### 📚 El Concepto

**Definición técnica**:
Sintaxis compacta para crear listas/dicts/sets a partir de iterables,
con transformación y filtrado opcional en una sola expresión.

**Cómo funciona internamente**:
1. Python crea estructura vacía (lista/dict/set)
2. Itera sobre el iterable fuente
3. Para cada elemento, evalúa condición (if) si existe
4. Si pasa filtro, aplica transformación
5. Añade resultado a la estructura
6. Retorna estructura completa

**Terminología clave**:
- **Expresión**: La transformación aplicada (`num ** 2`)
- **Iterable**: La fuente de datos (`numbers`, `range(10)`)
- **Condición**: Filtro opcional (`if num % 2 == 0`)
- **Comprehension**: La expresión completa

**Sintaxis**:
```python
# Lista
[expresion for item in iterable if condicion]

# Dict
{key: value for item in iterable if condicion}

# Set
{expresion for item in iterable if condicion}
```

#### ❌ Ejemplo Incorrecto

**Código**:
```python
# Problema: Código verboso y propenso a errores
products = [
    {'name': 'Laptop', 'price': 1200},
    {'name': 'Mouse', 'price': 25},
    {'name': 'Monitor', 'price': 300},
]

# Filtrar productos caros
expensive = []
for product in products:
    if product['price'] > 100:
        expensive.append(product)

# Aplicar descuento
discounted = []
for product in expensive:
    discounted.append(product['price'] * 0.8)

# Crear diccionario
result = {}
for i, product in enumerate(expensive):
    result[product['name']] = discounted[i]

print(result)
```

**Problemas**:
- 15 líneas para algo simple
- 3 listas intermedias (expensive, discounted, result)
- 4 lugares donde meter bugs (cada loop, cada append)
- Difícil ver la intención (¿qué estamos haciendo?)
- No es idiomático Python

#### ✅ Ejemplo Correcto

**Código**:
```python
# Solución: Una línea, intención clara
products = [
    {'name': 'Laptop', 'price': 1200},
    {'name': 'Mouse', 'price': 25},
    {'name': 'Monitor', 'price': 300},
]

result = {p['name']: p['price'] * 0.8 
          for p in products if p['price'] > 100}

print(result)  # {'Laptop': 960.0, 'Monitor': 240.0}
```

**Ventajas**:
- 1 línea vs 15 líneas
- Intención clara: "dame dict de nombres → precios con descuento para productos caros"
- Sin variables intermedias
- Más rápido (20-30%)
- Idiomático Python

#### 📊 Comparación Lado a Lado

| Aspecto | Loop Tradicional | Comprehension |
|---------|------------------|---------------|
| Líneas de código | 15 | 1-3 |
| Variables intermedias | 3 | 0 |
| Lugares para bugs | 4+ | 1 |
| Legibilidad | Baja (ejecutar mentalmente) | Alta (leer como frase) |
| Performance | Baseline | 20-30% más rápido |
| Idiomático | No | Sí |

#### 💡 Aprendizaje Clave

**Puntos críticos a recordar**:
1. Comprehensions son EXPRESIONES, loops son STATEMENTS
2. Úsalas para transformar/filtrar, no para efectos secundarios
3. Máximo 2 condiciones, sino usa loop tradicional
4. Si necesitas explicar qué hace, usa loop

**Cómo desarrollar intuición**:
- **Pregúntate**: "¿Puedo leer esto en voz alta naturalmente?"
  - SÍ → usa comprehension
  - NO → usa loop tradicional

- **Pregúntate**: "¿Estoy creando una nueva estructura de datos?"
  - SÍ → comprehension es ideal
  - NO (solo efectos secundarios) → usa loop

**Cuándo usar / NO usar**:
- ✅ **Usar cuando**:
  - Transformas lista → lista/dict/set
  - Filtras elementos
  - Mapeas valores
  - Lógica simple (1-2 condiciones)
  
- ❌ **NO usar cuando**:
  - Lógica compleja (>2 condiciones anidadas)
  - Efectos secundarios (print, modificar variables)
  - Múltiples transformaciones encadenadas
  - Hace código menos legible

**Referencia oficial**: [PEP 202 - List Comprehensions](https://peps.python.org/pep-0202/)
```

#### EJERCICIO

**Añadir después de la explicación**:

```markdown
## 🏋️ Ejercicio 1: Filtrar y Transformar Datos

**Objetivo**: Practicar list y dict comprehensions con filtrado

**Contexto real**: 
Trabajas en un e-commerce. Tienes datos de ventas y necesitas generar
un reporte de productos más vendidos con descuento aplicado.

**Instrucciones**:
1. Filtra productos con ventas > 50 unidades
2. Aplica 15% descuento al precio
3. Crea diccionario producto → precio_con_descuento

**Criterios de éxito**:
- [ ] Usa dict comprehension (no loops)
- [ ] Filtra correctamente (> 50 unidades)
- [ ] Aplica descuento correcto (precio * 0.85)
- [ ] Tests pasan
```

```python
# TODO: Completa esta función
def get_discounted_bestsellers(sales_data: list[dict]) -> dict[str, float]:
    """
    Get bestselling products with discount applied.
    
    :param sales_data: List of dicts with 'product', 'price', 'units_sold'
    :type sales_data: list[dict]
    :return: Dict of product -> discounted_price for bestsellers
    :rtype: dict[str, float]
    
    Example:
        >>> data = [
        ...     {'product': 'Laptop', 'price': 1000, 'units_sold': 100},
        ...     {'product': 'Mouse', 'price': 20, 'units_sold': 30},
        ... ]
        >>> get_discounted_bestsellers(data)
        {'Laptop': 850.0}
    """
    # Tu código aquí (1 línea con dict comprehension)
    pass

# Tests
sales_data = [
    {'product': 'Laptop', 'price': 1000, 'units_sold': 100},
    {'product': 'Mouse', 'price': 20, 'units_sold': 30},
    {'product': 'Keyboard', 'price': 80, 'units_sold': 75},
    {'product': 'Monitor', 'price': 300, 'units_sold': 45},
]

result = get_discounted_bestsellers(sales_data)
assert result == {'Laptop': 850.0, 'Keyboard': 68.0}
assert len(result) == 2
print("✅ Todos los tests pasaron!")
```

```markdown
<details>
<summary><b>💡 Pista 1</b></summary>

Recuerda la sintaxis de dict comprehension:
```python
{key: value for item in lista if condicion}
```

</details>

<details>
<summary><b>💡 Pista 2</b></summary>

- Filtra con: `if item['units_sold'] > 50`
- Descuento: `item['price'] * 0.85`
- Key: nombre del producto
- Value: precio con descuento

</details>

<details>
<summary><b>✅ Ver Solución Completa</b></summary>

```python
def get_discounted_bestsellers(sales_data: list[dict]) -> dict[str, float]:
    """Get bestselling products with discount applied."""
    return {item['product']: item['price'] * 0.85 
            for item in sales_data if item['units_sold'] > 50}
```

**Explicación paso a paso**:
1. `for item in sales_data`: Itera sobre cada producto
2. `if item['units_sold'] > 50`: Filtra solo bestsellers
3. `item['product']`: Key del diccionario (nombre)
4. `item['price'] * 0.85`: Value (precio con 15% descuento)
5. `{...}`: Crea diccionario con resultados

**Por qué funciona**:
- Dict comprehension crea diccionario en una expresión
- Filtro `if` se aplica antes de crear cada entrada
- Transformación (descuento) se aplica al value
- Resultado: solo bestsellers con descuento

**Alternativas**:
```python
# Alternativa 1: Más explícita (menos pythonic)
result = {}
for item in sales_data:
    if item['units_sold'] > 50:
        result[item['product']] = item['price'] * 0.85
return result

# Alternativa 2: Con filter y map (funcional)
bestsellers = filter(lambda x: x['units_sold'] > 50, sales_data)
return {item['product']: item['price'] * 0.85 for item in bestsellers}
```

**Conexión con conceptos**:
- **Comprehension**: Crea estructura nueva de forma declarativa
- **Filtrado**: `if` elimina elementos que no cumplen condición
- **Transformación**: Aplica operación a cada elemento
- **Expresión**: Todo en una línea, retorna valor directamente

</details>
```

---

### Aplicar Mismo Patrón a:
- Generators
- Context Managers
- Decorators

Cada uno necesita:
1. 🎯 Contexto con problema real Data/IA
2. 📚 Concepto puro con funcionamiento interno
3. ❌✅ Ejemplos MAL vs BIEN
4. 💡 Aprendizaje clave con pregunta para intuición
5. 🏋️ Ejercicio con solución oculta

---

## Notebooks Restantes

### 02_virtual_environments.ipynb
- Añadir contexto: Por qué entornos virtuales en proyectos ML
- Explicar problema de `pip freeze` en profundidad
- Comparar venv vs uv con ejemplos reales
- Ejercicio: Crear entorno y gestionar dependencias

### 03_modules_and_imports.ipynb
- Contexto: Organizar proyecto ML grande
- Profundizar en `__init__.py` (ya tenemos ejemplos)
- Ejercicio: Crear paquete con API limpia

### 04_type_hinting.ipynb
- Contexto: Prevenir bugs en pipelines de datos
- Ejemplos MAL vs BIEN con mypy
- Ejercicio: Añadir type hints a código existente

### 05_code_quality_tools.ipynb
- Contexto: Mantener calidad en equipo
- Configurar Ruff, pre-commit
- Ejercicio: Configurar CI/CD para calidad

### 06_package_distribution.ipynb
- Contexto: Compartir librería ML con equipo
- Crear pyproject.toml completo
- Ejercicio: Publicar paquete a PyPI test

---

## Prioridades

1. ✅ **HECHO**: Documentos de conceptos creados
2. ✅ **HECHO**: Steering documents actualizados
3. ✅ **HECHO**: Plan de revisión creado
4. ✅ **HECHO**: 01_python_idioms_intro.ipynb completamente revisado
5. 🔄 **EN PROGRESO**: Aplicar a notebooks restantes

---

## Próximos Pasos

1. Revisar este plan
2. Aplicar estructura a 01_python_idioms_intro.ipynb completamente
3. Continuar con notebooks restantes
4. Verificar que cada concepto cumple checklist pedagógico
5. Añadir ejercicios con soluciones ocultas a todos

---

## Notas para Implementación

- Cada concepto debe tomar 15-20 minutos de lectura
- Ejercicios deben tomar 10-15 minutos
- Total por notebook: 60-90 minutos
- Profundidad > Amplitud
- Siempre contexto Data/IA primero
