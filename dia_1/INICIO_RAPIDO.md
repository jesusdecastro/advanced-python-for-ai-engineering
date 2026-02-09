# 🚀 Inicio Rápido - Día 1

## Para Estudiantes Impacientes

Esta guía te permite empezar en **5 minutos**. Si tienes problemas, consulta el `README.md` completo.

---

## Paso 1: Verificar Python (30 segundos)

```bash
python --version
```

**Debe mostrar:** `Python 3.11.x` o superior

❌ **Si no:** Instala Python 3.11+ desde [python.org](https://www.python.org/downloads/)

**Si tenéis ordenador de empresa probar con el portal de empresa.**

---

## Paso 2: Crear Entorno Virtual (1 minuto)

### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/Mac
```bash
python -m venv venv
source venv/bin/activate
```

**Verificar que funciona:**
```bash
python -c "import sys; print(sys.prefix)"
```

Debe mostrar una ruta que contiene `venv`

---

## Paso 3: Instalar Dependencias (2 minutos)

```bash
# Desde la raíz del proyecto (donde está pyproject.toml)
pip install -e ".[dev]"
```

**Verificar:**
```bash
pytest --version
ruff --version
pyright --version
```

Todos deben funcionar sin errores.

---

## Paso 4: Abrir Jupyter (30 segundos)

```bash
cd dia_1
jupyter notebook
```

Se abre tu navegador → Haz clic en `01_python_idioms_intro.ipynb`

---

## Paso 5: Ejecutar Tu Primer Test (1 minuto)

```bash
# Desde dia_1/
pytest exercises/tests/test_02_type_hinting.py -v
```

**Verás muchos FAILED** - ¡Es normal! Son los ejercicios que completarás.

---

## ✅ ¡Listo!

Ya tienes todo configurado. Ahora:

1. **Sigue los notebooks en orden** (01 → 06)
2. **Completa los ejercicios** cuando llegues al notebook 04
3. **Pregunta si te atascas**

---

## 🆘 Problemas Comunes

### "pytest: command not found"

```bash
# Verifica que venv está activo
which python  # Linux/Mac
where python  # Windows

# Debe mostrar ruta en venv/
# Si no, activa el venv de nuevo
```

### "ModuleNotFoundError"

```bash
# Asegúrate de estar en dia_1/
pwd  # Linux/Mac
cd   # Windows

# Debe mostrar: .../dia_1
```

### "No puedo instalar paquetes"

```bash
# Actualiza pip primero
python -m pip install --upgrade pip

# Luego intenta de nuevo
pip install -e ".[dev]"
```

---

## 📞 Ayuda

- **Instructor:** Levanta la mano
- **Compañeros:** Pregunta a tu lado
- **Documentación:** `README.md` en esta carpeta

---

**Tiempo total:** ~5 minutos  
**Siguiente paso:** Abre `01_python_idioms_intro.ipynb` y empieza a aprender 🎓
