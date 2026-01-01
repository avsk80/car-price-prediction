from fastapi import APIRouter
from app.core.security import create_access_token
from pydantic import BaseModel

router = APIRouter()

class AuthInput(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(auth_input: AuthInput):
    # In a real application, you would verify username and password here
    if auth_input.username == "admin" and auth_input.password == "password":
        token_data = {"sub": auth_input.username}
        access_token = create_access_token(data=token_data)
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        return {"error": "Invalid credentials"}