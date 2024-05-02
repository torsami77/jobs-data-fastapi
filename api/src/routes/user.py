from fastapi import APIRouter, HTTPException, Form, Body, Query, status, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm
import logging
import bleach
from typing_extensions import Annotated, Union, List
from passlib.context import CryptContext


from ..database import models, schemas, db_config
from ..utilities.token import create_access_token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

db_gen = db_config.get_db()
db = next(db_gen)

router = APIRouter()


@router.post('/sign_up_user', status_code=status.HTTP_201_CREATED, response_model=schemas.UserCreate)
async def sign_up_user(
    name: Annotated[Union[str, None], Form(min_length=3)],
    username: Annotated[str, Form(pattern= "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+${8,}", min_length=5)],
    password: Annotated[str, Form(pattern=r"^.*[A-Za-z]+.*\d+.*$|^.*\d+.*[A-Za-z]+.*$+.{8,}")],
    role: Annotated[str, Form()],
    affiliation: Annotated[str, Form()]
):
    role_list = ['Customer', 'Employee']
    if role not in role_list:
        raise HTTPException(status_code=400, detail=f"'role' must be in {role_list}")
    if db.query(models.User).filter(models.User.email == username).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    try:
        db_user = models.User(
            name = bleach.clean(name),
            email = bleach.clean(username),
            hashed_password = pwd_context.hash(password),
            role = role,
            affiliation = bleach.clean(affiliation)
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        db_user.access_token =  create_access_token(db_user)
        return db_user
    except Exception as error:
        logging.warning(f"Exception Name: {type(error).__name__}")
        logging.warning(f"Exception Desc: {error}")


@router.post("/token", status_code=status.HTTP_200_OK, response_model=schemas.Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    email = bleach.clean(form_data.username)
    plain_password = bleach.clean(form_data.password)
    db_user = db.query(models.User).filter(models.User.email == email).first()
    if db_user and pwd_context.verify(plain_password, db_user.hashed_password):
        del db_user.hashed_password
        access_token =  create_access_token(db_user)
        return schemas.Token(access_token=access_token, token_type="bearer", role=db_user.role)
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    