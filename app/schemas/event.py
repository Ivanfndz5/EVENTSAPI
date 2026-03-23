from pydantic import BaseModel, Field , validator
from datetime import datetime
from typing import Optional


class EventBase(BaseModel):
    title : str = Field(...,min_length=1)
    description : Optional[str] = None
    date : datetime
    place : str
    capacity : int = Field(...,gt=0)

class EventCreate(EventBase):
    pass

class EventUpdate(EventBase):
    title: str
    description: str
    date: datetime
    place: str
    capacity: int

    #Validator para aceptar strings tipo ISO desde/docs o Postman
    @validator('date',pre=True)
    def parse_date(cls,v):
        if isinstance(v,str):
            #quitamos la Z si viene en formato ISO con Z
            return datetime.fromisoformat(v.replace('Z', ""))
        return v

class EventResponse(EventBase):
    id: int

    class Config:
        orm_mode = True

