import pytest
from cv_converter.models import CurriculumVitae
from pydantic import ValidationError

def test_crear_cv_valido():
    """Prueba que podemos crear un CV con los datos mínimos necesarios."""
    
    # 1. ARRANGE (Preparar)
    datos_buenos = {
        "nombre_completo": "Tester Profesional",
        "perfil_profesional": "Experto en QA",
        "contacto": {"email": "test@ejemplo.com"},
        "tech_stack": ["Pytest", "Python"]
    }
    
    # 2. ACT (Ejecutar)
    cv = CurriculumVitae(**datos_buenos)
    
    # 3. ASSERT (Verificar)
    assert cv.nombre_completo == "Tester Profesional"
    assert cv.contacto.email == "test@ejemplo.com"
    assert len(cv.tech_stack) == 2
    assert cv.experiencia_laboral == [] 

def test_fallo_si_falta_nombre():
    """Prueba que el sistema lanza error si falta un campo obligatorio."""
    
    
    datos_malos = {
        "perfil_profesional": "Fantasma",
        "contacto": {"email": "boo@test.com"}
    }
    

    with pytest.raises(ValidationError):
        CurriculumVitae(**datos_malos)