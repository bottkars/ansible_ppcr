import os
import yaml
import json
from glob import glob

def extract_yaml_files(directory):
    """Recursively find all YAML files in a directory."""
    return glob(os.path.join(directory, '**', '*.yml'), recursive=True) + \
           glob(os.path.join(directory, '**', '*.yaml'), recursive=True)

def extract_task_names(task_files):
    """Extract task names from a list of YAML files."""
    task_names = []
    for file_path in task_files:
        try:
            with open(file_path, 'r') as f:
                content = yaml.safe_load(f)
                if isinstance(content, list):
                    for item in content:
                        if isinstance(item, dict) and 'name' in item:
                            task_names.append(item['name'])
        except Exception:
            continue
    return task_names

def extract_variables(var_files):
    """Extract variable names from a list of YAML files."""
    variables = []
    for file_path in var_files:
        try:
            with open(file_path, 'r') as f:
                content = yaml.safe_load(f)
                if isinstance(content, dict):
                    variables.extend(content.keys())
        except Exception:
            continue
    return variables

roles_dir = os.path.join(os.getcwd(), "roles")
manifest = []

for role_name in os.listdir(roles_dir):
    role_path = os.path.join(roles_dir, role_name)
    if not os.path.isdir(role_path):
        continue

    role_info = {
        "name": role_name,
        "description": "",
        "tasks": [],
        "defaults": [],
        "vars": []
    }

    # Extract description from meta/main.yml
    meta_path = os.path.join(role_path, "meta", "main.yml")
    if os.path.exists(meta_path):
        try:
            with open(meta_path, "r") as f:
                meta = yaml.safe_load(f)
                role_info["description"] = meta.get("galaxy_info", {}).get("description", "")
        except Exception:
            pass

    # Extract task names
    tasks_dir = os.path.join(role_path, "tasks")
    if os.path.exists(tasks_dir):
        task_files = extract_yaml_files(tasks_dir)
        role_info["tasks"] = extract_task_names(task_files)

    # Extract default variables
    defaults_dir = os.path.join(role_path, "defaults")
    if os.path.exists(defaults_dir):
        default_files = extract_yaml_files(defaults_dir)
        role_info["defaults"] = extract_variables(default_files)

    # Extract vars
    vars_dir = os.path.join(role_path, "vars")
    if os.path.exists(vars_dir):
        var_files = extract_yaml_files(vars_dir)
        role_info["vars"] = extract_variables(var_files)

    manifest.append(role_info)

# Save the manifest to a JSON file
with open("ansible_roles_manifest.json", "w") as f:
    json.dump(manifest, f, indent=2)

print("✅ Manifest generated and saved to ansible_roles_manifest.json")
