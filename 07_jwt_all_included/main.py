from fastapi import FastAPI, Depends, HTTPException, Body
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fake_db import fake_users_db, hash_password
from auth import create_access_token, create_refresh_token, verify_access_token
from jose import jwt, JWTError
import bcrypt
import os

#Review README.md and create .env 
app = FastAPI(
    title="FastAPI JWT Auth Demo",
    description="""
🚀 **Educational JWT Authentication API built with FastAPI**

This API demonstrates:

- JWT Access Tokens (short-lived)
- JWT Refresh Tokens (long-lived)
- Refresh Token Rotation
- Role-based authorization (scopes)
- Secure password hashing (bcrypt)
- Token expiration handling

---
### 🔑 Quick Steps to Test

1️⃣ **Register** → `POST /register`  
   Example: `{ "username": "alice", "password": "secret123" }`

2️⃣ **Login** → `POST /login`  
   Returns `access_token` + `refresh_token`.

3️⃣ **Protected route** → `GET /protected`  
   Use the `access_token`.

4️⃣ **Refresh tokens** → `POST /refresh`  
   Send the `refresh_token` to get new tokens.

5️⃣ **User info** → `GET /me`  
   Inspect token payload.

6️⃣ **Admin route** → `GET /admin`  
   Requires role `admin`.
---

### 🧑‍💻 Plus: Hardcoded Admin User
For demo purposes, you can log in and test `/admin` with:  
- **username:** `alejandro`  
- **password:** `password123`  
---

⚠️ **Important**  
This project uses in-memory storage. For production, use persistent storage and extra security layers.
""",
    version="1.0.0",
)
security = HTTPBearer()

active_refresh_tokens = {}

# User Registration
@app.post("/register", tags=["Authentication"] ,
    summary="Register a new user",
    description="""
Creates a new user account.

- Passwords are hashed using **bcrypt**
- Default role assigned: `user`

⚠️ This endpoint exists for educational purposes.
""",)
def register(username: str = Body(...,min_length=3), password: str = Body(...,min_length=4)):
    if username in fake_users_db:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    hashed_password = hash_password(password) 
    fake_users_db[username] = {
        "username": username,
        "hashed_password": hashed_password,
        "scopes": ["user"]
    }
    return {"message": f"User {username} registered successfully"}

# Login
@app.post("/login" , tags=["Authentication"] , summary="Authenticate user and issue JWT tokens",
    description="""
Authenticates a user using username and password.

On success, returns:
- **Access Token** → Used to access protected endpoints
- **Refresh Token** → Used to obtain new tokens when the access token expires

🕒 Access tokens are short-lived.
🔁 Refresh tokens are rotated on each use.
""")
def login(username: str, password: str):
    user = fake_users_db.get(username)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    if not bcrypt.checkpw(password.encode(), user["hashed_password"].encode()):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    access_token = create_access_token({"sub": username, "scopes": user["scopes"]})
    refresh_token = create_refresh_token({"sub": username})
    
    active_refresh_tokens[username] = refresh_token
    
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}

# ---------------------------
# tokens rotation
@app.post("/refresh" , tags=["Authentication"] ,
    summary="Refresh access token (with token rotation)",
    description="""
Issues a new access token and a new refresh token.

### Token Rotation Explained
1. Client sends a valid refresh token
2. Server invalidates the old refresh token
3. Server issues:
   - A new access token
   - A new refresh token

This mechanism protects against refresh token replay attacks.
""", )
def refresh(refresh_token: str):
    try:
        payload = jwt.decode(
            refresh_token, 
            os.getenv("SECRET_KEY"), 
            algorithms=[os.getenv("ALGORITHM")]
        )
        if payload.get("type") != "refresh":
            raise HTTPException(status_code=400, detail="Invalid refresh token")
        
        username = payload.get("sub")
        user = fake_users_db.get(username)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        # Verificamos que el refresh token esté activo
        if active_refresh_tokens.get(username) != refresh_token:
            raise HTTPException(status_code=400, detail="Refresh token invalidated")
        
        # Generamos nuevos tokens
        new_access = create_access_token({"sub": username, "scopes": user["scopes"]})
        new_refresh = create_refresh_token({"sub": username})
        
        # Rotamos el refresh token
        active_refresh_tokens[username] = new_refresh
        
        return {"access_token": new_access, "refresh_token": new_refresh, "token_type": "bearer"}
    except JWTError:
        raise HTTPException(status_code=400, detail="Invalid refresh token")

# ---------------------------
# Protected endpoints 
@app.get("/protected" , tags=["Protected"] ,
    summary="User-protected endpoint",
    description="""
Protected endpoint that requires a valid **access token**
with the `user` scope.

Used to demonstrate basic JWT authorization.
""")
def protected(credentials: HTTPAuthorizationCredentials = Depends(security)):
    payload = verify_access_token(credentials.credentials, ["user"])
    return {"message": f"Hello {payload['sub']}, you have user access!"}

@app.get("/admin" , tags=["Protected"] , 
    summary="Admin-only endpoint",
    description="""
Protected endpoint that requires:
- A valid access token
- The `admin` scope

Demonstrates role-based access control using JWT scopes.
""",)
def admin(credentials: HTTPAuthorizationCredentials = Depends(security)):
    payload = verify_access_token(credentials.credentials, ["admin"])
    if "admin" not in payload.get("scopes", []):
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return {"message": f"Welcome admin {payload['sub']}"}

# User information (/me)
@app.get("/me" , tags=["User"] , 
    summary="Get current user information",
    description="""
Returns information extracted from the access token:
- Username
- Scopes
- Token type
- Expiration timestamp

Useful for debugging and learning JWT payloads.
""",)
def me(credentials: HTTPAuthorizationCredentials = Depends(security)):
    payload = verify_access_token(credentials.credentials, ["user"])
    return {
        "username": payload.get("sub"),
        "scopes": payload.get("scopes", []),
        "token_type": payload.get("type"),
        "expires": payload.get("exp")
    }

# ---------------------------
# root route (/)
@app.get("/")
def root():
    return {"message": "Welcome to the JWT demo API. Go to /docs for API documentation."}
