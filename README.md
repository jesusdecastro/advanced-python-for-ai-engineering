# Curso de Python Avanzado para IA - Día 1

Rama dedicada al **Día 1: Fundamentos - Configuración de Proyectos Python** del curso intensivo de Python avanzado aplicado a Ingeniería de IA.

> **Nota:** Esta rama (`dia_1`) contiene únicamente el material del Día 1. El contenido de los días restantes se irá integrando progresivamente a la rama principal mediante merges.

## Descripción

Esta rama contiene todo el material necesario para el primer día del curso, enfocado en establecer las bases profesionales para proyectos Python: entornos virtuales, sistema de módulos, estructura de paquetes, gestión de dependencias y herramientas de calidad de código.

**Duración:** 8 horas  
**Modalidad:** Remoto  
**Nivel:** Intermedio-Avanzado

## Contenido del Día 1

### Temas Cubiertos

1. **Python Idioms Intro** - Introducción a código pythónico
2. **Virtual Environments** - Gestión de entornos virtuales (venv, uv)
3. **Modules and Imports** - Sistema de módulos e imports en Python
4. **Type Hinting** - Type hints y validación de tipos
5. **Code Quality Tools** - Herramientas de calidad (ruff, pyright)
6. **Package Distribution** - Distribución de paquetes Python

### Estructura del Día 1

```
dia_1/
├── 01_python_idioms_intro.ipynb      # Notebook: Introducción a idioms
├── 02_virtual_environments.ipynb     # Notebook: Entornos virtuales
├── 03_modules_and_imports.ipynb      # Notebook: Módulos e imports
├── 04_type_hinting.ipynb             # Notebook: Type hints
├── 05_code_quality_tools.ipynb       # Notebook: Herramientas de calidad
├── 06_package_distribution.ipynb     # Notebook: Distribución de paquetes
├── exercises/                        # Ejercicios prácticos
│   ├── 01_python_idioms.py
│   ├── 02_type_hinting.py
│   ├── 04_package_distribution.py
│   ├── 05_code_quality_tools.py
│   └── tests/                        # Tests unitarios
├── examples/                         # Ejemplos de código
│   ├── regular_package/              # Ejemplo de paquete regular
│   └── namespace_package/            # Ejemplo de namespace package
├── example_project/                  # Proyecto de ejemplo
├── README.md                         # Guía del día
├── EXERCISES_GUIDE.md                # Guía de ejercicios
└── requirements.txt                  # Dependencias del día
```

## Inicio Rápido

### Requisitos Previos

- Python 3.11 o superior instalado
- Git instalado
- VS Code con las siguientes extensiones:
  - Python (Microsoft)
  - Ruff (Astral Software)
- Conocimientos básicos de Python

### Instalación

1. Clona el repositorio y cambia a la rama `dia_1`:
```bash
git clone https://github.com/tu-usuario/advanced-python-for-ai-engineering.git
cd advanced-python-for-ai-engineering
git checkout dia_1
```

2. Crea y activa el entorno virtual:

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

3. Instala las dependencias del Día 1:
```bash
pip install -r dia_1/requirements.txt
```

4. Inicia Jupyter Notebook:
```bash
cd dia_1
jupyter notebook
```

## Cómo Usar Este Material

### 1. Notebooks Teóricos

Cada notebook contiene:
- Explicaciones teóricas en castellano
- Ejemplos ejecutables con código en inglés
- Ejercicios prácticos integrados
- Referencias oficiales

Abre los notebooks en orden secuencial (01 → 06).

### 2. Ejercicios Prácticos

Los ejercicios están en `dia_1/exercises/`:

```bash
# Completa los ejercicios
code dia_1/exercises/02_type_hinting.py

# Ejecuta los tests
pytest dia_1/exercises/tests/ -v

# Ejecuta tests específicos
pytest dia_1/exercises/tests/test_02_type_hinting.py -v
```

### 3. Validación de Código

**Type checking:**
```bash
pyright dia_1/exercises/
```

**Linting:**
```bash
ruff check dia_1/exercises/
```

**Formateo:**
```bash
ruff format dia_1/exercises/
```

## Objetivos de Aprendizaje

Al finalizar el Día 1, serás capaz de:

- ✅ Configurar entornos virtuales profesionales con venv y uv
- ✅ Entender el sistema de módulos e imports de Python
- ✅ Estructurar paquetes Python siguiendo mejores prácticas (src layout)
- ✅ Usar type hints para código más robusto
- ✅ Aplicar herramientas de calidad (ruff, pyright)
- ✅ Crear paquetes distribuibles con pyproject.toml
- ✅ Escribir código pythónico siguiendo idioms estándar

## Stack Tecnológico del Día 1

**Core:**
- Python 3.11+
- pytest (testing)
- ruff (linting y formateo)
- pyright (type checking)

**Herramientas:**
- Jupyter Notebook
- Git
- VS Code

## Recursos Adicionales

- **Guía de instalación completa:** [virtual_env_installation_guide.md](virtual_env_installation_guide.md)
- **Plugins recomendados de VS Code:** [vscode_plugins.md](vscode_plugins.md)
- **Guía de ejercicios:** [dia_1/EXERCISES_GUIDE.md](dia_1/EXERCISES_GUIDE.md)
- **Plan de formación completo:** [plan_de_formacion.md](plan_de_formacion.md)

## Estándares de Código

Este curso sigue estándares estrictos:

- **Documentación en Markdown:** Castellano
- **Código Python:** Inglés
- **Docstrings:** Inglés (formato Sphinx)
- **Type hints:** Obligatorios en todas las funciones
- **Linting:** Todo el código debe pasar ruff sin errores

Ver [.kiro/steering/course-standards.md](.kiro/steering/course-standards.md) para detalles completos.

## Próximos Pasos

Una vez completado el Día 1:

1. Asegúrate de que todos los ejercicios pasan los tests
2. Verifica que tu código pasa ruff y pyright
3. Revisa los conceptos clave en los notebooks
4. Prepárate para el Día 2: Código Pythónico (próximamente en main)

## Soporte

Si encuentras problemas:

1. Revisa la guía de instalación: [virtual_env_installation_guide.md](virtual_env_installation_guide.md)
2. Verifica que tu entorno virtual esté activado
3. Asegúrate de tener Python 3.11+ instalado
4. Consulta los ejemplos en `dia_1/examples/`

## Licencia

Este material educativo está disponible bajo licencia MIT para uso educativo y formación.

---

**¡Comienza tu aprendizaje en `dia_1/README.md`!**
