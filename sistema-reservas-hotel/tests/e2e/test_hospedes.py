
import pytest
from playwright.sync_api import expect

from tests.e2e.pages.hospedes_page import HospedesPage


@pytest.mark.e2e
def test_cadastrar_hospede_pela_interface(page, server_url):
    hospedes = HospedesPage(page)
    hospedes.abrir(server_url)

    hospedes.cadastrar(
        nome="Maria da Silva",
        email="maria@email.com",
        telefone="13999999999",
        documento="12345678900"
    )

    expect(page.get_by_role("status")).to_contain_text(
        "Hóspede cadastrado com sucesso!"
    )

    expect(page.locator("#lista-hospedes")).to_contain_text(
        "Maria da Silva"
    )
