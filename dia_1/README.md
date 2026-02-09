# Día 1: Fundamentos - Configuración de Proyectos Python

##  Objetivo del Día

Establecer las bases profesionales para desarrollo en Python: entornos virtuales, sistema de módulos, type hints y herramientas de calidad de código.

**Al finalizar este día, serás capaz de:**
-  Crear y gestionar entornos virtuales profesionales
-  Estructurar proyectos Python siguiendo mejores prácticas
-  Usar type hints para código más robusto y mantenible
-  Aplicar herramientas de calidad (ruff, pyright) en tu flujo de trabajo
-  Entender el sistema de módulos e imports de Python

---

##  Contenido del Día

### 1. Python Idioms Intro (30 min)
**Archivo:** `01_python_idioms_intro.ipynb`

Introducción motivacional al código pythónico. Verás ejemplos de código elegante que escribirás al final del curso.

**Conceptos clave:**
- Comprehensions vs loops tradicionales
- Generadores para eficiencia de memoria
- Context managers
- Decoradores básicos

**No requiere instalación** - solo Python stdlib

---

### 2. Virtual Environments (90 min)  CRÍTICO
**Archivo:** `02_virtual_environments.ipynb`

Por qué los entornos virtuales son esenciales y cómo usarlos correctamente.

**Conceptos clave:**
- El problema de las dependencias conflictivas
- Crear y activar entornos virtuales
- Gestión de dependencias con pip
- Buenas prácticas

**Práctica:** Crearás tu propio entorno virtual para el curso

** IMPORTANTE:** Todos deben tener su venv funcionando antes de continuar

---

### 3. Modules and Imports (75 min)
**Archivo:** `03_modules_and_imports.ipynb`

Cómo funciona el sistema de módulos de Python y cómo estructurar paquetes.

**Conceptos clave:**
- Diferencia entre módulo y paquete
- `__init__.py`: cuándo y por qué usarlo
- Imports absolutos vs relativos
- Namespace packages vs regular packages

**Práctica:** Ejecutarás ejemplos reales en `examples/`

---

### 4. Type Hinting (90 min)  CRÍTICO
**Archivo:** `04_type_hinting.ipynb`

Type hints para código más seguro, legible y mantenible.

**Conceptos clave:**
- Sintaxis básica de type hints
- Tipos complejos (List, Dict, Optional, Union)
- Type checking con pyright
- Beneficios reales en proyectos grandes

**Práctica:** Ejercicios con 30 tests unitarios

** EJERCICIO OBLIGATORIO:** `exercises/02_type_hinting.py`

---

### 5. Code Quality Tools (75 min)  CRÍTICO
**Archivo:** `05_code_quality_tools.ipynb`

Herramientas profesionales para mantener calidad de código.

**Conceptos clave:**
- Ruff: linting y formateo ultrarrápido
- Pyright: type checking estático
- Integración con VS Code
- Configuración en pyproject.toml

**Práctica:** Configurarás estas herramientas en tu entorno

---

### 6. Package Distribution (45 min)
**Archivo:** `06_package_distribution.ipynb`

Cómo crear paquetes Python distribuibles.

**Conceptos clave:**
- pyproject.toml moderno
- Src layout
- Crear wheels
- Publicar en PyPI (conceptual)

**Nota:** Introducción conceptual, profundizaremos en días posteriores

---

##  Inicio Rápido

### Paso 1: Verificar Requisitos

```bash
# Verificar Python 3.11+
python --version

# Debe mostrar: Python 3.11.x o superior
```

### Paso 2: Crear Entorno Virtual

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python -m venv venv
source venv/bin/activate
```

**Verificar que está activo:**
```bash
which python  # Linux/Mac
where python  # Windows

# Debe mostrar ruta dentro de venv/
```

### Paso 3: Instalar Dependencias

```bash
# Desde la raíz del proyecto
pip install -e ".[dev]"

# Verificar instalación
pytest --version
ruff --version
pyright --version
```

### Paso 4: Iniciar Jupyter

```bash
cd dia_1
jupyter notebook
```

Se abrirá tu navegador con la lista de notebooks.

---

##  Ejercicios Prácticos

### Ejercicio Principal: Type Hinting

**Archivo:** `exercises/02_type_hinting.py`  
**Tiempo estimado:** 30-45 minutos  
**Tests:** 30 tests unitarios

**Cómo trabajar:**

1. **Leer el notebook:** `04_type_hinting.ipynb`
2. **Abrir el ejercicio:** `exercises/02_type_hinting.py`
3. **Completar las funciones** marcadas con `# TODO`
4. **Ejecutar tests:**
   ```bash
   pytest exercises/tests/test_02_type_hinting.py -v
   ```
5. **Validar con pyright:**
   ```bash
   pyright exercises/02_type_hinting.py
   ```

**Criterio de éxito:**
-  Todos los tests pasan (30/30)
-  Pyright sin errores
-  Ruff sin warnings

### Ejercicio Opcional: Python Idioms

**Archivo:** `exercises/01_python_idioms.py`

Para alumnos que terminen rápido o quieran práctica extra.

---

##  Herramientas y Comandos

### Ejecutar Tests

```bash
# Todos los tests del día 1
pytest dia_1/exercises/tests/ -v

# Solo type hinting
pytest dia_1/exercises/tests/test_02_type_hinting.py -v

# Con cobertura
pytest dia_1/exercises/tests/ --cov=exercises --cov-report=html
```

### Validar Código

```bash
# Type checking
pyright dia_1/exercises/

# Linting
ruff check dia_1/exercises/

# Formateo
ruff format dia_1/exercises/
```

### Ejemplos Prácticos

```bash
# Ejecutar ejemplos de paquetes
cd dia_1
python examples/run_regular_package.py
python examples/run_namespace_package.py
```

---

##  Solución de Problemas

### Problema: "pytest: command not found"

**Causa:** Dependencias no instaladas o venv no activado

**Solución:**
```bash
# Verificar venv activo
which python  # Debe mostrar ruta en venv/

# Si no está activo
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -e ".[dev]"
```

### Problema: "ModuleNotFoundError: No module named 'exercises'"

**Causa:** Ejecutando desde directorio incorrecto

**Solución:**
```bash
# Debe estar en dia_1/
cd dia_1
pytest exercises/tests/ -v
```

### Problema: "Tests fallan pero no sé por qué"

**Solución:** Leer el mensaje de error de pytest

```
FAILED test_calculate_area
Expected: 20.0
Got: 0

Significa: Tu función devuelve 0 en lugar de 20.0
```

### Problema: "Pyright reporta errores pero tests pasan"

**Causa:** Type hints incorrectos

**Solución:** Revisar los tipos de:
- Parámetros de función
- Tipo de retorno
- Variables locales (si es necesario)

---

##  Recursos Adicionales

### Documentación Oficial

- **Python Type Hints:** https://docs.python.org/3/library/typing.html
- **Virtual Environments:** https://docs.python.org/3/tutorial/venv.html
- **Python Packaging:** https://packaging.python.org/

### Herramientas

- **Ruff:** https://docs.astral.sh/ruff/
- **Pyright:** https://github.com/microsoft/pyright
- **Pytest:** https://docs.pytest.org/

### PEPs Relevantes

- **PEP 484 - Type Hints:** https://www.python.org/dev/peps/pep-0484/
- **PEP 517 - Build System:** https://www.python.org/dev/peps/pep-0517/
- **PEP 518 - pyproject.toml:** https://www.python.org/dev/peps/pep-0518/

### Guías Adicionales

- **Guía de Ejercicios:** `EXERCISES_GUIDE.md`
- **Guía del Profesor:** `GUIA_PROFESOR.md` (para instructores)

---

## ⏱ Distribución del Tiempo

| Horario | Actividad | Duración |
|---------|-----------|----------|
| 9:00 - 9:30 | Bienvenida y setup | 30 min |
| 9:30 - 10:30 | Notebook 01: Python Idioms | 60 min |
| 10:30 - 10:45 |  Descanso | 15 min |
| 10:45 - 12:15 | Notebook 02: Virtual Environments | 90 min |
| 12:15 - 13:00 | Notebook 03: Modules & Imports | 45 min |
| 13:00 - 14:00 |  Almuerzo | 60 min |
| 14:00 - 15:30 | Notebook 04: Type Hinting + Ejercicios | 90 min |
| 15:30 - 15:45 |  Descanso | 15 min |
| 15:45 - 17:00 | Notebook 05: Code Quality Tools | 75 min |
| 17:00 - 17:45 | Notebook 06: Package Distribution | 45 min |
| 17:45 - 18:00 | Cierre y Q&A | 15 min |

**Total:** 8 horas (incluyendo descansos)

---

##  Checklist de Finalización

Al terminar el Día 1, debes haber:

- [ ] Creado y activado tu entorno virtual
- [ ] Instalado todas las dependencias (pytest, ruff, pyright)
- [ ] Completado el notebook 01 (Python Idioms)
- [ ] Completado el notebook 02 (Virtual Environments)
- [ ] Completado el notebook 03 (Modules & Imports)
- [ ] Completado el notebook 04 (Type Hinting)
- [ ] Completado el notebook 05 (Code Quality Tools)
- [ ] Completado el notebook 06 (Package Distribution)
- [ ] Completado ejercicios de type hinting (30/30 tests)
- [ ] Configurado ruff y pyright en tu entorno
- [ ] Entendido cómo ejecutar tests con pytest

---

##  Próximos Pasos

**Tarea para casa (opcional):**
- Revisar los conceptos del día
- Completar ejercicios opcionales
- Leer documentación de type hints

**Día 2: Código Pythónico**
- Comprehensions avanzadas
- Generadores e iteradores
- Decoradores
- Programación funcional
- Context managers
- Métodos mágicos

---

##  Soporte

**Durante el curso:**
- Preguntar al instructor
- Ayudar a compañeros
- Consultar la documentación

**Recursos del curso:**
- Repositorio: [GitHub]
- Documentación: Carpeta `.kiro/steering/`
- Ejemplos: Carpeta `examples/`

---

**¡Bienvenido al Día 1! Vamos a construir bases sólidas para tu desarrollo profesional en Python.**
