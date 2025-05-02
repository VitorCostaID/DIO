from datetime import datetime
import time

saldo = 0
request = 0
sistema = 0
transacoes = 0
cpf_busca = "000.000.000-00"
numero_clientes = 0

extrato = []
clientes = [{"nome": "Teste", "data_de_nascimento": "00/00/00", "cpf": "000.000.000-00", "endereço": "Brasil"}]
contas = [{"cpf": "000.000.000-00", "digito_conta": 0, "senha": "123", "saldo": 0}]
c = 0
hoje = datetime.now().strftime("%d/%m/%Y")

def checar_conta():
    cpf = input("Digite o CPF: ")

    if not any(cliente["cpf"] == cpf for cliente in clientes):
        print("CPF inserido inválido, por favor crie um cliente para este CPF ou insira um existente.")
        time.sleep(1)
        return None, None  

    senha = input("Digite a senha de login: ")
    time.sleep(0.5)
    return senha, cpf

def salvar_saque(cpf_busca, request):
    saldo_apos_saque = None # Redefinindo a variável para cada chamada da função
    for conta in contas:
        if conta["cpf"] == cpf_busca:
            conta["saldo"] -= request
            saldo_apos_saque = conta["saldo"]
            break
    
    extrato.append({
        "cpf": cpf_busca,
        "data": datetime.now().strftime("%d/%m/%Y"),
        "hora": datetime.now().strftime("%H:%M:%S"),
        "tipo": "Saque",
        "valor": -request,
        "saldo": saldo_apos_saque 
    })
      
def salvar_deposito(cpf_busca, valor):
    saldo_apos_deposito = None # Redefinindo a variável para cada chamada da função
    for conta in contas:
        if conta["cpf"] == cpf_busca:
            conta["saldo"] += valor
            saldo_apos_deposito = conta["saldo"]
            break  
    
    extrato.append({
        "cpf": cpf_busca,
        "data": datetime.now().strftime("%d/%m/%Y"),
        "hora": datetime.now().strftime("%H:%M:%S"),
        "tipo": "Depósito",
        "valor": valor,
        "saldo": saldo_apos_deposito
    })

def obter_saldo(cpf_busca, lista_de_contas):
    for conta in lista_de_contas:
        if conta.get("cpf") == cpf_busca:
            return conta.get("saldo")

def mostrar_extrato():
    print("==================== EXTRATO ====================")
    print(f"- Transações dia {hoje} -")

    transacoes_do_usuario_hoje = [t for t in extrato if t["cpf"] == cpf_busca and t["data"] == hoje] # Conta as transações do usuário logado.

    if transacoes_do_usuario_hoje: # Se transações for >0
        for t in transacoes_do_usuario_hoje: # Display das transações do usuário logado.
            print(f"{t['hora']} - Tipo: {t['tipo']} - Valor: {t['valor']} - Saldo: {t['saldo']}")
    else:
        print("Nenhuma transação foi realizada hoje para esta conta.")

    print("=================================================")

def criar_cliente():
    nome = input("Digite o nome do cliente: ")
    data_de_nascimento = input("Digite a data de nascimento do cliente: ")
    cpf = 0

    while True:
        cpf = input("Digite o CPF do cliente: ")
    
        if any(cliente["cpf"] == cpf for cliente in clientes):  
            print("CPF já cadastrado! Insira um novo CPF ou prossiga para criar uma conta.")  
        else:
            break

    endereco = input("Digite o endereço do cliente: ")
    clientes.append({"nome": nome, "data_de_nascimento": data_de_nascimento, "cpf": cpf, "endereço": endereco})

def criar_conta(numero_clientes):
    numero_clientes += 1
    digito_conta = "0001-" + str(numero_clientes)
    senha, cpf = checar_conta()  
    if cpf:  # Verifica se um CPF válido foi inserido
        nova_conta = {"cpf": cpf, "digito_conta": digito_conta, "senha": senha, "saldo": 0.0}
        contas.append(nova_conta)
        print(f"Conta {digito_conta} criada para o CPF {cpf}.")
        time.sleep(1)
        return numero_clientes
    else:
        return numero_clientes

def logar_conta():
    senha, cpf = checar_conta()  
    if cpf:
        for conta in contas:
            if conta["cpf"] == cpf:
                if conta["senha"] == senha:
                    print("Login bem-sucedido!")
                    time.sleep(1)
                    return cpf
                else:
                    print("Senha incorreta.")
                    time.sleep(1)
                    return None
        print("CPF não encontrado.")
        time.sleep(1)
        return None
    else:
        return None

def buscar_nome_por_cpf(cpf):
    for cliente in clientes:
        if cliente.get("cpf") == cpf:
            return cliente.get("nome")
    return None

                   
while sistema != 4: # [Sistema bancário]
    #Mensagem
    print("""Digite a operação desejada:  
        [1] Extrato
        [2] Saque
        [3] Depósito
        [4] Sair
        [cl] Criar Cliente
        [cc] Criar Conta
        [e] Entrar na conta
        """)
    
    try:
        if c == 0: # [Mensagem]
            sistema = input("")
            c += 1
        else:
            sistema = input("Digite uma nova operação: ")

        if sistema == "e": # [Entrar na conta]
            login = logar_conta()

            if login is not None and login != cpf_busca:
                cpf_busca = login
                nome_cliente = buscar_nome_por_cpf(cpf_busca)
                if nome_cliente:
                    print(f"Bem-vindo(a), {nome_cliente}")
                else:
                    print("CPF encontrado, mas nome não localizado.")
            else:
                print("Falha ao logar.")
                time.sleep(1)

        elif sistema == "1": # [Extrato]
            mostrar_extrato()
            print("Prosseguir? (s) Sim")
            while True:
                pross = input("").lower()
                if pross == "s":
                    break

        elif sistema == "2": # [Saque]
            if any(conta.get("cpf") == cpf_busca for conta in contas):

                if sum(1 for t in extrato if t["data"] == hoje) < 10:
                    request = int(input("Digite a quantidade que deseja sacar: "))
                    saldo = obter_saldo(cpf_busca, contas)
                    
                    if saldo > request:
                            salvar_saque(cpf_busca, request)
                            print("Transação sucedida!")
                            time.sleep(1)
                    
                    else:
                        print("Saldo insuficiente!\n") # Caso não tenha saldo
                        time.sleep(1)

                else:
                    print("O máximo de transações de hoje já foi sucedida!\n")
                    time.sleep(1)

            else:
                print("Logue em alguma conta antes de fazer uma operação.\n")
                time.sleep(1)

        elif sistema == "3": # [Depósito]
            
            if cpf_busca:
                if any(conta["cpf"] == cpf_busca for conta in contas):
                    while True:
                        valor = int(input("Digite a quantidade que deseja depositar: "))
                        if valor > 0:
                            salvar_deposito(cpf_busca, valor)
                            print("Transação sucedida!")
                            time.sleep(1)
                            break
                        else:
                            print("Valor a depositar não pode ser negativo!\n") # Caso o valor seja negativo
                            time.sleep(1)
                else:
                    print("Conta não encontrada.\n")
                    time.sleep(1)
            else:
                print("Por favor, logue na sua conta para fazer um depósito.\n")
                time.sleep(1)
            
        elif sistema == "4": # [Sair do sistema]
            print("Saindo do sistema...")
            time.sleep(1)
            break

        elif sistema == "cc": # [Criar Conta]
            numero_clientes = criar_conta(numero_clientes)

        elif sistema == "cl": # [Cadastrar Cliente]
            criar_cliente()
        

    except ValueError:
        print("Valor inserido inválido!")