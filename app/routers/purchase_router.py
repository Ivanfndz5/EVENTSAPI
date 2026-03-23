from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.purchase import PurchaseCreate,PurchaseResponse
from app.services.purchase_service import create_purchase, get_all_purchases,get_purchase_by_id
from app.models.user import User
from app.core.security import get_current_user


router = APIRouter(prefix='/purchases',tags=['Purchases'])

@router.post('/', response_model=PurchaseResponse)
def create(purchase: PurchaseCreate, db:Session = Depends(get_db), current_user :User = Depends(get_current_user)):
    try:
        return create_purchase(db,purchase,current_user.id)
    except Exception as e:
        print(f"ERROR:{e}")
        raise

@router.get('/', response_model=list[PurchaseResponse])
def get_all(db:Session = Depends(get_db), current_user:User = Depends(get_current_user)):
    return get_all_purchases(db)



@router.get('/{purchase_id}', response_model = PurchaseResponse)
def get_by_id(purchase_id:int,db:Session = Depends(get_db), current_user:User = Depends(get_current_user)):
    return get_purchase_by_id(db, purchase_id)


