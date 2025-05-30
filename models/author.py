from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base 

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birth_year = Column(String, nullable=False)

    books = relationship("Book", back_populates='author')

