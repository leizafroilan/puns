from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from fastapi import Depends, FastAPI, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from code.config.auth.users_model import Token, TokenData
from code.config.auth.users_auth import authenticate_user, create_access_token, get_current_active_user
from code.config.db import get_db
from code.config.auth.users_model import User

ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter(
    # prefix="/login",
    tags=["authentication"],
)

@router.post("/login", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), 
            db: Session = Depends(get_db) ):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.Username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user
