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


class Cliente:

    def __init__(self, cpf, nome, senha):
        self.cpf = cpf
        self.nome = nome
        self.senha = senha
        self.saldo = 0.0
        self.extrato = []

    def sacar(self):
        print(f"Seu saldo R${self.saldo:.2f}")
        valor_saque = float(input("Informe quanto deseja sacar: "))
        agora = datetime.now()
        timestamp = agora.strftime("%H:%M")
        if valor_saque > self.saldo:
            print("Saldo insuficiente")
        elif valor_saque <= self.saldo:
            self.saldo -= valor_saque
            clientes[self.cpf]["saldo"] = self.saldo
            self.extrato.append(
                f"Saque: R${valor_saque:.2f}  {timestamp}")
            print(f"R${self.saldo:.2f}")

    def depositar(self):
        print(f"Seu saldo R${self.saldo:.2f}")
        valor_deposito = float(input("Informe o valor de deposito: "))
        agora = datetime.now()
        timestamp = agora.strftime("%H:%M")
        if valor_deposito > 0:
            self.saldo += valor_deposito
            clientes[self.cpf]["saldo"] = self.saldo
            self.extrato.append(
                f"Deposito: R${valor_deposito:.2f}  {timestamp}")
            print(f"Depostito realizado")
            print(f"Saldo atual R${self.saldo:.2f}")
        else:
            print("Valor invalido")

    def ver_extrato(self):
        print("\n ========== Hoje ==========")
        print("\n".join(self.extrato))
        print(f"Saldo atual R${self.saldo:.2f}")
        print("==========================")


def salvar(clientes):
    with open("clientes.json", "w") as arquivo:
        json.dump(clientes, arquivo, indent=4)


def login(clientes):  # adicionar alguns paths depois
    cpf = input("Informe seu CPF: ")
    if cpf in clientes:
        senha_digitada = input("Informe sua senha de acesso: ")
        if senha_digitada == clientes[cpf]["senha"]:
            print("login realizado")
            dados = clientes[cpf]
            cliente_logado = Cliente(cpf, dados["nome"], dados["senha"])
            cliente_logado.saldo = dados["saldo"]
            cliente_logado.extrato = dados["extrato"]
            print(f"Bem vindo {cliente_logado.nome}")
            print(menu)
            return cliente_logado

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


def funcao_menu(cliente_logado):
    while True:
        opcao_menu = int(input("Informe a opção desejada: "))
        if opcao_menu == 1:
            cliente_logado.sacar()
            salvar(clientes)

        elif opcao_menu == 2:
            cliente_logado.depositar()
            salvar(clientes)

        elif opcao_menu == 3:
            cliente_logado.ver_extrato()
            salvar(clientes)

        elif opcao_menu == 4:
            break

        else:
            print("Opção invalida")


# Area logica de login;

while True:
    opcao_login = int(
        input("Se ja é cliente digite 1 caso não seja digite 2: "))

    if opcao_login == 1:
        cliente_logado = login(clientes)
        if cliente_logado:
            funcao_menu(cliente_logado)
            break

    elif opcao_login == 2:
        cpf, cliente_logado = criar_cadastro(clientes)
        salvar(clientes)

    else:
        print("opção invalida")
