from fastapi import APIRouter, HTTPException, status

router = APIRouter()


@router.get("/")
def read_root():
    return {"message": "Hiii"}
