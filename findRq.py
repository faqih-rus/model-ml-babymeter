import os
import re

def find_imports_in_file(file_path):
    imports = set()
    with open(file_path, 'r') as file:
        for line in file:
            match = re.match(r'^\s*(import|from)\s+(\S+)', line)
            if match:
                imports.add(match.group(2).split('.')[0])
    return imports

def find_imports_in_project(directory):
    all_imports = set()
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                imports = find_imports_in_file(file_path)
                all_imports.update(imports)
    return all_imports

project_directory = 'C:\Users\62818\Downloads\BabyMeter'
imports = find_imports_in_project(project_directory)

with open('requirements.txt', 'w') as f:
    for imp in sorted(imports):
        f.write(f"{imp}\n")

print(f"Libraries have been written to requirements.txt")

