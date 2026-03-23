from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.purchase import Purchase
from app.models.ticket import Ticket
from app.schemas.purchase import PurchaseResponse, PurchaseCreate
from typing import List

def create_purchase(db:Session, purchase_data: PurchaseCreate, user_id:int) -> Purchase:
    purchase = Purchase(
        user_id = user_id,
        total_price = 0  #lo calculo dsp
    )
    db.add(purchase)
    db.flush()

    # Calcular total_price sumando los tickets
    total = 0
    for ticket_id in purchase_data.ticket_ids:  # asumimos lista de ids
        ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
        if  not ticket:
            raise HTTPException(
                status_code = 404,
                detail = f"Ticket {ticket_id} not found"
            )
        total += ticket.price
        ticket.purchase_id = purchase.id

    purchase.total_price = total
    db.commit()
    db.refresh(purchase)
    return purchase

def get_all_purchases(db: Session) -> List[Purchase]:
    return db.query(Purchase).all()

def get_purchase_by_id(db: Session, purchase_id: int) -> Purchase | None:
    return db.query(Purchase).filter(Purchase.id == purchase_id).first()

def get_purchases_by_user(db: Session, user_id: int) -> List[Purchase]:
    return db.query(Purchase).filter(Purchase.user_id == user_id).all()
