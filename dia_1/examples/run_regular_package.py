"""
Entry point for regular package example (WITH __init__.py).

This demonstrates what WORKS with regular packages and the benefits of __init__.py.

Run from dia_1 directory:
    python examples/run_regular_package.py
"""

import sys
from pathlib import Path

# Add parent directory to path to allow imports
sys.path.insert(0, str(Path(__file__).parent.parent))

print("=" * 70)
print("EJEMPLO 2: REGULAR PACKAGE (CON __init__.py)")
print("=" * 70)
print()

# ============================================================================
# ✅ FUNCIONA: Import del paquete directamente
# ============================================================================

print("✅ FUNCIONA: Import del paquete directamente")
print("-" * 70)

import examples.regular_package as pkg

print(f"1. Package imported: {pkg}")
print(f"2. Package version: {pkg.__version__}")
print(f"3. Package author: {pkg.__author__}")
print()

# ============================================================================
# ✅ FUNCIONA: Acceso directo a funciones y clases
# ============================================================================

print("✅ FUNCIONA: Acceso directo desde el paquete")
print("-" * 70)

# Acceso directo a funciones
message = pkg.greet("Alice")
print(f"1. pkg.greet('Alice') = {message}")

total = pkg.calculate_sum([1, 2, 3, 4, 5])
print(f"2. pkg.calculate_sum([1,2,3,4,5]) = {total}")

# Acceso directo a clases
user = pkg.User("Bob", "bob@example.com")
print(f"3. pkg.User created: {user}")

product = pkg.Product("Laptop", 999.99)
print(f"4. pkg.Product created: {product}")

print()

# ============================================================================
# ✅ FUNCIONA: from package import *
# ============================================================================

print("✅ FUNCIONA: from package import * (usa __all__)")
print("-" * 70)

# Clear previous imports for clean demo
if 'greet' in dir():
    del greet, calculate_sum, User, Product

from examples.regular_package import *

print("Importado con 'from regular_package import *':")
print(f"  • greet: {greet}")
print(f"  • calculate_sum: {calculate_sum}")
print(f"  • User: {User}")
print(f"  • Product: {Product}")

# Test imported items
print(f"\nUsando items importados:")
print(f"  greet('Charlie') = {greet('Charlie')}")
print(f"  User('Dave', 'dave@example.com') = {User('Dave', 'dave@example.com')}")

print()

# ============================================================================
# ✅ FUNCIONA: Imports selectivos
# ============================================================================

print("✅ FUNCIONA: Imports selectivos")
print("-" * 70)

from examples.regular_package import greet as say_hello
from examples.regular_package import User as UserModel

print(f"1. Alias import: say_hello('Eve') = {say_hello('Eve')}")
print(f"2. Alias import: UserModel('Frank', 'frank@example.com') = {UserModel('Frank', 'frank@example.com')}")

print()

# ============================================================================
# ℹ️ INFORMACIÓN: Funciones privadas no exportadas
# ============================================================================

print("ℹ️  INFORMACIÓN: Control de API pública con __init__.py")
print("-" * 70)

print("Funciones/clases en __all__ (públicas):")
print(f"  {pkg.__all__}")

print("\nIntentando acceder a función privada (_internal_helper):")
try:
    # Esta función existe en utils.py pero NO está en __init__.py
    pkg._internal_helper()
except AttributeError as e:
    print(f"  ❌ {e}")
    print("  ✅ Correcto: Funciones privadas no se exponen")

print("\nPero SÍ puedes acceder si importas el módulo directamente:")
from examples.regular_package.utils import _internal_helper
print(f"  {_internal_helper()}")
print("  (Esto es intencional para casos avanzados)")

print()

# ============================================================================
# ℹ️ INFORMACIÓN: Inspeccionar el regular package
# ============================================================================

print("ℹ️  INFORMACIÓN: Características del regular package")
print("-" * 70)

print(f"1. Tipo: {type(pkg)}")
print(f"2. Tiene __file__: {hasattr(pkg, '__file__')}")
if hasattr(pkg, '__file__'):
    print(f"   __file__ = {pkg.__file__}")

print(f"3. __path__: {pkg.__path__}")
print(f"4. Es regular package: {hasattr(pkg, '__file__')}")
print(f"5. Atributos públicos: {[x for x in dir(pkg) if not x.startswith('_')]}")

print()

# ============================================================================
# ✅ COMPARACIÓN: Regular vs Namespace Package
# ============================================================================

print("=" * 70)
print("COMPARACIÓN: Regular Package vs Namespace Package")
print("=" * 70)
print()

print("REGULAR PACKAGE (con __init__.py):")
print("  ✅ import package → package.function()")
print("  ✅ from package import *")
print("  ✅ Acceso directo a contenido")
print("  ✅ Control de API pública con __all__")
print("  ✅ Metadata del paquete (__version__, etc.)")
print("  ✅ Inicialización personalizada")
print()

print("NAMESPACE PACKAGE (sin __init__.py):")
print("  ❌ import package → package.function() NO funciona")
print("  ❌ from package import * NO útil")
print("  ✅ from package.module import function")
print("  ✅ Útil para plugins distribuidos")
print()

print("=" * 70)
print("RESUMEN: Regular Packages (con __init__.py)")
print("=" * 70)
print()
print("💡 VENTAJAS:")
print("   • API limpia y fácil de usar")
print("   • Control sobre qué se expone")
print("   • Metadata del paquete")
print("   • Mejor experiencia para usuarios")
print()
print("📚 CUÁNDO USAR:")
print("   • Librerías públicas")
print("   • Paquetes con API clara")
print("   • Cuando quieres simplificar imports")
print()
print("🎯 RECOMENDACIÓN:")
print("   Siempre usa __init__.py para tus paquetes.")
print("   Es la mejor práctica de la industria.")
print("=" * 70)
