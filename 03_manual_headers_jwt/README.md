
# 📘 README — `03_manual_headers_jwt/README.md`

## 📑 Index

* [Project: FastAPI JWT Manual Headers](#project-fastapi-jwt-manual-headers)

  * [1. General Description](#1-general-description)
  * [2.🧑‍💻 What This Project Does](#2-what-this-project-does)
  * [3.🔑 Key Concepts](#3-key-concepts)
  * [4.⚙️ Requirements](#4️-requirements)
  * [5.✅ Installation](#5-installation)
  * [6.▶️ How to Run](#6️-how-to-run)
  * [7.🔍 Important Endpoints](#7-important-endpoints)
  * [8.⚠️ Security Details](#8️-security-details)
  * [9.📘 Technical Notes](#9-notes-technical)
  * [10. License](#10-license)
* [Versión en Español](#-versión-en-español)

---

# Project: FastAPI JWT Manual Headers

## 1. General Description

This example demonstrates **JWT authentication using raw HTTP headers** in FastAPI.

The goal is to teach JWT **at the HTTP protocol level**, not through Swagger or OpenAPI automation.

This module intentionally avoids `HTTPBearer` to expose how JWT actually works under the hood.

---

## 2.🧑‍💻 What This Project Does

This example:

* Generates a JWT via `/login`
* Protects a route using **manual `Authorization` header parsing**
* Shows why Swagger UI fails in this scenario
* Demonstrates why real HTTP clients (curl, Postman) succeed
* Separates **protocol behavior** from **documentation tools**

---

## 3.🔑 Key Concepts

* **JWT:** Signed token containing user identity
* **Authorization Header:** `Authorization: Bearer <token>`
* **HTTP Protocol:** Where JWT truly operates
* **Swagger UI:** Client tool, not the protocol
* **Manual Header Parsing:** Using `Header(...)` instead of OpenAPI security

---

## 4.⚙️ Requirements

* Python 3.12+
* fastapi
* uvicorn
* python-jose

---

## 5.✅ Installation

```bash
git clone <repository_url>
cd 03_manual_headers_jwt
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

Protected route requiring **manual Authorization header**.

❌ Swagger UI → **Fails**
✅ curl / real HTTP clients → **Works**

Example:

```bash
curl -H "Authorization: Bearer YOUR_TOKEN" \
http://127.0.0.1:8000/protected
```

---

## 8.⚠️ Security Details

* HS256 token signing
* Expiration enforced
* Manual Bearer scheme validation
* Invalid or expired tokens rejected

---

## 9.📘 Technical Notes

* Swagger does NOT send headers defined with `Header(...)`
* This is **expected behavior**, not a bug
* JWT security lives at the HTTP layer
* OpenAPI security is introduced in the next example

---

## 10. License

[MIT License](../LICENSE)
See root `LICENSE` file.

---

---

# 🇪🇸 Versión en Español

## 📑 Índice

* [Proyecto: FastAPI JWT Headers Manuales](#proyecto-fastapi-jwt-headers-manuales)

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
* [English Version](#-index)
---

# Proyecto: FastAPI JWT Headers Manuales

## 1. Descripción General

Este ejemplo demuestra **autenticación JWT usando headers HTTP manuales** en FastAPI.

El objetivo es enseñar JWT **a nivel de protocolo HTTP**, no mediante automatización de Swagger.

---

## 2.🧑‍💻 Qué hace el proyecto

* Genera un JWT con `/login`
* Protege rutas leyendo el header `Authorization` manualmente
* Demuestra por qué Swagger falla
* Explica por qué curl funciona
* Separa protocolo de herramientas visuales

---

## 3.🔑 Conceptos clave

* **JWT:** Token firmado
* **Authorization:** Header `Bearer`
* **HTTP:** Capa real de seguridad
* **Swagger:** Cliente, no protocolo
* **Headers manuales:** Uso de `Header(...)`

---

## 4.⚙️ Requisitos

* Python 3.12+
* fastapi
* uvicorn
* python-jose

---

## 5.✅ Instalación

```bash
git clone <repository_url>
cd 03_manual_headers_jwt
pip install fastapi uvicorn python-jose
```

---

## 6.▶️ Cómo correr el proyecto

```bash
uvicorn app:app --reload
```

---

## 7.🔍 Endpoints importantes

### `/login`

Devuelve un token JWT.

---

### `/protected`

Ruta protegida que **requiere header manual**.

Swagger ❌
curl ✅

---

## 8.⚠️ Detalles de seguridad

* Firma HS256
* Expiración activa
* Validación manual del esquema Bearer

---

## 9.📘 Notas técnicas

* Swagger no envía headers definidos con `Header(...)`
* Es comportamiento esperado
* JWT vive en HTTP
* El siguiente módulo usa `HTTPBearer`

---

## 10. Licencia

[Licencia MIT](../LICENSE)
Ver archivo `LICENSE` en el root.

