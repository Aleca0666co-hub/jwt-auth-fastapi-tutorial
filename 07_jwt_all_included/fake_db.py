import bcrypt

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

fake_users_db = {
    "alejandro": {
        "username": "alejandro",
        "hashed_password": hash_password("password123"),
        "scopes": ["user", "admin"]
    },
    "maria": {
        "username": "maria",
        "hashed_password": hash_password("password456"),
        "scopes": ["user"]
    }
}
