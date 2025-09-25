# 🌌 Ansible Galaxy Role Documentation Template
This template provides metadata and documentation structure for publishing roles to Ansible Galaxy.
---

### 🔧 Role: `storage`
- **Description**: _No description provided_
- **Tasks**:
  - Get all storage endpoints
  - Get all storage endpoints
  - Get all storage endpoints mtrees
  - Create a new storage endpoint
- **Defaults**:
  - `api_base_url`
  - `validate_certs`
- **Variables**:
  - `auth_token`
  - `new_storage`
  - `apiver`

---

### 🔧 Role: `authentication`
- **Description**: _No description provided_
- **Tasks**:
  - Login to Cyber Recovery
  - Logout user
- **Defaults**:
  - `api_base_url`
- **Variables**:
  - `login_payload`
  - `user_id`
  - `refresh_token`
  - `apiver`

---

### 🔧 Role: `login`
- **Description**: _No description provided_
- **Tasks**:
  - Login to Cyber Recovery and get token
  - Show access token
- **Defaults**:
  - `api_base_url`
  - `validate_certs`
- **Variables**:
  - `login_payload`
  - `apiver`

---

### 🔧 Role: `users`
- **Description**: _No description provided_
- **Tasks**:
  - Get all users
  - Create a new user
- **Defaults**:
  - `api_base_url`
- **Variables**:
  - `auth_token`
  - `new_user`

---

## 📦 Galaxy Metadata Tips
To publish to Galaxy, ensure each role includes:
- `meta/main.yml` with author, license, platforms, and dependencies
- `README.md` with usage examples
- `defaults/main.yml` and `vars/main.yml` for configuration
- `tasks/main.yml` with role logic
