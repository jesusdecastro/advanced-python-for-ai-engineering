#!/usr/bin/env python3
"""Manual fix for problematic notebooks."""
import json
import re
from pathlib import Path

def manual_fix_notebook(path):
    """Manually fix common JSON issues in notebooks."""
    print(f"\n🔧 Fixing {path.name}...")
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix 1: Remove trailing commas before closing brackets/braces
        content = re.sub(r',(\s*\])', r'\1', content)
        content = re.sub(r',(\s*})', r'\1', content)
        
        # Fix 2: Fix cell array structure - cells should be in array
        # Pattern: ] , { should be ] } , {
        content = re.sub(r'\]\s*,\s*\{', r']},{', content)
        
        # Fix 3: Ensure proper cell structure
        # Each cell should end with } not },
        content = re.sub(r'}\s*}\s*,', r'}},', content)
        
        # Fix 4: Fix metadata structure
        content = re.sub(r'}\s*},\s*\{', r'}},{', content)
        
        # Try to parse
        try:
            nb = json.loads(content)
        except json.JSONDecodeError as e:
            print(f"   ❌ Still has error at line {e.lineno}: {e.msg}")
            
            # More aggressive fix - try to rebuild structure
            # Find all cells
            cells_match = re.search(r'"cells":\s*\[(.*?)\]\s*,?\s*"metadata"', content, re.DOTALL)
            if cells_match:
                cells_content = cells_match.group(1)
                # Ensure cells are properly separated
                cells_content = re.sub(r'}\s*\{', r'},{', cells_content)
                content = content[:cells_match.start(1)] + cells_content + content[cells_match.end(1):]
                
                try:
                    nb = json.loads(content)
                except:
                    print(f"   ❌ Could not fix automatically")
                    return False
        
        # Clear outputs
        for cell in nb.get('cells', []):
            if cell.get('cell_type') == 'code':
                cell['outputs'] = []
                cell['execution_count'] = None
        
        # Write back
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
        
        print(f"   ✅ Fixed successfully")
        return True
        
    except Exception as e:
        print(f"   ❌ Error: {str(e)[:100]}")
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
    
    print("🔧 Manual repair of remaining notebooks...")
    
    fixed = 0
    for nb_path in notebooks:
        path = Path(nb_path)
        if path.exists():
            if manual_fix_notebook(path):
                fixed += 1
    
    print(f"\n📊 Result: {fixed}/{len(notebooks)} fixed")
    
    if fixed < len(notebooks):
        print("\n⚠️  Some notebooks still need Jupyter repair")

if __name__ == '__main__':
    main()
