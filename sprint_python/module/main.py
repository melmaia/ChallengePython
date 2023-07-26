from functions_user import*
from functions_bike import*

op = input("Bem vindo ao seguro de bike da porto, você já é cliente? s/n: ").upper()
if op == "N":

#CADASTRO DO CLIENTE
    print("Insira os dados do usuario")
    cadastrar_user()

#MENU
while True:
    print("-"*20)
    print("1 - Cadastrar Usuário")
    print("2 - Exibir Usuário ")
    print("3 - Exibir Usuários")
    print("4 - Cadastrar Bicicletas")
    print("5 - Exibir Bicicleta")
    print("6 - Excluir Bicicletas")
    print("7 - Sair")
    print("-"*20)
    op = input("O que deseja: \n")

#CHAMANDO AS FUNÇÕES CONFORME A OPÇÃO DIGITADA
    if op == "1":
       cadastrar=cadastrar_user()
    elif op == "2":
       exibir= exibir_user(usuarios, input("Qual o CPF que deseja pesquisar?"))
    elif op == "3":
       exibir=exibir_users()
    elif op == "4":
        cadastrar_bike()
    elif op == "5":
        exibir_bike()
    # elif op == "6":
    #     excluir_bike()
    else:
        print("Obrigado pela preferência, esperamos ter ajudado!!")
        break