from faker import Faker

fake = Faker("pt_BR")


class HospedeFactory:

    @staticmethod
    def criar():
        return {
            "nome": fake.name(),
            "email": fake.email(),
            "telefone": fake.phone_number(),
            "documento": fake.cpf()
        }