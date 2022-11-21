from fastapi import APIRouter
from api.public.blogs import views as blogs

api = APIRouter()


api.include_router(blogs.router, prefix="/blogs", tags=["blogs"])



