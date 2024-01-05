from pydantic import BaseModel


class BookBase(BaseModel):
    release_date : int
    pages : int
    title: str
    image: str
    description: str | None = None


class BookCreate(BookBase):
    pass

class Book(BookBase):
    id : int
    author_id : int
    
    class Config:
        from_attributes = True


class AuthorBase(BaseModel):
    name: str
    image: str



class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id : int
    book_list : list[Book] = []
    class Config:
        from_attributes = True

