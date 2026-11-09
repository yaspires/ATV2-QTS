from fastapi import APIRouter

from app.data.quartos import quartos

router = APIRouter()


@router.get("/quartos")
def listar_quartos():
    return quartos