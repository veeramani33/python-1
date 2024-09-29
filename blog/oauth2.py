from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from . import token

o2auth_schema =OAuth2PasswordBearer(tokenUrl='login')

def get_current_user(data: str = Depends(o2auth_schema)):
    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail= "Could not validate credentials",
        headers={'WW-Authenticate':"Bearer"},
    )

    return token.verify_token(data, credentials_exception)