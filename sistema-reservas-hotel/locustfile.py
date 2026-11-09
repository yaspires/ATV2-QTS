
from locust import HttpUser, task, between


class HotelUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def acessar_pagina_inicial(self):
        self.client.get("/")

    @task
    def listar_quartos(self):
        self.client.get("/quartos")

    @task
    def listar_hospedes(self):
        self.client.get("/hospedes")

    @task
    def listar_reservas(self):
        self.client.get("/reservas")
