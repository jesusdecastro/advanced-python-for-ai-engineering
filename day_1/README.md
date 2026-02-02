# Día 1: Entornos Virtuales y Configuración de Python

## Descripción General

Este es el punto de entrada del curso. Aquí aprenderás a configurar tu entorno de desarrollo Python, que es fundamental para todo lo que viene después.

## Inicio Rápido (5 minutos)

### Paso 1: Navega a la Raíz del Repositorio

```bash
cd ..
```

(Si estás en `day_1/`, vuelve a la carpeta raíz del proyecto)

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

Esto instala solo lo esencial para el Día 1 (menos de 2 minutos).

### Paso 5: Inicia Jupyter

```bash
jupyter notebook
```

Se abrirá una ventana en tu navegador. Navega a `day_1/01_virtual_environments.ipynb`.

## Contenido del Día 1

### Notebook: 01_virtual_environments.ipynb

En este notebook aprenderás:

1. **Qué son los entornos virtuales** - Conceptos fundamentales
2. **Por qué son esenciales** - Visualización del problema de conflictos de dependencias
3. **Cómo crear entornos con venv** - Paso a paso
4. **Herramientas modernas como uv** - Alternativas rápidas
5. **Mejores prácticas** - Cómo gestionar proyectos Python profesionalmente

Tiempo estimado: 45-60 minutos

## Objetivos de Aprendizaje

Al finalizar el Día 1, serás capaz de:

- Comprender la importancia de los entornos Python aislados
- Crear y gestionar entornos virtuales usando `venv`
- Utilizar herramientas modernas como `uv` para gestión rápida de dependencias
- Aplicar mejores prácticas en la configuración de proyectos Python
- Verificar que tu entorno de desarrollo esté correctamente configurado

## Requisitos Previos

- Python 3.10 o superior instalado
- Conocimientos básicos de línea de comandos
- Editor de texto o IDE (VS Code, PyCharm, etc.)

## Solución de Problemas

### "python: command not found" o "python3: command not found"
Python no está instalado o no está en tu PATH. Descárgalo desde [python.org](https://www.python.org/downloads/)

### "pip: command not found"
Asegúrate de que el entorno virtual está activado. Deberías ver `(venv)` en tu terminal.

### "ModuleNotFoundError: No module named 'jupyter'"
Verifica que instalaste las dependencias:
```bash
pip install -r day_1/requirements-minimal.txt
```

### Instalación lenta
Si la instalación es muy lenta, intenta:
```bash
pip install --upgrade pip
pip install -r day_1/requirements-minimal.txt --no-cache-dir
```

## Lista de Verificación

Antes de pasar al Día 2, asegúrate de haber:

- [ ] Creado un entorno virtual en la raíz del proyecto
- [ ] Activado el entorno virtual
- [ ] Instalado `day_1/requirements-minimal.txt`
- [ ] Ejecutado `jupyter notebook` exitosamente
- [ ] Completado todas las celdas del notebook
- [ ] Respondido las preguntas de autoevaluación

## Próximos Pasos

Una vez completes el Día 1:

1. Mantén el entorno virtual activado
2. Instala las dependencias completas: `pip install -r requirements.txt`
3. Dirígete al Día 2 para aprender sobre NumPy

## Recursos Adicionales

- [Documentación de Python venv](https://docs.python.org/3/library/venv.html)
- [Documentación de uv](https://docs.astral.sh/uv/)
- [Guía de Empaquetado de Python](https://packaging.python.org/)

