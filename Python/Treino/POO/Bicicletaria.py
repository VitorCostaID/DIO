import time

class Bicicleta:
    def __init__ (self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim plim")

    def parar(self):
        print("Parando bicicleta...")
        time.sleep(1)
        print("Bicicleta parada!")

    def pedalar(self):
        print("Vruummm")

b1 = Bicicleta("Laranja", "colli", 2019, 545.60)

b1.pedalar()
time.sleep(2)
b1. parar()