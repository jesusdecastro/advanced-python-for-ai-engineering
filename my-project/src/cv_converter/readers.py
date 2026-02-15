import json
from pathlib import Path
from typing import Dict, Any

class JSONReader:
    """
    Clase encargada de leer archivos JSON del disco y devolver diccionarios.
    Aplica programación defensiva manejando errores de lectura.
    """
    
    def read(self, file_path: str) -> Dict[str, Any]:
        path = Path(file_path)
        
        # Validación de existencia
        if not path.exists():
            raise FileNotFoundError(f"Error: No encuentro el archivo '{file_path}'")
            
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            raise ValueError(f"Error: El archivo '{file_path}' no es un JSON válido.")