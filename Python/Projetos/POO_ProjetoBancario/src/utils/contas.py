class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def realizar_transacao(self, tipo, valor):
        if not self.contas:
            raise Exception("Cliente não possui conta.")
        
        conta = self.contas[0]  # Usa a primeira conta
        if tipo == "d":
            conta.depositar(valor)
        elif tipo == "s":
            conta.sacar(valor)
        else:
            raise Exception("Tipo de transação inválido!")


class Conta:
    def __init__(self, numero, agencia, cliente):
        self._saldo = 0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = []

    def saldo(self):
        print(f"Saldo atual: R${self._saldo:.2f}")

    def sacar(self, valor):
        if valor > self._saldo:
            print("Saldo insuficiente.")
            return False
        self._saldo -= valor
        self.historico.append(f"Saque de R${valor:.2f}")
        print("Saque realizado!")
        return True

    def depositar(self, valor):
        self._saldo += valor
        self.historico.append(f"Depósito de R${valor:.2f}")
        print("Depósito realizado!")
        return True
    

