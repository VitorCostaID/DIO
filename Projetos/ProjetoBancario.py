'''
[1] Extrato
[2] Saque
[3] Depósito
[4] Sair
'''
saldo = 0
request = 0
sistema = 0
c = 0

print("""Digite a operação desejada:  
        [1] Extrato
        [2] Saque
        [3] Depósito
        [4] Sair
        """)

                        
while sistema != 4:
    try:
        if c == 0:
            sistema = int(input(""))
        else:
            sistema = int(input("Digite uma nova operação: "))

        if sistema == 1:
            print(f"O valor do seu saldo atual é de: {saldo}")

        elif sistema == 2:
            request = int(input("Digite a quantidade que deseja sacar: "))
            if saldo > request:
                    saldo = saldo - request
            else:
                print("Saldo insuficiente!") # Caso não tenha saldo

        elif sistema == 3:
            valor = -1 # Variável para começar o loop
            while valor < 0:
                valor = int(input("Digite a quantidade que deseja depositar: "))
                if valor > 0:
                    saldo += valor
                else:
                    print("Valor a depositar não pode ser negativo!") # Caso o valor seja negativo
        
        elif sistema == 4:
            break
        c += 1

    except ValueError:
        print("Valor inserido inválido!")