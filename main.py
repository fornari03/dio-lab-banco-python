options = ["1. Depósito", "2. Saque", "3. Extrato", "4. Sair"]
transactions = []
withdrawals = 0
WITHDRAWAL_LIMIT = 500
balance = 0


while True:
    print("Escolha uma operação a ser feita:")
    [print(option) for option in options]
    try:
        operation = int(input("\nOperação: "))

        if operation == 1:
            value = float(input("Digite o valor a ser depositado: "))
            if value <= 0:
                print("Valor inválido. Tente novamente.\n\n")
                continue
            balance += value
            transactions.append(("Depósito", value))
            print(f"Depósito de R$ {value:.2f} realizado com sucesso.\n\n")

        elif operation == 2:
            if withdrawals == 3:
                print("Limite de saques diários atingido.\n\n")
                continue
            value = float(input("Digite o valor a ser sacado: "))
            if value > WITHDRAWAL_LIMIT:
                print("Valor máximo de saque permitido é R$ 500.00. Tente novamente.\n\n")
                continue
            if value > balance:
                print("Saldo insuficiente. Tente novamente.\n\n")
                continue
            balance -= value
            transactions.append(("Saque", value))
            withdrawals += 1
            print(f"Saque de R$ {value:.2f} realizado com sucesso.\n\n")

        elif operation == 3:
            print("Extrato:")
            print("Transações:")
            [print(f"\t{transaction[0].rjust(8)}: R$ {transaction[1]:.2f}") for transaction in transactions]
            print(f"Saldo: R$ {balance:.2f}")
            print("\n")

        elif operation == 4:
            print("Saindo...")
            break

    except:
        print("Operação inválida. Tente novamente.\n\n")