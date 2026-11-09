
import pytest
from axe_playwright_python.sync_playwright import Axe
from playwright.sync_api import expect


@pytest.mark.accessibility
def test_acessibilidade_pagina_inicial(page, server_url):
    page.goto(server_url)

    resultado = Axe().run(page)

    assert resultado.violations_count == 0, resultado.generate_report()


@pytest.mark.accessibility
def test_acessibilidade_pagina_hospedes(page, server_url):
    page.goto(f"{server_url}/pagina-hospedes")

    resultado = Axe().run(page)

    assert resultado.violations_count == 0, resultado.generate_report()


@pytest.mark.accessibility
def test_acessibilidade_pagina_reservas(page, server_url):
    page.goto(f"{server_url}/pagina-reservas")

    resultado = Axe().run(page)

    assert resultado.violations_count == 0, resultado.generate_report()


@pytest.mark.accessibility
def test_navegacao_por_teclado(page, server_url):
    page.goto(server_url)

    page.keyboard.press("Tab")

    expect(
        page.get_by_role("link", name="Início", exact=True)
    ).to_be_focused()
