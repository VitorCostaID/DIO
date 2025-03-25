'''
[1] Extrato
[2] Saque
[3] Depósito
[4] Sair
'''
saldo = 0
request = 0
sistema = 0

print("""Digite a operação desejada:  
        [1] Extrato
        [2] Saque
        [3] Depósito
        [4] Sair
        """)

                        
while (sistema != 4):
    try:
        sistema = int(input(""))
        if sistema == 1:
            print(f"O valor do seu saldo atual é de: {saldo}")

        elif sistema == 2:
            request = int(input("Digite a quantidade que deseja sacar: "))
            if saldo > request:
                saldo = saldo - request
            else:
                print("Saldo insuficiente!")

        elif sistema == 3:
            saldo += int(input("Digite a quantidade que deseja depositar: "))

    except ValueError:
        print("Valor inserido inválido!")