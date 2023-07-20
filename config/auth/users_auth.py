from fastapi import Depends, FastAPI, HTTPException, status, Security
from fastapi.security import (
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm,
    SecurityScopes,
)
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from jose import JWTError, jwt
from code.config.auth.hash import verify_password
from code.schemas.pun_schema import Users
from code.config.auth.users_model import User, Token, TokenData
from code.config.db import get_db

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login",
    scopes={"ro": "Read Only", "rw": "Read/Write"},
)

def get_user(db: Session, username: str):
    return db.query(Users).filter(Users.Username == username).first()

def authenticate_user(db: Session, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.Hashed_Password):
        return False

    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(
                    security_scopes: SecurityScopes,
                    token: str = Depends(oauth2_scheme),
                    db: Session = Depends(get_db)
                    ):

    if security_scopes.scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
    else:
        authenticate_value = "Bearer"

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_scopes = payload.get("scopes", [])

        token_data = TokenData(scopes=token_scopes, username=username)

    except JWTError:
        raise credentials_exception

    user = get_user(db, username=token_data.username)

    if user is None:
        raise credentials_exception

    if token_data.scopes in security_scopes.scopes:
        return user
    else:
        raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Not enough permissions",
                    headers={"WWW-Authenticate": authenticate_value}
        )

async def get_current_active_user(user: User = Depends(get_current_user)):
    user_data = vars(user)  
    current_user = User(**user_data)

    if current_user.Disabled == 1:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user