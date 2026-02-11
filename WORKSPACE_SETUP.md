# Configuración de UV Workspace

Este proyecto está configurado como un **UV Workspace** para gestionar múltiples paquetes de ejercicios con configuración compartida.

## ¿Qué es un Workspace?

Un workspace permite:
- Gestionar múltiples proyectos relacionados desde un directorio raíz
- Compartir configuración común (Ruff, Pytest, etc.)
- Instalar dependencias de todos los proyectos con un solo comando
- Mantener consistencia en herramientas y estándares

## Estructura del Workspace

```
advanced-python-for-ai-engineering/
├── pyproject.toml              # Configuración raíz (compartida)
├── dia_2/exercises/
│   └── pyproject.toml          # Hereda config de root
├── dia_3/exercises/
│   └── pyproject.toml          # Hereda config de root
└── [futuros ejercicios]
```

## Configuración Heredada

Los proyectos de ejercicios **heredan automáticamente** del root:

### Ruff (Linter/Formatter)
- ✅ 40+ reglas de linting habilitadas
- ✅ `line-length = 100`
- ✅ Configuración completa de docstrings (Google style)
- ✅ Type hints enforcement
- ✅ Reglas de seguridad y performance
- ✅ Ordenamiento de imports (isort)

### Pytest
- ✅ Configuración de test discovery
- ✅ Opciones de output

### Pyright
- ✅ Type checking mode
- ✅ Python version target

## Cómo Usar el Workspace

### Instalación Inicial (desde el root)

```bash
# Instalar el workspace completo
uv sync --all-packages

# Esto instala:
# - Dependencias del root (jupyter, notebook)
# - Dependencias de dia_2/exercises (pytest, ruff, pyright)
# - Dependencias de dia_3/exercises (pytest, pytest-cov, ruff, pyright)
```

### Trabajar en un Proyecto Específico

```bash
# Opción 1: Desde el root (recomendado)
uv run --package exercises pytest dia_2/exercises/tests/

# Opción 2: Navegar al proyecto
cd dia_2/exercises
uv run pytest

# Opción 3: Usar el workspace desde cualquier lugar
uv run --directory dia_2/exercises pytest
```

### Verificar Código con Ruff

```bash
# Desde el root: verificar todos los ejercicios
uv run ruff check dia_2/exercises/src/ dia_3/exercises/src/

# Desde un proyecto específico
cd dia_2/exercises
uv run ruff check src/

# Formatear código
uv run ruff format src/
```

### Ejecutar Tests

```bash
# Todos los tests del workspace
uv run pytest dia_2/exercises/tests/ dia_3/exercises/tests/

# Tests de un proyecto específico
cd dia_3/exercises
uv run pytest

# Con coverage
uv run pytest --cov=exercises --cov-report=term-missing
```

## Ventajas del Workspace

### 1. Configuración Centralizada
- Una sola fuente de verdad para reglas de Ruff
- Cambios en el root se aplican a todos los proyectos
- Consistencia garantizada

### 2. Gestión Simplificada
```bash
# Antes (sin workspace)
cd dia_2/exercises && uv sync && cd ../..
cd dia_3/exercises && uv sync && cd ../..

# Ahora (con workspace)
uv sync --all-packages
```

### 3. Herencia Inteligente
Los proyectos pueden:
- Heredar configuración del root
- Override solo lo necesario (ej: permitir prints en ejercicios)
- Mantener configuración específica cuando sea necesario

## Configuración Específica por Proyecto

Cada proyecto puede tener overrides específicos en su `pyproject.toml`:

```toml
[tool.ruff.lint.per-file-ignores]
# Ejercicios: permitir prints para debugging
"src/exercises/**/*.py" = ["T20", "D103"]
```

## Añadir Nuevos Proyectos al Workspace

1. Crear el directorio del proyecto:
```bash
mkdir -p dia_4/exercises
cd dia_4/exercises
```

2. Crear `pyproject.toml` básico:
```toml
[project]
name = "exercises-dia4"
version = "0.1.0"
requires-python = ">=3.11"

[tool.ruff]
line-length = 100  # Heredar del root
```

3. Añadir al workspace en el `pyproject.toml` del root:
```toml
[tool.uv.workspace]
members = [
    "dia_2/exercises",
    "dia_3/exercises",
    "dia_4/exercises",  # Nuevo
]
```

4. Sincronizar:
```bash
cd ../../..  # Volver al root
uv sync --all-packages
```

## Verificar la Configuración

```bash
# Ver qué configuración de Ruff se está usando
cd dia_2/exercises
uv run ruff check --show-settings

# Verificar que hereda del root
# Deberías ver todas las reglas (F, E, W, I, N, D, etc.)
```

## Troubleshooting

### "No se heredan las reglas de Ruff"

**Problema**: Los ejercicios no usan la configuración completa del root.

**Solución**:
```bash
# 1. Verificar que el workspace está configurado
cat pyproject.toml | grep -A 5 "tool.uv.workspace"

# 2. Re-sincronizar
uv sync --all-packages

# 3. Verificar configuración
cd dia_2/exercises
uv run ruff check --show-settings
```

### "ModuleNotFoundError al importar"

**Problema**: Los paquetes no están instalados en el workspace.

**Solución**:
```bash
# Desde el root
uv sync --all-packages

# O desde el proyecto específico
cd dia_2/exercises
uv sync
```

## Referencias

- **UV Workspaces**: https://docs.astral.sh/uv/concepts/workspaces/
- **Ruff Configuration**: https://docs.astral.sh/ruff/configuration/
- **Ruff Rules**: https://docs.astral.sh/ruff/rules/

## Resumen

✅ **Configurado**: El proyecto ahora es un UV Workspace  
✅ **Herencia**: Los ejercicios heredan la configuración de Ruff del root  
✅ **Consistencia**: `line-length = 100` en todos los proyectos  
✅ **Centralizado**: Una sola configuración de Ruff con 40+ reglas  
✅ **Flexible**: Cada proyecto puede hacer overrides específicos  

Para empezar a trabajar:
```bash
# Desde el root
uv sync --all-packages

# Verificar que funciona
uv run ruff check dia_2/exercises/src/
```
