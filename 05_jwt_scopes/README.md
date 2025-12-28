
# 📘 FastAPI JWT Auth — Scopes Authorization (05)

---

## 📑 Index

- [Project: FastAPI JWT Auth](#project-fastapi-jwt-auth)
  - [1. General Description](#1-general-description)
  - [2.🧑‍💻 What This Project Does](#2-what-this-project-does)
  - [3.🔑 Key Concepts](#3-key-concepts)
  - [4.⚙️ Requirements](#4️-requirements)
  - [5.✅ Installation](#5-installation)
  - [6.▶️ How to Run](#6️-how-to-run)
  - [7.🔍 Important Endpoints](#7-important-endpoints)
  - [8.⚠️ Security Details](#8️-security-details)
  - [9.📘 Technical Notes](#9-technical-notes)
  - [10. License](#10-license)
- [Spanish version](#-índice)

---

# Project: FastAPI JWT Auth

## 1. General Description

This example demonstrates **permission-based authorization**
using **JWT scopes** in FastAPI.

Each issued token includes a list of permissions (scopes) that define
which endpoints the user is allowed to access.
Authorization is enforced at **route level** using dependency injection.

This example introduces **fine-grained access control**.

---

## 2.🧑‍💻 What This Project Does

This API:

- Issues JWT tokens with embedded scopes.
- Differentiates users by permission level.
- Protects routes based on required scopes.
- Uses HTTPBearer as OpenAPI security scheme.
- Validates permissions dynamically.
- Demonstrates real-world authorization patterns.

---

## 3.🔑 Key Concepts

- **JWT (JSON Web Token):** Signed token containing identity and permissions.
- **Scopes:** Explicit list of permissions inside the token.
- **HTTPBearer:** Declares Bearer authentication in OpenAPI.
- **Dependency Injection:** Enforces authorization per route.
- **Authorization Header:** Transports the JWT token.

---

## 4.⚙️ Requirements

- Python 3.12+
- fastapi
- uvicorn
- python-jose

---

## 5.✅ Installation

```bash
pip install fastapi uvicorn python-jose
```

---

## 6.▶️ How to Run

```bash
uvicorn app:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

Swagger UI works as a real authentication client.

---

## 7.🔍 Important Endpoints

| Endpoint        | Description                         |
| --------------- | ----------------------------------- |
| `/login_read`   | Token with `read` scope             |
| `/login_admin`  | Token with `read`, `write`, `admin` |
| `GET /data`     | Requires `read`                     |
| `POST /data`    | Requires `write`                    |
| `DELETE /users` | Requires `admin`                    |

---

## 8.⚠️ Security Details

* JWT signature verification.
* Scope-based authorization.
* Token expiration enforced.
* Stateless authorization model.
* Route-level permission checks.

---

## 9.📘 Technical Notes

* No database used.
* Static demo users.
* Scopes stored inside token payload.
* Authorization logic isolated via dependencies.
* Easily extensible for real systems.

---

## 10. License

[MIT License.](../LICENSE)
See root LICENSE file.

---

# Versión en Español 🇪🇸

---

## 📑 Índice

* [Proyecto: FastAPI JWT Auth](#proyecto-fastapi-jwt-auth)

  * [1. Descripción General](#1-descripción-general)
  * [2.🧑‍💻 Qué hace el proyecto](#2-qué-hace-el-proyecto)
  * [3.🔑 Conceptos clave](#3-conceptos-clave)
  * [4.⚙️ Requisitos](#4️-requisitos)
  * [5.✅ Instalación](#5-instalación)
  * [6.▶️ Cómo correr el proyecto](#6️-cómo-correr-el-proyecto)
  * [7.🔍 Endpoints importantes](#7-endpoints-importantes)
  * [8.⚠️ Detalles de seguridad](#8️-detalles-de-seguridad)
  * [9.📘 Notas técnicas](#9-notas-técnicas)
  * [10. Licencia](#10-licencia)
* [Versión en inglés](#-fastapi-jwt-auth--scopes-authorization-05)
---

# Proyecto: FastAPI JWT Auth

## 1. Descripción General

Este ejemplo implementa **autorización basada en permisos**
utilizando **JWT con scopes** en FastAPI.

Cada token contiene una lista explícita de permisos
que determinan a qué rutas puede acceder cada usuario.
La autorización se aplica directamente en cada endpoint.

---

## 2.🧑‍💻 Qué hace el proyecto

La API:

* Genera tokens JWT con permisos.
* Diferencia usuarios por nivel de acceso.
* Protege rutas según scopes requeridos.
* Integra seguridad mediante HTTPBearer.
* Valida permisos en tiempo de ejecución.
* Simula patrones reales de autorización.

---

## 3.🔑 Conceptos clave

* **JWT:** Token firmado con identidad y permisos.
* **Scopes:** Lista de permisos dentro del token.
* **HTTPBearer:** Seguridad declarada en OpenAPI.
* **Depends:** Inyección de dependencias para autorización.
* **Authorization Header:** Transporte del token JWT.

---

## 4.⚙️ Requisitos

* Python 3.12+
* fastapi
* uvicorn
* python-jose

---

## 5.✅ Instalación

```bash
pip install fastapi uvicorn python-jose
```

---

## 6.▶️ Cómo correr el proyecto

```bash
uvicorn app:app --reload
```

Abrir:

```
http://127.0.0.1:8000/docs
```

Swagger permite autenticación interactiva.

---

## 7.🔍 Endpoints importantes

| Ruta            | Descripción      |
| --------------- | ---------------- |
| `/login_read`   | Permiso `read`   |
| `/login_admin`  | Acceso completo  |
| `GET /data`     | Requiere `read`  |
| `POST /data`    | Requiere `write` |
| `DELETE /users` | Requiere `admin` |

---

## 8.⚠️ Detalles de seguridad

* Verificación de firma JWT.
* Control de permisos por scope.
* Expiración activa.
* Autorización sin estado.
* Protección por endpoint.

---

## 9.📘 Notas técnicas

* Sin base de datos.
* Usuarios de ejemplo.
* Scopes embebidos en el token.
* Autorización desacoplada del endpoint.
* Preparado para refresh tokens.

---

## 10. Licencia

[Licencia MIT.](../LICENSE)
Ver archivo LICENSE en la raíz.

