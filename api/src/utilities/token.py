from fastapi import HTTPException, status, Header
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from typing_extensions import Annotated, Union
import os
from dotenv import load_dotenv

load_dotenv()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = os.environ.get('SECRET_KEY')
ALGORITHM = os.environ.get("ALGORITHM")

def create_access_token(to_encode: dict):
    expire = datetime.now(timezone.utc) + timedelta(minutes=60)
    payload = {
        "data": jsonable_encoder(to_encode),
        "exp": expire
    }
    encoded_jwt = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(to_decode):
    try:
        decoded =  jwt.decode(to_decode, SECRET_KEY, algorithms=ALGORITHM)
        return decoded["data"]
    except JWTError:
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid 'authorization': 'Bearer token' in header",
                headers={"WWW-Authenticate": "Bearer"},
            )
