# Dependency Ingestion logic for API KEY and JWT token verification
from fastapi import Header, HTTPException
from app.core.config import settings
from app.core.security import verify_access_token

def get_api_key(x_api_key: str = Header(...)) -> str:
    if x_api_key != settings.API_SECRET_KEY:
        raise HTTPException(status_code=403, detail="Could not validate API KEY")
    return x_api_key

def get_current_user(token: str = Header(...)) -> dict:
    payload = verify_access_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Could not validate credentials")
    return payload

