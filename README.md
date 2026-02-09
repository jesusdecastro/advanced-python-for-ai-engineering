# Curso de Python Avanzado para IA - Día 1

Curso intensivo enfocado en Python avanzado aplicado a Ingeniería de IA, con énfasis en Clean Code, arquitectura de software y mejores prácticas de desarrollo.

##  Bienvenido al Día 1

Este repositorio contiene todo el material para el **Día 1: Fundamentos - Configuración de Proyectos Python**.

**Duración:** 8 horas  
**Nivel:** Intermedio-Avanzado

---

##  Inicio Rápido

### Paso 1: Clonar el Repositorio

```bash
git clone https://github.com/jesusdecastro/advanced-python-for-ai-engineering.git
cd advanced-python-for-ai-engineering
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

### Paso 3: Instalar Dependencias

```bash
pip install -e ".[dev]"
```

### Paso 4: Iniciar Jupyter

```bash
cd dia_1
jupyter notebook
```

**¿Necesitas ayuda?** Lee `dia_1/INICIO_RAPIDO.md` para una guía detallada.

---

##  Contenido del Día 1

### Notebooks

1. **01_python_idioms_intro.ipynb** - Introducción a código pythónico
2. **02_virtual_environments.ipynb** - Entornos virtuales  CRÍTICO
3. **03_modules_and_imports.ipynb** - Sistema de módulos e imports
4. **04_type_hinting.ipynb** - Type hints  CRÍTICO
5. **05_code_quality_tools.ipynb** - Ruff y Pyright  CRÍTICO
6. **06_package_distribution.ipynb** - Distribución de paquetes

### Ejercicios

Los ejercicios están en `dia_1/exercises/` con tests unitarios en `dia_1/exercises/tests/`.

**Ejecutar tests:**
```bash
cd dia_1
pytest exercises/tests/ -v
```

---

##  Documentación

- **README del Día 1:** `dia_1/README.md` - Guía completa
- **Inicio Rápido:** `dia_1/INICIO_RAPIDO.md` - Setup en 5 minutos
- **FAQ:** `dia_1/FAQ.md` - Preguntas frecuentes
- **Guía de Ejercicios:** `dia_1/EXERCISES_GUIDE.md` - Cómo trabajar con ejercicios

---

##  Objetivos de Aprendizaje

Al finalizar el Día 1, serás capaz de:

-  Crear y gestionar entornos virtuales profesionales
-  Estructurar proyectos Python siguiendo mejores prácticas
-  Usar type hints para código más robusto
-  Aplicar herramientas de calidad (ruff, pyright)
-  Entender el sistema de módulos e imports de Python

---

##  Requisitos

- Python 3.11 o superior
- Git
- VS Code (recomendado)
- Conexión a internet

**Verificar Python:**
```bash
python --version
```

Debe mostrar `Python 3.11.x` o superior.

---

##  Soporte

**Problemas comunes:**
- Consulta `dia_1/FAQ.md` para soluciones rápidas
- Lee `dia_1/README.md` para documentación completa

**Durante el curso:**
- Pregunta al instructor
- Consulta con compañeros
- Revisa la documentación

---

##  Estructura del Repositorio

```
.
 dia_1/                    # Todo el contenido del Día 1
    notebooks (6)         # Notebooks educativos
    exercises/            # Ejercicios prácticos
    examples/             # Ejemplos de código
    README.md             # Guía completa del día
    INICIO_RAPIDO.md      # Setup rápido
    FAQ.md                # Preguntas frecuentes
 proyectos_integradores/   # Proyectos finales (próximamente)
 .kiro/steering/           # Estándares del curso
 pyproject.toml            # Configuración del proyecto
 README.md                 # Este archivo
```

---

##  Herramientas del Curso

- **pytest** - Testing
- **ruff** - Linting y formateo
- **pyright** - Type checking
- **jupyter** - Notebooks interactivos

---

##  Próximos Días

El contenido de los días 2-5 se irá añadiendo progresivamente:

- **Día 2:** Código Pythónico (próximamente)
- **Día 3:** Código Limpio (próximamente)
- **Día 4:** Diseño OOP (próximamente)
- **Día 5:** Testing y Optimización (próximamente)

---

##  Contacto

**Repositorio:** https://github.com/jesusdecastro/advanced-python-for-ai-engineering

---

##  Licencia

Este material educativo está disponible bajo licencia MIT para uso educativo y formación.

---

**¡Comienza tu aprendizaje en `dia_1/README.md`!**
