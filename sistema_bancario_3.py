# Sistema Bancário Simples
saldo = 0.0
limite_saque_diario = 500.0
saques_realizados = 0
MAX_SAQUES_DIARIOS = 3
extrato = []

print("Bem-vindo ao Sistema Bancário!")

while True:
    print("\nMenu:")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Ver Extrato")
    print("4 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    # Opção 1: Depositar
    if opcao == "1":
        try:
            valor = float(input("Digite o valor do depósito: "))
            if valor > 0:
                saldo += valor
                extrato.append(f"Depósito: R$ {valor:.2f}")
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("O valor do depósito deve ser positivo.")
        except ValueError:
            print("Valor inválido. Digite um número.")
    
    # Opção 2: Sacar
    elif opcao == "2":
        try:
            valor = float(input("Digite o valor do saque: "))
            
            if valor <= 0:
                print("O valor do saque deve ser positivo.")
            elif valor > saldo:
                print("Saldo insuficiente para realizar o saque.")
            elif valor > limite_saque_diario:
                print(f"O valor excede o limite de R$ {limite_saque_diario:.2f} por saque.")
            elif saques_realizados >= MAX_SAQUES_DIARIOS:
                print("Limite diário de saques atingido.")
            else:
                saldo -= valor
                saques_realizados += 1
                extrato.append(f"Saque: R$ {valor:.2f}")
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        except ValueError:
            print("Valor inválido. Digite um número.")
    
    # Opção 3: Ver Extrato
    elif opcao == "3":
        print("\nExtrato Bancário:")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            for movimento in extrato:
                print(movimento)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
    
    # Opção 4: Sair
    elif opcao == "4":
        print("Obrigado por usar nosso sistema bancário. Até logo!")
        break
    
    # Opção inválida
    else:
        print("Opção inválida. Por favor, escolha uma opção de 1 a 4.")