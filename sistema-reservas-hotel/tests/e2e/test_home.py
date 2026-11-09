import pytest

from tests.e2e.pages.home_page import HomePage


@pytest.mark.e2e
def test_carregar_pagina_inicial(page, server_url):
    # Arrange
    home = HomePage(page)

    # Act
    home.abrir(server_url)

    # Assert
    assert home.titulo_principal().is_visible()
    assert page.get_by_role(
        "heading",
        name="Bem-vindo!",
        level=2
    ).is_visible()


@pytest.mark.e2e
def test_navegar_para_pagina_de_hospedes(page, server_url):
    # Arrange
    home = HomePage(page)
    home.abrir(server_url)

    # Act
    home.link_hospedes().click()

    # Assert
    assert page.url.endswith("/pagina-hospedes")