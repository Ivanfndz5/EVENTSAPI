from sqlalchemy.orm import Session
from app.models.event import Event
from app.schemas.event import EventCreate


def create_event(db:Session, event_data: EventCreate) -> Event:
    event = Event(
        title = event_data.title,
        description = event_data.description,
        date = event_data.date,
        place = event_data.place,
        capacity = event_data.capacity
    )

    db.add(event)
    db.commit()
    db.refresh(event)

    return event


def get_events(db:Session):
    return db.query(Event).all()

def get_event(db: Session, event_id: int):
    return db.query(Event).filter(Event.id == event_id).first()

def delete_event(db:Session, event_id:int):
    event = db.query(Event).filter(Event.id == event_id).first()
    if event:
        db.delete(event)
        db.commit()
    return event


def update_event(db:Session, event_id:int, event_data : EventCreate):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        return None
    event.title = event_data.title
    event.description = event_data.description
    event.date = event_data.date
    event.place = event_data.place
    event.capacity = event_data.capacity

    db.commit()
    db.refresh(event)

    return event



