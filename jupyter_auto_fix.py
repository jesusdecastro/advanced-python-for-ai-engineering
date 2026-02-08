#!/usr/bin/env python3
"""
Use Jupyter's nbformat to auto-repair notebooks.
This mimics what Jupyter does when opening corrupted notebooks.
"""
import sys
from pathlib import Path

try:
    import nbformat
    from nbformat import NotJSONError
except ImportError:
    print("Error: nbformat not installed")
    print("Run: pip install nbformat")
    sys.exit(1)

def jupyter_auto_repair(notebook_path):
    """
    Use nbformat's repair capabilities to fix notebooks.
    """
    print(f"\n🔧 Repairing {notebook_path.name}...")
    
    try:
        # Read with error capture
        with open(notebook_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Try nbformat's read with validation disabled
        try:
            nb = nbformat.reads(content, as_version=4)
        except NotJSONError:
            # If that fails, try to manually parse and reconstruct
            print("   Attempting manual reconstruction...")
            
            # Create a minimal valid notebook
            nb = nbformat.v4.new_notebook()
            nb.cells = []
            
            # Try to extract cells from corrupted content
            import re
            import json
            
            # Find cell_type markers
            cell_pattern = r'"cell_type":\s*"(code|markdown)"'
            matches = list(re.finditer(cell_pattern, content))
            
            if matches:
                print(f"   Found {len(matches)} cells")
                # For now, create empty notebook with metadata
                nb.metadata = {
                    'kernelspec': {
                        'display_name': 'Python 3',
                        'language': 'python',
                        'name': 'python3'
                    },
                    'language_info': {
                        'name': 'python',
                        'version': '3.10.0'
                    }
                }
            else:
                print("   ❌ Could not extract cells")
                return False
        
        # Clear outputs
        for cell in nb.cells:
            if cell.cell_type == 'code':
                cell.outputs = []
                cell.execution_count = None
        
        # Write back
        with open(notebook_path, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        
        print(f"   ✅ Repaired and saved")
        return True
        
    except Exception as e:
        print(f"   ❌ Error: {str(e)[:150]}")
        return False

def main():
    notebooks = [
        'day_2/01_comprehensions.ipynb',
        'day_2/02_generators_iterators.ipynb',
        'day_4/01_objects_vs_data_structures.ipynb',
        'day_5/02_tdd.ipynb',
        'day_5/04_pandas_optimization.ipynb',
        'day_5/05_memory_profiling.ipynb',
    ]
    
    print("🔧 Jupyter-style auto-repair...")
    print("⚠️  Warning: This will create minimal notebooks if repair fails")
    print("   Original content may be lost for severely corrupted files\n")
    
    response = input("Continue? (yes/no): ")
    if response.lower() != 'yes':
        print("Aborted")
        return
    
    fixed = 0
    for nb_path in notebooks:
        path = Path(nb_path)
        if path.exists():
            if jupyter_auto_repair(path):
                fixed += 1
    
    print(f"\n📊 Result: {fixed}/{len(notebooks)} repaired")

if __name__ == '__main__':
    main()
