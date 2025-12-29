from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError, ExpiredSignatureError
from datetime import datetime, timedelta, timezone

app = FastAPI(
    title="JWT Access & Refresh Token Example",
    description="""
🔐 This API shows how to use **Access Tokens** and **Refresh Tokens** with FastAPI.

✨ How to test this API:

1️⃣ Call **POST /login**  
   → You will receive:
   - `access_token` (short-lived ⏳)
   - `refresh_token` (longer-lived 🌞)

2️⃣ Click **Authorize** in Swagger and paste:
   - ACCESS token → to access `/protected`
   - REFRESH token → to access `/refresh`

3️⃣ Call **/refresh** using the REFRESH token.  
   → You’ll get a brand new set of tokens 🔄

4️⃣ Use **/me** to inspect the contents of any token 👤

⚡ Important notes:
- The **Access Token** is required for protected routes.  
- The **Refresh Token** is ONLY for refreshing tokens.  
""",
    version="1.0"
)

SECRET_KEY = "supersecret"
ALGORITHM = "HS256"

security = HTTPBearer()

# Access Token: short-lived (5 minutes) → used for protected routes
def create_access_token(username: str):
    return jwt.encode(
        {
            "sub": username,
            "type": "access",
            "exp": datetime.now(timezone.utc) + timedelta(minutes=5)
        },
        SECRET_KEY,
        algorithm=ALGORITHM
    )

# Refresh Token: long-lived (1 day) → used for token rotation
def create_refresh_token(username: str):
    return jwt.encode(
        {
            "sub": username,
            "type": "refresh",
            "exp": datetime.now(timezone.utc) + timedelta(days=1)
        },
        SECRET_KEY,
        algorithm=ALGORITHM
    )

# 🆕 New login: now returns TWO tokens (access + refresh)
@app.post("/login", tags=["Auth"])
def login(username: str):
    return {
        "access_token": create_access_token(username),
        "refresh_token": create_refresh_token(username),
        "token_type": "bearer"
    }

# 🔄 Token rotation: using the refresh token creates NEW access & refresh tokens
@app.post("/refresh", tags=["Auth"])
def refresh(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        if payload.get("type") != "refresh":
            raise HTTPException(status_code=401, detail="Not a refresh token")
        # Generate fresh tokens to continue the authentication cycle
        new_access = create_access_token(payload["sub"])
        new_refresh = create_refresh_token(payload["sub"])

        return {
            "access_token": new_access,
            "refresh_token": new_refresh
        }

    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Refresh token expired")

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


@app.get("/me", tags=["User"])
def show_my_tokens(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(401, "Invalid token")


@app.get("/protected", tags=["Protected"])
def protected(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])

        if payload.get("type") != "access":
            raise HTTPException(401, "This route requires access token")

        return {
            "message": "Access granted",
            "user": payload["sub"]
        }
    except ExpiredSignatureError:
        raise HTTPException(401, "Access token expired")

    except JWTError:
        raise HTTPException(401, "Invalid token")


@app.get("/")
def root():
    return {
        "message": "JWT Access & Refresh Token API",
        "docs": "http://127.0.0.1:8000/docs",
        "redoc": "http://127.0.0.1:8000/redoc",
    }
