from fastapi import Depends, FastAPI, Form, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from db import crud, models, schemas
from db.database import SessionLocal, engine
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from fastapi.staticfiles import StaticFiles


templates = Jinja2Templates(directory="templates")

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @app.post("/authors/", response_model=schemas.author)
# def create_author(author: schemas.authorCreate, db: Session = Depends(get_db)):
    # return crud.create_author(db=db, author=author)

@app.get("/")
def read_authors(request:Request,skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    authors = crud.get_authors(db, skip=skip, limit=limit)

    return templates.TemplateResponse("authors.html", {"request": request, "authors": authors})
# 
# 
@app.get("/book/get-all/{author_id}")
def read_author(request:Request, author_id: int, db: Session = Depends(get_db)):
    books = crud.get_books_by_author(db, author_id=author_id)
    print(books)
    return templates.TemplateResponse("books.html", {"request": request, "books": books, "author_id": author_id})

@app.get("/book/view/{book_id}")
def read_author(request:Request, book_id: int, db: Session = Depends(get_db)):
    book = crud.get_books_by_author(db, book_id=book_id)
    print(book)
    return templates.TemplateResponse("books_view.html", {"request": request, "book": book, "book_id": book_id})


@app.get("/author/edit/{author_id}")
def get_user(request: Request, author_id: int, db: Session = Depends(get_db)):
    author = crud.get_author(author_id=author_id, db=db)

    return templates.TemplateResponse("edit.html", {"request": request, "author": author})

@app.post("/author/edit/{author_id}")
def edit_author(author_id: int, db: Session = Depends(get_db), name: str = Form()):
    author = schemas.Author(id=author_id, name=name)
    crud.update_author(user=author, db=db)

    return RedirectResponse("/", status_code=303)

#@app.get("/book/delete/{user_id}")
#def delete_item(book_id: int, db: Session = Depends(get_db)):
#    crud.delete_user(user_id=user_id, db=db)
#
#    return RedirectResponse("/", status_code=303)



