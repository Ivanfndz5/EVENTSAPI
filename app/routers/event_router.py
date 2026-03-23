from fastapi import APIRouter, Depends,HTTPException,status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.event import EventCreate,EventResponse,EventUpdate
from app.core.security import get_current_user
from app.services.event_service import (get_events,get_event,create_event,delete_event,update_event)
from app.models.user import User
router = APIRouter(prefix='/events', tags=['Events'])

@router.post('/',response_model=EventResponse)
def create(event: EventCreate, db:Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    return create_event(db,event)

@router.get('/', response_model = list[EventResponse])
def get_all(db:Session = Depends(get_db)):
    return get_events(db)

@router.get('/{event_id}', response_model=EventResponse)
def get_one(event_id:int, db:Session = Depends(get_db)):
    event = get_event(db,event_id)
    if not event:
        raise HTTPException(
            status_code= 404,
            detail= 'Event not found'
        )
    return event

@router.put('/{event_id}', response_model=EventResponse)
def update(event_id:int,event_data: EventUpdate ,db:Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    event = update_event(db,event_id,event_data)
    if not event:
        raise HTTPException(
            status_code=404,
            detail='Event not found'
        )
    return event





@router.delete('/{event_id}', status_code=status.HTTP_200_OK)
def remove(event_id:int, db:Session = Depends(get_db), current_user : User = Depends(get_current_user)):
    event = delete_event(db, event_id)
    if not event:
        raise HTTPException(
            status_code = 404,
            detail = 'not found'
        )
    return {'message': 'Event deleted'}