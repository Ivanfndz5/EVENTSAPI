from sqlalchemy import Integer, Float, String, DateTime, Column
from sqlalchemy.orm import relationship

from app.core.database import Base

class Event(Base):
    __tablename__= 'events'

    id = Column(Integer, primary_key=True, index= True)

    title = Column(String, index = True, nullable = False)
    description = Column(String)
    date = Column(DateTime,nullable= False)
    place = Column(String, nullable= False)
    capacity = Column(Integer, nullable=False)

    tickets = relationship('Ticket', back_populates='event')
