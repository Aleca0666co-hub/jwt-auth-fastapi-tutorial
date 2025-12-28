from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone

app = FastAPI(
    title="JWT Scopes Authorization (05)",
    description="""
Implements fine-grained permission control using JWT scopes.

## 🔐 Permission Scopes

The API uses *scopes* inside the JWT to control access to each endpoint.

### **Available Scopes**

| Scope | Description |
|-------|-------------|
| **read** | Allows access to read-only resources. Required for `GET /data`. |
| **write** | Allows creating or modifying resources. Required for `POST /data`. |
| **admin** | Allows performing critical administrative actions. Required for `DELETE /users`. |

### **Authentication Flow**

1. Request a token using `/login_read` or `/login_admin`.
2. Include the token in the header(Authorize button in Swagger UI):  
   `Authorization: Bearer <token>`
3. Access protected endpoints according to your permissions.

---
""",
)





SECRET_KEY = "supersecret"
ALGORITHM = "HS256"

security = HTTPBearer()


def create_token(user_id: str, scopes: list) -> str:
    """
    Issues a JWT containing:
    - User identity
    - Permission scopes
    - Expiration time
    """
    payload = {
        "sub": user_id,
        "scopes": scopes,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=5)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)) -> dict:
    """
    Validates token integrity, signature and expiration.
    """
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")


def require_scope(required_scope: str):
    """
    Factory function that creates permission-check dependencies.

    Each protected route declares the required scope explicitly.
    """
    def permission_checker(payload: dict = Depends(verify_token)):
        if required_scope not in payload.get("scopes", []):
            raise HTTPException(status_code=403, detail="Insufficient permissions")
        return payload

    return permission_checker


# Login that returns a limited permission token
@app.get("/login_read", tags=["Authentication"])
def login_read():
    return {"access_token": create_token("reader_user", ["read"])}


# Login that returns a full-permission token
@app.get("/login_admin", tags=["Authentication"])
def login_admin():
    return {"access_token": create_token("admin_user", ["read", "write", "admin"])}


# Route protected by "read" permission
@app.get("/data", tags=["Protected"])
def read_data(payload: dict = Depends(require_scope("read"))):
    return {"message": "Read access granted"}


# Route protected by "write" permission
@app.post("/data", tags=["Protected"])
def write_data(payload: dict = Depends(require_scope("write"))):
    return {"message": "Write access granted"}


# Route restricted to "admin" permission
@app.delete("/users", tags=["Protected"])
def delete_users(payload: dict = Depends(require_scope("admin"))):
    return {"message": "Admin access granted"}

@app.get("/")
def root():
    return {
        "message": "JWT Scopes Authorization Example",
        "docs": "/docs",
    }

# INTEGRATION NOTE:
# The next module introduces access tokens and refresh tokens.

