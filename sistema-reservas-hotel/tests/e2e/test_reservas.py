
import pytest
from datetime import date, timedelta
from playwright.sync_api import expect

from tests.e2e.pages.hospedes_page import HospedesPage
from tests.e2e.pages.reservas_page import ReservasPage


@pytest.mark.e2e
def test_realizar_reserva_pela_interface(page, server_url):
    # Primeiro, cadastra um hóspede pela interface.
    hospedes = HospedesPage(page)
    hospedes.abrir(server_url)

    hospedes.cadastrar(
        nome="João da Silva",
        email="joao@email.com",
        telefone="13988888888",
        documento="98765432100"
    )

    expect(page.get_by_role("status")).to_contain_text(
        "Hóspede cadastrado com sucesso!"
    )

    # Depois, realiza a reserva.
    reservas = ReservasPage(page)
    reservas.abrir(server_url)

    check_in = date.today() + timedelta(days=10)
    check_out = check_in + timedelta(days=2)

    reservas.realizar_reserva(
        hospede_id=1,
        quarto_id=1,
        adultos=1,
        criancas=0,
        check_in=check_in.isoformat(),
        check_out=check_out.isoformat(),
        cupom="HOTEL10"
    )

    expect(page.get_by_role("status")).to_contain_text(
        "Reserva realizada com sucesso!"
    )

    expect(page.locator("#lista-reservas")).to_contain_text(
        "Reserva 1"
    )
