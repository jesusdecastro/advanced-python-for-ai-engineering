"""
Entry point for namespace package example (WITHOUT __init__.py).

This demonstrates what WORKS and what DOESN'T WORK with namespace packages.

Run from day_1 directory:
    python examples/run_namespace_package.py
"""

import sys
from pathlib import Path

# Add parent directory to path to allow imports
sys.path.insert(0, str(Path(__file__).parent.parent))

print("=" * 70)
print("EJEMPLO 1: NAMESPACE PACKAGE (SIN __init__.py)")
print("=" * 70)
print()

# ============================================================================
# ✅ ESTO FUNCIONA: Imports explícitos de módulos
# ============================================================================

print("✅ FUNCIONA: Imports explícitos")
print("-" * 70)

from examples.namespace_package.utils import greet, calculate_sum
from examples.namespace_package.models import User, Product

# Usar funciones importadas
message = greet("Alice")
print(f"1. greet('Alice') = {message}")

total = calculate_sum([1, 2, 3, 4, 5])
print(f"2. calculate_sum([1,2,3,4,5]) = {total}")

# Usar clases importadas
user = User("Bob", "bob@example.com")
print(f"3. User created: {user}")

product = Product("Laptop", 999.99)
print(f"4. Product created: {product}")

print()

# ============================================================================
# ❌ ESTO NO FUNCIONA: Import del paquete directamente
# ============================================================================

print("❌ NO FUNCIONA: Import del paquete directamente")
print("-" * 70)

try:
    import examples.namespace_package as pkg
    print(f"Package imported: {pkg}")
    print(f"Package type: {type(pkg)}")
    print(f"Package attributes: {dir(pkg)}")
    
    # Intentar acceder a funciones/clases directamente
    print("\nIntentando acceder a pkg.greet...")
    pkg.greet("Charlie")  # ❌ Esto fallará
    
except AttributeError as e:
    print(f"❌ ERROR: {e}")
    print("   Razón: Sin __init__.py, el paquete no expone sus módulos")
    print("   Solución: Usa imports explícitos como arriba")

print()

# ============================================================================
# ❌ ESTO NO FUNCIONA: from package import *
# ============================================================================

print("❌ NO FUNCIONA: from package import *")
print("-" * 70)

try:
    # Esto no importará nada útil
    from examples.namespace_package import *
    print("Import ejecutado, pero...")
    print(f"Variables disponibles: {[x for x in dir() if not x.startswith('_')]}")
    print("❌ No se importó nada útil (no hay __all__ sin __init__.py)")
    
except Exception as e:
    print(f"❌ ERROR: {e}")

print()

# ============================================================================
# ℹ️ INFORMACIÓN: Inspeccionar el namespace package
# ============================================================================

print("ℹ️  INFORMACIÓN: Características del namespace package")
print("-" * 70)

import examples.namespace_package as pkg

print(f"1. Tipo: {type(pkg)}")
print(f"2. Tiene __file__: {hasattr(pkg, '__file__')}")
if hasattr(pkg, '__file__'):
    print(f"   __file__ = {pkg.__file__}")
else:
    print("   __file__ = None (típico de namespace packages)")

print(f"3. __path__: {pkg.__path__}")
print(f"4. Es namespace package: {not hasattr(pkg, '__file__')}")

print()

# ============================================================================
# ✅ RESUMEN: Cómo usar namespace packages correctamente
# ============================================================================

print("=" * 70)
print("RESUMEN: Namespace Packages (sin __init__.py)")
print("=" * 70)
print()
print("✅ FUNCIONA:")
print("   • from package.module import function")
print("   • from package.module import Class")
print("   • import package.module")
print()
print("❌ NO FUNCIONA:")
print("   • import package → package.function()")
print("   • from package import *")
print("   • Acceso directo a contenido del paquete")
print()
print("💡 CONCLUSIÓN:")
print("   Namespace packages requieren imports EXPLÍCITOS de módulos.")
print("   Para una API más amigable, usa __init__.py (ver ejemplo 2).")
print("=" * 70)
