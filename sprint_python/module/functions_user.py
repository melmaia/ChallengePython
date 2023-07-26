from treatment_functions import*
#DICIONARIOS
usuarios = {}

#FUNÇÕES REFERENTES AO PROGRAMA DE CADASTRO DOS USUARIOS

def cadastrar_user():
    usuarios[get_int("CPF: ")]={ 
    "nome": get_string("Nome completo: ").upper(),
    "data_nasc":input("Data de nascimento: "),
    "email":input("E-mail: \n").upper(),
    "bem_assegurado": []}
       
def exibir_user(dicionario,cpf):
    lista= dicionario.get (cpf)
    if lista!= None:
            print(usuarios[cpf]['nome'])
            print(usuarios[cpf]['data_nasc'])
            print(usuarios[cpf]['email'])
            print(usuarios[cpf]['bem_assegurado'])
           
def exibir_users():
     print(usuarios)
     
#-------------------------------------------------------------------------

    
