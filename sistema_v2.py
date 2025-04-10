import json
from datetime import datetime

try:  # tenta abrir o arquivo "clientes.json"
    with open("clientes.json", "r") as arquivo:
        clientes = json.load(arquivo)

except FileNotFoundError:  # caso o erro descrito aconteça cria dicionario "clientes"
    clientes = {}

menu = """
           ========== MENU ==========

    Bem-vindo ao sistema de gerenciamento financeiro!
           O que você deseja fazer?

           [1] Sacar
           [2] Depositar
           [3] Extrato
           [4] Sair

           ========================="""


def salvar(clientes):
    with open("clientes.json", "w") as arquivo:
        json.dump(clientes, arquivo, indent=4)


def login(clientes):  # adicionar alguns paths depois
    cpf = input("Informe seu CPF: ")
    if cpf in clientes:
        senha_digitada = input("Informe sua senha de acesso: ")
        if senha_digitada == clientes[cpf]["senha"]:
            print("login realizado")
            cliente_logado = clientes[cpf]
            print(f"Bem vindo {cliente_logado["nome"]}")
            print(menu)
            return cpf, clientes[cpf]

        else:
            print("senha incorreta")
            return

    else:
        print("CPF não cadastrado")
        return
        # voltar no menu anterior


def criar_cadastro(clientes):

    cpf = (input("Informe seu CPF: "))
    if cpf in clientes:
        print("CPF ja cadastrado.")
        return
    else:
        clientes[cpf] = {}
        clientes[cpf]["nome"] = str(input("Informe seu nome: ")).title()
        clientes[cpf]["senha"] = str(input("Informe sua senha de acesso: "))
        clientes[cpf]["saldo"] = 0.0
        clientes[cpf]["extrato"] = []
        print(f"Bem vindo, {clientes[cpf]["nome"]}")
        return cpf, clientes[cpf]


def sacar(cliente_logado):
    print(f"Seu saldo R${cliente_logado["saldo"]:.2f}")
    valor_saque = float(input("Informe quanto deseja sacar: "))
    agora = datetime.now()
    timestamp = agora.strftime("%H:%M")
    if valor_saque > cliente_logado["saldo"]:
        print("Saldo insuficiente")
    elif valor_saque < cliente_logado["saldo"]:
        cliente_logado["saldo"] -= valor_saque
        cliente_logado["extrato"].append(
            f"Saque: R${valor_saque:.2f}  {timestamp}")
        print(f"R${cliente_logado["saldo"]:.2f}")
        salvar(clientes)


def depositar(cliente_logado):
    print(f"Seu saldo R${cliente_logado["saldo"]:.2f}")
    valor_deposito = float(input("Informe o valor de deposito: "))
    agora = datetime.now()
    timestamp = agora.strftime("%H:%M")
    if valor_deposito > 0:
        cliente_logado["saldo"] += valor_deposito
        cliente_logado["extrato"].append(
            f"Deposito: R${valor_deposito:.2f}  {timestamp}")
        print(f"Depostito realizado")
        print(f"Saldo atual R${cliente_logado["saldo"]:.2f}")
        salvar(clientes)
    else:
        print("Valor invalido")


def extrato(cliente_logado):
    print("\n ========== Hoje ==========")
    print("\n".join(cliente_logado["extrato"]))
    print(f"Saldo atual R${cliente_logado["saldo"]:.2f}")
    print("==========================")


def funcao_menu():
    while True:
        opcao_menu = int(input("Informe a opção desejada: "))
        if opcao_menu == 1:
            sacar(cliente_logado)

        elif opcao_menu == 2:
            depositar(cliente_logado)

        elif opcao_menu == 3:
            extrato(cliente_logado)

        elif opcao_menu == 4:
            break

        else:
            print("Opção invalida")


# Area logica de login;

while True:
    opcao_login = int(
        input("Se ja é cliente digite 1 caso não seja digite 2: "))

    if opcao_login == 1:
        resultado = login(clientes)
        if resultado:
            cpf, cliente_logado = resultado
            funcao_menu()
            break

        else:
            print("Cliente não cadastrado")

    elif opcao_login == 2:
        cpf, cliente_logado = criar_cadastro(clientes)
        salvar(clientes)

    else:
        print("opção invalida")
