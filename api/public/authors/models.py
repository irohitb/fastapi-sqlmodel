from pydantic.types import Optional
from sqlmodel import SQLModel, Field,Relationship
from typing import List


class AuthorBase(SQLModel): 
    email: str
    name: str
    

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase, table=True):
    id: int = Field(default=None, primary_key=True)
    email:str = Field(index=True)


class AuthorUpdate(AuthorBase):
    name: Optional[str] = None
    