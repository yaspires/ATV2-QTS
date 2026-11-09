from pydantic import BaseModel, EmailStr


class HospedeCreate(BaseModel):
    nome: str
    email: EmailStr
    telefone: str
    documento: str