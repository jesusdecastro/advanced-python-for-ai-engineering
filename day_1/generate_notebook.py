"""
Script para generar el notebook del Día 1 con referencias a documentación oficial.
"""
import json

notebook = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Día 1: Entornos Virtuales en Python\n",
                "\n",
                "## Objetivos de Aprendizaje\n",
                "\n",
                "Al finalizar este notebook, serás capaz de:\n",
                "\n",
                "1. Comprender qué son los entornos virtuales y por qué son esenciales\n",
                "2. Identificar los problemas que resuelven los entornos virtuales\n",
                "3. Crear y gestionar entornos virtuales con `venv`\n",
                "4. Utilizar herramientas modernas como `uv` para gestión de dependencias\n",
                "5. Aplicar mejores prácticas en la gestión de proyectos Python"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## ¿Qué son los Entornos Virtuales?\n",
                "\n",
                "Un **entorno virtual** es un directorio aislado que contiene:\n",
                "\n",
                "- Una instalación específica de Python\n",
                "- Un conjunto de paquetes instalados independientes del sistema\n",
                "- Sus propios ejecutables y scripts\n",
                "\n",
                "### El Problema que Resuelven\n",
                "\n",
                "Considera este escenario real:\n",
                "\n",
                "- **Proyecto A**: Requiere `numpy==1.21.0` y `pandas==1.3.0`\n",
                "- **Proyecto B**: Requiere `numpy==1.24.0` y `pandas==2.0.0`\n",
                "\n",
                "Sin entornos virtuales, ambos proyectos compartirían las mismas dependencias a nivel del sistema. Instalar una versión diferente de NumPy para el Proyecto B rompería el Proyecto A. Los entornos virtuales resuelven este problema creando espacios aislados donde cada proyecto puede tener sus propias versiones de dependencias.\n",
                "\n",
                "La visualización a continuación muestra este problema y su solución."
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.10.0"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

with open("01_virtual_environments.ipynb", "w") as f:
    json.dump(notebook, f, indent=1, ensure_ascii=False)

print("Notebook generado exitosamente")
