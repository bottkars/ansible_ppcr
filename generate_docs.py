import os
import json
import yaml
from datetime import datetime

def extract_description(role_path):
    meta_path = os.path.join(role_path, "meta", "main.yml")
    readme_path = os.path.join(role_path, "README.md")
    if os.path.exists(meta_path):
        with open(meta_path, "r") as f:
            try:
                meta = yaml.safe_load(f)
                return meta.get("galaxy_info", {}).get("description", "").strip()
            except Exception:
                return ""
    elif os.path.exists(readme_path):
        with open(readme_path, "r") as f:
            for line in f:
                if line.strip():
                    return line.strip()
    return ""

def extract_tasks(role_path):
    tasks_dir = os.path.join(role_path, "tasks")
    task_names = []
    if os.path.isdir(tasks_dir):
        for file in os.listdir(tasks_dir):
            if file.endswith(".yml") or file.endswith(".yaml"):
                with open(os.path.join(tasks_dir, file), "r") as f:
                    try:
                        content = yaml.safe_load(f)
                        if isinstance(content, list):
                            for item in content:
                                if isinstance(item, dict) and "name" in item:
                                    task_names.append(item["name"])
                    except Exception:
                        continue
    return task_names

def extract_vars(file_path):
    variables = []
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            try:
                content = yaml.safe_load(f)
                if isinstance(content, dict):
                    variables.extend(content.keys())
            except Exception:
                pass
    return variables

roles_manifest = []
readme_lines = [
    "# 🛠️ Ansible Roles Collection\n",
    "This repository contains a collection of Ansible roles for managing Cyber Recovery environments.\n",
    "## 📦 Roles Included\n"
]
galaxy_lines = [
    "# 🌌 Ansible Galaxy Role Documentation Template\n",
    "This template provides metadata and documentation structure for publishing roles to Ansible Galaxy.\n",
    "---\n"
]

roles_dir = "roles"
if os.path.isdir(roles_dir):
    for role_name in os.listdir(roles_dir):
        role_path = os.path.join(roles_dir, role_name)
        if os.path.isdir(role_path):
            description = extract_description(role_path) or "_No description provided_"
            tasks = extract_tasks(role_path)
            defaults = extract_vars(os.path.join(role_path, "defaults", "main.yml"))
            vars_ = extract_vars(os.path.join(role_path, "vars", "main.yml"))

            # Update manifest
            roles_manifest.append({
                "name": role_name,
                "description": description,
                "tasks": tasks,
                "defaults": defaults,
                "vars": vars_
            })

            # Update README
            readme_lines.append(f"- `{role_name}`: {description}\n")

            # Update Galaxy documentation
            galaxy_lines.append(f"\n### 🔧 Role: `{role_name}`\n")
            galaxy_lines.append(f"- **Description**: {description}\n")
            galaxy_lines.append("- **Tasks**:\n")
            for task in tasks:
                galaxy_lines.append(f"  - {task}\n")
            galaxy_lines.append("- **Defaults**:\n")
            for default in defaults:
                galaxy_lines.append(f"  - `{default}`\n")
            galaxy_lines.append("- **Variables**:\n")
            for var in vars_:
                galaxy_lines.append(f"  - `{var}`\n")
            galaxy_lines.append("\n---\n")

readme_lines.extend([
    "\n## 📄 Documentation\n",
    "Detailed documentation for each role is available in [GALAXY_DOCUMENTATION_TEMPLATE.md](GALAXY_DOCUMENTATION_TEMPLATE.md).\n",
    "\n## 📜 License\n",
    "This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.\n"
])

galaxy_lines.extend([
    "\n## 📦 Galaxy Metadata Tips\n",
    "To publish to Galaxy, ensure each role includes:\n",
    "- `meta/main.yml` with author, license, platforms, and dependencies\n",
    "- `README.md` with usage examples\n",
    "- `defaults/main.yml` and `vars/main.yml` for configuration\n",
    "- `tasks/main.yml` with role logic\n"
])

# Write README.md
with open("README.md", "w") as f:
    f.writelines(readme_lines)

# Write LICENSE
mit_license = f"""MIT License

Copyright (c) {datetime.now().year}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
with open("LICENSE", "w") as f:
    f.write(mit_license)

# Write GALAXY_DOCUMENTATION_TEMPLATE.md
with open("GALAXY_DOCUMENTATION_TEMPLATE.md", "w") as f:
    f.writelines(galaxy_lines)

# Write ansible_roles_manifest.json
with open("ansible_roles_manifest.json", "w") as f:
    json.dump(roles_manifest, f, indent=2)

