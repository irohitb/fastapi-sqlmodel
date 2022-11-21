import select

from api.public.blogs.models import Blog, BlogCreate
from sqlmodel import Session
from fastapi import Depends, HTTPException, status
from api.database import get_session


def create_blog(blog: BlogCreate, session: Session = Depends(get_session)): 
    result = Blog(title=blog.title, body=blog.body)
    session.add(result)
    session.commit()
    session.refresh(result)
    return result


def get_blogs(session:Session = Depends(get_session)):
    result = session.execute(select(Blog)).scalars().all()
    return result

def get_blog(id: int, session:Session = Depends(get_session)):
    result = session.get(Blog, id)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Blog with blog id {id} not found"
        )
    return result

