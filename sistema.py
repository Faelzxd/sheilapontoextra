LOGINS_FILEPATH = 'logins.txt'
RESERVAS_FILEPATH = 'reservations.txt'

def get_logins(filepath=LOGINS_FILEPATH):
    with open(filepath, 'r') as file_local:
        logins_local = file_local.readlines()
    return logins_local

def write_logins(logins_arg, filepath=LOGINS_FILEPATH):
    with open(filepath, 'w') as file_local:
        file_local.writelines(logins_arg)

def get_reservations(filepath=RESERVAS_FILEPATH):
    try:
        with open(filepath, 'r') as file_local:
            reservations = file_local.readlines()
        return reservations
    except FileNotFoundError:
        return []

def write_reservations(reservations_arg, filepath=RESERVAS_FILEPATH):
    with open(filepath, 'w') as file_local:
        file_local.writelines(reservations_arg)

def register_user():
    nome = input('Digite o seu nome completo: ')
    email = input('Digite o seu e-mail: ')
    senha = input('Digite sua senha: ')
    data_nascimento = input('Digite sua data de nascimento: ')
    cpf = input('Digite o seu cpf: ')
    regiao = input('Digite seu pais/estado/cidade: ')
    profissao = input('Digite sua profissão: ')
    nacionalidade = input('Digite sua nacionalidade: ')
    sexo = input('Digite seu sexo: ')
    endereco = input('Digite seu endereço/numero/complemento: ')
    fone = input('Digite seu numero: ')

    new_login = get_logins()
    new_login.append(f"{email} {senha}\n")
    write_logins(new_login)

def login_user():
    email = input('Digite o seu e-mail: ')
    senha = input('Digite sua senha: ')
    
    logins = get_logins()
    found = False

    for login in logins:
        stored_email, stored_password = login.strip().split()
        if email == stored_email and senha == stored_password:
            print("Login bem-sucedido.")
            found = True
            break
    
    if not found:
        print("Credenciais inválidas.")

    else:
        choice = input("Digite [1] para fazer reserva ou [2] para suporte: ")
        if choice == '1':
            fazer_reserva()
        elif choice == '2':
            entrar_em_contato_com_suporte()
        else:
            print("Escolha inválida.")


def fazer_reserva():
    data = input("Digite a data da reserva (dd/mm/aaaa): ")
    quarto = input("Digite o número do quarto: ")
    num_hospedes = int(input("Digite a quantidade de hóspedes (máximo 4): "))
    

    reservations = get_reservations()
    for reservation in reservations:
        stored_data, stored_quarto, _, _ = reservation.strip().split('|')
        if data == stored_data and quarto == stored_quarto:
            print("Este quarto já está reservado para esta data.")
            return

    if num_hospedes > 4:
        print("Desculpe, o número de hóspedes não pode ser superior a 4.")
        return
    
    formas_pagamento = ["boleto", "pix", "cartão", "dinheiro"]
    print("Opções de formas de pagamento:", formas_pagamento)
    forma_pagamento = input("Escolha a forma de pagamento: ")
    while forma_pagamento not in formas_pagamento:
        print("Forma de pagamento inválida. Escolha entre", formas_pagamento)
        forma_pagamento = input("Escolha a forma de pagamento: ")
    
    new_reservation = f"{data}|{quarto}|{num_hospedes}|{forma_pagamento}\n"
    reservations.append(new_reservation)
    write_reservations(reservations)
    print("Reserva realizada com sucesso.")

    
def entrar_em_contato_com_suporte():
    numero_empresa = input("Digite o número da empresa de suporte: ")
    opcao = input("Digite [1] para reembolso ou [2] para realocamento: ")

def main():
    while True:
        login_registro = int(input('Digite [1] para registro [2] para login ou 0 para sair: '))

        if login_registro == 0:
            print("Saindo...")
            break
        elif login_registro == 1:
            register_user()
        elif login_registro == 2:
            login_user()
        else:
            print("Opção inválida. Escolha 1 para registro, 2 para login ou 0 para sair.")

if __name__ == "__main__":
    main()