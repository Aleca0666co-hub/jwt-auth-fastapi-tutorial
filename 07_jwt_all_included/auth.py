from datetime import datetime, timedelta , timezone
from jose import jwt, JWTError
from fastapi import HTTPException, status
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS"))

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """
    Creates a short-lived JWT access token.

    Access tokens:
    - Are sent on every authenticated request
    - Expire quickly to reduce attack surface
    - Contain user identity and scopes
    """
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire, "type": "access"}) 
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def create_refresh_token(data: dict):
    """
    Creates a long-lived JWT refresh token.

    Refresh tokens:
    - Are never used to access protected endpoints
    - Are used only to obtain new tokens
    - Are rotated on every refresh request
    """
    expire = datetime.now(timezone.utc) + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode = {**data, "exp": expire, "type": "refresh"}
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_access_token(token: str, required_scopes: list[str]):
    """
    Validates and authorizes a JWT access token.

    Validation steps:
    1. Decode and verify JWT signature
    2. Ensure token type is 'access'
    3. Check expiration (`exp`)
    4. Enforce required scopes (authorization)

    Raises:
    - 401 if token is invalid or expired
    - 403 if token lacks required permissions
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if payload.get("type") != "access":
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token type")
        token_scopes = payload.get("scopes", [])
        if not set(required_scopes).issubset(set(token_scopes)):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                detail="Not enough permissions")
        return payload
    except JWTError:
        raise Exception("Invalid token")
    
