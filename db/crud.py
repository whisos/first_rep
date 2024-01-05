from sqlalchemy.orm import Session
from . import models, schemas


def get_author(db: Session, author_id: int):
    return db.query(models.Author).filter(models.Author.id == author_id).first()

def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()



def get_authors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Author).offset(skip).limit(limit).all()


def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.Author(
    name = author.name)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def get_books_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()

def get_books_by_author(db: Session, author_id: int):
    return db.query(models.Book).filter(models.Book.author_id == author_id).all()


def create_author_book(db: Session, book: schemas.BookCreate, author_id: int):
    db_book = models.Book(**book.dict(), parent_id=author_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def update_author(db: Session, author: schemas.Author):
    db_author = db.query(models.User).filter(models.Author.id == author.id).first()
    if db_author:
        db_author.name = author.name
        db.commit()
        db.refresh(db_author)
       

#def delete_author(db: Session, user_id: int):
#    db_user = db.query(models.User).filter(models.User.id == user_id).first()
#    if db_user:
#        db.delete(db_user)
#        db.commit()


