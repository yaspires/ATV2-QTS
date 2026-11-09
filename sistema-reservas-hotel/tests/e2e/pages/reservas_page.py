
class ReservasPage:
    def __init__(self, page):
        self.page = page

    def abrir(self, url):
        self.page.goto(f"{url}/pagina-reservas")

    def realizar_reserva(
        self,
        hospede_id,
        quarto_id,
        adultos,
        criancas,
        check_in,
        check_out,
        cupom=""
    ):
        self.page.get_by_label("Hóspede:").select_option(
            value=str(hospede_id)
        )
        self.page.get_by_label("Quarto:").select_option(
            value=str(quarto_id)
        )
        self.page.get_by_label("Quantidade de adultos:").fill(
            str(adultos)
        )
        self.page.get_by_label("Quantidade de crianças:").fill(
            str(criancas)
        )
        self.page.get_by_label("Check-in:").fill(check_in)
        self.page.get_by_label("Check-out:").fill(check_out)
        self.page.get_by_label("Cupom promocional (opcional):").fill(
            cupom
        )

        self.page.get_by_role(
            "button",
            name="Realizar reserva"
        ).click()
