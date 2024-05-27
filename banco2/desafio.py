
def usuario_existe(usuarios, cpf):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return True
    return False

def criar_usuario(usuarios):
    cpf = input("Digite o cpf do usuario: ")
    if usuario_existe(usuarios, cpf):
        print("Usuario com o cpf passado já existe")
        return
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento do usuário: ")
    endereco = input("Digite o endereço do usuario: ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

def criar_conta(agencia, numero_conta, contas, usuarios):
    cpf = input("Digite cpf do usuário: ")
    if usuario_existe(usuarios, cpf):
        contas.append({"agencia": agencia, "numero_conta": numero_conta, "cpf": cpf})
        return
    print("Usuário passado não existe.")
    return
    
def depositar(valor, saldo, extrato, /):
    saldo += valor
    extrato = extrato + f"Depósito: {valor:.2f}\n"
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques == limite_saques:
        print("Limite de sacos diários atingido.")
        return
    elif valor <= 0:
        print("Valor inválido.")
        return
    elif valor > limite:
        print("Valor superior ao limite de saque.")
        return
    elif valor > saldo:
        print("Saldo insuficiente.")
        return
    else:
        saldo -= valor
        extrato = extrato + f"Saque: {valor:.2f}\n"
        numero_saques += 1
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /,*, extrato):
    print(extrato if extrato else "Sem movimentações realizadas.")
    print(f"Saldo: {saldo:.2f}")

def main():
    menu = """
    [b] Criar usuário
    [c] Criar conta
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = [] 
    contas = []  

    while True:

        opcao = input(menu)

        if opcao == "b":
            criar_usuario(usuarios)
        elif opcao == "c":
            numero_conta = len(contas) + 1
            criar_conta(AGENCIA, numero_conta, contas, usuarios)

        elif opcao == "d":
            valor = float(input("Digite o valor que deseja depositar: "))
            if valor <= 0:
                print("Valor inválido.")
            else:
                saldo, extrato = depositar(valor, saldo, extrato)
        elif opcao == "s":
            valor = float(input("Digite o valor que deseja sacar: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
            
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()

