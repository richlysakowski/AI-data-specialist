import ast
import os
import sys

def get_imports(source_code):
    tree = ast.parse(source_code)
    import_nodes = [node for node in ast.walk(tree) if isinstance(node, ast.Import)]
    import_from_nodes = [node for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)]
    return ([node.names[0].name for node in import_nodes], [node.module for node in import_from_nodes])

def get_all_imports_in_folder(folder_path):
    import_set = set()
    import_from_set = set()
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.py'):
                with open(os.path.join(root, file), 'r') as f:
                    source_code = f.read()
                imports, import_froms = get_imports(source_code)
                import_set.update(imports)
                import_from_set.update(import_froms)
    return import_set, import_from_set

# Example usage:
if len(sys.argv) != 2:
  print("Please provide the folder path as a command line argument.")
  sys.exit(1)

folder_path = sys.argv[1]
import_set, import_from_set = get_all_imports_in_folder(folder_path)
import_from_set_without_dot = [s for s in import_from_set if '.' not in s]
print("Import from -from-",import_from_set_without_dot)
print("Imports:", import_set)
print("Import Froms:", import_from_set)

conda_config = """
channels:
  - conda-forge
  - defaults

dependencies:
  - python

  # Packages from import_set
  - {import_set_packages}

  # Packages from import_from_set_without_dot
  - {import_from_set_packages}
"""

import_set_packages = "\n  - ".join(import_set)
import_from_set_packages = "\n  - ".join(import_from_set_without_dot)

conda_config = conda_config.format(import_set_packages=import_set_packages, import_from_set_packages=import_from_set_packages)

folder_name = os.path.basename(folder_path)
conda_config = "name: " + folder_name + "\n" + conda_config

with open("conda_config.yaml", "w") as f:
  f.write(conda_config)

# if there are packages no avialables, look at anaconda.org
# identify which packges should install via pip
# os module is a default module in python, so dont need to be installed
# what others are default modules in python ?