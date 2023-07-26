from treatment_functions import*
from functions_user import*

#FUNÇÕES REFERENTES AO PROGRAMA DE CADASTRO DOS BENS ASSEGURADOS

def cadastrar_bike():
    cpf = get_int("Insira seu cpf: ")
    foto_serie = get_int("Envie 1 foto do número da série da bicicleta:")
    while True:
        n_serie = get_int('Número de série: ')

        if n_serie != foto_serie:
            print("Você não pode prosseguir com o seguro")
            continue
        else:
            break

    bem_assegurado = {
    "n_serie": n_serie,
    "marca": get_string('Marca: '),
    "modelo": get_string('Modelo: '),
    "valor": get_float('Valor: '),
    "modalide": get_string('Modalidade: '),
    "a_fabric": get_int('Ano de fabricação: '),
    "acess": get_string('Acessorios: '),
    "tipo_quadro": get_string ('Tipo de quadro: '),
    "tamanho_quadro": get_int ('Qual o tamanho do quadro(em cm): '),
    "tipo_pneu": get_string('Qual o tipo do pneu: '),
    "tamanho_pneu": get_int('Qual o tamanho do pneu: '),
    "qtnd_marcha": get_int('Quantidade de marcha: '),
    "suspensao": get_string('Qual o tipo de suspensão: '),
    "freio": get_string('Qual o tipo de freio: '),
    "estado_bike": vistoria(),
    "plano": select_plano(),
    }

    usuarios[cpf]["bem_assegurado"].append(bem_assegurado)

def exibir_bike():
    cpf = get_int("Insira seu cpf: ")
    for bike in usuarios[cpf]["bem_assegurado"]:
        print(f'Número de série: {bike["n_serie"]} - Marca:{bike["marca"]} - Modelo:{bike["modelo"]} - Plano Atual: {bike ["plano"]}')

# def excluir_bike():
#     cpf = leia_int("Insira seu cpf: ")
#     n_serie = leia_int("Insira  número de série da bike: ")
#     for bike in usuarios[cpf]["bem_assegurado"]:
#         if bike["n_serie"] == n_serie:
#             usuarios[cpf]["bem_assegurado"].remove(bike[""])
            
def vistoria():
    bike_status = { 
        "foto_quadro":print("Envie 1 foto do quadro"),
        "foto_roda":print("Envie 1 foto da roda dianteira"),
        "roda_traseira":print("Envie 1 foto da roda traseira"),
        "guidao":print("Envie 1 foto do guidão"),
        "foto_catraca":print("Envie 1 foto da catraca"), 
        "foto_vela":print("Envie 1 foto de pé de vela"), 
        "foto_freio":print("Envie 1 foto do freio:"),
        "foto_banco":print("Envie 1 foto do banco:"),
        "foto_suspensao":print("Envie 1 foto suspensão:"), 
        "foto_cambio":print("Envie 1 foto do câmbio:"),
        "foto_bike":print("Envie 1 foto da bicicleta inteira: "),
    }
    return bike_status

def select_plano():
    
    print("1 - Plano Pedal Essencial")
    print("2 - Plano Pedal Leve")
    print("3 - Plano Pedal Elite")

    op_plano = (int(input("Qual plano você deseja?: \n")))

    while True:
        if op_plano == 1:
            plano = "Plano Pedal Essencial"
            print("Você contratou o 'Plano Pedal Essencial'")
            break
        elif op_plano == 2:
            plano = "Plano Pedal leve"
            print("Você contratou o 'Plano Pedal Leve'")
            break 
        elif op_plano == 3:
            plano = "Plano Pedal Elite"
            print("Você contratou o 'Plano Pedal Elite'")
            break
        else:
            print("Erro! Insira uma opção válida.")
            continue
    return plano