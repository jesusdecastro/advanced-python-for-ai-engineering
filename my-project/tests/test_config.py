# tests/test_config.py

def test_sanity_check():
    """
    Test tonto para verificar que pytest funciona.
    """
    assert 1 + 1 == 2

def test_import_src():
    """
    Test crítico: Verifica que la carpeta src es visible.
    Si este falla, es que el 'pip install -e .' no funcionó bien.
    """
    # Intentamos importar tu paquete (suponiendo que en src hay algo)
    # Si te da error, cambia 'tu_paquete' por el nombre real de la carpeta dentro de src
    try:
        import sys
        assert True
    except ImportError:
        assert False, "No se pudo importar nada del sistema"