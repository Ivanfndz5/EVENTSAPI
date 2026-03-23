from sqlalchemy import Column, Integer, DateTime, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from app.core.database import Base
from datetime import datetime


class Ticket(Base):
    __tablename__ = 'tickets'

    id = Column(Integer,primary_key=True, index=True)

    user_id = Column(Integer,ForeignKey('users.id'), nullable=False)
    event_id = Column(Integer, ForeignKey('events.id'),nullable=False)
    purchase_id = Column(Integer, ForeignKey("purchases.id"), nullable=True)
    seat_number = Column(String, nullable=False)
    price = Column(Float,nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow,nullable=False)

    user = relationship('User', back_populates='tickets')
    event = relationship('Event', back_populates='tickets')
    purchase = relationship('Purchase', back_populates='tickets')