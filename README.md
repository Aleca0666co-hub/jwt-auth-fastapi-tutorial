
# 📚 JWT Learning Repository (Python & FastAPI)

---
## English Version 🇬🇧
---

  ## 📑 Index 
- [📚 JWT Learning Repository (Python \& FastAPI)](#-jwt-learning-repository-python--fastapi)
  - [🎯 Purpose of This Repository](#-purpose-of-this-repository)
  - [🧠 Learning Philosophy](#-learning-philosophy)
  - [📂 Repository Structure](#-repository-structure)
  - [📘 Folder Overview](#-folder-overview)
  - [⚠️ Important Notes](#️-important-notes)
  - [🧪 How to Run Examples](#-how-to-run-examples)
  - [📜 License](#-license)
    
    - [Versión en Español 🇪🇸](#versión-en-español-)


## 🎯 Purpose of This Repository

This repository is **purely educational**.

Its goal is to **teach JSON Web Tokens (JWT) step by step**, starting from the **most basic concepts** (manual token creation) and progressively moving toward **real-world authentication flows** using **FastAPI**, including:

* Access tokens
* Refresh tokens
* Token rotation
* HTTP Bearer authentication
* Scopes and authorization

Each example is **isolated, simple, and focused on a specific topic**, so learners can understand JWT **without magic or hidden abstractions**.

This is **not a production-ready project**, but a **learning path**.

---

## 🧠 Learning Philosophy

* One concept at a time
* No premature abstractions
* No frameworks hiding JWT internals
* Each folder = one complete lesson
* Each example can be run and understood independently

You should be able to:

* Read the README of a folder
* Run `app.py`
* Understand **what problem is being solved and why**

---

## 📂 Repository Structure

Each folder represents **one learning step**.
Every folder contains:

* `app.py` → runnable example
* `README.md` → explanation of concepts used

```
.
├── 01_jwt_hs256_example/
│   ├── app.py
│   └── README.md
│
├── 02_login_jwt_fastapi/
│   ├── app.py
│   └── README.md
│
├── 03_manual_headers_jwt/
│   ├── app.py
│   └── README.md
│
├── 04_httpbearer_jwt/
│   ├── app.py
│   └── README.md
│
├── 05_jwt_scopes/
│   ├── app.py
│   └── README.md
│
├── 06_jwt_access_and_refresh/
│   ├── app.py
│   └── README.md
│
├── 07_jwt_all_included/
│   ├──docs/
│   │   ├──images/
│   │   │   └──swagger.png
│   │   └──auth-flow.md
│   ├──.env                   -> just as an example
│   ├──auth.py 
│   ├──fake_db.py
│   ├──main.py
│   └── README.md
│
├── 08_bonus/
│   ├── app.py
│   └── README.md
│
├── .gitignore
├── LICENSE
└── README.md
```

---

## 📘 Folder Overview

### 🔹 01_jwt_hs256_example

Basic JWT creation and validation using **HS256**.
Focuses on:

* Token structure
* Claims
* Expiration
* Signature validation

---

### 🔹 02_login_jwt_fastapi

Simple login flow using **FastAPI**.
Focuses on:

* Login endpoint
* Token generation

---

### 🔹 03_manual_headers_jwt

JWT sent manually via HTTP headers.
Focuses on:

* Authorization headers
* Manual token extraction
* Understanding what frameworks usually automate

---

### 🔹 04_httpbearer_jwt

JWT authentication using **HTTPBearer**.
Focuses on:

* FastAPI security utilities
* Bearer token standards
* Cleaner authentication handling

---

### 🔹 05_jwt_scopes

Authorization using **JWT scopes**.
Focuses on:

* Scopes inside JWT
* Role-based / permission-based access
* Protected routes with scope validation

---

### 🔹 06_jwt_access_and_refresh

Access & Refresh token flow.
Focuses on:

* Short-lived access tokens
* Long-lived refresh tokens
* Refresh endpoint logic
* Token rotation basics

---

### 🔹 07_jwt_all_included

Complete JWT authentication system.
Focuses on:

* Login
* Access tokens
* Refresh tokens
* Rotation
* HTTPBearer
* Scopes
* Protected routes

This folder ties everything together.

---

### 🔹 08_bonus

Extra concepts and experiments.
May include:

* Security edge cases
* Common JWT mistakes
* Token invalidation strategies
* Advanced patterns

---

## ⚠️ Important Notes

* Secrets are **hardcoded for learning purposes only**
* No database is used unless explicitly stated
* This repo favors **clarity over completeness**
* Do **not** use this code directly in production

---

## 🧪 How to Run Examples

Each folder is independent.

```bash
cd 01_jwt_hs256_example
python app.py
```

Or for FastAPI examples:

```bash
uvicorn app:app --reload
```

(Check each folder README for details.)

---

## 📜 License

This project is licensed under the **MIT License**.
See the `LICENSE` file for details.


---

---

# 📚 Repositorio de Aprendizaje JWT (Python & FastAPI)

---

## Versión en Español 🇪🇸

---

## 📑  Índice 
- [📚 Repositorio de Aprendizaje JWT (Python \& FastAPI)](#-repositorio-de-aprendizaje-jwt-python--fastapi)

  - [🎯 Propósito de este Repositorio](#-propósito-de-este-repositorio)
  - [🧠 Filosofía de Aprendizaje](#-filosofía-de-aprendizaje)
  - [📂 Estructura del Repositorio](#-estructura-del-repositorio)
  - [📘 Descripción de las Carpetas](#-descripción-de-las-carpetas)
  - [⚠️ Notas Importantes](#️-notas-importantes)
  - [🧪 Cómo Ejecutar los Ejemplos](#-cómo-ejecutar-los-ejemplos)
  - [📜 Licencia](#-licencia)
  - 
  -   - [English Version 🇬🇧](#english-version-)



## 🎯 Propósito de este Repositorio

Este repositorio es **puramente educativo**.

Su objetivo es **enseñar JSON Web Tokens (JWT) paso a paso**, comenzando desde los **conceptos más básicos** (creación manual de un token) y avanzando progresivamente hacia **flujos de autenticación reales** usando **FastAPI**, incluyendo:

* Access tokens
* Refresh tokens
* Rotación de tokens
* Autenticación HTTP Bearer
* Scopes y autorización

Cada ejemplo es **aislado, simple y enfocado en un tema específico**, para que quien aprende pueda entender JWT **sin magia ni abstracciones ocultas**.

Este **no es un proyecto listo para producción**, sino un **camino de aprendizaje**.

---

## 🧠 Filosofía de Aprendizaje

* Un concepto a la vez
* Sin abstracciones prematuras
* Sin frameworks ocultando el funcionamiento interno de JWT
* Cada carpeta = una lección completa
* Cada ejemplo puede ejecutarse y entenderse de forma independiente

Deberías poder:

* Leer el README de una carpeta
* Ejecutar `app.py`
* Entender **qué problema se está resolviendo y por qué**

---

## 📂 Estructura del Repositorio

Cada carpeta representa **un paso de aprendizaje**.
Cada carpeta contiene:

* `app.py` → ejemplo ejecutable
* `README.md` → explicación de los conceptos utilizados

```
.
├── 01_jwt_hs256_example/
│   ├── app.py
│   └── README.md
│
├── 02_login_jwt_fastapi/
│   ├── app.py
│   └── README.md
│
├── 03_manual_headers_jwt/
│   ├── app.py
│   └── README.md
│
├── 04_httpbearer_jwt/
│   ├── app.py
│   └── README.md
│
├── 05_jwt_scopes/
│   ├── app.py
│   └── README.md
│
├── 06_jwt_access_and_refresh/
│   ├── app.py
│   └── README.md
│
├── 07_jwt_all_included/
│   ├── docs/
│   │   ├── images/
│   │   │   └── swagger.png
│   │   └── auth-flow.md
│   ├── .env                   ->solo como ejemplo 
│   ├── auth.py
│   ├── fake_db.py
│   ├── main.py
│   └── README.md
│
├── 08_bonus/
│   ├── app.py
│   └── README.md
│
├── .gitignore
├── LICENSE
└── README.md
```

---

## 📘 Descripción de las Carpetas

### 🔹 01_jwt_hs256_example

Creación y validación básica de JWT usando **HS256**.
Se enfoca en:

* Estructura del token
* Claims
* Expiración
* Validación de la firma

---

### 🔹 02_login_jwt_fastapi

Flujo de login simple usando **FastAPI**.
Se enfoca en:

* Endpoint de login
* Generación de tokens

---

### 🔹 03_manual_headers_jwt

JWT enviados manualmente a través de headers HTTP.
Se enfoca en:

* Headers de autorización
* Extracción manual del token
* Entender qué cosas suelen automatizar los frameworks

---

### 🔹 04_httpbearer_jwt

Autenticación JWT usando **HTTPBearer**.
Se enfoca en:

* Utilidades de seguridad de FastAPI
* Estándar Bearer token
* Manejo de autenticación más limpio

---

### 🔹 05_jwt_scopes

Autorización usando **scopes en JWT**.
Se enfoca en:

* Scopes dentro del token
* Acceso basado en roles o permisos
* Rutas protegidas con validación de scopes

---

### 🔹 06_jwt_access_and_refresh

Flujo de Access y Refresh tokens.
Se enfoca en:

* Access tokens de corta duración
* Refresh tokens de larga duración
* Lógica del endpoint de refresh
* Conceptos básicos de rotación de tokens

---

### 🔹 07_jwt_all_included

Sistema completo de autenticación JWT.
Se enfoca en:

* Login
* Access tokens
* Refresh tokens
* Rotación
* HTTPBearer
* Scopes
* Rutas protegidas

Esta carpeta integra todos los conceptos anteriores.

---

### 🔹 08_bonus

Conceptos y experimentos extra.
Puede incluir:

* Casos límite de seguridad
* Errores comunes al usar JWT
* Estrategias de invalidación de tokens
* Patrones avanzados

---

## ⚠️ Notas Importantes

* Las claves secretas están **hardcodeadas solo con fines educativos**
* No se utiliza base de datos salvo que se indique explícitamente
* Este repositorio prioriza la **claridad por sobre la completitud**
* **No uses este código directamente en producción**

---

## 🧪 Cómo Ejecutar los Ejemplos

Cada carpeta es independiente.

```bash
cd 01_jwt_hs256_example
python app.py
```

O para ejemplos con FastAPI:

```bash
uvicorn app:app --reload
```

(Revisar el README de cada carpeta para más detalles.)

---

## 📜 Licencia

Este proyecto está licenciado bajo la **Licencia MIT**.
Ver el archivo `LICENSE` para más detalles.

