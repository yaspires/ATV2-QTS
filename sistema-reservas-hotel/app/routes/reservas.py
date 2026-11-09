from fastapi import APIRouter, HTTPException
from app.data.reservas import reservas
from app.schemas.reserva import ReservaCreate
from app.data.quartos import quartos
from app.data.hospedes import hospedes
from datetime import date
from app.services.calculo_reserva import calcular_valor_reserva

router = APIRouter()


@router.get("/reservas")
def listar_reservas():
    return reservas

@router.post("/reservas")
def cadastrar_reserva(reserva: ReservaCreate):
    if reserva.check_in <= date.today():
        return {"erro": "A data de check-in deve ser futura."}

    if reserva.check_out <= reserva.check_in:
        return {"erro": "A data de check-out deve ser posterior ao check-in."}

    noites = (reserva.check_out - reserva.check_in).days

    if noites > 30:
        return {"erro": "A hospedagem não pode ultrapassar 30 noites."}

    hospede = next(
        (hospede for hospede in hospedes if hospede["id"] == reserva.hospede_id),
        None
    )

    if hospede is None:
        return {"erro": "Hóspede não encontrado."}

    quarto = next(
        (quarto for quarto in quartos if quarto["id"] == reserva.quarto_id),
        None
    )

    if quarto is None:
        return {"erro": "Quarto não encontrado."}

    total_hospedes = reserva.adultos + reserva.criancas

    if total_hospedes > quarto["capacidade"]:
        return {"erro": "Quantidade de hóspedes excede a capacidade do quarto."}

    for reserva_existente in reservas:
        if reserva_existente["quarto_id"] == reserva.quarto_id:
            if reserva_existente["status"] == "ativa":
                if (
                    reserva.check_in < reserva_existente["check_out"]
                    and reserva.check_out > reserva_existente["check_in"]
                ):
                    return {"erro": "Quarto indisponível para o período informado."}

    nova_reserva = reserva.model_dump()
    nova_reserva["id"] = len(reservas) + 1
    nova_reserva["status"] = "ativa"

    nova_reserva["valor_total"] = calcular_valor_reserva(
        quarto["preco_diaria"],
        reserva.criancas,
        noites,
        reserva.cupom
    )

    reservas.append(nova_reserva)

    return nova_reserva

@router.get("/reservas/{reserva_id}")
def consultar_reserva(reserva_id: int):
    reserva = next(
        (reserva for reserva in reservas if reserva["id"] == reserva_id),
        None
    )

    if reserva is None:
        raise HTTPException(
            status_code=404,
            detail="Reserva não encontrada."
        )

    return reserva

@router.delete("/reservas/{reserva_id}")
def cancelar_reserva(reserva_id: int):
    reserva = next(
        (reserva for reserva in reservas if reserva["id"] == reserva_id),
        None
    )

    if reserva is None:
        raise HTTPException(
            status_code=404,
            detail="Reserva não encontrada."
        )

    if reserva["status"] == "cancelada":
        raise HTTPException(
            status_code=400,
            detail="Esta reserva já está cancelada."
        )

    reserva["status"] = "cancelada"

    return {
        "mensagem": "Reserva cancelada com sucesso.",
        "reserva": reserva
    }