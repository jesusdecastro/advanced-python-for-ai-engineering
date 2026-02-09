# ❓ Preguntas Frecuentes - Día 1

## Antes de Empezar

### ¿Qué necesito tener instalado?

**Requisitos mínimos:**
- Python 3.11 o superior
- Git
- VS Code (recomendado) o cualquier editor de texto
- Conexión a internet (para instalar paquetes)

**Verificar:**
```bash
python --version  # Debe ser 3.11+
git --version     # Cualquier versión reciente
```

### ¿Puedo usar Python 3.10 o anterior?

**No recomendado.** El curso usa características de Python 3.11+:
- Mejor sintaxis de type hints (`int | str` en lugar de `Union[int, str]`)
- Mejoras de rendimiento significativas (10-60% más rápido que 3.10)
- Mensajes de error más claros y detallados
- Mejor soporte para tipos genéricos

**Si solo tienes 3.10:** El código funcionará en su mayoría, pero te perderás las mejoras de rendimiento y algunos ejemplos pueden necesitar ajustes menores.

### ¿Qué sistema operativo necesito?

**Cualquiera:** Windows, Linux, o macOS.

Los comandos están adaptados para cada sistema. Busca las secciones específicas en la documentación.

---

## Entornos Virtuales

### ¿Por qué necesito un entorno virtual?

**Problema real:** Imagina que trabajas en dos proyectos:
- Proyecto A necesita `numpy==1.21.0`
- Proyecto B necesita `numpy==1.24.0`

Sin entorno virtual: **Conflicto** - solo puedes tener una versión instalada.

Con entorno virtual: **Aislamiento** - cada proyecto tiene su propia versión.

### ¿Cómo sé si mi venv está activo?

**Señales visuales:**
1. Tu prompt muestra `(venv)` al inicio
2. `which python` (Linux/Mac) o `where python` (Windows) muestra ruta en `venv/`

**Verificación definitiva:**
```bash
python -c "import sys; print(sys.prefix)"
```

Debe mostrar una ruta que contiene `venv`.

### ¿Tengo que activar el venv cada vez?

**Sí.** Cada vez que abres una nueva terminal, debes activar el venv:

```bash
# Linux/Mac
source venv/bin/activate

# Windows
venv\Scripts\activate
```

**Tip:** Crea un alias o script para hacerlo más rápido.

### ¿Puedo usar conda en lugar de venv?

**Sí, pero no es recomendado para este curso.**

El curso enseña `venv` porque:
- Es parte de Python (no requiere instalación extra)
- Es el estándar en la industria
- Es más ligero y rápido

Si usas conda, adapta los comandos según sea necesario.

---

## Instalación de Paquetes

### ¿Qué hace `pip install -e ".[dev]"`?

**Desglose:**
- `pip install`: Instala paquetes
- `-e`: Modo "editable" (cambios en el código se reflejan inmediatamente)
- `.`: Instala el paquete actual (el que tiene `pyproject.toml`)
- `[dev]`: Instala también las dependencias de desarrollo (pytest, ruff, etc.)

### "pip: command not found"

**Causa:** pip no está en tu PATH o Python no está instalado correctamente.

**Solución:**
```bash
# Usar el módulo pip directamente
python -m pip install --upgrade pip

# Luego instalar paquetes
python -m pip install -e ".[dev]"
```

### "ERROR: Could not find a version that satisfies the requirement"

**Causa:** Versión de Python muy antigua o paquete mal escrito.

**Solución:**
1. Verificar versión de Python: `python --version`
2. Actualizar pip: `python -m pip install --upgrade pip`
3. Intentar de nuevo

### ¿Puedo instalar paquetes globalmente?

**No recomendado.** Siempre usa un entorno virtual para:
- Evitar conflictos entre proyectos
- Mantener tu sistema limpio
- Facilitar la reproducibilidad

---

## Tests y Ejercicios

### ¿Por qué todos los tests fallan al principio?

**Es normal.** Los ejercicios vienen con tests que verifican tu código. Al principio, las funciones están vacías (`pass`), por eso fallan.

**Tu trabajo:** Implementar las funciones para que los tests pasen.

### ¿Cómo leo los mensajes de error de pytest?

**Ejemplo:**
```
FAILED test_calculate_area
Expected: 20.0
Got: 0
```

**Interpretación:**
- `FAILED test_calculate_area`: El test `test_calculate_area` falló
- `Expected: 20.0`: El test esperaba que devuelvas `20.0`
- `Got: 0`: Tu función devolvió `0`

**Acción:** Revisa tu función `calculate_area` y corrige la lógica.

### "ModuleNotFoundError: No module named 'exercises'"

**Causa:** Estás ejecutando pytest desde el directorio incorrecto.

**Solución:**
```bash
# Navega a dia_1/
cd dia_1

# Ejecuta los tests desde ahí
pytest exercises/tests/ -v
```

### ¿Puedo modificar los tests?

**No.** Los tests definen el comportamiento esperado. Modificarlos sería hacer trampa.

**Si un test parece incorrecto:** Pregunta al instructor.

### ¿Qué significa "coverage"?

**Coverage** = Porcentaje de tu código que es ejecutado por los tests.

**Ejemplo:**
- 80% coverage = Los tests ejecutan el 80% de tus líneas de código
- 100% coverage = Los tests ejecutan todo tu código

**Objetivo:** ≥80% coverage en proyectos profesionales.

---

## Type Hints

### ¿Los type hints son obligatorios?

**En Python:** No, son opcionales.  
**En este curso:** Sí, son obligatorios.  
**En la industria:** Cada vez más empresas los requieren.

**Por qué:**
- Detectan bugs antes de ejecutar el código
- Mejoran el autocompletado del IDE
- Sirven como documentación ejecutable
- Facilitan el mantenimiento

### "Pyright reporta errores pero los tests pasan"

**Causa:** Tus type hints son incorrectos, aunque la lógica funciona.

**Ejemplo:**
```python
def add(a, b):  # Sin type hints
    return a + b

add(1, 2)      # Funciona
add("a", "b")  # También funciona, pero ¿es lo que querías?
```

**Con type hints:**
```python
def add(a: int, b: int) -> int:
    return a + b

add(1, 2)      # OK
add("a", "b")  # Pyright: Error! Expected int, got str
```

### ¿Qué es `Optional[int]`?

**Significa:** "Puede ser `int` o `None`"

**Ejemplo:**
```python
def find_user(user_id: int) -> Optional[User]:
    """
    Find a user by ID.
    
    :return: User if found, None otherwise
    """
    # Puede devolver User o None
```

**Equivalente en Python 3.11+:** `User | None`

### ¿Qué es `Union[int, str]`?

**Significa:** "Puede ser `int` O `str`"

**Ejemplo:**
```python
def process_id(id: Union[int, str]) -> str:
    """Accept ID as int or str, return as str"""
    return str(id)

process_id(123)    # OK
process_id("123")  # OK
process_id(12.3)   # Pyright: Error! Expected int or str, got float
```

**Equivalente en Python 3.11+:** `int | str`

---

## Herramientas de Calidad

### ¿Qué hace Ruff?

**Ruff = Linter + Formateador**

**Linter:** Detecta problemas en el código
- Variables no usadas
- Imports innecesarios
- Código inalcanzable
- Violaciones de estilo

**Formateador:** Arregla el formato automáticamente
- Indentación
- Espacios
- Longitud de línea
- Orden de imports

### ¿Por qué Ruff y no Black/Flake8/isort?

**Ruff es más rápido:** 10-100x más rápido que las herramientas tradicionales.

**Ruff es todo-en-uno:** Reemplaza múltiples herramientas:
- Black (formateo)
- Flake8 (linting)
- isort (ordenar imports)
- pyupgrade (modernizar código)

**Ruff es moderno:** Mantenido activamente, adopción rápida en la industria.

### ¿Qué hace Pyright?

**Pyright = Type Checker**

Analiza tu código sin ejecutarlo y detecta:
- Type hints incorrectos
- Llamadas a funciones con argumentos incorrectos
- Acceso a atributos inexistentes
- Variables no definidas

**Ejemplo:**
```python
def greet(name: str) -> str:
    return f"Hello, {name}"

greet(123)  # Pyright: Error! Expected str, got int
```

### "Ruff reporta E501: line too long"

**Causa:** Línea de código > 100 caracteres.

**Solución:**
```python
# Mal: línea muy larga
result = some_function(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10)

# Bien: dividir en múltiples líneas
result = some_function(
    arg1, arg2, arg3, arg4, arg5,
    arg6, arg7, arg8, arg9, arg10
)
```

**O usar auto-fix:**
```bash
ruff format tu_archivo.py
```

---

## VS Code

### ¿Qué extensiones necesito?

**Esenciales:**
- Python (Microsoft)
- Ruff (Astral Software)

**Recomendadas:**
- Jupyter (Microsoft)
- Python Debugger (Microsoft)

### ¿Cómo configuro VS Code para usar mi venv?

1. Abre VS Code en la carpeta del proyecto
2. `Ctrl+Shift+P` (o `Cmd+Shift+P` en Mac)
3. Escribe "Python: Select Interpreter"
4. Selecciona el intérprete dentro de `venv/`

**Verificar:** La barra inferior debe mostrar la ruta del venv.

### ¿Cómo habilito el formateo automático?

**Archivo:** `.vscode/settings.json`

```json
{
  "editor.formatOnSave": true,
  "python.formatting.provider": "none",
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff"
  }
}
```

Ahora, cada vez que guardes, Ruff formateará automáticamente.

---

## Conceptos del Curso

### ¿Qué es un "idiom" en Python?

**Idiom** = Forma idiomática/natural de hacer algo en Python.

**Ejemplo:**

**No idiomático (funciona, pero no es pythónico):**
```python
i = 0
while i < len(items):
    print(items[i])
    i += 1
```

**Idiomático (pythónico):**
```python
for item in items:
    print(item)
```

### ¿Qué es "pythónico"?

**Pythónico** = Código que sigue las convenciones y filosofía de Python.

**Características:**
- Legible ("código que se lee como inglés")
- Conciso (sin ser críptico)
- Explícito (claro en sus intenciones)
- Simple (evita complejidad innecesaria)

**Filosofía:** "The Zen of Python" (`import this`)

### ¿Qué es un "namespace package"?

**Namespace package** = Paquete sin `__init__.py`

**Uso:** Cuando múltiples proyectos contribuyen al mismo namespace.

**Ejemplo:** Plugins, extensiones

**En este curso:** Aprenderás la diferencia y cuándo usar cada uno.

### ¿Qué es "src layout"?

**Src layout** = Estructura de proyecto con carpeta `src/`

**Estructura:**
```
proyecto/
├── src/
│   └── mi_paquete/
│       ├── __init__.py
│       └── modulo.py
├── tests/
├── pyproject.toml
└── README.md
```

**Ventajas:**
- Evita imports accidentales del código sin instalar
- Fuerza a instalar el paquete correctamente
- Mejor para distribución

---

## Problemas Técnicos

### "Permission denied" al instalar paquetes

**Causa:** Intentando instalar en directorios del sistema sin permisos.

**Solución:**
```bash
# Opción 1: Usar venv (recomendado)
python -m venv venv
source venv/bin/activate  # o venv\Scripts\activate en Windows
pip install -e ".[dev]"

# Opción 2: Instalar solo para tu usuario
pip install --user -e ".[dev]"
```

### "SSL Certificate Error"

**Causa:** Firewall corporativo o proxy.

**Solución:**
```bash
# Opción 1: Usar HTTP en lugar de HTTPS (menos seguro)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -e ".[dev]"

# Opción 2: Configurar proxy
export HTTP_PROXY=http://proxy.empresa.com:8080
export HTTPS_PROXY=http://proxy.empresa.com:8080
```

### Jupyter no se abre en el navegador

**Solución:**
```bash
# Ver la URL que genera Jupyter
jupyter notebook --no-browser

# Copiar la URL (algo como http://localhost:8888/?token=...)
# Pegarla en tu navegador
```

### "Kernel died" en Jupyter

**Causa:** Error en el código que crashea el kernel.

**Solución:**
1. Reiniciar el kernel: Kernel → Restart
2. Revisar el código que causó el error
3. Si persiste, revisar logs: `jupyter notebook --debug`

---

## Mejores Prácticas

### ¿Cuánto tiempo debo dedicar a cada notebook?

**Estimado:**
- Notebook 01: 30 min (lectura)
- Notebook 02: 90 min (práctica intensiva)
- Notebook 03: 75 min (lectura + ejemplos)
- Notebook 04: 90 min (lectura + ejercicios)
- Notebook 05: 75 min (configuración + práctica)
- Notebook 06: 45 min (lectura)

**Total:** ~6.5 horas + descansos = 8 horas

### ¿Debo memorizar todo?

**No.** El objetivo es:
- **Entender** los conceptos
- **Saber** cuándo aplicarlos
- **Poder** buscar la sintaxis cuando la necesites

**Memoriza:** Conceptos clave, no sintaxis exacta.

### ¿Qué hago si me quedo atascado?

**Proceso:**
1. **Lee el error** cuidadosamente
2. **Busca en la documentación** del curso
3. **Pregunta a un compañero**
4. **Pregunta al instructor**
5. **Busca en Google/Stack Overflow** (con contexto)

**No te quedes atascado más de 15 minutos** en un problema.

### ¿Puedo usar ChatGPT/Copilot?

**Para aprender:** No recomendado. Necesitas entender, no solo copiar.

**Para trabajar:** Sí, son herramientas útiles.

**En este curso:** Intenta resolver los ejercicios por ti mismo primero.

---

## Después del Día 1

### ¿Qué debo repasar?

**Conceptos críticos:**
- Cómo crear y activar entornos virtuales
- Sintaxis básica de type hints
- Cómo ejecutar tests con pytest
- Cómo usar ruff y pyright

**Si solo recuerdas una cosa:** Siempre usa entornos virtuales.

### ¿Hay tarea?

**Opcional:** Completar ejercicios que no terminaste en clase.

**Recomendado:** Leer la documentación de type hints.

### ¿Qué viene en el Día 2?

**Día 2: Código Pythónico**
- Comprehensions avanzadas
- Generadores e iteradores
- Decoradores
- Programación funcional
- Context managers
- Métodos mágicos

---

## Contacto

**Durante la clase:**
- Levanta la mano
- Pregunta en el chat
- Pide ayuda a compañeros

**Fuera de clase:**
- Email del instructor
- Canal de Slack/Discord (si existe)
- Documentación del curso

---

**Última actualización:** Febrero 2026  
**¿Falta algo?** Sugiere nuevas preguntas al instructor.
