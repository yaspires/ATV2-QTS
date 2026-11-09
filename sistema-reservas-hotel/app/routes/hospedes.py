from fastapi import APIRouter

from app.data.hospedes import hospedes
from app.schemas.hospede import HospedeCreate

router = APIRouter()


@router.get("/hospedes")
def listar_hospedes():
    return hospedes


@router.post("/hospedes")
def cadastrar_hospede(hospede: HospedeCreate):
    novo_hospede = hospede.model_dump()
    novo_hospede["id"] = len(hospedes) + 1

    hospedes.append(novo_hospede)

    return novo_hospede