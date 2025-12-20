
# FastAPI JWT Login Example (Bilingual)

## 📑 Index 
  - [1. General Description](#1-general-description)
  - [2.🧑‍💻 What This Project Does](#2-what-this-project-does)
  - [3.🔑 Key Concepts](#3-key-concepts)
  - [4.⚙️ Requirements](#4️-requirements)
  - [5.✅ Installation](#5-installation)
  - [6.▶️ How to Run](#6️-how-to-run)
  - [7.🔍 Important Endpoints](#7-important-endpoints)
    - [`/login`](#login)
    - [`/`](#)
  - [8.⚠️ Security Details](#8️-security-details)
  - [9.📘 Technical Notes](#9-technical-notes)
  - [10. License](#10-license)
  ### [Versión en Español 🇪🇸](#versión-en-español-)
  
---

### English Version 🇬🇧

## 1. General Description

This project demonstrates a minimal authentication system using **FastAPI** and **JSON Web Tokens (JWT)**.
It focuses on generating JWT tokens via a login endpoint and providing automatic documentation with Swagger UI and Redoc.
The project is **educational and portfolio-oriented**.

---

## 2.🧑‍💻 What This Project Does

* Provides a `/login` endpoint that returns a signed JWT.
* Implements HS256 token signing.
* Enforces token expiration (10 minutes).
* Exposes interactive API docs (`/docs`, `/redoc`).
* Serves as a base for further authentication flows.

---

## 3.🔑 Key Concepts

* **JWT (JSON Web Token):** Compact way to securely transmit user identity and claims.
* **HS256:** Symmetric algorithm for signing and verifying tokens.
* **Claims:** `sub` (user ID), `exp` (expiration time).
* **Bearer Token Format:** Introduced in next examples.
* **FastAPI Routing:** Endpoints defined using Python functions and decorators (`@app.get`).

---

## 4.⚙️ Requirements

* Python 3.12+
* fastapi
* uvicorn
* python-jose

---

## 5.✅ Installation

1. Clone the repository:

```bash
git clone <repository_url>
cd <project_folder>
```

2. Install dependencies:

```bash
pip install fastapi uvicorn python-jose
```

---

## 6.▶️ How to Run

```bash
uvicorn app:app --reload
```

Open in browser:

```
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc
```

---

## 7.🔍 Important Endpoints

### `/login`

Returns a JWT token:

```json
{
  "access_token": "<JWT>",
  "token_type": "bearer"
}
```

### `/`

Returns welcome message and documentation links:

```json
{
  "message": "Welcome to the JWT demo. Use /login to get a token.",
  "docs": "/docs",
  "redoc": "/redoc"
}
```

---

## 8.⚠️ Security Details

* Tokens signed using HS256.
* Secret key required for decoding.
* Expiration enforced (10 minutes).
* Tampered tokens are rejected.

---

## 9.📘 Technical Notes

* No database included.
* Static demo user.
* Timezone-aware datetimes.
* Clean minimal educational design.

---

## 10. License

[MIT LICENSE](../LICENSE).
See LICENSE file in root.

---

### Versión en Español 🇪🇸

---
## 📑Índice
- [1. Descripción General](#1-descripción-general)
  - [2.🧑‍💻 Qué hace el proyecto](#2-qué-hace-el-proyecto)
  - [3.🔑 Conceptos clave](#3-conceptos-clave)
  - [4.⚙️ Requisitos](#4️-requisitos)
  - [5.✅ Instalación](#5-instalación)
  - [6.▶️ Cómo correr el proyecto](#6️-cómo-correr-el-proyecto)
  - [7.🔍 Endpoints importantes](#7-endpoints-importantes)
    - [`/login`](#login-1)
    - [`/`](#-1)
  - [8.⚠️ Detalles de seguridad](#8️-detalles-de-seguridad)
  - [9.📘 Notas técnicas](#9-notas-técnicas)
  - [10. Licencia](#10-licencia)

  #### [English Version 🇬🇧](#english-version-)
 
---

## 1. Descripción General

Este proyecto muestra un sistema mínimo de autenticación usando **FastAPI** y **JWT (JSON Web Tokens)**.
Se centra en generar tokens JWT mediante un endpoint de login y exponer documentación automática con Swagger UI y Redoc.
Es un proyecto **educativo y orientado a portafolio**.

---

## 2.🧑‍💻 Qué hace el proyecto

* Proporciona un endpoint `/login` que devuelve un JWT firmado.
* Implementa firma de tokens con HS256.
* Controla expiración de tokens (10 minutos).
* Expone documentación interactiva (`/docs`, `/redoc`).
* Sirve como base para flujos de autenticación futuros.

---

## 3.🔑 Conceptos clave

* **JWT (JSON Web Token):** Forma compacta de transmitir identidad y claims de forma segura.
* **HS256:** Algoritmo simétrico para firmar y validar tokens.
* **Claims:** `sub` (ID de usuario), `exp` (fecha de expiración).
* **Formato Bearer:** Formato Bearer (utilizado en los siguientes ejemplos)
* **Rutas FastAPI:** Endpoints definidos con funciones Python y decoradores (`@app.get`).

---

## 4.⚙️ Requisitos

* Python 3.12+
* fastapi
* uvicorn
* python-jose

---

## 5.✅ Instalación

1. Clonar el repositorio:

```bash
git clone <repository_url>
cd <project_folder>
```

2. Instalar dependencias:

```bash
pip install fastapi uvicorn python-jose
```

---

## 6.▶️ Cómo correr el proyecto

```bash
uvicorn app:app --reload
```

Abrir en el navegador:

```
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc
```

---

## 7.🔍 Endpoints importantes

### `/login`

Devuelve un token JWT:

```json
{
  "access_token": "<JWT>",
  "token_type": "bearer"
}
```

### `/`

Devuelve mensaje de bienvenida y links de documentación:

```json
{
  "message": "Bienvenido al demo de JWT. Usa /login para obtener un token.",
  "docs": "/docs",
  "redoc": "/redoc"
}
```

---

## 8.⚠️ Detalles de seguridad

* Tokens firmados con HS256.
* Clave secreta requerida para decodificar.
* Expiración activa (10 minutos).
* Tokens manipulados son rechazados.

---

## 9.📘 Notas técnicas

* Sin base de datos.
* Usuario de ejemplo estático.
* Datetimes con zona horaria.
* Diseño educativo, limpio y minimalista.

---

## 10. Licencia

[Licencia MIT](../LICENSE).
Ver archivo LICENSE en el root.

