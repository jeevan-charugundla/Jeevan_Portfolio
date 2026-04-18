import os
import base64
import json

base_dir = r'c:\Users\jeeva\G1portfolio\NeoBrutalist'
ignore_dirs = {'.git', '.kilo', '.playwright-mcp'}

code_upserts = []
assets_upserts = []

for root, dirs, files in os.walk(base_dir):
    dirs[:] = [d for d in dirs if d not in ignore_dirs]
    for file in files:
        full_path = os.path.join(root, file)
        rel_path = os.path.relpath(full_path, base_dir).replace('\\', '/')
        if rel_path.startswith('scratch/'): continue # Skip scratch files
        
        is_asset = any(rel_path.lower().endswith(ext) for ext in 
                        ['.png', '.jpg', '.jpeg', '.gif', '.pdf', '.ico', '.svg']) or 'Assets/' in rel_path
        
        try:
            if is_asset:
                encoding = 'base64'
                with open(full_path, 'rb') as f:
                    content = base64.b64encode(f.read()).decode('utf-8')
                assets_upserts.append({"path": rel_path, "content": content, "encoding": encoding})
            else:
                encoding = 'utf-8'
                with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                code_upserts.append({"path": rel_path, "content": content, "encoding": encoding})
        except Exception as e:
            print(f"Error reading {rel_path}: {e}")

with open('code_payload.json', 'w', encoding='utf-8') as f:
    json.dump(code_upserts, f)
with open('assets_payload.json', 'w', encoding='utf-8') as f:
    json.dump(assets_upserts, f)

print(f"Prepared {len(code_upserts)} code files and {len(assets_upserts)} assets.")
