from sqlalchemy.orm import Session
from app.models.ticket import Ticket
from app.schemas.ticket import TicketCreate


def create_ticket(db:Session, ticket_data: TicketCreate,user_id:int) -> Ticket:
    ticket = Ticket(
        event_id = ticket_data.event_id,
        user_id = user_id,
        seat_number = ticket_data.seat_number, 
        price = ticket_data.price
    )

    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket

