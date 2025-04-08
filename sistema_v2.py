import json

try:
    with open("clientes.json", "r") as arquivo:
        CLIENTES = json.load(arquivo)

except FileNotFoundError:
    CLIENTES = {}

menu = """
           ========== MENU ==========

    Bem-vindo ao sistema de gerenciamento financeiro!
           O que você deseja fazer?

           [1] Sacar
           [2] Depositar
           [3] Extrato
           [4] Sair

           ========================="""


# função de criar cadastro


def criar_cadastro():
    cpf = (input("Informe seu CPF: "))
    if cpf in CLIENTES:
        print("CPF ja cadastrado.")
        return

    CLIENTES[cpf] = {}
    CLIENTES[cpf]["nome"] = str(input("Informe seu nome: ")).title()
    CLIENTES[cpf]["senha"] = int(input("Informe sua senha de acesso: "))


# Area de login;
opcao_login = int(input("Se ja é cliente digite 1 caso não seja digite 2: "))

if opcao_login == 1:
    print("criar função de login")

elif opcao_login == 2:
    criar_cadastro()
    print(CLIENTES)

    with open("clientes.json", "w") as arquivo:
        json.dump(CLIENTES, arquivo, indent=4)


else:
    print("opção invalida")
