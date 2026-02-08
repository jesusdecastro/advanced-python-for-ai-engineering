# ✅ Checklist del Instructor - Día 1

## 1 Semana Antes del Curso

### Comunicación con Estudiantes

- [ ] **Email de bienvenida enviado** con:
  - [ ] Requisitos técnicos (Python 3.11+, VS Code, Git)
  - [ ] Link al repositorio del curso
  - [ ] Instrucciones de instalación (`INICIO_RAPIDO.md`)
  - [ ] Fecha, hora y duración del curso
  - [ ] Link a la reunión (si es remoto)

- [ ] **Verificar que todos recibieron el email**
  - [ ] Enviar recordatorio a quienes no confirmaron

- [ ] **Crear canal de comunicación** (opcional)
  - [ ] Slack/Discord/Teams para dudas
  - [ ] Compartir link con los estudiantes

### Preparación del Material

- [ ] **Clonar repositorio** en máquina de enseñanza
  ```bash
  git clone <repo-url>
  cd advanced-python-for-ai-engineering
  git checkout dia_1
  ```

- [ ] **Crear entorno virtual** y verificar instalación
  ```bash
  python -m venv venv
  source venv/bin/activate  # o venv\Scripts\activate
  pip install -e ".[dev]"
  ```

- [ ] **Ejecutar todos los notebooks** para verificar que funcionan
  - [ ] 01_python_idioms_intro.ipynb
  - [ ] 02_virtual_environments.ipynb
  - [ ] 03_modules_and_imports.ipynb
  - [ ] 04_type_hinting.ipynb
  - [ ] 05_code_quality_tools.ipynb
  - [ ] 06_package_distribution.ipynb

- [ ] **Ejecutar todos los tests** para verificar que pasan
  ```bash
  pytest dia_1/exercises/tests/ -v
  ```

- [ ] **Verificar ejemplos** en `examples/`
  ```bash
  cd dia_1
  python examples/run_regular_package.py
  python examples/run_namespace_package.py
  ```

### Preparación de Demos

- [ ] **Demo 1: Conflicto de dependencias**
  - [ ] Script preparado para mostrar el problema
  - [ ] Script preparado para mostrar la solución con venv
  - [ ] Probado en tu máquina

- [ ] **Demo 2: Type hints detectando bugs**
  - [ ] Ejemplo de código con bug preparado
  - [ ] Pyright configurado para detectarlo
  - [ ] Probado en tu máquina

- [ ] **Demo 3: Ruff en acción**
  - [ ] Archivo con código mal formateado preparado
  - [ ] Comandos de ruff listos para copiar/pegar
  - [ ] Probado en tu máquina

### Material de Apoyo

- [ ] **Slides preparadas** (si las usas)
  - [ ] Slide de bienvenida
  - [ ] Slide de objetivos del día
  - [ ] Slides de conceptos clave
  - [ ] Slide de cierre

- [ ] **Documentos impresos** (opcional)
  - [ ] INICIO_RAPIDO.md
  - [ ] Comandos útiles
  - [ ] Troubleshooting común

---

## 1 Día Antes del Curso

### Verificación Técnica

- [ ] **Equipo de enseñanza funcionando**
  - [ ] Laptop/PC encendida y actualizada
  - [ ] Batería cargada (si es laptop)
  - [ ] Cargador disponible

- [ ] **Software actualizado**
  - [ ] Python 3.11+ instalado
  - [ ] VS Code actualizado
  - [ ] Extensiones de VS Code instaladas (Python, Ruff, Jupyter)
  - [ ] Git actualizado

- [ ] **Proyector/Pantalla compartida**
  - [ ] Cable HDMI/adaptador disponible
  - [ ] Resolución de pantalla configurada
  - [ ] Probado compartir pantalla (si es remoto)

- [ ] **Internet funcionando**
  - [ ] Conexión estable
  - [ ] Velocidad adecuada para compartir pantalla
  - [ ] Plan B si falla (hotspot móvil)

### Preparación del Entorno

- [ ] **Terminal configurada**
  - [ ] Fuente grande y legible
  - [ ] Colores claros y contrastados
  - [ ] Historial limpio
  - [ ] Venv activado

- [ ] **VS Code configurado**
  - [ ] Fuente grande (14-16pt)
  - [ ] Tema claro y legible
  - [ ] Extensiones visibles
  - [ ] Workspace abierto en el proyecto

- [ ] **Jupyter funcionando**
  - [ ] Notebooks abren correctamente
  - [ ] Kernel se conecta
  - [ ] Celdas ejecutan sin errores

### Material Listo

- [ ] **Repositorio actualizado**
  ```bash
  git pull origin dia_1
  ```

- [ ] **Ejemplos de código listos**
  - [ ] Archivos de demo en carpeta separada
  - [ ] Scripts de troubleshooting preparados

- [ ] **Notas del instructor**
  - [ ] GUIA_PROFESOR.md revisada
  - [ ] Puntos clave marcados
  - [ ] Timing anotado

---

## Día del Curso - Antes de Empezar

### Llegada Temprana (15-30 min antes)

- [ ] **Llegar al aula/conectarse** 15-30 min antes

- [ ] **Configurar el espacio**
  - [ ] Proyector/pantalla funcionando
  - [ ] Audio funcionando (si es remoto)
  - [ ] Cámara funcionando (si es remoto)
  - [ ] Pizarra/whiteboard disponible

- [ ] **Verificar conexión**
  - [ ] Internet funcionando
  - [ ] Compartir pantalla funciona
  - [ ] Audio se escucha bien

- [ ] **Preparar terminal**
  - [ ] Abrir 2-3 terminales
  - [ ] Activar venv en cada una
  - [ ] Navegar a dia_1/
  - [ ] Limpiar historial

- [ ] **Abrir aplicaciones**
  - [ ] VS Code con proyecto abierto
  - [ ] Jupyter Notebook
  - [ ] Navegador con documentación
  - [ ] Slides (si las usas)

### Material Físico

- [ ] **Laptop/PC lista**
- [ ] **Cargador conectado**
- [ ] **Ratón** (si lo usas)
- [ ] **Agua/café** para ti
- [ ] **Notas del instructor** a mano

### Verificación Final

- [ ] **Ejecutar un test rápido**
  ```bash
  pytest dia_1/exercises/tests/test_02_type_hinting.py::TestCalculateRectangleArea -v
  ```

- [ ] **Abrir un notebook**
  - Verificar que se ve bien en el proyector

- [ ] **Compartir pantalla** (si es remoto)
  - Verificar que se ve bien para los estudiantes

---

## Durante el Curso

### Inicio (9:00 - 9:30)

- [ ] **Bienvenida y presentación** (5 min)
  - [ ] Presentarte
  - [ ] Objetivos del curso
  - [ ] Estructura del día

- [ ] **Verificar setup de estudiantes** (20 min)
  - [ ] ¿Todos tienen Python 3.11+?
  - [ ] ¿Todos tienen VS Code?
  - [ ] ¿Todos tienen Git?
  - [ ] ¿Todos clonaron el repo?

- [ ] **Ayudar con problemas** (5 min)
  - Circular y ayudar a quienes tengan problemas

### Durante las Sesiones

- [ ] **Monitorear engagement**
  - [ ] ¿Todos siguen el ritmo?
  - [ ] ¿Hay caras de confusión?
  - [ ] ¿Hacen preguntas?

- [ ] **Pausar para preguntas** cada 20-30 min
  - "¿Alguna duda hasta aquí?"

- [ ] **Circular durante ejercicios**
  - Ayudar individualmente
  - Identificar problemas comunes

- [ ] **Ajustar ritmo** según necesidad
  - Acelerar si van muy rápido
  - Ralentizar si van muy lentos

### Descansos

- [ ] **Descanso de 15 min** a media mañana (10:30)
- [ ] **Almuerzo de 60 min** (13:00)
- [ ] **Descanso de 15 min** a media tarde (15:30)

**Durante descansos:**
- [ ] Estar disponible para preguntas
- [ ] Ayudar con problemas técnicos
- [ ] Preparar siguiente sesión

---

## Monitoreo Durante el Día

### Señales de Alerta

**Van muy rápido:**
- [ ] Estudiantes distraídos
- [ ] Terminan ejercicios muy rápido
- [ ] Preguntan sobre temas futuros

**Acción:** Acelerar, profundizar, ejercicios extra

**Van muy lento:**
- [ ] Muchos se quedan atrás
- [ ] Caras de confusión
- [ ] No hacen preguntas (por miedo)

**Acción:** Ralentizar, explicar de nuevo, más ejemplos

### Problemas Técnicos Comunes

- [ ] **"No puedo activar el venv"**
  - Verificar que lo crearon correctamente
  - Verificar permisos
  - Verificar PATH

- [ ] **"pytest no funciona"**
  - Verificar que venv está activo
  - Verificar que instalaron dependencias
  - Verificar que están en directorio correcto

- [ ] **"Jupyter no abre"**
  - Verificar que instalaron jupyter
  - Verificar puerto 8888 disponible
  - Usar `--no-browser` y copiar URL

---

## Cierre del Día (17:45 - 18:00)

### Resumen

- [ ] **Recapitular conceptos clave** (5 min)
  - Entornos virtuales
  - Type hints
  - Herramientas de calidad

- [ ] **Verificar que todos completaron** (5 min)
  - [ ] Tienen venv funcionando
  - [ ] Ejecutaron al menos un test
  - [ ] Entienden cómo continuar

- [ ] **Tarea opcional** (2 min)
  - Completar ejercicios pendientes
  - Leer documentación de type hints

- [ ] **Preview del Día 2** (2 min)
  - Qué veremos mañana
  - Por qué es importante

### Feedback

- [ ] **Encuesta rápida** (1 min)
  - ¿Qué fue más difícil?
  - ¿El ritmo fue adecuado?
  - ¿Qué mejorarías?

- [ ] **Preguntas finales**
  - Responder dudas de último minuto

---

## Después del Curso

### Inmediatamente Después

- [ ] **Guardar notas**
  - Qué funcionó bien
  - Qué mejorar
  - Problemas comunes encontrados

- [ ] **Responder preguntas pendientes**
  - Por email/chat
  - Actualizar FAQ si es necesario

### Ese Mismo Día

- [ ] **Enviar email de seguimiento**
  - Resumen del día
  - Recursos adicionales
  - Recordatorio de tarea (si hay)
  - Preview del Día 2

- [ ] **Actualizar material** si es necesario
  - Corregir errores encontrados
  - Mejorar explicaciones confusas
  - Añadir ejemplos que funcionaron bien

### Preparación para Día 2

- [ ] **Revisar material del Día 2**
- [ ] **Preparar demos del Día 2**
- [ ] **Actualizar checklist del Día 2**

---

## Troubleshooting Rápido

### Estudiante no puede instalar paquetes

```bash
# Verificar Python
python --version

# Verificar pip
python -m pip --version

# Actualizar pip
python -m pip install --upgrade pip

# Instalar con módulo pip
python -m pip install -e ".[dev]"
```

### Estudiante no puede activar venv

```bash
# Windows
venv\Scripts\activate

# Si falla, probar con PowerShell
venv\Scripts\Activate.ps1

# Si falla, verificar permisos
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Linux/Mac
source venv/bin/activate

# Si falla, verificar que existe
ls venv/bin/activate
```

### Tests no pasan

```bash
# Verificar directorio
pwd  # Debe estar en dia_1/

# Ejecutar con más detalle
pytest exercises/tests/ -vv

# Ejecutar test específico
pytest exercises/tests/test_02_type_hinting.py::TestCalculateRectangleArea -vv
```

---

## Recursos de Emergencia

### Si falla el proyector

- [ ] Compartir pantalla por Zoom/Teams
- [ ] Usar laptop de respaldo
- [ ] Continuar sin proyector (menos ideal)

### Si falla internet

- [ ] Usar hotspot móvil
- [ ] Trabajar offline (notebooks ya descargados)
- [ ] Posponer instalación de paquetes

### Si un estudiante tiene problemas graves

- [ ] Asignar compañero para que lo ayude
- [ ] Ayudar durante descanso
- [ ] Proporcionar máquina virtual (si está disponible)

---

## Notas Personales

**Espacio para tus notas durante el curso:**

```
Hora: _____
Nota: _______________________________________________
____________________________________________________
____________________________________________________

Hora: _____
Nota: _______________________________________________
____________________________________________________
____________________________________________________

Hora: _____
Nota: _______________________________________________
____________________________________________________
____________________________________________________
```

---

## Contactos de Emergencia

**IT Support:** _______________  
**Coordinador del curso:** _______________  
**Backup instructor:** _______________

---

**Última actualización:** Febrero 2026  
**Versión:** 1.0

**¡Buena suerte con el curso! 🚀**
