from datetime import datetime

saldo = 0
request = 0
sistema = 0
c = 0
transacoes = 0
cpf_busca = 0
numero_clientes = 0
hoje = datetime.now().strftime("%d/%m/%Y")


extrato = []
clientes = []
contas = []

def checar_conta():
    cpf = input("Digite o CPF: ")  # Get CPF before checking

    while not any(cliente[2] == cpf for cliente in clientes):    
        print("CPF inserido inválido, por favor crie um cliente para este CPF ou insira um existente.")
        cpf = input("Digite o CPF novamente: ")

    senha = input("Digite a senha de login: ")

    return senha, cpf

    return senha, cpf

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

def mostrar_extrato():
    print("==================== EXTRATO ====================")
    print(f"- Transações dia {hoje} -")
    if any(t["data"] == hoje for t in extrato):
        for t in extrato:
            print(f"{t['hora']} - Tipo: {t['tipo']} - Valor: {t['valor']} - Saldo: {t['saldo']}")
    else: 
        print("Nenhuma transação foi realizada hoje.")
    print("=================================================")

def criar_cliente():
    nome = input("Digite o nome do cliente: ")
    data_de_nascimento = input("Digite a data de nascimento do cliente: ")
    cpf = -1

    while not any(cliente[2] == cpf for cliente in clientes): 
        cpf = input("Digite o cpf do cliente: ")
        if not any(cliente[2] == cpf for cliente in clientes):
            print("CPF inserido já existe, por favor insira um novo CPF, ou prossiga para criar uma conta.")

    endereco = input("Digite o endereço do cliente: ")
    clientes.append([nome, data_de_nascimento, cpf, endereco])

def criar_conta(numero_clientes):
    numero_clientes += 1
    digito_conta = "0001-" + numero_clientes
    saldo = 0

    senha, cpf = checar_conta()

    contas.append([cpf, digito_conta, saldo, senha])

def logar_conta():
    senha, cpf = checar_conta()

    for conta in contas:  
        if conta[0] == cpf:  # Checar o cpf  
            if conta[3] == senha:  # Checar a senha 
                print("Login bem-sucedido!")  
            else:  
                print("Senha incorreta.")  
                break  
        else:  
            print("CPF não encontrado.") 




print("""Digite a operação desejada:  
        [1] Extrato
        [2] Saque
        [3] Depósito
        [4] Sair
        [cc] Criar Conta
        [ag] Cadastrar Agência
        """)


                        
while sistema != 4: # [Sistema bancário]
    try:
        if c == 0: # [Mensagem]
            sistema = input("")
        else:
            sistema = input("Digite uma nova operação: ")

        if sistema == 1: # [Extrato]
            mostrar_extrato()

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

        elif sistema == "cc": # [Criar Conta]
            criar_conta()

        elif sistema == "cl": # [Cadastrar Cliente]
            criar_cliente(numero_clientes)

        elif sistema == "e": # [Entrar na conta]
            logar_conta()

        c += 1

    except ValueError:
        print("Valor inserido inválido!")