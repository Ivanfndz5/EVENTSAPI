from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.ticket import TicketCreate,TicketResponse
from app.services.ticket_service import create_ticket
from app.models.user import User
from app.core.security import get_current_user


router = APIRouter(prefix='/tickets', tags= ['tickets'])

@router.post('/',response_model=TicketResponse)
def create(ticket: TicketCreate,db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        return create_ticket(db, ticket, user_id=current_user.id)
    except Exception as e:
        print(f"Error ticket: {e}")
        raise



