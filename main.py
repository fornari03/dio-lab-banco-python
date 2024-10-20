from datetime import datetime

menu_options = ["1. Entrar", "2. Criar usuário", "3. Listar contas", "4. Sair"]
user_options = ["1. Depositar", "2. Sacar", "3. Ver extrato", "4. Criar conta", "5. Sair"]
WITHDRAWAL_LIMIT = 500
AGENCY = "0001"

users = []
accounts = []

current_account = None


def deposit(balance, value, transactions, /):
    if value <= 0:
        print("Valor inválido. Tente novamente.\n\n")
        return balance, transactions
    balance += value
    transactions.append(("Depósito", value))
    print(f"Depósito de R$ {value:.2f} realizado com sucesso.\n\n")
    return balance, transactions

def withdraw(*, balance, value, transactions, withdrawals):
    if withdrawals == 3:
        print("Limite de saques diários atingido.\n\n")
        return balance, transactions
    if value <= 0:
        print("Valor inválido. Tente novamente.\n\n")
        return balance, transactions
    if value > WITHDRAWAL_LIMIT:
        print("Valor máximo de saque permitido é R$ 500.00. Tente novamente.\n\n")
        return balance, transactions
    if value > balance:
        print("Saldo insuficiente. Tente novamente.\n\n")
        return balance, transactions
    balance -= value
    transactions.append(("Saque", value))
    withdrawals += 1
    print(f"Saque de R$ {value:.2f} realizado com sucesso.\n\n")
    return balance, transactions, withdrawals

def view_extract(balance, /, *, transactions):
    print("Extrato:")
    print("Transações:")
    [print(f"\t{transaction[0].rjust(8)}: R$ {transaction[1]:.2f}") for transaction in transactions]
    print(f"Saldo: R$ {balance:.2f}")
    print("\n")

def create_user():
    name = input("Digite seu nome: ")
    try:
        birth_date = input("Digite sua data de nascimento (DD/MM/YYYY): ")
        birth_date = datetime.strptime(birth_date, "%d/%m/%Y")
    except:
        print("Data de nascimento inválida. Tente novamente.\n\n")
        return create_user()
    try:
        cpf = int(input("Digite seu CPF (apenas números): "))
    except:
        print("CPF inválido. Tente novamente.\n\n")
        return create_user()
    finally:
        if cpf in [user["cpf"] for user in users]:
            print("CPF já cadastrado. Tente novamente.\n\n")
            return create_user()
    address = input("Digite seu endereço: ")
    print("Conta criada com sucesso.\n\n")
    user = {"name": name, "birth_date": birth_date, "cpf": cpf, "address": address}
    users.append(user)
    return user

def create_account(user):
    agency = AGENCY
    account_number = len(accounts) + 1
    account = {"agency": agency, "account_number": account_number, "user": user, "balance": 0, "transactions": [], "withdrawals": 0}
    accounts.append(account)
    print(f"Conta criada com sucesso. Número da conta: {account_number}\n\n")

def list_accounts():
    print("Contas:")
    [print(f"\tAgência: {account['agency']}\n\tConta: {account['account_number']}\n\tTitular: {account['user']['cpf']}\n") for account in accounts]
    print("\n")

def login():
    cpf = int(input("Digite seu CPF (apenas números): "))
    account_number = int(input("Digite o número da conta: "))
    account = next((account for account in accounts if account["user"]["cpf"] == cpf and account["account_number"] == account_number), None)
    if account is None:
        print("Conta não encontrada. Tente novamente.\n\n")
        return login()
    print(f"\n\nOlá, {account['user']['name']}.")
    return account

def main():
    while True:
        print("Escolha uma operação a ser feita:")
        [print(option) for option in menu_options]
        try:
            operation = int(input("\nOperação: "))

            if operation == 1:
                current_account = login()
                while True:
                    print("Escolha uma operação a ser feita:")
                    [print(option) for option in user_options]
                    try:
                        user_operation = int(input("\nOperação: "))
                        if user_operation == 1:
                            value = float(input("Digite o valor a ser depositado: "))
                            current_account["balance"], current_account["transactions"] = deposit(current_account["balance"], value, current_account["transactions"])
                        elif user_operation == 2:
                            value = float(input("Digite o valor a ser sacado: "))
                            current_account["balance"], current_account["transactions"], current_account["withdrawals"] = withdraw(balance=current_account["balance"], value=value, transactions=current_account["transactions"], withdrawals=current_account["withdrawals"])
                        elif user_operation == 3:
                            view_extract(current_account["balance"], transactions=current_account["transactions"])
                        elif user_operation == 4:
                            create_account(current_account["user"])
                        elif user_operation == 5:
                            print("Saindo da conta...\n\n")
                            break
                        else:
                            print("Operação inválida. Tente novamente.\n\n")
                    except:
                        print("Operação inválida. Tente novamente.\n\n")

            elif operation == 2:
                user = create_user()
                create_account(user)

            elif operation == 3:
                list_accounts()

            elif operation == 4:
                print("Saindo do sistema...")
                break

        except:
            print("Operação inválida. Tente novamente.\n\n")


if __name__ == "__main__":
    main()