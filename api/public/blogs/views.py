from fastapi import APIRouter, Depends, Query
from pydantic.types import List
from sqlmodel import Session
from api.database import get_session

from api.public.blogs.controller import (
    get_blogs,
    get_blog,
    create_blog,
    update_blog
)

from api.public.blogs.models import (
    Blog,
    BlogCreate
)

router = APIRouter()

@router.get("", response_model=List[Blog])
def get_all_blogs(db: Session = Depends(get_session)):
    result = get_blogs(db)
    return result

@router.get("/{blog_id}")
def get_blog_post(blog_id:int, db: Session = Depends(get_session)):
    return get_blog(blog_id, db)


@router.post("/")
def create_blog_post(blog: BlogCreate, db: Session = Depends(get_session)):
    result = create_blog(blog, db)
    return result


@router.patch("/{blog_id}")
def update_blog_content(blog_id: int, blog:BlogCreate, session:Session = Depends(get_session)):
    new_blog = update_blog(blog_id, blog, session)
    return new_blog
    
    