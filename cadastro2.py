def exibir_menu():
    print('''Escolha uma opção:

    1. Cadastrar uma pessoa
    2. Listar pessoas cadastradas
    3. Procurar dados de uma pessoa
    ''')

def cadastrar(pessoas):
    identificador = input('Id: ')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    pessoas.append((identificador, nome, idade))

def listar(pessoas):
    for pessoa in pessoas:
        identificador, nome, idade = pessoa
        print(f'Nome: {nome}')
        print(f'idade: {idade}')
        print(f'id: {identificador}')
        print(f'')

def buscar(pessoas):
    identificador_desejado = input('Id: ')
    for pessoa in pessoas:
        identificador, nome, idade = pessoa
        if identificador == identificador_desejado:
            print(f'')
            print(f'Nome: {nome}')
            print(f'idade: {idade}')
            print(f'id: {identificador}')
            print(f'')
            break
    else:
        print(f'')
        print(f'Pessoa com ID {identificador_desejado} não encontrada!')
        print(f'')


def main():
    pessoas = []

    while True:
        exibir_menu()
        print(f'')
        opcao = int(input('Digite uma opção: '))
        if opcao == 1:
            cadastrar(pessoas)
        elif opcao == 2:
            listar(pessoas)
        elif opcao == 3:
            buscar(pessoas)
        else:
            print('Opção inválida!')

main()