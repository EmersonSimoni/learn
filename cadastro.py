print("nome",nome_pessoa,"idade",idade_pessoa,"id",id_pessoa)

listas = [[]] #uma lista de lista

while True:
    print("1-Cadastrar pessoa")
    print("2-Lista Cadastros")
    print("3-Procurar Pessoa Especifica")
    op = int(input())#Escolha da opcao
    if op == 1:
        nova = [] # cria uma lista para adicionar o id, nome e idade da pessoa
        id = input("Id da pessoa")
        nome = input("Digite o nome da pessoa")
        idade = input("Idade da pessoa")
        nova.append(id)
        nova.append(nome)
        nova.append(idade)
        listas.append(nova)#Adiciona a lista criada com o cadastro da pessoa dentro da lista

    elif op == 2:
        for mostrar in listas:
            for mostrar2 in mostrar:
                print(mostrar2)#mostra tudo dentro da

    elif op == 3:
        print("pensando")


def exibir_menu():
    print('''Escolha uma opção:

    1. Cadastrar uma pessoa
    2. Listar pessoas cadastradas
    3. Procurar dados de uma pessoa
    ''')

    def cadastrar(pessoas):
        identificador = input('Id? ')
        nome = input('Nome? ')
        idade = int(input('Idade? '))
        pessoas.append((identificador, nome, idade))

        def listar(pessoas):
            for pessoa in pessoas:
                identificador, nome, idade = pessoa
                print(f'Nome: {nome}, idade: {idade}, id: {identificador}')


def buscar(pessoas):
    identificador_desejado = input('Id? ')
    for pessoa in pessoas:
        identificador, nome, idade = pessoa
        if identificador == identificador_desejado:
            print(f'Nome: {nome}, idade: {idade}, id: {identificador}')
            break
    else:
        print(f'Pessoa com id {identificador_desejado} não encontrada')

