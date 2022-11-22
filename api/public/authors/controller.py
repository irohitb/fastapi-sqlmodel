from sqlalchemy import select
from api.public.authors.models import Author, AuthorCreate, AuthorUpdate
from sqlmodel import Session
from fastapi import Depends, HTTPException, status
from api.database import get_session


def create_author(author: AuthorCreate, session: Session = Depends(get_session)): 
    result = Author(name=author.name, email=author.email)
    session.add(result)
    session.commit()
    session.refresh(result)
    return result


def get_authors(session:Session = Depends(get_session)):
    result = session.execute(select(Author))
    authors = result.scalars().all()
    return authors

def get_author(id: int, session:Session = Depends(get_session)):
    result = session.get(Author, id)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Author with id {id} not found"
        )
    return result

def update_author(id: int, author: AuthorUpdate, session:Session = Depends(get_session)): 
    author_db = get_author(id, session)
    author_data = author.dict(exclude_unset=True)
    for key, value in author_data.items():
        setattr(author_db, key, value)
    session.add(author_db)
    session.commit()
    session.refresh(author_db)
    return author_db
    
    