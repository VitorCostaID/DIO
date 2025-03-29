from datetime import datetime

saldo = 0
request = 0
sistema = 0
c = 0
transacoes = 0
hoje = datetime.now().strftime("%d/%m/%Y")


extrato = []

def salvar_saque(saldo, request):
    extrato.append({
        "data": datetime.now().strftime("%d/%m/%Y"),
        "hora": datetime.now().strftime("%H:%M:%S"),
        "tipo": "Saque",
        "valor": -request,
        "saldo": saldo 
    })

def salvar_deposito(saldo, valor):
    extrato.append({
        "data": datetime.now().strftime("%d/%m/%Y"),
        "hora": datetime.now().strftime("%H:%M:%S"),
        "tipo": "Depósito",
        "valor": valor,
        "saldo": saldo
    })


print("""Digite a operação desejada:  
        [1] Extrato
        [2] Saque
        [3] Depósito
        [4] Sair
        """)


                        
while sistema != 4: # [Sistema bancário]
    try:
        if c == 0: # [Mensagem]
            sistema = int(input(""))
        else:
            sistema = int(input("Digite uma nova operação: "))

        if sistema == 1: # [Extrato]
            print(f"- Transações dia {hoje} -")
            if any(t["data"] == hoje for t in extrato):
                for t in extrato:
                    print(f"{t['hora']} - Tipo: {t['tipo']} - Valor: {t['valor']} - Saldo: {t['saldo']}")
            else: 
                print("Nenhuma transação foi realizada hoje.")

        elif sistema == 2: # [Saque]
            if sum(1 for t in extrato if t["data"] == hoje) < 10:
                request = int(input("Digite a quantidade que deseja sacar: "))
                if saldo > request:
                        saldo = saldo - request
                        salvar_saque(saldo, request)
                
                else:
                    print("Saldo insuficiente!") # Caso não tenha saldo
            else:
                print("O máximo de transações de hoje já foi sucedida!")

        elif sistema == 3: # [Depósito]
            valor = -1 # Variável para começar o loop
            if sum(1 for t in extrato if t["data"] == hoje) < 10:
                while valor < 0:
                    valor = int(input("Digite a quantidade que deseja depositar: "))
                    if valor > 0:
                            saldo += valor
                            salvar_deposito(saldo, valor)
                        
                    else:
                        print("Valor a depositar não pode ser negativo!") # Caso o valor seja negativo
            else:
                print("O máximo de transações de hoje já foi sucedida!")
            
        elif sistema == 4: # [Sair]
            break
        c += 1

    except ValueError:
        print("Valor inserido inválido!")