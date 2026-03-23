from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.security import hash_password, verify_password, verify_token, create_access_token
from app.schemas.auth import UserCreate, UserLogin
from app.models.user import User

def register(db:Session,user_data: UserCreate):
    #Verificamos si existe el email
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(
            status_code = 400,
            detail = 'Email already registered'
        )
    user = User(
        name = user_data.name,
        email = user_data.email,
        hashed_password = hash_password(user_data.password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    # Generar token automaticamente
    token = create_access_token(data={'sub': user.email})
    return {'access_token': token, 'token_type': 'bearer'}


def login(db:Session, user_data: UserLogin):
    #buscar usuario por email
    user = db.query(User).filter(User.email == user_data.email).first()

    #Si no existe el usuario...
    if not user:
        return None

    #verificamos la contraseña
    if not verify_password(user_data.password, user.hashed_password):
        return None


    #Crear y retornar el token
    token = create_access_token(data={'sub':user.email})
    return {'access_token':token, 'token_type':'bearer'}



