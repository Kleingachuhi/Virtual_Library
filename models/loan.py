from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from models.base import Base
from sqlalchemy.orm import relationship
from datetime import datetime

class Loan(Base):
    __tablename__ = 'loans'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    book_title = Column(String, nullable=False)     # New
    username = Column(String, nullable=False)       # New
    borrowed_at = Column(DateTime, default=datetime.utcnow)
    returned_at = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="loans")
    book = relationship("Book", back_populates="loans")
