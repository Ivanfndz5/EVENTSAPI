from pydantic import BaseModel, ConfigDict


class TicketBase(BaseModel):
    event_id : int


class TicketCreate(TicketBase):
    quantity : int
    seat_number : str
    price : float


class TicketResponse(TicketBase):
    id : int
    user_id : int
    seat_number: str
    price: float

    model_config = ConfigDict(from_attributes=True)

