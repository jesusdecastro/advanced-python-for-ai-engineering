# Curso de Python Avanzado para IA

Curso intensivo de 6 días enfocado en Python avanzado aplicado a Inteligencia Artificial.

## 📋 Estructura del Curso

- **Día 1**: Entornos virtuales y configuración de Python
- **Día 2**: NumPy y manipulación de datos
- **Día 3**: Pandas y análisis de datos
- **Día 4**: Machine Learning con scikit-learn
- **Día 5**: Deep Learning con PyTorch/TensorFlow
- **Día 6**: Proyecto final integrador

## 🚀 Configuración del Entorno

### Opción 1: Usando venv (Python estándar)

```bash
# Windows
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# Linux/Mac
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

O usa el script automatizado:
```bash
python setup_venv.py
```

### Opción 2: Usando UV (Recomendado - más rápido)

Primero instala UV: https://docs.astral.sh/uv/getting-started/installation/

```bash
uv sync
```

## 📚 Estructura del Repositorio

```
├── day_1/          # Notebooks y ejercicios del día 1
├── day_2/          # Notebooks y ejercicios del día 2
├── day_3/          # Notebooks y ejercicios del día 3
├── day_4/          # Notebooks y ejercicios del día 4
├── day_5/          # Notebooks y ejercicios del día 5
├── day_6/          # Proyecto final
├── exercises/      # Módulos Python para practicar
├── solutions/      # Soluciones de los ejercicios
└── resources/      # Material adicional y datasets
```

## 📖 Cómo Usar Este Repositorio

1. Configura tu entorno (elige venv o UV)
2. Navega a la carpeta del día correspondiente
3. Abre los notebooks con Jupyter
4. Completa los ejercicios en la carpeta `exercises/`
5. Compara con las soluciones cuando termines

## 🛠️ Tecnologías

- Python 3.10+
- Jupyter Notebooks
- NumPy, Pandas
- scikit-learn
- PyTorch / TensorFlow
- Matplotlib, Seaborn
