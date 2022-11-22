

from pydantic.types import Optional
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, ForeignKey, Integer, Table
from api.public.authors.models import Author
class BlogBase(SQLModel): 
    title: str
    # author:str = Field(default=None, foreign_key="author.id")
    body: str
    author:Author = Field(default=None, foreign_key="author.id")
    

class Blog(BlogBase, table=True): 
    id: int = Field(default=None, primary_key=True)
    author_id:Author= Relationship(back_populates="blog")

class BlogCreate(BlogBase): 
    pass

class BlogUpdate(BlogBase):
    title: Optional[str] = None
    body: Optional[str] = None
