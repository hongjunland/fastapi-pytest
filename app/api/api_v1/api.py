from api.api_v1.endpoints import posts
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(posts.router, prefix='/posts',tags=['posts'])