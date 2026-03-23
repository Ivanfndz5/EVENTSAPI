from fastapi import APIRouter, Depends,HTTPException,status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.auth import TokenResponse,UserCreate,UserLogin
from app.core.security import create_access_token
from app.services.auth_service import register as register_user
from app.services.auth_service import login as login_user



router = APIRouter(prefix = '/auth', tags= ['Auth'])


@router.post('/register',response_model=TokenResponse)
def register(user: UserCreate, db:Session = Depends(get_db)):
    return register_user(db,user)



@router.post('/login', response_model=TokenResponse)
def login(user: UserLogin, db: Session = Depends(get_db)):
    result = login_user(db, user)
    if not result:
        raise HTTPException(status_code=401, detail='Invalid credentials')
    return result
