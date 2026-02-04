# Curso de Python Avanzado para IA

Curso intensivo de 6 días enfocado en Python avanzado aplicado a Inteligencia Artificial.

## Inicio Rápido

Para comenzar el curso, dirígete a la carpeta `day_1/` y sigue las instrucciones en su README:

```bash
cd day_1
```

Allí encontrarás el punto de entrada completo con instrucciones paso a paso para configurar tu entorno.

## Estructura del Curso

- **Día 1**: Entornos virtuales y configuración de Python
- **Día 2**: NumPy y manipulación de datos
- **Día 3**: Pandas y análisis de datos
- **Día 4**: Machine Learning con scikit-learn
- **Día 5**: Deep Learning con PyTorch/TensorFlow
- **Día 6**: Proyecto final integrador

## Requisitos

- Python 3.10 o superior
- Conexión a internet (para descargar paquetes)
- Editor de texto o IDE (VS Code, PyCharm, etc.)

## Tecnologías Utilizadas

- Python 3.10+
- Jupyter Notebooks
- NumPy, Pandas
- scikit-learn
- PyTorch / TensorFlow
- Matplotlib, Seaborn

## Estructura del Repositorio

```
├── day_1/              # Punto de entrada - Entornos virtuales
├── day_2/              # NumPy y manipulación de datos
├── day_3/              # Pandas y análisis de datos
├── day_4/              # Machine Learning
├── day_5/              # Deep Learning
├── day_6/              # Proyecto final
├── exercises/          # Módulos Python para practicar
├── solutions/          # Soluciones de ejercicios
├── resources/          # Material adicional
├── requirements.txt    # Dependencias completas
└── pyproject.toml      # Configuración del proyecto
```

## Cómo Usar Este Repositorio

1. Clona o descarga el repositorio
2. Abre `day_1/README.md` para comenzar
3. Sigue las instrucciones para configurar tu entorno
4. Completa los notebooks en orden
5. Practica con los ejercicios en la carpeta `exercises/`

## Ejercicios Prácticos

Cada notebook tiene ejercicios asociados con tests unitarios:

```bash
# Desde la carpeta day_1
cd day_1

# Completa los ejercicios en exercises/02_type_hinting.py
code exercises/02_type_hinting.py

# Ejecuta los tests para validar tu solución
pytest exercises/tests/test_02_type_hinting.py -v

# O usa el script helper
./run_tests.sh          # En Linux/Mac
run_tests.bat           # En Windows
```

Todos los tests deben pasar para considerar el ejercicio como completado.

## Validación de Código

Asegúrate de que tu código siga los estándares del curso:

```bash
# Validar type hints con Pyright
pyright exercises/02_type_hinting.py

# Verificar calidad con Ruff
ruff check exercises/02_type_hinting.py

# Formatear código
ruff format exercises/02_type_hinting.py
```

## Notas Importantes

- Cada día tiene su propio README con instrucciones específicas
- Mantén el entorno virtual activado mientras trabajas
- Completa los notebooks en orden para mejor comprensión
- Los ejercicios son fundamentales para el aprendizaje

¡Bienvenido al curso! Comienza en `day_1/README.md`.
