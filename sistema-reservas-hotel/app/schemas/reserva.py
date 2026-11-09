from datetime import date
from pydantic import BaseModel
from pydantic import BaseModel, Field


class ReservaCreate(BaseModel):
    hospede_id: int
    quarto_id: int
    adultos: int = Field(ge=1)
    criancas: int = Field(ge=0, le=4)
    check_in: date
    check_out: date
    cupom: str | None = None