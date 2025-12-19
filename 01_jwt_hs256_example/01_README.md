
# FastAPI JWT Auth (HS256 Example)

---
# English Version 🇬🇧
---

## 1. General Description
This project demonstrates a basic but professional implementation of **JSON Web Tokens (JWT)** using Python and the `python-jose` library. It focuses on generating and validating tokens signed with the HS256 algorithm.

---

  ## 📑 Index 

- [English Version 🇬🇧](#english-version-)
  - [1. General Description](#1-general-description)
  - [2.🧑‍💻 What This Project Does](#2-what-this-project-does)
  - [3.🔑 Key Concepts](#3-key-concepts)
  - [4.⚙️ Requirements](#4️-requirements)
  - [5.✅ Installation](#5-installation)
  - [6.▶️ How to Run](#6️-how-to-run)
  - [7.🔍 Important Endpoints](#7-important-endpoints)
  - [8.⚠️ Security Details](#8️-security-details)
  - [9.📘 Technical Notes](#9-technical-notes)
  - [10.🧩 How a JWT is Formed and Decoded](#10-how-a-jwt-is-formed-and-decoded)
    - [Example Code Flow:](#example-code-flow)
    - [🔎 Flow Explanation:](#-flow-explanation)
  - [11. License](#11-license)
- [Versión en Español 🇪🇸](#versión-en-español-)


---

## 2.🧑‍💻 What This Project Does
- Generates a JWT with expiration.  
- Signs tokens using HS256.  
- Decodes and validates tokens.  
- Displays claims (information inside the token).  
- Handles token expiration.  

---

## 3.🔑 Key Concepts
- **JWT (JSON Web Token):** Compact format for securely transmitting data.  
- **HS256:** Symmetric signing algorithm.  
- **Claims:**  
  - `sub`: User identifier.  
  - `exp`: Expiration date.  
- **Integrity:** Ensures the token has not been altered.  
- **Expiration:** Prevents permanent tokens.  

---

## 4.⚙️ Requirements
- Python 3.12.11  
- Library `python-jose`  

Install dependencies:  
```bash
pip install python-jose
```

---

## 5.✅ Installation
Clone the repository and install dependencies:  
```bash
git clone <repository_url>
cd <project_folder>
pip install python-jose
```

---

## 6.▶️ How to Run
Execute the script:  
```bash
python app.py
```

---

## 7.🔍 Important Endpoints
- `/login` → Generates a token.  
- `/refresh` → Refreshes the token.  
- `/protected` → Protected route requiring a valid token.  

---

## 8.⚠️ Security Details
- HS256 signing with secret key.  
- Mandatory expiration to avoid indefinite tokens.  
- Token invalid if modified or expired.  

---

## 9.📘 Technical Notes
- Token lifetime: **10 minutes**.  
- Uses `datetime` with timezone (`timezone.utc`).  
- No database used (educational example).  
- Designed as a foundation for larger projects.  

---

## 10.🧩 How a JWT is Formed and Decoded

A **JWT** consists of three parts:  
1. **Header** → Algorithm and token type.  
2. **Payload** → Data (*claims*) such as user and expiration.  
3. **Signature** → Ensures integrity.  

### Example Code Flow:

```python
from jose import jwt
from datetime import datetime, timedelta, timezone

SECRET = "supersecret"  
ALGORITHM = "HS256"

# 1. Create payload with claims
payload = {
    "sub": "user123",  # user identifier
    "exp": datetime.now(timezone.utc) + timedelta(minutes=10)  # expires in 10 minutes
}

# 2. Generate token (includes signature)
token = jwt.encode(payload, SECRET, algorithm=ALGORITHM)
print("\nGenerated token:", token)

# 3. Decode token
decoded = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
print("\nDecoded payload:", decoded)
```

---

### 🔎 Flow Explanation:
- Define a **payload** with `sub` (user) and `exp` (expiration).  
- Build a **header** specifying algorithm (`HS256`) and type (`JWT`).  
- **Token signature:**  
  - Convert header and payload to JSON, then Base64URL.  
  - Concatenate with a dot: `header.payload`.  
  - Apply the signing algorithm (HS256) with the **secret key** (`SECRET`).  
  - Result is the **signature**, also in Base64URL.  
- Final token format:  
  ```
  header.payload.signature
  ```
- When decoding, `jwt.decode` validates that the **signature** matches and that the token has not expired.  
- If the signature does not match (tampered token) or expiration has passed, the token is invalid.  

---

## 11. License
[MIT LICENSE](../LICENSE). See LICENSE file in the root.  


---

# Versión en Español 🇪🇸

---



## 1. Descripción General
Este proyecto muestra una implementación básica pero profesional de **JSON Web Tokens (JWT)** usando Python y la librería `python-jose`. Se enfoca en la generación y validación de tokens firmados con el algoritmo HS256.


## 📑  Índice 
- [English Version 🇬🇧](#english-version-)

  - [1. Descripción General](#1-descripción-general)
  - [2.🧑‍💻 Qué hace el proyecto](#2-qué-hace-el-proyecto)
  - [3.🔑 Conceptos clave](#3-conceptos-clave)
  - [4.⚙️ Requisitos](#4️-requisitos)
  - [5.✅ Instalación](#5-instalación)
  - [6.▶️ Cómo correr el proyecto](#6️-cómo-correr-el-proyecto)
  - [7.🔍 Endpoints importantes](#7-endpoints-importantes)
  - [8.⚠️ Detalles de seguridad](#8️-detalles-de-seguridad)
  - [9.📘 Notas técnicas](#9-notas-técnicas)
  - [10.🧩 Cómo se forma y se decodifica un JWT](#10-cómo-se-forma-y-se-decodifica-un-jwt)
    - [Ejemplo de flujo en código:](#ejemplo-de-flujo-en-código)
    - [🔎 Explicación del flujo:](#-explicación-del-flujo)
  - [11. Licencia](#11-licencia)


---

## 2.🧑‍💻 Qué hace el proyecto
- Genera un JWT con expiración.  
- Firma tokens con HS256.  
- Decodifica y valida los tokens.  
- Muestra los *claims* (información contenida en el token).  
- Controla la expiración del token.  

---

## 3.🔑 Conceptos clave
- **JWT (JSON Web Token):** Formato compacto para transmitir datos de forma segura.  
- **HS256:** Algoritmo de firma simétrica.  
- **Claims:**  
  - `sub`: Identificador del usuario.  
  - `exp`: Fecha de expiración.  
- **Integridad:** Garantiza que el token no haya sido alterado.  
- **Expiración:** Evita tokens permanentes.  

---

## 4.⚙️ Requisitos
- Python 3.12.11  
- Librería `python-jose`  

Instalación de dependencias:  
```bash
pip install python-jose
```

---

## 5.✅ Instalación
Clonar el repositorio e instalar dependencias:  
```bash
git clone <repository_url>
cd <project_folder>
pip install python-jose
```

---

## 6.▶️ Cómo correr el proyecto
Ejecutar el script:  
```bash
python app.py
```

---

## 7.🔍 Endpoints importantes
- `/login` → Genera un token.  
- `/refresh` → Refresca el token.  
- `/protected` → Ruta protegida que requiere token válido.  

---

## 8.⚠️ Detalles de seguridad
- Firma HS256 con clave secreta.  
- Expiración obligatoria para evitar tokens indefinidos.  
- Token inválido si se modifica o expira.  

---

## 9.📘 Notas técnicas
- El token dura **10 minutos**.  
- Se usa `datetime` con zona horaria (`timezone.utc`).  
- No se usa base de datos (ejemplo educativo).  
- Diseño pensado como base para proyectos más grandes.  

---

## 10.🧩 Cómo se forma y se decodifica un JWT

Un **JWT** se compone de tres partes:  
1. **Header** → Algoritmo y tipo de token.  
2. **Payload** → Datos (*claims*) como usuario y expiración.  
3. **Signature** → Firma que asegura integridad.  

### Ejemplo de flujo en código:

```python
from jose import jwt
from datetime import datetime, timedelta, timezone

SECRET = "supersecret"  
ALGORITHM = "HS256"

# 1. Crear payload con claims
payload = {
    "sub": "user123",  # identificador del usuario
    "exp": datetime.now(timezone.utc) + timedelta(minutes=10)  # expiración en 10 min
}

# 2. Generar token (firma incluida)
token = jwt.encode(payload, SECRET, algorithm=ALGORITHM)
print("\nGenerated token:", token)

# 3. Decodificar token
decoded = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
print("\nDecoded payload:", decoded)
```

---

### 🔎 Explicación del flujo:
- Se define un **payload** con `sub` (usuario) y `exp` (tiempo de expiración).  
- Se construye un **header** que indica el algoritmo (`HS256`) y el tipo (`JWT`).  
- **Firma del token:**  
  - Se toma el **header** y el **payload**, se convierten a JSON y luego a Base64URL.  
  - Se concatenan con un punto: `header.payload`.  
  - Se aplica el algoritmo de firma (HS256 en este caso) usando la **clave secreta** (`SECRET`).  
  - El resultado es la **signature**, también en Base64URL.  
- El token final es:  
  ```
  header.payload.signature
  ```
- Al decodificar, la librería `jwt.decode` valida que la **firma** corresponda al contenido y que el token no haya expirado.  
- Si la firma no coincide (token alterado) o el tiempo de expiración ya pasó, el token se considera inválido.  

---

## 11. Licencia
[MIT LICENSE](../LICENSE). Ver archivo LICENSE en el root.  

