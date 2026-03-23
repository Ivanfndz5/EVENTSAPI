from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.user import UserCreate, UserResponse

from app.services.user_service import (create_user, get_user,get_users,delete_user)

router = APIRouter(prefix='/users', tags=['Users'])


@router.post('/',response_model=UserResponse)
def create(user:UserCreate, db: Session = Depends(get_db)):
    return create_user(db,user)

@router.get('/', response_model=list[UserResponse])
def read_all(user_id:int,db:Session = Depends(get_db)):
    return get_users(db)

@router.get('/{user_id}',response_model=UserResponse)
def read_one(user_id:int, db:Session = Depends(get_db)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(
            status_code= 404,
            detail = 'User not found'
        )
    return user


@router.delete('/{user_id}', status_code=status.HTTP_200_OK)
def remove(user_id: int, db:Session = Depends(get_db)):
    user = delete_user(db,user_id)
    if not user:
        raise HTTPException(
            status_code= 404,
            detail= 'User not found'
        )
    return {'message': 'User deleted'}

