def main():
    print("Hello from my-project!")


if __name__ == "__main__":
    main()

import sys
import os

print("--------------------------------------------------")
print("✅ ¡ÉXITO! Tu entorno está funcionando.")
print(f"📂 Estás ejecutando el archivo: {os.path.basename(__file__)}")
print(f"🐍 Python está corriendo desde: {sys.executable}")
print("--------------------------------------------------")