
def cadastrar_aluno():
    aluno = input("Digite o seu nome: ")
    nota1 = int(input("Digite a primeira nota: "))
    nota2 = int(input("Digite a segunda nota: "))
    nota3 = int(input("Digite a terceira nota: "))
    aluno_cadastrado = {'aluno':aluno,'nota1':nota1,'nota2':nota2,'nota3':nota3}
    alunos.append(aluno_cadastrado)


def listar_alunos():
    for aluno in alunos:
        print(f"nome:{aluno['aluno']},nota1:{aluno['nota1']},nota2:{aluno['nota2']},nota3:{aluno['nota3']}")


def pesquisar_aluno():
    nome_pesquisado = input("Digite o nome que deseja pesquisar: ")
    for aluno in alunos:
        if aluno['aluno'] == nome_pesquisado:
            print(f"nome:{aluno['aluno']},nota1:{aluno['nota1']},nota2:{aluno['nota2']},nota3:{aluno['nota3']}")
            return  
    print("aluno nao encontrado")


def excluir_todos():
    comfirmaçao = input("Tem certeza que deseja excluir? (s/n)\n")
    if comfirmaçao.lower == 's' or comfirmaçao.lower == 'sim':
        alunos.clear()
        print("Todos alunos removidos com sucesso")


def excluir_aluno():
    nome_excluir = input("Digite o nome que voce quer excluir da lista: ")
    for aluno in alunos:
        if aluno['aluno'] == nome_excluir:
            alunos.remove(aluno)
            print("aluno excluido com sucesso")
            return
    print("este aluno nao existe na lista")


alunos = []
while True:

    print("Digite 1 para cadastrar\nDigite 2 para listar\nDigite 3 para excluir\nDigite 4 para pesquisar\nDigite 5 para excluir todos\nDigite 6 para encerrar\n")
    opçao = int(input("Digite a opçao desejada: "))

    if opçao == 1:
        cadastrar_aluno()

    elif opçao == 2:
        listar_alunos()

    elif opçao == 5:
        excluir_todos()

    elif opçao == 3:
        excluir_aluno()

    elif opçao == 4:
        pesquisar_aluno()

    elif opçao == 6:
        break




    #cadastro de produtos
produtos = []

def cadastrar_produtos():
    nome = input("Digite o nome do produto que voce vai comprar: ")
    preço = float(input("Digite o preço do produto: "))
    produto = {"nome": nome, "preco": preço}
    produtos.append(produto)


def listar_produtos():
    for produto in produtos:
           print(f"Nome do produto: {produto['nome']} | Preço do produto: {produto['preco']}")


def excluir_produtos():
    nome_do_produto = input("Digite o nome do produto que vai excluir: ")
    for produto in produtos:
        if produto['nome'] == nome_do_produto:
            produtos.remove(produto)
            print("Produto removido com sucesso")
            return
    print("Produto nao existe na lista para ser excluido")


def pesquisar_produto():
    produto_pesquisado = input("Digite o produto que deseja pesquisar: ")
    for produto in produtos:
        if produto['nome'] == produto_pesquisado:
            print(f"nome do produto:{produto['nome']},:{produto['preco']}")
            return
    print("Produto nao encontrado na lista")


def excluir_todos():
    comfirmaçao = input("Tem certeza que deseja excluir?(s/n)\n")
    if comfirmaçao.lower == 's' or comfirmaçao.lower == 'sim':
        produtos.clear()
        print("Todos produtos removidos com sucesso")


#repetiçao com while
while True:
    opçao = int(input("Digite 1 para cadastrar um produto\nDigite 2 para listar um produto\nDigite 3 para excluir\nDigite 4 para pesquisar\nDigite 5 para excluir tudo\nDigite 6 para encerrar\n"))

    if opçao == 1:
        cadastrar_produtos()

    elif opçao == 2:
        listar_produtos()

    elif opçao == 4:
        pesquisar_produto()

    elif opçao == 5:
        excluir_todos()

    elif opçao == 6:
        print("encerrando programa")
        break

    elif opçao == 3:
       excluir_produtos()

    else:
        print("digite uma opçao valida")