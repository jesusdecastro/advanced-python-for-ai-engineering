# UV: Gestor de Paquetes Python Ultrarrápido

## ¿Qué es UV y Por Qué Importa?

UV es una herramienta moderna para gestionar paquetes y entornos virtuales en Python. Piensa en ella como una versión **10-100x más rápida** de pip, escrita en Rust.

**Problema que resuelve**: pip es lento, especialmente con muchas dependencias. UV hace lo mismo pero mucho más rápido.

**Para este curso**: Usaremos UV como reemplazo directo de pip. Es más rápido y te prepara para herramientas modernas.

---

## Instalación de UV

### Windows (PowerShell)
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# o

irm https://astral.sh/uv/install.ps1 | iex
```

### macOS/Linux
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Verificar Instalación
```bash
uv --version
```

Si ves un número de versión, ¡está instalado correctamente!

---

## Dos Formas de Usar UV

UV ofrece dos workflows. Para entenderlos, imagina que estás organizando tu cocina:

### Modo 1: Compatibilidad con pip (`uv pip`)
**Analogía**: Tú decides qué comprar, dónde guardarlo, y llevas una lista en papel.

- **Comandos**: `uv pip install`, `uv pip list`
- **Control**: Tú gestionas todo manualmente
- **Cuándo usarlo**: Proyectos simples, scripts, aprendizaje

### Modo 2: Proyecto Moderno (`uv add`, `uv sync`)
**Analogía**: Tienes un sistema automatizado que gestiona tu lista de compras y verifica que todo esté en orden.

- **Comandos**: `uv add`, `uv remove`, `uv sync`
- **Control**: UV gestiona automáticamente archivos de configuración
- **Cuándo usarlo**: Proyectos profesionales, equipos, producción

---

## Parte 1: Modo Compatibilidad (uv pip)

Este es el modo que usaremos en el curso. Si conoces pip, ya sabes usar UV.

### Crear Entorno Virtual

**¿Qué es un entorno virtual?**
Un espacio aislado para instalar paquetes sin afectar tu sistema. Como tener una carpeta separada para cada proyecto.

```bash
# Crear entorno virtual llamado .venv
uv venv

# Resultado: Crea carpeta .venv/ con Python aislado
```

**¿Qué hace internamente?**
1. Crea carpeta `.venv/`
2. Copia el intérprete de Python
3. Configura rutas para que los paquetes se instalen ahí

### Activar Entorno Virtual

**¿Por qué activar?**
Para que tu terminal use el Python del entorno, no el del sistema.

```bash
# Windows (CMD)
.venv\Scripts\activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate
```

**Señal de éxito**: Verás `(.venv)` al inicio de tu prompt.

### Instalar Paquetes

```bash
# Instalar un paquete
uv pip install pandas

# Instalar versión específica
uv pip install pandas==2.0.0

# Instalar múltiples paquetes
uv pip install pandas numpy matplotlib

# Instalar desde requirements.txt
uv pip install -r requirements.txt
```

**¿Qué hace internamente?**
1. Descarga el paquete desde PyPI
2. Resuelve dependencias (qué otros paquetes necesita)
3. Instala todo en `.venv/lib/site-packages/`

### Instalar Paquete Local en Modo Editable

**Caso de uso**: Estás desarrollando un paquete y quieres probarlo sin reinstalar cada vez que cambias el código.

```bash
# Instalar el paquete actual en modo desarrollo
uv pip install -e .

# Instalar con dependencias opcionales
uv pip install -e ".[dev]"
```

**¿Qué significa `-e`?**
- **Editable**: Crea un enlace al código fuente
- Los cambios en tu código se reflejan inmediatamente
- No necesitas reinstalar después de cada cambio

**¿Qué hace internamente?**
1. Lee `pyproject.toml` para saber qué instalar
2. Crea un archivo `.pth` en `site-packages/`
3. Este archivo apunta a tu carpeta `src/`
4. Python importa directamente desde tu código fuente

### Listar Paquetes Instalados

```bash
# Ver todos los paquetes
uv pip list

# Buscar un paquete específico
uv pip list | grep pandas

# Ver en formato JSON
uv pip list --format=json
```

### Ver Información de un Paquete

```bash
# Detalles del paquete
uv pip show pandas

# Muestra: versión, ubicación, dependencias, etc.
```

**Ejemplo de requirements.txt:**
```
pandas==2.0.0
numpy==1.24.3
matplotlib==3.7.1
```

### Desinstalar Paquetes

```bash
# Desinstalar un paquete
uv pip uninstall pandas

# Desinstalar múltiples
uv pip uninstall pandas numpy

# Desinstalar sin confirmación
uv pip uninstall -y pandas
```

### Desactivar Entorno

```bash
# Volver al Python del sistema
deactivate
```

---

## Parte 2: Modo Proyecto Moderno (uv add/sync)

Este modo es más avanzado. UV gestiona automáticamente tu configuración.

### ¿Cuándo Usar Este Modo?

**Usa `uv pip` si:**
- Estás aprendiendo Python
- Proyecto simple o script
- Quieres control manual

**Usa `uv add/sync` si:**
- Proyecto profesional
- Trabajas en equipo
- Quieres reproducibilidad exacta

### Inicializar Proyecto

```bash
# Crear nuevo proyecto con estructura completa
uv init mi-proyecto
cd mi-proyecto
```

**¿Qué crea?**
```
mi-proyecto/
├── pyproject.toml      # Configuración del proyecto
├── README.md           # Documentación
├── .python-version     # Versión de Python
└── src/
    └── mi_proyecto/
        └── __init__.py
```

### Añadir Dependencias

```bash
# Añadir paquete (actualiza pyproject.toml automáticamente)
uv add pandas

# Añadir con versión específica
uv add "pandas>=2.0.0"

# Añadir dependencia de desarrollo
uv add --dev pytest
```

**¿Qué hace internamente?**
1. Añade la dependencia a `pyproject.toml`
2. Resuelve todas las dependencias
3. Crea/actualiza `uv.lock` (más sobre esto abajo)
4. Instala el paquete

**Ejemplo de pyproject.toml después de `uv add pandas`:**
```toml
[project]
name = "mi-proyecto"
version = "0.1.0"
dependencies = [
    "pandas>=2.0.0",
]
```

### Sincronizar Entorno

```bash
# Instalar todas las dependencias del pyproject.toml
uv sync

# Solo dependencias de producción (sin dev)
uv sync --no-dev

# Actualizar paquetes a últimas versiones
uv sync --upgrade
```

**¿Qué hace `uv sync`?**
1. Lee `pyproject.toml` y `uv.lock`
2. Compara con lo instalado en `.venv/`
3. Instala lo que falta
4. Desinstala lo que sobra
5. Resultado: Entorno exactamente como debe ser

### Ejecutar Código

```bash
# Ejecutar script (gestiona entorno automáticamente)
uv run python script.py

# Ejecutar comando
uv run pytest

# Ejecutar módulo
uv run -m pytest
```

**Ventaja**: No necesitas activar el entorno manualmente. UV lo hace por ti.

### Eliminar Dependencias

```bash
# Eliminar paquete
uv remove pandas

# Eliminar dependencia de desarrollo
uv remove --dev pytest
```

**¿Qué hace internamente?**
1. Elimina del `pyproject.toml`
2. Actualiza `uv.lock`
3. Desinstala del entorno

---

## El Lockfile (uv.lock): ¿Qué Es y Por Qué Importa?

### ¿Qué es un Lockfile?

**Analogía**: Imagina que escribes una receta que dice "azúcar". ¿Cuánto? ¿Qué tipo? Un lockfile es como escribir "exactamente 200g de azúcar blanca marca X".

**Definición técnica**: Un archivo que registra las versiones **exactas** de todos los paquetes instalados, incluyendo subdependencias.

### ¿Por Qué Necesitamos un Lockfile?

**Problema sin lockfile:**
```toml
# pyproject.toml
dependencies = ["pandas>=2.0.0"]
```

- Hoy instalas: pandas 2.0.0
- En 6 meses instalas: pandas 2.2.0
- Resultado: Código puede comportarse diferente

**Solución con lockfile:**
```
# uv.lock (simplificado)
pandas==2.0.0
numpy==1.24.3  # Dependencia de pandas
pytz==2023.3   # Dependencia de pandas
```

- Siempre instalas exactamente estas versiones
- Reproducibilidad garantizada

### ¿Qué Contiene uv.lock?

```
# Ejemplo simplificado de uv.lock
[[package]]
name = "pandas"
version = "2.0.0"
dependencies = [
    "numpy>=1.20.0",
    "pytz>=2020.1",
]

[[package]]
name = "numpy"
version = "1.24.3"
dependencies = []

[[package]]
name = "pytz"
version = "2023.3"
dependencies = []
```

**Información que guarda:**
- Nombre exacto del paquete
- Versión exacta
- Dependencias exactas
- Hash del archivo (para verificar integridad)
- Fuente (PyPI, Git, etc.)

### ¿Cuándo se Crea/Actualiza uv.lock?

```bash
# Se crea/actualiza automáticamente con:
uv add pandas        # Añadir paquete
uv remove pandas     # Remover paquete
uv sync --upgrade    # Actualizar versiones
```

### ¿Debo Commitear uv.lock en Git?

**Sí, siempre.** Es parte esencial del proyecto.

**Razones:**
1. **Reproducibilidad**: Otros desarrolladores instalan exactamente lo mismo
2. **CI/CD**: Tests corren con las mismas versiones
3. **Producción**: Despliegas con versiones probadas

### Workflow con Lockfile

**Desarrollador A:**
```bash
uv add pandas        # Añade pandas, actualiza uv.lock
git add pyproject.toml uv.lock
git commit -m "Add pandas dependency"
git push
```

**Desarrollador B:**
```bash
git pull             # Obtiene pyproject.toml y uv.lock
uv sync              # Instala exactamente lo mismo que A
```

### Actualizar Dependencias

```bash
# Actualizar todas las dependencias a últimas versiones
uv sync --upgrade

# Actualizar solo un paquete
uv add pandas --upgrade

# Ver qué paquetes tienen actualizaciones disponibles
uv pip list --outdated
```

**¿Qué hace `--upgrade`?**
1. Busca versiones más recientes que cumplan restricciones
2. Actualiza `uv.lock` con nuevas versiones
3. Reinstala paquetes actualizados

### Lockfile vs requirements.txt

| Aspecto | requirements.txt | uv.lock |
|---------|------------------|---------|
| **Formato** | Texto simple | Formato estructurado |
| **Subdependencias** | Opcional | Siempre incluidas |
| **Hashes** | Opcional | Siempre incluidos |
| **Gestión** | Manual | Automática |
| **Reproducibilidad** | Parcial | Total |

**Ejemplo comparativo:**

```
# requirements.txt
pandas==2.0.0
numpy==1.24.3
pytz==2023.3
```

```toml
# uv.lock (simplificado)
[[package]]
name = "pandas"
version = "2.0.0"
source = { registry = "https://pypi.org/simple" }
dependencies = ["numpy>=1.20.0", "pytz>=2020.1"]
wheels = [
    { url = "...", hash = "sha256:abc123..." }
]
```

---

## Comparación directa

### Instalar Pandas

**Modo pip:**
```bash
uv venv
.venv\Scripts\activate
uv pip install pandas
```

**Modo moderno:**
```bash
uv init
uv add pandas
# No necesitas activar entorno
```

### Compartir Proyecto

```bash
# Desarrollador A
uv add pandas
git add pyproject.toml uv.lock
git commit -m "Add pandas"

# Desarrollador B
git pull
uv sync
# ¡Listo! Mismo entorno exacto
```

---

## Tabla Resumen de Comandos

### Comandos Modo pip

| Comando | Descripción |
|---------|-------------|
| `uv venv` | Crear entorno virtual |
| `.venv\Scripts\activate` | Activar entorno (Windows) |
| `source .venv/bin/activate` | Activar entorno (macOS/Linux) |
| `uv pip install pandas` | Instalar paquete |
| `uv pip install -e .` | Instalar paquete local editable |
| `uv pip install -r requirements.txt` | Instalar desde archivo |
| `uv pip list` | Listar paquetes |
| `uv pip show pandas` | Info de paquete |
| `uv pip freeze > requirements.txt` | Exportar dependencias |
| `uv pip uninstall pandas` | Desinstalar paquete |
| `deactivate` | Desactivar entorno |

### Comandos Modo Moderno

| Comando | Descripción |
|---------|-------------|
| `uv init mi-proyecto` | Crear proyecto nuevo |
| `uv add pandas` | Añadir dependencia |
| `uv add --dev pytest` | Añadir dependencia de desarrollo |
| `uv remove pandas` | Remover dependencia |
| `uv sync` | Sincronizar entorno con pyproject.toml |
| `uv sync --upgrade` | Actualizar dependencias |
| `uv run python script.py` | Ejecutar script |
| `uv run pytest` | Ejecutar comando |

---

## Preguntas Frecuentes

### ¿UV reemplaza a pip completamente?

**Sí y no.**
- Para instalar paquetes: Sí, UV es más rápido
- Para publicar en PyPI: Todavía necesitas otras herramientas
- Para este curso: UV hace todo lo que necesitamos

### ¿Necesito desinstalar pip?

**No.** UV y pip pueden coexistir. UV es un complemento, no un reemplazo obligatorio.

### ¿Qué pasa si uso pip en lugar de uv pip?

Funciona igual, solo que más lento. UV es compatible con pip.

### ¿Puedo usar UV en proyectos existentes?

**Sí.** Simplemente usa `uv pip` en lugar de `pip`. Todo lo demás funciona igual.

### ¿El lockfile es como package-lock.json de Node.js?

**Exacto.** Mismo concepto, diferente ecosistema.

### ¿Debo usar modo pip o modo moderno?

**Para aprender**: Modo pip (más simple)
**Para proyectos reales**: Modo moderno (más robusto)

---

## Solución de Problemas

### Error: "command not found: uv"

**Causa**: UV no está en el PATH.

**Solución**:
```bash
# Windows: Reinicia PowerShell después de instalar
# macOS/Linux: Añade a ~/.bashrc o ~/.zshrc
export PATH="$HOME/.cargo/bin:$PATH"
```

### Error: "No module named 'mi_paquete'"

**Causa**: No instalaste el paquete en modo editable.

**Solución**:
```bash
uv pip install -e .
```

### Entorno virtual no se activa

**Causa**: Estás en el directorio incorrecto.

**Solución**:
```bash
# Verifica que existe .venv/
ls .venv

# Si no existe, créalo
uv venv
```

### UV es muy lento en Windows

**Causa**: Antivirus escaneando cada archivo.

**Solución**: Añade `.venv/` a exclusiones del antivirus.

---

## Recursos Oficiales

- **Documentación UV**: https://docs.astral.sh/uv/
- **GitHub**: https://github.com/astral-sh/uv
- **Guía de Migración desde pip**: https://docs.astral.sh/uv/pip/

---

## Resumen: Lo Esencial

**Para este curso, recuerda:**

1. **Instalar UV**: Más rápido que pip
2. **Usar `uv pip`**: Compatible con lo que conoces
3. **Crear entorno**: `uv venv`
4. **Activar**: `.venv\Scripts\activate`
5. **Instalar editable**: `uv pip install -e ".[dev]"`
6. **Ejecutar tests**: `pytest`

**Siguiente nivel (opcional):**
- Explora `uv add/sync` para proyectos profesionales
- Entiende lockfiles para reproducibilidad
- Usa `uv run` para ejecutar sin activar entorno

**Lo más importante**: UV hace lo mismo que pip, pero más rápido. No te preocupes por los detalles avanzados hasta que los necesites.
