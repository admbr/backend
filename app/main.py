from fastapi import FastAPI
from app.routers.api import router

app = FastAPI(title="test", version="1.0.0")

app.include_router(router=router, prefix="/api")
