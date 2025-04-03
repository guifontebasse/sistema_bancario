
menu = """
           ========== MENU ==========

    Bem-vindo ao sistema de gerenciamento financeiro!
           O que você deseja fazer?

           [1] Sacar
           [2] Depositar
           [3] Extrato
           [4] Sair

           ========================="""
saldo = 1000
LIMITE = 500.00
extrato = []
numero_saques = 1
LIMITE_DE_SAQUES = 3

print(menu)

while True:
    opcao = int(input("Informe a opção desejada: "))
    if opcao == 1:
        valor_de_saque = float(input("Informe quanto deseja sacar: "))
        if valor_de_saque > saldo or valor_de_saque > LIMITE:
            print("Valor insuficiente :(")

        elif valor_de_saque <= saldo and numero_saques <= LIMITE_DE_SAQUES:
            print("operação realizada")
            numero_saques = numero_saques + 1
            saldo = saldo - valor_de_saque
            extrato.append(
                f"Saque R${valor_de_saque:.2f}. Saldo R${saldo:.2f}")
            print(f"Seu saldo atual: R${saldo:.2f}")

        elif numero_saques >= LIMITE_DE_SAQUES:
            print("limite de saque diario, tente novamente amanhã")

    elif opcao == 2:
        deposito = float(input("Informe quanto deseja depositar: "))
        if deposito > 0:
            saldo = deposito + saldo
            extrato.append(f"Deposito R${deposito:.2f}. Saldo R${saldo:.2f}")
            print(f"seu saldo atual: R${saldo:.2f} ")
        else:
            print("Valor invalido")

    elif opcao == 3:
        print("\n".join(extrato))
        print(f"saldo atual R${saldo:.2f}")

    elif opcao == 4:
        break

    else:
        print("Opção invalida")
        continue
