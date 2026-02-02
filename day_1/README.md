# Día 1: Entornos Virtuales y Configuración de Python

## Descripción General

Este día se enfoca en comprender y configurar entornos de desarrollo Python adecuados, lo cual es crucial para cualquier proyecto de IA/ML.

## Contenido

### Notebooks

1. **01_virtual_environments.ipynb** - Fundamentos de entornos virtuales
   - Qué son los entornos virtuales y por qué son importantes
   - Crear entornos con `venv`
   - Gestión moderna de dependencias con `uv`
   - Mejores prácticas para gestión de proyectos

## Objetivos de Aprendizaje

Al finalizar el Día 1, los estudiantes serán capaces de:

- Comprender la importancia de los entornos Python aislados
- Crear y gestionar entornos virtuales usando `venv`
- Utilizar herramientas modernas como `uv` para gestión rápida de dependencias
- Aplicar mejores prácticas en la configuración de proyectos Python
- Verificar que su entorno de desarrollo esté correctamente configurado

## Requisitos Previos

- Python 3.10 o superior instalado
- Conocimientos básicos de línea de comandos
- Editor de texto o IDE (VS Code, PyCharm, etc.)

## Inicio Rápido

### Paso 1: Crear el Entorno Virtual

Desde el directorio del curso, ejecuta:

```bash
# Windows
python -m venv venv

# Linux/Mac
python3 -m venv venv
```

### Paso 2: Activar el Entorno

```bash
# Windows (CMD)
venv\Scripts\activate

# Windows (PowerShell)
venv\Scripts\Activate.ps1

# Linux/Mac
source venv/bin/activate
```

Deberías ver `(venv)` al inicio de tu línea de comandos.

### Paso 3: Instalar Dependencias Mínimas

Para ejecutar el notebook del Día 1, instala solo lo esencial:

```bash
pip install -r day_1/requirements-minimal.txt
```

Esto instala:
- **jupyter** y **notebook**: Para ejecutar los notebooks
- **matplotlib**: Para las visualizaciones del notebook
- **numpy** y **pandas**: Para ejemplos de código

La instalación debería completarse en menos de 2 minutos.

### Paso 4: Ejecutar el Notebook

```bash
jupyter notebook day_1/01_virtual_environments.ipynb
```

## Entornos de Dependencias

### requirements-minimal.txt

Este archivo contiene solo lo esencial para ejecutar el Día 1. Es ideal para:
- Instalación rápida
- Verificar que tu entorno funciona
- Comenzar a aprender sin esperar descargas largas

### requirements.txt (Completo)

El archivo `requirements.txt` en la raíz del proyecto contiene todas las dependencias para todo el curso. Úsalo cuando estés listo para los días posteriores:

```bash
pip install -r requirements.txt
```

## Flujo Recomendado

1. **Primero**: Instala `requirements-minimal.txt` (Día 1)
2. **Luego**: Completa el notebook del Día 1
3. **Después**: Instala `requirements.txt` completo para los días 2-6

## Solución de Problemas

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

- [ ] Creado un entorno virtual
- [ ] Activado el entorno virtual
- [ ] Instalado `requirements-minimal.txt`
- [ ] Ejecutado `jupyter notebook` exitosamente
- [ ] Completado todas las celdas del notebook
- [ ] Respondido las preguntas de autoevaluación

## Recursos Adicionales

- [Documentación de Python venv](https://docs.python.org/3/library/venv.html)
- [Documentación de uv](https://docs.astral.sh/uv/)
- [Guía de Empaquetado de Python](https://packaging.python.org/)
