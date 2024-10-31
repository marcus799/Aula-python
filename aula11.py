
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



alunos = []
while True:

    print("Digite 1 para cadastrar\nDigite 2 para listar\nDigite 3 para excluir\nDigite 4 para pesquisar\nDigite 5 para encerrar")
    opçao = int(input("Digite a opçao desejada: "))

    if opçao == 1:
        cadastrar_aluno()

    elif opçao == 2:
        listar_alunos()

    elif opçao == 5:
        break