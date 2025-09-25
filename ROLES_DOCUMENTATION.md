# 📘 Ansible Roles Documentation

## 🔧 Role: `storage`
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

## 🔧 Role: `authentication`
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

## 🔧 Role: `login`
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

## 🔧 Role: `users`
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

