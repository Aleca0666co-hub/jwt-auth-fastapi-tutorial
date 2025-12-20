
from fastapi import FastAPI
from jose import jwt
from datetime import datetime, timedelta, timezone

app = FastAPI(
    title="JWT Login Example (02)",
    description="FastAPI example demonstrating JWT creation using python-jose.",
    version="1.0.0"
)

SECRET_KEY = "supersecret"
ALGORITHM = "HS256"

def create_token(user_id: str) -> str:
    """
    Generates a signed JWT with expiration.
    
    Contain:
    - User identity
    - Expiration time
    
    """
    payload = {
        "sub": user_id,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=10)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

@app.get("/login", tags=["Auth"] , summary="Login to get a JWT token")
def login():
    """
    Returns a JWT token for demonstration purposes.
    """
    return {
        "access_token": create_token("user123"),
        "token_type": "bearer"
    }

@app.get("/")
def root():
    return {
        "message": "Welcome to the JWT demo. Use /login to get a token.",
        "docs": "/docs",
        "redoc": "/redoc"
    }

# NOTE:
# This example integrates with the next directory(03_manual_headers_jwt),
# which demonstrates JWT validation and protected routes.
