menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor que deseja depositar: "))
        if valor <= 0:
            print("Valor inválido.")
        else:
            saldo += valor
            extrato = extrato + f"Depósito: {valor:.2f}\n"

    elif opcao == "s":
        if numero_saques == LIMITE_SAQUES:
            print("Limite de sacos diários atingido.")
        else:
            valor = float(input("Digite o valor que deseja sacar: "))
            if valor <= 0:
                print("Valor inválido.")
            elif valor > limite:
                print("Valor superior ao limite de saque.")
            elif valor > saldo:
                print("Saldo insuficiente.")
            else:
                saldo -= valor
                extrato = extrato + f"Saque: {valor:.2f}\n"
                numero_saques += 1
    
    elif opcao == "e":
        print(extrato if extrato else "Sem movimentações realizadas.")
        print(f"Saldo: {saldo:.2f}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")