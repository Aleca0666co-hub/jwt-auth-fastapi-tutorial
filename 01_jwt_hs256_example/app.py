from jose import jwt
from datetime import datetime, timedelta, timezone


# JWT example (01)


# Secret used to sign JWTs.
# In production this must be stored in environment variables.
SECRET = "supersecret"  
ALGORITHM = "HS256"  #Algorithm used to sign the JWT

# Generate token
payload = {
    "sub": "user123",                                      # user identifier
    "exp": datetime.now(timezone.utc) + timedelta(minutes=10)  # expires in 10 minutes
}
token = jwt.encode(payload, SECRET, algorithm=ALGORITHM)
print("\nGenerated token:", token)

# Decode token
decoded = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
print("\nDecoded payload:", decoded)
