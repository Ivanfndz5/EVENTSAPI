from sqlalchemy import Column, Float,Integer,String,ForeignKey,DateTime
from sqlalchemy.orm import Relationship, relationship
from datetime import datetime
from app.core.database import Base

class Purchase(Base):
    __tablename__ = 'purchases'

    id = Column(Integer, primary_key=True,index=True)
    user_id = Column(Integer,ForeignKey('users.id'),nullable=False)
    total_price = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    tickets = relationship('Ticket', back_populates='purchase')
    user = relationship('User', back_populates='purchases')