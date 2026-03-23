from pydantic import BaseModel, ConfigDict
from datetime import datetime
from app.schemas.ticket import TicketResponse

class PurchaseCreate(BaseModel):
    user_id : int
    ticket_ids : list[int]


#lo que devolvemos como respuesta

class PurchaseResponse(BaseModel):
    id : int
    user_id : int
    total_price : float
    created_at : datetime
    tickets: list[TicketResponse] #lista de tickets generados

    model_config = ConfigDict(from_attributes=True)