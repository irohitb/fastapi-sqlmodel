from pydantic.types import Optional
from sqlmodel import SQLModel, Field,Relationship
from typing import List


class AuthorBase(SQLModel): 
    email: str
    name: str
    

class AuthorCreate(AuthorBase):
    pass

class Author():
    id: int = Field(default=None, primary_key=True)
    blogs: List["Blog"] = Relationship(back_populates="Author")


class AuthorUpdate(AuthorBase):
    name: Optional[str] = None
    