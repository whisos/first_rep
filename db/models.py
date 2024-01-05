from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base


class Author(Base):
    __tablename__ = "author"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    image = Column(String)
    books = relationship("Book", back_populates="author")


class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    release_date = Column(Integer)
    pages = Column(Integer)
    image = Column(String)
    author_id = Column(Integer, ForeignKey("author.id"))
    
    author = relationship("Author", back_populates="books")

