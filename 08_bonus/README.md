
#  JWT Authentication in Production (08)
This directory complements the educational demo by explaining how **JWT authentication** should be implemented in a **production environment**, highlighting best practices and missing features not covered in the tutorial code.

---
## 📑 Index (EN)
- [08_bonus – JWT Authentication in Production](#jwt-authentication-in-production-08)  
  - [JWT in Production vs Demo Code](#-jwt-in-production-vs-demo-code)  
  - [Security Best Practices](#️-security-best-practices)  
  - [Correct Use of FastAPI with JWT & Databases](#️-correct-use-of-fastapi-with-jwt--databases)  
  - [Token Rotation (Beyond Demo)](#-token-rotation-beyond-demo)
  - [🔑 Key Rotation](#-key-rotation)  
  - [What This Repo Did Not Cover](#-what-this-repo-did-not-cover)  
  - [Summary](#-summary)  
- [Spanish Version](#autenticación-jwt-en-producción-08)

---
## 🔑 JWT in Production vs Demo Code

- **Demo Code**  
  - Uses in-memory storage (`fake_users_db`, `active_refresh_tokens`).  
  - Tokens are generated and validated but **no persistence** or revocation is implemented.  
  - Refresh tokens are rotated but old ones remain valid until expiration.  
  - Passwords are hashed with bcrypt but stored in memory.  

- **Production**  
  - Requires **persistent storage** (SQL/NoSQL database) for users and tokens.  
  - Refresh tokens must be **revoked/blacklisted** once rotated.  
  - Tokens should be stored securely (e.g., in **HTTP-only cookies**).  
  - Passwords must be hashed with bcrypt/argon2 and stored in a database.  
  - Access control should be enforced with **roles/scopes** stored in DB.  
  - Logging and monitoring for suspicious activity is essential.

---

## 🛡️ Security Best Practices

- **Use HTTPS**: Always serve tokens over TLS.  
- **Secure Password Hashing**: Use bcrypt or argon2 with proper salt.  
- **Short-lived Access Tokens**: Minimize exposure (e.g., 5–15 minutes).  
- **Refresh Token Rotation**: Issue a new refresh token each time and revoke the old one.  
- **Blacklist/Revocation**: Maintain a blacklist table to invalidate stolen/old refresh tokens.  
- **Store Tokens in Cookies**: Use HTTP-only, Secure cookies for better UX and protection against XSS.  
- **Scopes & Roles**: Implement fine-grained authorization with scopes (e.g., `user`, `admin`).  
- **Rate Limiting**: Prevent brute-force attacks on login endpoints.  
- **Audit Logging**: Track login attempts, refresh events, and token revocations.

---

## ⚙️ Correct Use of FastAPI with JWT & Databases

1. **User Registration**  
   - Store users in a database with hashed passwords.  
   - Assign roles/scopes at registration or via admin tools.  

2. **Login**  
   - Validate credentials against DB.  
   - Issue access + refresh tokens.  
   - Store refresh token in DB with expiration.  

3. **Protected Routes**  
   - Use `Depends` with JWT verification.  
   - Check scopes/roles from token payload.  

4. **Token Rotation**  
   - On `/refresh`, validate refresh token against DB.  
   - Invalidate the old refresh token (blacklist).  
   - Issue new access + refresh tokens.  

5. **Logout**  
   - Delete or blacklist refresh token in DB.  
   - Clear cookies on client side.  

---

## 🔄 Token Rotation (Beyond Demo)

The demo rotates refresh tokens but does not revoke old ones. In production:

- **Blacklist System**  
  - Store refresh tokens in DB.  
  - Mark old tokens as invalid once a new one is issued.  
  - Reject any attempt to reuse invalidated tokens.  

- **Cookies for UX**  
  - Store refresh tokens in secure, HTTP-only cookies.  
  - This avoids manual handling in headers and improves user experience.  

- **Session Management**  
  - Allow multiple sessions per user (e.g., different devices).  
  - Track refresh tokens per device and revoke individually if needed.  

---

## 🔑 Key Rotation

In addition to token rotation, production systems must implement **key rotation** for the cryptographic keys used to sign JWTs.

- **Why it matters**  
  - Limits exposure if a signing key is compromised.  
  - Ensures compliance with security standards (PCI-DSS, GDPR, etc.).  
  - Reduces risk of long-term attacks using old keys.  

- **How to implement**  
  - Maintain a **key set** (multiple active keys).  
  - Use the newest key to sign new tokens.  
  - Accept older keys temporarily to validate tokens issued before rotation.  
  - Automate rotation (e.g., every 30–90 days).  
  - Publish keys via **JWKS (JSON Web Key Set)** for distributed systems.  

- **Best practices**  
  - Store keys in secure vaults (AWS KMS, Azure Key Vault, HashiCorp Vault).  
  - Never hardcode keys in source code.  
  - Audit and log every rotation event.  
  - Combine with refresh token rotation for maximum security.  

---

## 📘 What This Repo Did Not Cover

- Persistent storage with SQL/NoSQL databases for users and tokens.  
- Proper **token revocation/blacklist** to invalidate old or stolen refresh tokens.  
- Secure cookie handling (HTTP-only, Secure) for refresh tokens to improve UX.  
- Multi-device session management (tracking refresh tokens per device).  
- Advanced monitoring, logging, and auditing of authentication events.  
- Integration with OAuth2/OpenID Connect for external identity providers.  
- **Key rotation** for JWT signing keys, including use of JWKS and secure vaults.  
- Use of **pepper** in addition to salt for password hashing.  
- Rate limiting and brute-force protection on login endpoints.  
- Centralized secret management (AWS KMS, Azure Key Vault, HashiCorp Vault).  

---

## ✅ Summary

This repo provided a **didactic introduction** to JWT authentication with FastAPI.  
For production-ready systems, you must add:

- **Databases** for users and tokens.  
- **Revocation/blacklist** for refresh tokens.  
- **Secure cookies** for better UX.  
- **Scopes/roles** enforced from DB.  
- **Security layers**: HTTPS, rate limiting, logging.  

#### 🙌 Final Words 
Thank you for taking the time to explore this repository.  
It was designed as a learning resource, not a production-ready solution.  
If you’ve reached this point, we hope you’ve gained clarity on how JWT works and what is needed to make authentication secure in real-world applications.  
Keep experimenting, keep learning, and use this demo as a stepping stone toward building robust systems.

---

# Autenticación JWT en Producción (08)

Este directorio complementa el demo educativo mostrando cómo la **autenticación JWT** debe implementarse en un entorno **de producción**, resaltando buenas prácticas y las características que faltan en el código de ejemplo.

## 📑 Índice (ES)
- [08\_bonus – Autenticación JWT en Producción](#autenticación-jwt-en-producción-08)
  - [🔑 JWT en Producción vs Código Demo](#-jwt-en-producción-vs-código-demo)
  - [🛡️ Buenas Prácticas de Seguridad](#️-buenas-prácticas-de-seguridad)
  - [⚙️ Uso Correcto de FastAPI con JWT y Bases de Datos](#️-uso-correcto-de-fastapi-con-jwt-y-bases-de-datos)
  - [🔄 Rotación de Tokens (Más Allá del Demo)](#-rotación-de-tokens-más-allá-del-demo)
  - [🔑 Rotación de Claves](#-rotación-de-claves-es)
  - [📘 Lo que este Repo No Cubrió](#-lo-que-este-repo-no-cubrió)
  - [✅ Resumen](#-resumen)
- [Versión en Inglés](#jwt-authentication-in-production-08)
---

## 🔑 JWT en Producción vs Código Demo

- **Código Demo**  
  - Usa almacenamiento en memoria (`fake_users_db`, `active_refresh_tokens`).  
  - Los tokens se generan y validan, pero no hay persistencia ni revocación.  
  - Los refresh tokens se rotan, pero los antiguos siguen siendo válidos hasta expirar.  
  - Las contraseñas se hashean con bcrypt pero se guardan en memoria.  

- **Producción**  
  - Requiere **almacenamiento persistente** (base de datos SQL/NoSQL) para usuarios y tokens.  
  - Los refresh tokens deben ser **revocados/blacklisteados** al rotarse.  
  - Los tokens deben almacenarse de forma segura (ej. en **cookies HTTP-only**).  
  - Las contraseñas deben hashearse con bcrypt/argon2 y guardarse en DB.  
  - Los roles y scopes deben gestionarse desde la base de datos.  
  - Es esencial el monitoreo y logging de actividad sospechosa.

---

## 🛡️ Buenas Prácticas de Seguridad

- **Usar HTTPS**: siempre servir tokens sobre TLS.  
- **Hashing seguro de contraseñas**: bcrypt o argon2 con salt adecuado.  
- **Access tokens de corta duración**: minimizar exposición (5–15 minutos).  
- **Rotación de refresh tokens**: emitir uno nuevo en cada uso y revocar el anterior.  
- **Blacklist/Revocación**: mantener tabla/lista para invalidar tokens robados o antiguos.  
- **Almacenar tokens en cookies**: HTTP-only y Secure para mejor UX y protección contra XSS.  
- **Scopes y roles**: autorización granular (`user`, `admin`, etc.).  
- **Rate limiting**: prevenir ataques de fuerza bruta en login.  
- **Audit logging**: registrar intentos de login, eventos de refresh y revocaciones.

---

## ⚙️ Uso Correcto de FastAPI con JWT y Bases de Datos

1. **Registro de usuarios**  
   - Guardar usuarios en DB con contraseñas hasheadas.  
   - Asignar roles/scopes en el registro o mediante administración.  

2. **Login**  
   - Validar credenciales contra DB.  
   - Emitir access + refresh tokens.  
   - Guardar refresh token en DB con fecha de expiración.  

3. **Rutas protegidas**  
   - Usar `Depends` para verificar JWT.  
   - Validar scopes/roles desde el payload.  

4. **Rotación de tokens**  
   - En `/refresh`, validar refresh token contra DB.  
   - Invalidar el token viejo (blacklist).  
   - Emitir nuevos access + refresh tokens.  

5. **Logout**  
   - Eliminar o revocar refresh token en DB.  
   - Limpiar cookies en el cliente.  

---

## 🔄 Rotación de Tokens (Más Allá del Demo)

El demo rota refresh tokens pero no revoca los antiguos. En producción:

- **Sistema de blacklist**  
  - Guardar refresh tokens en DB.  
  - Marcar tokens viejos como inválidos al emitir uno nuevo.  
  - Rechazar cualquier intento de reutilizar tokens invalidados.  

- **Cookies para UX**  
  - Guardar refresh tokens en cookies seguras (HTTP-only, Secure).  
  - Evita manejo manual en headers y mejora la experiencia de usuario.  

- **Gestión de sesiones**  
  - Permitir múltiples sesiones por usuario (ej. distintos dispositivos).  
  - Rastrear refresh tokens por dispositivo y revocar individualmente si es necesario.  

---
## 🔑 Rotación de Claves 

Además de la rotación de tokens, en producción se debe implementar la **rotación de claves** criptográficas usadas para firmar los JWT.

- **Por qué es importante**  
  - Limita la exposición si una clave de firma es comprometida.  
  - Cumple con normativas de seguridad (PCI-DSS, GDPR, etc.).  
  - Reduce el riesgo de ataques prolongados con claves antiguas.  

- **Cómo implementarlo**  
  - Mantener un **conjunto de claves** (key set).  
  - Usar la clave más reciente para firmar nuevos tokens.  
  - Aceptar claves anteriores temporalmente para validar tokens emitidos antes de la rotación.  
  - Automatizar la rotación (ej. cada 30–90 días).  
  - Publicar claves mediante **JWKS (JSON Web Key Set)** en sistemas distribuidos.  

- **Buenas prácticas**  
  - Almacenar claves en gestores seguros (AWS KMS, Azure Key Vault, HashiCorp Vault).  
  - Nunca hardcodear claves en el código fuente.  
  - Auditar y registrar cada evento de rotación.  
  - Combinar con la rotación de refresh tokens para máxima seguridad.  

---

## 📘 Lo que este Repo No Cubrió

- Integración con bases de datos persistentes (SQL/NoSQL) para usuarios y tokens.  
- **Revocación/blacklist** adecuada para invalidar refresh tokens viejos o robados.  
- Manejo seguro de cookies (HTTP-only, Secure) para refresh tokens y mejor UX.    
- Gestión de sesiones multi-dispositivo (rastrear refresh tokens por dispositivo).  
- Monitoreo, logging y auditoría avanzada de eventos de autenticación.  
- Integración con OAuth2/OpenID Connect para proveedores externos de identidad.  
- **Rotación de claves** de firma JWT, incluyendo uso de JWKS y gestores seguros.  
- Uso de **pepper** además de salt para hashing de contraseñas.  
- Rate limiting y protección contra fuerza bruta en login.  
- Gestión centralizada de secretos (AWS KMS, Azure Key Vault, HashiCorp Vault).  

---

## ✅ Resumen

Este repositorio ofreció una **introducción didáctica** a JWT con FastAPI.  
Para un sistema listo para producción se debe añadir:

- **Bases de datos** para usuarios y tokens.  
- **Revocación/blacklist** de refresh tokens.  
- **Cookies seguras** para mejor UX.  
- **Scopes/roles** gestionados desde DB.  
- **Capas de seguridad**: HTTPS, rate limiting, logging.  

#### 🙌 Palabras Finales 

Gracias por dedicar tu tiempo a revisar este repositorio.  
Fue creado como recurso educativo, no como solución lista para producción.  
Si llegaste hasta aquí, esperamos que hayas comprendido mejor cómo funciona JWT y qué se necesita para asegurar la autenticación en aplicaciones reales.  
Sigue experimentando, sigue aprendiendo y utiliza este demo como un punto de partida hacia sistemas más robustos y seguros.



