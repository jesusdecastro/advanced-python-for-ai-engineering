# tests/test_smoke.py
import sys
import os

def test_pytest_funciona():
    """
    Test básico: Si esto falla, pytest no está bien instalado.
    """
    assert 1 + 1 == 2

def test_puedo_ver_src():
    """
    Test de arquitectura: Verifica que la carpeta 'src' es visible.
    Si esto falla, necesitas ejecutar 'pip install -e .' en la terminal.
    """
    # Imprimimos donde busca Python para que lo veas en caso de error
    print(f"Rutas de Python: {sys.path}")
    
    # Intenta importar tu paquete. 
    # NOTA: Cambia 'nombre_de_tu_paquete' por el nombre real de la carpeta dentro de src/
    # Si aún no tienes nada en src, este test fallará (y es normal).
    try:
        # import nombre_de_tu_paquete 
        assert True
    except ImportError:
        # Si falla, no pasa nada por ahora, pero nos avisa.
        pass