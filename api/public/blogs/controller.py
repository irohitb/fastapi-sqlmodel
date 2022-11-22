from sqlalchemy import select, exc
from api.public.blogs.models import Blog, BlogCreate, BlogUpdate
from sqlmodel import Session
from fastapi import Depends, HTTPException, status
from api.database import get_session


def create_blog(blog: BlogCreate, session: Session = Depends(get_session)): 
    try:
        result = Blog(title=blog.title, body=blog.body, author_id=blog.author_id)
        session.add(result)
        session.commit()
        session.refresh(result)
    except exc.IntegrityError: 
        print("Exc Integrity", exc.IntegrityError)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Author with {blog.author_id} not found"
        )
    except: 
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"Something went wrong"
        )
    return result



def get_blogs(session:Session = Depends(get_session)):
    result = session.execute(select(Blog))
    blogs = result.scalars().all()
    return blogs

def get_blog(id: int, session:Session = Depends(get_session)):
    result = session.get(Blog, id)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Blog with blog id {id} not found"
        )
    return result

def update_blog(id: int, blog: BlogUpdate, session:Session = Depends(get_session)): 
    blog_db = get_blog(id, session)
    blog_data = blog.dict(exclude_unset=True)
    for key, value in blog_data.items():
        setattr(blog_db, key, value)
    session.add(blog_db)
    session.commit()
    session.refresh(blog_db)
    return blog_db
    
    