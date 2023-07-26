#FUNÇÕES DE TRATAMENTO DE DADOS 

def get_string(message):
    while True:
        user_in = input(message)
        ok = True
        for digit in user_in:
            if digit.isnumeric():
                ok = False
                break
        if ok == False:
            print("Erro! Insira caracteres válidos")
            continue
        else:
            return user_in
             
def get_int(message):
    while True:
        try:
            value = input(message)
            value = int (value)
            return value
        except ValueError:
            print("Digite um número inteiro\n")

def get_float(message):
    while True:
        try:
            value = input(message)
            value = float(value)
            return value
        except ValueError:
            print("Digite um número real\n")
