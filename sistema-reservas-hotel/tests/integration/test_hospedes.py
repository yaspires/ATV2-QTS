from tests.factories.hospede_factory import HospedeFactory
import pytest


@pytest.mark.integration
def test_listar_hospedes_sem_cadastro(client):
    # Arrange
    # A fixture já prepara a aplicação sem hóspedes cadastrados.

    # Act
    resposta = client.get("/hospedes")

    # Assert
    assert resposta.status_code == 200
    assert resposta.json() == []


@pytest.mark.integration
def test_cadastrar_hospede_com_sucesso(client):
    # Arrange
    dados_hospede = {
        "nome": "Maria da Silva",
        "email": "maria@email.com",
        "telefone": "13999999999",
        "documento": "12345678900"
    }

    # Act
    resposta = client.post("/hospedes", json=dados_hospede)

    # Assert
    assert resposta.status_code == 200
    assert resposta.json()["nome"] == "Maria da Silva"
    assert resposta.json()["email"] == "maria@email.com"
    assert resposta.json()["id"] == 1

@pytest.mark.integration
def test_cadastrar_hospede_com_dados_faker(client):
    # Arrange
    dados_hospede = HospedeFactory.criar()

    # Act
    resposta = client.post("/hospedes", json=dados_hospede)

    # Assert
    assert resposta.status_code == 200
    assert resposta.json()["nome"] == dados_hospede["nome"]
    assert resposta.json()["email"] == dados_hospede["email"]
    assert resposta.json()["id"] == 1

    