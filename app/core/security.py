from datetime import datetime, timedelta
from fastapi import HTTPException, Depends
from app.core.database import get_db
from app.models.user import User
from jose import JWTError,jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from typing import Annotated
import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(dotenv_path=BASE_DIR / '.env')


#Configuration
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/login')
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30
#hasheo of passwords
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


#Convierte "1234" → "$2b$12$..."
def hash_password(password : str) -> str:
    return pwd_context.hash(password)

#Compara password con el hash
def verify_password(plain_password:str, hashed_password:str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

#create token
def create_access_token(data:dict)-> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes= ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expire})
    return jwt.encode(to_encode, SECRET_KEY,algorithm=ALGORITHM)

def verify_token(token:str) ->dict:
    try:
        payload = jwt.decode(token,SECRET_KEY, algorithms= [ALGORITHM])
        return payload
    except JWTError:
        return None


# Dependency
credentials_exception = HTTPException(
    status_code=401,
    detail='Could not validate credentials',
    headers={'WWW-Authenticate': 'Bearer'},
)

#verifica quien hace la request ya esta autenticado
def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db:Session = Depends(get_db)):
    payload = verify_token(token)
    if payload is None:
        raise credentials_exception

    email = payload.get('sub')
    if email is None:
        raise credentials_exception

    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise credentials_exception
    return user



