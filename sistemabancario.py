# Sistema bancário com saque depósito e extrato

valor = 0.0
valor_extrato = []
saques = 3
LIMITE_SAQUE = 500.0
def main():
    global valor, valor_extrato, saques

    while True:
        print("\nBem-vindo ao Sistema Bancário!")
        print("1. Sacar")
        print("2. Depositar")
        print("3. Extrato")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            sacar()
        elif opcao == '2':
            depositar()
        elif opcao == '3':
            extrato()
        elif opcao == '4':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")


def sacar():
    global valor, valor_extrato, saques

    if saques <= 0:
        print("Número de saques excedido. Você não pode mais sacar hoje.")
        return

    try:
        valor_saque = float(input("Informe o valor do saque: R$ "))
        
        if valor_saque > LIMITE_SAQUE:
            print(f"Valor máximo para saque é R$ {LIMITE_SAQUE:.2f}.")
            return
        
        if valor_saque > valor:
            print("Saldo insuficiente para realizar o saque.")
            return
        
        valor -= valor_saque
        valor_extrato.append(f"Saque: R$ {valor_saque:.2f}")
        saques -= 1
        print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!")
    except ValueError:
        print("Valor inválido! Por favor, informe um número válido.")
    


def depositar():
    global valor, valor_extrato

    try:
        valor_deposito = float(input("Informe o valor do depósito: R$ "))
        
        if valor_deposito <= 0:
            print("Valor de depósito deve ser maior que zero.")
            return
        
        valor += valor_deposito
        valor_extrato.append(f"Depósito: R$ {valor_deposito:.2f}")
        print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!")
    except ValueError:
        print("Valor inválido! Por favor, informe um número válido.")
    


def extrato():
    global valor, valor_extrato

    print("\n--- Extrato ---")
    if not valor_extrato:
        print("Nenhuma transação realizada.")
    else:
        for transacao in valor_extrato:
            print(transacao)
    
    print(f"Saldo atual: R$ {valor:.2f}")
    print(f"Saques restantes: {saques}\n")

if __name__ == "__main__":
    main()

    

