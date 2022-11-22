from fastapi import APIRouter, Depends, Query
from pydantic.types import List
from sqlmodel import Session
from api.database import get_session

from api.public.authors.controller import (
    get_authors,
    get_author,
    create_author,
    update_author
)

from api.public.authors.models import (
    Author,
    AuthorCreate
)

router = APIRouter()

@router.get("", response_model=List[Author])
def get_all_authors(db: Session = Depends(get_session)):
    result = get_authors(db)
    return result

@router.get("/{author_id}")
def get_author_post(author_id:int, db: Session = Depends(get_session)):
    return get_author(author_id, db)


@router.post("/")
def create_author_post(author: AuthorCreate, db: Session = Depends(get_session)):
    result = create_author(author, db)
    return result


@router.patch("/{author_id}")
def update_author_content(author_id: int, author:AuthorCreate, session:Session = Depends(get_session)):
    new_author = update_author(author_id, author, session)
    return new_author
    
    