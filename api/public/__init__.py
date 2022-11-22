from fastapi import APIRouter
from api.public.blogs import views as blogs
from api.public.authors import views as authors

api = APIRouter()


api.include_router(blogs.router, prefix="/blogs", tags=["blogs"])
api.include_router(authors.router, prefix="/authors", tags=["authors"])


