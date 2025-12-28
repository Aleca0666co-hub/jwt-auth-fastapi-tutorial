
# 📘 FastAPI JWT Auth — HTTPBearer (04)

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
  - [9.📘 Technical Notes](#9-notes)
  - [10. License](#10-license)
- [Spanish Version](#versión-en-español-)

---

# Project: FastAPI JWT Auth

## 1. General Description

This example introduces **HTTPBearer authentication** using FastAPI.

Unlike the previous example (`03_manual_headers_jwt`), authentication is now declared
at the **OpenAPI security level**, allowing Swagger UI to work as a real authentication client.

This marks the transition from *manual JWT handling* to *framework-native JWT integration*.

---

## 2.🧑‍💻 What This Project Does

This API:

- Generates JWT access tokens.
- Declares authentication via `HTTPBearer`.
- Enables Swagger UI authorization support.
- Protects routes using `Depends()`.
- Validates token expiration and integrity.
- Simulates a production-style JWT flow.

---

## 3.🔑 Key Concepts

- **JWT (JSON Web Token):** Signed token containing user identity.
- **HTTPBearer:** FastAPI security scheme for Bearer tokens.
- **OpenAPI Security:** Authentication defined at documentation level.
- **Dependency Injection:** Automatic token validation using `Depends`.
- **Token Expiration:** Limits token lifetime.

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

---

### `/protected`

Protected endpoint that requires authentication.

Swagger automatically injects:

```
Authorization: Bearer <token>
```

Example response:

```json
{
  "message": "Access granted",
  "user": "user123"
}
```

---

## 8.⚠️ Security Details

* Tokens signed with HS256.
* Expiration enforced(now it's 5 minutes).
* Invalid or expired tokens rejected.
* Authorization handled automatically by Swagger.

---

## 9.📘 Notes

* No database included.
* Static demo user.
* Focused on learning HTTPBearer.
* Clean separation between token creation and validation.
* Designed to mirror real-world FastAPI auth patterns.

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
* [Versión en Inglés](#-fastapi-jwt-auth--httpbearer-04)
---

# Proyecto: FastAPI JWT Auth

## 1. Descripción General

Este ejemplo introduce **HTTPBearer** como método profesional de autenticación en FastAPI.

A diferencia del ejemplo anterior (`03_manual_headers_jwt`),
la seguridad se declara directamente en OpenAPI,
permitiendo que Swagger funcione como un cliente real de autenticación.

---

## 2.🧑‍💻 Qué hace el proyecto

La API:

* Genera tokens JWT.
* Declara autenticación mediante HTTPBearer.
* Permite que Swagger inyecte headers automáticamente.
* Protege rutas con `Depends()`.
* Valida expiración e integridad del token.
* Simula un flujo real de autenticación.

---

## 3.🔑 Conceptos clave

* **JWT:** Token firmado con identidad del usuario.
* **HTTPBearer:** Esquema de seguridad para tokens Bearer.
* **OpenAPI:** Seguridad definida a nivel documentación.
* **Inyección de dependencias:** Validación automática.
* **Expiración:** Control del tiempo de sesión.

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

---

### `/protected`

Ruta protegida que requiere autenticación.

Swagger envía automáticamente:

```
Authorization: Bearer <token>
```

---

## 8.⚠️ Detalles de seguridad

* Tokens firmados con HS256.
* Expiración activa(ahora son 5 minutos).
* Tokens inválidos son rechazados.
* Swagger automatiza autenticación.

---

## 9.📘 Notas técnicas

* Sin base de datos.
* Usuario de ejemplo.
* Diseño didáctico.
* Separación clara de responsabilidades.
* Preparado para scopes en el siguiente módulo.

---

## 10. Licencia

[Licencia MIT.](../LICENSE)
Ver archivo LICENSE en el root.

