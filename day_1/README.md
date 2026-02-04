# Día 1: Configuración de Proyectos Python

## Descripción General

Este módulo cubre los fundamentos de la configuración profesional de proyectos Python. Aprenderás a gestionar entornos virtuales, configurar herramientas de calidad de código y estructurar proyectos de forma profesional.

## Inicio Rápido

### Paso 1: Navega a la Raíz del Repositorio

```bash
cd ..
```

Si estás en `day_1/`, vuelve a la carpeta raíz del proyecto.

### Paso 2: Crea el Entorno Virtual

```bash
# Windows
python -m venv venv

# Linux/Mac
python3 -m venv venv
```

### Paso 3: Activa el Entorno

```bash
# Windows (CMD)
venv\Scripts\activate

# Windows (PowerShell)
venv\Scripts\Activate.ps1

# Linux/Mac
source venv/bin/activate
```

Deberías ver `(venv)` al inicio de tu línea de comandos.

### Paso 4: Instala las Dependencias Mínimas

```bash
pip install -r day_1/requirements-minimal.txt
```

### Paso 5: Inicia Jupyter

```bash
jupyter notebook
```

Se abrirá una ventana en tu navegador. Navega a `day_1/01_virtual_environments.ipynb`.

## Contenido del Día 1

### Notebooks Disponibles

1. **01_virtual_environments.ipynb** - Entornos Virtuales
   - Conceptos fundamentales de aislamiento de dependencias
   - Creación y gestión de entornos con venv
   - Herramientas modernas como uv
   - Mejores prácticas

2. **02_type_hinting.ipynb** - Type Hinting
   - Anotaciones de tipo en Python
   - Tipos básicos y complejos
   - Validación con pyright
   - Type hints en clases

3. **03_modules_and_imports.ipynb** - Módulos e Imports
   - Sistema de módulos de Python
   - Estructura de paquetes profesional
   - Importaciones absolutas y relativas
   - Configuración con pyproject.toml

4. **04_package_distribution.ipynb** - Distribución de Paquetes
   - Creación de paquetes distribuibles
   - Wheels y source distributions
   - Publicación en PyPI
   - Versionado semántico

5. **05_code_quality_tools.ipynb** - Herramientas de Calidad
   - Linting con ruff
   - Type checking con pyright
   - Formateo automático
   - Integración en flujo de trabajo

Tiempo estimado por notebook: 45-60 minutos

## Objetivos de Aprendizaje

Al finalizar el Día 1, serás capaz de:

- Comprender la importancia de los entornos Python aislados
- Crear y gestionar entornos virtuales usando venv y uv
- Aplicar type hints para mejorar la calidad del código
- Estructurar proyectos Python de forma profesional
- Configurar herramientas de calidad de código
- Crear paquetes distribuibles

## Ejercicios Prácticos

Los ejercicios están en la carpeta `exercises/` con sus tests correspondientes:

```bash
# Ejecutar tests de un ejercicio específico
pytest exercises/tests/test_02_type_hinting.py -v

# Ejecutar todos los tests del día
pytest exercises/tests/ -v

# Con el script helper
./run_tests.sh          # Linux/Mac
run_tests.bat           # Windows
```

## Validación de Código

Verifica que tu código cumple con los estándares:

```bash
# Type checking
pyright exercises/

# Linting
ruff check exercises/

# Formateo
ruff format exercises/
```

## Solución de Problemas

### "python: command not found"
Python no está instalado o no está en tu PATH. Descárgalo desde [python.org](https://www.python.org/downloads/)

### "pip: command not found"
Asegúrate de que el entorno virtual está activado. Deberías ver `(venv)` en tu terminal.

### "ModuleNotFoundError: No module named 'jupyter'"
Verifica que instalaste las dependencias:
```bash
pip install -r day_1/requirements-minimal.txt
```

## Lista de Verificación

Antes de pasar al Día 2, asegúrate de haber:

- [ ] Creado un entorno virtual en la raíz del proyecto
- [ ] Activado el entorno virtual
- [ ] Instalado las dependencias mínimas
- [ ] Completado los 5 notebooks
- [ ] Ejecutado los ejercicios con tests pasando
- [ ] Validado el código con ruff y pyright

## Próximos Pasos

Una vez completes el Día 1:

1. Mantén el entorno virtual activado
2. Instala las dependencias completas: `pip install -r requirements.txt`
3. Continúa con el Día 2: Código Pythónico

## Recursos Adicionales

- [Documentación de Python venv](https://docs.python.org/3/library/venv.html)
- [Documentación de uv](https://docs.astral.sh/uv/)
- [Guía de Empaquetado de Python](https://packaging.python.org/)
- [PEP 484 - Type Hints](https://www.python.org/dev/peps/pep-0484/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [Pyright Documentation](https://microsoft.github.io/pyright/)
