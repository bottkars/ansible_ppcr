import json
from datetime import datetime

# Load the roles manifest from the JSON file
with open("ansible_roles_manifest.json", "r") as f:
    roles_data = json.load(f)

# Generate README.md
readme_lines = [
    "# 🛠️ Ansible Roles Collection\n",
    "This repository contains a collection of Ansible roles for managing Cyber Recovery environments.\n",
    "## 📦 Roles Included\n"
]

for role in roles_data:
    name = role.get("name", "Unnamed Role")
    description = role.get("description", "").strip() or "_No description provided_"
    readme_lines.append(f"- `{name}`: {description}\n")

readme_lines.extend([
    "\n## 📄 Documentation\n",
    "Detailed documentation for each role is available in[GALAXY_DOCUMENTATION_TEMPLATE.md.\n",
    "\n## 📜 License\n",
    "This project islicensed under the MIT License - see the [LICENSE file for details.\n"
])

with open("README.md", "w") as f:
    f.writelines(readme_lines)

# Generate LICENSE (MIT)
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

# Generate GALAXY_DOCUMENTATION_TEMPLATE.md
galaxy_lines = [
    "# 🌌 Ansible Galaxy Role Documentation Template\n",
    "This template provides metadata and documentation structure for publishing roles to Ansible Galaxy.\n",
    "---\n"
]

for role in roles_data:
    name = role.get("name", "Unnamed Role")
    description = role.get("description", "").strip() or "_No description provided_"
    tasks = role.get("tasks", [])
    defaults = role.get("defaults", [])
    vars_ = role.get("vars", [])

    galaxy_lines.append(f"\n### 🔧 Role: `{name}`\n")
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

galaxy_lines.extend([
    "\n## 📦 Galaxy Metadata Tips\n",
    "To publish to Galaxy, ensure each role includes:\n",
    "- `meta/main.yml` with author, license, platforms, and dependencies\n",
    "- `README.md` with usage examples\n",
    "- `defaults/main.yml` and `vars/main.yml` for configuration\n",
    "- `tasks/main.yml` with role logic\n"
])

with open("GALAXY_DOCUMENTATION_TEMPLATE.md", "w") as f:
    f.writelines(galaxy_lines)
