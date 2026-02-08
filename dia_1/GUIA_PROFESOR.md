# Guía del Profesor - Día 1

## Resumen Ejecutivo

**Duración:** 8 horas (con descansos)  
**Nivel:** Intermedio  
**Objetivo:** Establecer bases sólidas para desarrollo profesional en Python

## Estructura del Día

### Mañana (9:00 - 13:00)

**9:00 - 9:30: Bienvenida y Contexto**
- Presentación del curso y objetivos
- Expectativas y metodología
- Configuración inicial del entorno

**9:30 - 10:30: Notebook 01 - Python Idioms Intro**
- Mostrar código pythónico vs no pythónico
- Motivar el aprendizaje con ejemplos reales
- **Clave:** Generar entusiasmo, no profundizar

**10:30 - 10:45: Descanso**

**10:45 - 12:00: Notebook 02 - Virtual Environments**
- Por qué son críticos (conflictos de dependencias)
- Demostración en vivo de creación de venv
- Práctica guiada: cada alumno crea su venv
- **Clave:** Todos deben tener su entorno funcionando

**12:00 - 13:00: Notebook 03 - Modules and Imports**
- Sistema de módulos de Python
- Diferencia entre paquetes regulares y namespace
- Ejemplos prácticos con los archivos en `examples/`
- **Clave:** Ejecutar los ejemplos en vivo

### Tarde (14:00 - 18:00)

**14:00 - 15:30: Notebook 04 - Type Hinting**
- Por qué type hints mejoran el código
- Demostración con pyright
- Ejercicios prácticos (30 min)
- **Clave:** Mostrar errores que type hints previenen

**15:30 - 15:45: Descanso**

**15:45 - 17:00: Notebook 05 - Code Quality Tools**
- Ruff: linting y formateo
- Pyright: type checking
- Integración con VS Code
- **Clave:** Configurar en sus máquinas

**17:00 - 17:45: Notebook 06 - Package Distribution**
- pyproject.toml
- Crear un paquete distribuible
- **Clave:** Concepto, no profundizar

**17:45 - 18:00: Cierre y Tarea**
- Resumen del día
- Tarea: completar ejercicios de type hinting
- Preparación para día 2

## Puntos Críticos de Enseñanza

### 1. Virtual Environments (CRÍTICO)

**Problema común:** Alumnos no entienden por qué son necesarios.

**Solución:**
1. Mostrar un conflicto real de dependencias
2. Demostrar cómo venv lo resuelve
3. Hacer que TODOS creen su venv antes de continuar

**Script de demostración:**
```bash
# Terminal 1: Sin venv
pip list  # Mostrar paquetes globales
pip install requests==2.25.0
python -c "import requests; print(requests.__version__)"

# Terminal 2: Con venv
python -m venv demo_venv
source demo_venv/bin/activate  # Windows: demo_venv\Scripts\activate
pip list  # Mostrar que está limpio
pip install requests==2.31.0
python -c "import requests; print(requests.__version__)"
```

### 2. Type Hints (CRÍTICO)

**Problema común:** "Es solo documentación, no hace nada"

**Solución:**
1. Mostrar un bug que type hints habrían prevenido
2. Demostrar pyright detectando errores
3. Mostrar autocompletado mejorado en VS Code

**Ejemplo de bug prevenible:**
```python
# Sin type hints - bug oculto
def calculate_discount(price, discount):
    return price - (price * discount)

# Bug: alguien pasa discount como porcentaje entero
calculate_discount(100, 20)  # Esperaba 80, obtiene -1900

# Con type hints - pyright lo detecta
def calculate_discount(price: float, discount: float) -> float:
    """discount debe ser 0.0-1.0"""
    return price - (price * discount)

calculate_discount(100, 20)  # pyright: error, expected float 0-1
```

### 3. Imports y Paquetes (MEDIO)

**Problema común:** Confusión entre módulos, paquetes, y namespace packages

**Solución:**
1. Usar los ejemplos en `examples/` para demostrar
2. Ejecutar en vivo `run_regular_package.py` y `run_namespace_package.py`
3. Mostrar qué pasa con y sin `__init__.py`

**Demostración:**
```bash
cd dia_1
python examples/run_regular_package.py    # Funciona
python examples/run_namespace_package.py  # Muestra limitaciones
```

### 4. Ruff (MEDIO)

**Problema común:** "Otro linter más, ¿por qué?"

**Solución:**
1. Mostrar velocidad: ruff vs flake8+black+isort
2. Demostrar auto-fix de problemas comunes
3. Configurar en VS Code para feedback inmediato

**Demostración:**
```bash
# Crear archivo con problemas
cat > demo.py << EOF
import sys
import os
def bad_function(x,y,z):
    if x==1:
        return y+z
    else:
        return y-z
EOF

# Mostrar problemas
ruff check demo.py

# Auto-fix
ruff check --fix demo.py
ruff format demo.py

# Mostrar resultado
cat demo.py
```

## Errores Comunes de Alumnos

### Error 1: No activar el venv

**Síntoma:** "No encuentra pytest/ruff/pyright"

**Solución:**
```bash
# Verificar si venv está activo
which python  # Linux/Mac
where python  # Windows

# Debe mostrar ruta dentro de venv/
# Si no: source venv/bin/activate (o venv\Scripts\activate en Windows)
```

### Error 2: Ejecutar tests desde directorio incorrecto

**Síntoma:** "ModuleNotFoundError: No module named 'exercises'"

**Solución:**
```bash
# Debe estar en dia_1/
cd dia_1
pytest exercises/tests/ -v
```

### Error 3: No entender los mensajes de error de pytest

**Solución:** Enseñar a leer los mensajes:
```
FAILED exercises/tests/test_02_type_hinting.py::test_calculate_area
Expected: 20.0
Got: 0

Significa: La función devuelve 0 en lugar de 20.0
```

## Material de Apoyo

### Slides Recomendadas

1. **Slide 1:** "Por qué Python para IA"
   - Ecosistema rico (numpy, pandas, sklearn, pytorch)
   - Sintaxis clara y expresiva
   - Comunidad activa

2. **Slide 2:** "El problema de las dependencias"
   - Diagrama: Proyecto A (numpy 1.21) vs Proyecto B (numpy 1.24)
   - Sin venv: conflicto
   - Con venv: aislamiento

3. **Slide 3:** "Type hints = Documentación ejecutable"
   - Código sin types: ambiguo
   - Código con types: claro
   - Pyright detectando errores

### Demos en Vivo (CRÍTICO)

**Demo 1: Conflicto de dependencias**
- Instalar dos versiones de un paquete
- Mostrar el problema
- Resolver con venv

**Demo 2: Type hints salvando el día**
- Función sin types con bug
- Agregar types
- Pyright detecta el bug

**Demo 3: Ruff en acción**
- Código mal formateado
- `ruff format` lo arregla
- Mostrar la velocidad

## Timing y Ritmo

### Señales de que vas muy rápido:
- Alumnos no hacen preguntas
- Muchos se quedan atrás en ejercicios
- Caras de confusión

**Acción:** Pausa, pregunta "¿Alguna duda hasta aquí?"

### Señales de que vas muy lento:
- Alumnos distraídos (móviles, otras ventanas)
- Preguntas sobre temas futuros
- Terminan ejercicios muy rápido

**Acción:** Acelera, propón ejercicios extra

## Ejercicios y Evaluación

### Ejercicio Principal: Type Hinting

**Tiempo:** 30-45 minutos  
**Archivo:** `exercises/02_type_hinting.py`  
**Tests:** 30 tests unitarios

**Monitoreo:**
- Circular por la sala
- Ayudar con errores comunes
- Identificar quién necesita ayuda extra

**Criterio de éxito:**
- Todos los tests pasan
- Pyright sin errores
- Ruff sin warnings

### Ejercicio Opcional: Python Idioms

**Para alumnos avanzados que terminan rápido**

**Archivo:** `exercises/01_python_idioms.py`  
**Objetivo:** Reforzar comprehensions y código pythónico

## Recursos para Compartir

### Documentación Oficial
- Python Type Hints: https://docs.python.org/3/library/typing.html
- Virtual Environments: https://docs.python.org/3/tutorial/venv.html
- Ruff: https://docs.astral.sh/ruff/

### Artículos Recomendados
- "Why Type Hints Matter" (Real Python)
- "Python Packaging User Guide" (PyPA)

### Videos
- "Modern Python Developer's Toolkit" (PyCon)
- "Type Hints in Python" (mCoding)

## Preparación Pre-Clase

### 1 Semana Antes
- [ ] Enviar email con requisitos (Python 3.11+, VS Code)
- [ ] Compartir link al repositorio
- [ ] Instrucciones de instalación

### 1 Día Antes
- [ ] Verificar que todos los notebooks funcionan
- [ ] Probar los ejemplos en `examples/`
- [ ] Verificar que los tests pasan
- [ ] Preparar demos en vivo

### Día de la Clase
- [ ] Llegar 15 min antes
- [ ] Verificar proyector/pantalla compartida
- [ ] Tener terminal lista con venv activado
- [ ] Tener VS Code abierto con extensiones instaladas

## Troubleshooting en Vivo

### Problema: "No puedo instalar paquetes"

**Diagnóstico:**
```bash
python --version  # Verificar versión
pip --version     # Verificar pip
which python      # Verificar ruta
```

**Soluciones comunes:**
- Permisos: usar `--user` flag
- Proxy corporativo: configurar pip
- Python viejo: actualizar a 3.11+

### Problema: "VS Code no detecta el venv"

**Solución:**
1. Ctrl+Shift+P → "Python: Select Interpreter"
2. Elegir el intérprete dentro de venv/
3. Reiniciar VS Code si es necesario

### Problema: "Los tests no pasan"

**Diagnóstico:**
```bash
pytest exercises/tests/ -v  # Ver qué falla
pytest exercises/tests/ -vv # Más detalle
pytest exercises/tests/ -vv -s  # Con prints
```

## Feedback y Mejora Continua

### Al Final del Día

**Encuesta rápida (5 min):**
1. ¿Qué concepto fue más difícil? (1-5)
2. ¿El ritmo fue adecuado? (muy lento / bien / muy rápido)
3. ¿Qué mejorarías?

**Observaciones del profesor:**
- ¿Qué conceptos generaron más dudas?
- ¿Qué ejemplos funcionaron mejor?
- ¿Qué timing ajustar para próxima vez?

## Notas Importantes

### Para Alumnos con Experiencia

Si hay alumnos con experiencia en Python:
- Asignarles rol de "ayudantes"
- Darles ejercicios extra más desafiantes
- Pedirles que compartan sus experiencias

### Para Alumnos Nuevos

Si hay alumnos muy nuevos:
- Emparejarlos con alumnos con más experiencia
- Dedicar tiempo extra en los descansos
- Proporcionar recursos adicionales

### Adaptación al Ritmo

**Si vas adelantado:**
- Profundizar en conceptos clave
- Hacer más ejercicios prácticos
- Discusión de casos reales

**Si vas atrasado:**
- Priorizar: venv, type hints, ruff
- Reducir tiempo en package distribution
- Asignar lectura para casa

## Checklist Final del Día

Al terminar, verificar que TODOS los alumnos:
- [ ] Tienen venv creado y funcionando
- [ ] Pueden ejecutar pytest
- [ ] Tienen ruff y pyright instalados
- [ ] Entienden cómo ejecutar los tests
- [ ] Saben dónde encontrar los ejercicios
- [ ] Tienen acceso al repositorio

## Contacto y Soporte

**Durante el curso:**
- Estar disponible en descansos
- Responder dudas por chat/email

**Después del curso:**
- Proporcionar email de contacto
- Crear canal de Slack/Discord (opcional)
- Office hours (opcional)

---

**Última actualización:** Febrero 2026  
**Versión:** 1.0
