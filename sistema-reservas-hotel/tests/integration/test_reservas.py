from datetime import date, timedelta

import pytest


@pytest.mark.integration
def test_cadastrar_reserva_com_sucesso(client):
    # Arrange: cadastra um hóspede
    dados_hospede = {
        "nome": "Maria da Silva",
        "email": "maria@email.com",
        "telefone": "13999999999",
        "documento": "12345678900"
    }
    resposta_hospede = client.post("/hospedes", json=dados_hospede)
    hospede_id = resposta_hospede.json()["id"]

    amanha = date.today() + timedelta(days=1)
    depois_de_amanha = amanha + timedelta(days=2)

    dados_reserva = {
        "hospede_id": hospede_id,
        "quarto_id": 1,
        "adultos": 1,
        "criancas": 0,
        "check_in": amanha.isoformat(),
        "check_out": depois_de_amanha.isoformat(),
        "cupom": None
    }

    # Act
    resposta = client.post("/reservas", json=dados_reserva)

    # Assert
    assert resposta.status_code == 200
    assert resposta.json()["status"] == "ativa"
    assert resposta.json()["quarto_id"] == 1
    assert resposta.json()["valor_total"] == 400.00


@pytest.mark.integration
def test_impedir_reservas_com_periodos_sobrepostos(client):
    # Arrange: cadastra um hóspede
    dados_hospede = {
        "nome": "João da Silva",
        "email": "joao@email.com",
        "telefone": "13988888888",
        "documento": "98765432100"
    }
    resposta_hospede = client.post("/hospedes", json=dados_hospede)
    hospede_id = resposta_hospede.json()["id"]

    amanha = date.today() + timedelta(days=1)
    checkout = amanha + timedelta(days=3)

    dados_reserva = {
        "hospede_id": hospede_id,
        "quarto_id": 1,
        "adultos": 1,
        "criancas": 0,
        "check_in": amanha.isoformat(),
        "check_out": checkout.isoformat(),
        "cupom": None
    }

    client.post("/reservas", json=dados_reserva)

    # Act: tenta reservar o mesmo quarto em um período sobreposto
    nova_reserva = dados_reserva.copy()
    nova_reserva["check_in"] = (amanha + timedelta(days=1)).isoformat()
    nova_reserva["check_out"] = (checkout + timedelta(days=1)).isoformat()

    resposta = client.post("/reservas", json=nova_reserva)

    # Assert
    assert resposta.status_code == 200
    assert resposta.json()["erro"] == "Quarto indisponível para o período informado."

@pytest.mark.integration
def test_impedir_reserva_com_hospede_inexistente(client):
    amanha = date.today() + timedelta(days=1)

    dados_reserva = {
        "hospede_id": 999,
        "quarto_id": 1,
        "adultos": 1,
        "criancas": 0,
        "check_in": amanha.isoformat(),
        "check_out": (amanha + timedelta(days=2)).isoformat(),
        "cupom": None
    }

    resposta = client.post("/reservas", json=dados_reserva)

    assert resposta.status_code == 200
    assert resposta.json()["erro"] == "Hóspede não encontrado."


@pytest.mark.integration
def test_cancelar_reserva_com_sucesso(client):
    dados_hospede = {
        "nome": "Ana Souza",
        "email": "ana@email.com",
        "telefone": "13977777777",
        "documento": "11122233344"
    }

    resposta_hospede = client.post("/hospedes", json=dados_hospede)
    hospede_id = resposta_hospede.json()["id"]

    amanha = date.today() + timedelta(days=1)

    dados_reserva = {
        "hospede_id": hospede_id,
        "quarto_id": 1,
        "adultos": 1,
        "criancas": 0,
        "check_in": amanha.isoformat(),
        "check_out": (amanha + timedelta(days=2)).isoformat(),
        "cupom": None
    }

    reserva = client.post("/reservas", json=dados_reserva).json()

    resposta = client.delete(f"/reservas/{reserva['id']}")

    assert resposta.status_code == 200
    assert resposta.json()["reserva"]["status"] == "cancelada"

    
@pytest.mark.integration
def test_falha_no_calculo_impede_cadastro_da_reserva(client, mocker):
    dados_hospede = {
        "nome": "João Silva",
        "email": "joao@email.com",
        "telefone": "13988888888",
        "documento": "98765432100"
    }

    hospede = client.post("/hospedes", json=dados_hospede).json()

    amanha = date.today() + timedelta(days=1)

    dados_reserva = {
        "hospede_id": hospede["id"],
        "quarto_id": 1,
        "adultos": 1,
        "criancas": 0,
        "check_in": amanha.isoformat(),
        "check_out": (amanha + timedelta(days=2)).isoformat(),
        "cupom": None
    }

    mocker.patch(
        "app.routes.reservas.calcular_valor_reserva",
        side_effect=ValueError("Falha simulada no cálculo")
    )

    with pytest.raises(ValueError):
        client.post("/reservas", json=dados_reserva)

    assert client.get("/reservas").json() == []


@pytest.mark.integration
def test_calcular_valor_reserva_com_mock_de_sucesso(client, mocker):
    # Arrange
    dados_hospede = {
        "nome": "Carlos Lima",
        "email": "carlos@email.com",
        "telefone": "13966666666",
        "documento": "55544433322"
    }
    hospede = client.post("/hospedes", json=dados_hospede).json()

    amanha = date.today() + timedelta(days=1)

    dados_reserva = {
        "hospede_id": hospede["id"],
        "quarto_id": 1,
        "adultos": 1,
        "criancas": 0,
        "check_in": amanha.isoformat(),
        "check_out": (amanha + timedelta(days=2)).isoformat(),
        "cupom": None
    }

    mocker.patch(
        "app.routes.reservas.calcular_valor_reserva",
        return_value=360.00
    )

    # Act
    resposta = client.post("/reservas", json=dados_reserva)

    # Assert
    assert resposta.status_code == 200
    assert resposta.json()["status"] == "ativa"
    assert resposta.json()["valor_total"] == 360.00
