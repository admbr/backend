from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.src.database import init_db
from app.api.v1.api import api_router
from app import models


@asynccontextmanager
async def lifspan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(title="test", version="1.0.0")

app.include_router(router=api_router, prefix="/api/v1")
