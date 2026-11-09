
class HospedesPage:
    def __init__(self, page):
        self.page = page

    def abrir(self, url):
        self.page.goto(f"{url}/pagina-hospedes")

    def cadastrar(self, nome, email, telefone, documento):
        self.page.get_by_label("Nome completo:").fill(nome)
        self.page.get_by_label("E-mail:").fill(email)
        self.page.get_by_label("Telefone:").fill(telefone)
        self.page.get_by_label("Documento:").fill(documento)
        self.page.get_by_role(
            "button",
            name="Cadastrar hóspede"
        ).click()
