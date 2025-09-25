import os
import yaml
import json

roles_dir = os.path.join(os.getcwd(), "roles")
manifest = []

for role_name in os.listdir(roles_dir):
    role_path = os.path.join(roles_dir, role_name)
    if not os.path.isdir(role_path):
        continue

    role_info = {
        "name": role_name,
        "description": "",
        "main_tasks": []
    }

    meta_path = os.path.join(role_path, "meta", "main.yml")
    if os.path.exists(meta_path):
        with open(meta_path, "r") as f:
            try:
                meta = yaml.safe_load(f)
                role_info["description"] = meta.get("galaxy_info", {}).get("description", "")
            except Exception:
                pass

    tasks_path = os.path.join(role_path, "tasks", "main.yml")
    if os.path.exists(tasks_path):
        with open(tasks_path, "r") as f:
            try:
                tasks = yaml.safe_load(f)
                if isinstance(tasks, list):
                    for task in tasks:
                        if "name" in task:
                            role_info["main_tasks"].append(task["name"])
            except Exception:
                pass

    manifest.append(role_info)

with open("ansible_roles_manifest.json", "w") as f:
    json.dump(manifest, f, indent=2)

print("✅ Manifest generated.")
