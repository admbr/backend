from fastapi import APIRouter, HTTPException, status
from app.api.v1.endpoints import moradores

api_router = APIRouter()
api_router.include_router(moradores.router, prefix="/moradores", tags=["Moradores"])
