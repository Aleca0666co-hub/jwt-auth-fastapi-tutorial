from fastapi import FastAPI, Depends, Header, HTTPException, status 
from jose import jwt, JWTError, ExpiredSignatureError
from datetime import datetime, timedelta, timezone

app = FastAPI(
    title="JWT Manual Header Authentication (03)",
    description="""
This example demonstrates JWT authentication using raw HTTP headers.

LEARNING OBJECTIVE:
Understand JWT at HTTP protocol level, not Swagger automation.

IMPORTANT:
Swagger does NOT attach Authorization headers when using Header(...).

Try this flow:
1) Call /login to get a token.
2) Call /protected from Swagger → it FAILS.
3) Even if you try writing Authorization manually → it FAILS.
4) Open a terminal and run:

    curl -H "Authorization: Bearer YOUR_TOKEN" http://127.0.0.1:8000/protected

This teaches JWT at HTTP protocol level,
not Swagger automation.
"""
)


SECRET_KEY = "supersecret"
ALGORITHM = "HS256"


def create_token(user_id: str) -> str:
    """
    Generates JWT token with expiration.
    """
    payload = {
        "sub": user_id,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=2)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def verify_token(authorization: str = Header(...)):
    """
    Reads and validates Authorization header manually.

    Swagger does NOT inject headers defined via Header().
    Real HTTP clients like curl DO send them.

    This function validates:
    - Bearer scheme
    - Token integrity
    - Expiration
    """
    print("RAW HEADER RECEIVED:", repr(authorization))

    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid scheme. Use: Bearer <token>"
        )

    token = authorization.split(" ")[1]

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload

    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


@app.get("/login", tags=["Auth"])
def login():
    """
    Generates demo token for demo purposes.
    """
    return {
        "access_token": create_token("user123"),
        "token_type": "bearer"
    }


@app.get("/protected", tags=["Protected"])
def protected(payload: dict = Depends(verify_token)):
    """
    Protected endpoint.
    Requires Authorization header manually.
    """
    return {
        "msg": "Access granted",
        "user": payload["sub"]
    }


@app.get("/")
def root():
    return {
        "message": "JWT Manual Header Example",
        "docs": "/docs",
        "note": "Use curl for /protected"
    }


# INTEGRATION NOTE:
# This example connects with the next directory(04_httpbearer_jwt)
# where HTTPBearer is introduced and Swagger authentication works properly.