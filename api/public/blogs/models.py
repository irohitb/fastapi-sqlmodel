

from pydantic.types import Optional
from sqlmodel import SQLModel, Field

class BlogBase(SQLModel): 
    title: str
    # author:str = Field(default=None, foreign_key="author.id")
    body: str

class Blog(BlogBase, table=True): 
    id: int = Field(default=None, primary_key=True)

class BlogCreate(BlogBase): 
    pass

class BlogUpdate(BlogBase):
    title: Optional[str] = None
    body: Optional[str] = None
