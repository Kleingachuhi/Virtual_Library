from sqlalchemy import Column, Integer, ForeignKey, DateTime
from models.base import Base
from datetime import datetime


class Loan(Base):
    __tablename__ ='loans'

    id = Column(Integer,primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    borrowed_at = Column(DateTime, default=datetime.utcnow)
    returned_at = Column(DateTime, nullable=True)