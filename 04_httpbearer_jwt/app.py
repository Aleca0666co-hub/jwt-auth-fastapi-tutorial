from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError, ExpiredSignatureError
from datetime import datetime, timedelta, timezone

app = FastAPI(
    title="JWT Authentication with HTTPBearer (04)",
    description="""
JWT authentication using FastAPI HTTPBearer security scheme.

Learning goal:
Understand how FastAPI declares security at OpenAPI level and how Swagger
becomes capable of injecting Authorization headers automatically.

Testing steps:
1. Call /login
2. Copy access_token
3. Click "Authorize"
4. Paste token
5. Call /protected
""",
    version="1.0"
)

SECRET_KEY = "supersecret"
ALGORITHM = "HS256"

# Declares HTTP Bearer authentication at OpenAPI level
# Enables Swagger authorization support
security = HTTPBearer()


def create_token(user_id: str) -> str:
    """
    Generates a signed JWT with expiration.
    """
    payload = {
        "sub": user_id,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=5)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Validates JWT using HTTPBearer security scheme.
    """
    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload

    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired"
        )

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )


@app.get("/login", tags=["Auth"])
def login():
    """
    Returns a valid JWT for testing.
    """
    return {
        "access_token": create_token("user123"),
        "token_type": "bearer"
    }


@app.get("/protected", tags=["Protected"])
def protected(payload: dict = Depends(verify_token)):
    """
    Protected route that requires JWT.
    """
    return {
        "message": "Access granted",
        "user": payload["sub"]
    }


@app.get("/")
def root():
    return {
        "info": "JWT HTTPBearer Example",
        "docs": "/docs"
    }


# INTEGRATION NOTE:
# This example connects with the next directory(05_jwt_scopes)
# where scopes are introduced for finer access control.