from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base


class User(Base):
    __tablename__ ='users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    card_number = Column(String(6), unique= True, nullable=False)
    loans = relationship("Loan", back_populates="user")