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
saldo = 10000
limite = 500
extrato = []
numero_saques = 0
limite_saques = 3


opcao = int(input("Informe a opção desejada: "))

while opcao == 1:

    if opcao == 1:
        valor_de_saque = float(input("Informe quanto deseja sacar: "))
        if valor_de_saque > saldo or valor_de_saque > limite:
            print("Valor insuficiente :(")

        elif valor_de_saque <= saldo and numero_saques <= limite_saques:
            print("operação realizada")
            numero_saques = +1
            saldo = valor_de_saque - saldo
            extrato.append(f"Saque realizado, saldo atual: {saldo}")
        if True:
            break
