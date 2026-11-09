class HomePage:
    def __init__(self, page):
        self.page = page

    def abrir(self, url):
        self.page.goto(url)

    def titulo_principal(self):
        return self.page.get_by_role(
            "heading",
            name="Sistema de Reservas de Hotel",
            level=1
        )

    def link_hospedes(self):
        return self.page.get_by_role(
            "link",
            name="Hóspedes",
            exact=True
        )

    def link_reservas(self):
        return self.page.get_by_role(
            "link",
            name="Reservas",
            exact=True
        )