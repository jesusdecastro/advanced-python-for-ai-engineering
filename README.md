# Python Avanzado para Ingeniería de IA

Curso intensivo de 5 días enfocado en Python avanzado aplicado a Ingeniería de IA, con énfasis en Clean Code, arquitectura de software y mejores prácticas de desarrollo.

**Duración:** 40 horas (5 días x 8 horas)  
**Nivel:** Intermedio-Avanzado  
**Enfoque:** Desarrollo de intuición profunda, no memorización

---

## Inicio Rápido

```bash
# Clonar repositorio
git clone https://github.com/jesusdecastro/advanced-python-for-ai-engineering.git
cd advanced-python-for-ai-engineering

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Instalar dependencias
pip install -e ".[dev]"

# Iniciar con el día que corresponda
cd dia_1  # o dia_2, dia_3, etc.
jupyter notebook
```

**Guías detalladas:** Cada día tiene su propio `README.md` e `INICIO_RAPIDO.md`

---

## Estructura del Curso

**Ver plan completo:** [`plan_de_formacion.md`](plan_de_formacion.md)

El curso está organizado en 5 días con enfoque progresivo:

- **Día 1:** Fundamentos de Python avanzado (entornos virtuales, módulos, type hints, herramientas)
- **Día 2:** Código pythónico (comprehensions, generators, decorators, context managers)
- **Día 3:** Clean Code práctico (error handling, logging, defensive programming, objetos)
- **Día 4:** Arquitectura y patrones de diseño (SOLID, patrones creacionales, estructurales y comportamentales)
- **Día 5:** Testing con pytest (fixtures, parametrize, mocks, testing funcional)

---

## Proyectos Integradores

Proyectos prácticos que integran conceptos de múltiples días:

1. **Data Pipeline** - Pipeline ETL con validación y logging
2. **Log Analyzer** - Análisis de logs con generators y comprehensions
3. **CSV Cleaner** - Limpieza de datos con context managers
4. **Config Manager** - Gestión de configuraciones con type hints
5. **Data Validator** - Validación defensiva de datasets
6. **Text Processing** - Procesamiento de texto con patrones pythónicos

**Documentación:** `proyectos_integradores/README.md`

---

## Requisitos

- **Python:** 3.11 o superior
- **Git:** Para clonar el repositorio
- **Editor:** VS Code recomendado
- **Sistema operativo:** Windows, Linux o macOS

**Verificar instalación:**
```bash
python --version  # Debe mostrar 3.11.x o superior
git --version
```

**Guías de instalación:**
- Python y entornos virtuales: `virtual_env_installation_guide.md`
- Plugins de VS Code: `vscode_plugins.md`

---

## Herramientas y Tecnologías

**Desarrollo:**
- pytest - Testing unitario
- ruff - Linting y formateo
- pyright - Type checking estático
- jupyter - Notebooks interactivos

**Gestión de proyectos:**
- uv - Gestor de paquetes moderno (opcional)
- pip - Gestor de paquetes estándar
- venv - Entornos virtuales

**Documentación:**
- Sphinx - Generación de documentación
- Markdown - Documentación de referencia

---

## Navegación Rápida

**Empezar el curso:**
- Día 1: `dia_1/README.md` o `dia_1/INICIO_RAPIDO.md`
- Día 2: `dia_2/README.md`
- Día 3: `dia_3/README.md`
- Día 4: `dia_4/README.md`
- Día 5: `dia_5/README.md`

**Material de referencia:**
- Clean Code: `dia_3/clean_code/README.md`
- Proyectos integradores: `proyectos_integradores/README.md`
- Plan completo: `plan_de_formacion.md`

**Guías de instalación:**
- Entornos virtuales: `virtual_env_installation_guide.md`
- VS Code: `vscode_plugins.md`

---

## Licencia

Este material educativo está disponible bajo licencia MIT para uso educativo y formación.

**Repositorio:** https://github.com/jesusdecastro/advanced-python-for-ai-engineering
