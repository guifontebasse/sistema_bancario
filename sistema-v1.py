menu = """
           ========== MENU ==========

    Bem-vindo ao sistema de gerenciamento financeiro!
           O que você deseja fazer?

           [1] Sacar
           [2] Depositar
           [3] Extrato
           [4] Sair

           ========================="""

print(menu)
saldo = 1000
limite = 500
extrato = []
numero_saques = 1
limite_saques = 3


while True:
    opcao = int(input("Informe a opção desejada: "))
    if opcao == 1:
        valor_de_saque = float(input("Informe quanto deseja sacar: "))
        if valor_de_saque <= saldo and numero_saques <= limite_saques:
            print("operação realizada")
            numero_saques = numero_saques + 1
            saldo = saldo - valor_de_saque
            extrato.append(f"Saque realizado, saldo atual:R$:{saldo}")
            print(f"Seu saldo atual é de:R${saldo}")
            print("\n".join(extrato))
        elif valor_de_saque > saldo and valor_de_saque > limite:
            print("Valor insuficiente :(")

        elif numero_saques >= limite_saques:
            print("limite de saque atingido, tente novamente amanhã")
    elif opcao == 3:
        print("\n".join(extrato))
        print(f"saldo atual:R$:{saldo}")
    elif opcao == 4:
        break
