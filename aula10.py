
def somar():
    media_aluno1 = sum(nota_aluno1) / 3
    media_aluno2 = sum(nota_aluno2) / 3
    print(media_aluno1)
    print(media_aluno2)


def verificar_notas():
    if nota_aluno1 > nota_aluno2:
        print("a media 1 é maior que a media 2")

    else:
        print("a media 1 é menor que a media 2")


nota_aluno1 = [5, 10, 8]
nota_aluno2 = [1, 3, 9]


somar()
verificar_nota = verificar_notas()





def cadastrar_notas():
    for i in range(3):
        nota1 = float(input("Digite a nota do aluno\n"))
        nota_aluno1.append(nota1)
    print(nota_aluno1)


    for i in range(3):
        nota2 = float(input("Digite a nota do segundo aluno\n"))
        nota_aluno2.append(nota2)
    print(nota_aluno2)


def calculo_media():
    media1 = sum(nota_aluno1) / 3
    print(media1)

    media2 = sum(nota_aluno2) / 3
    print(media2)

    if media1 > media2:
        print("A media do primeiro aluno é maior que a do segundo")
    else:
        print("A media do primeiro aluno é menor que o segundo")




nota_aluno1 = []
nota_aluno2 = []

cadastrar_notas()
calculo_media()



lista_de_alunos = []

quantidade = int(input("Quantos alunos quer cadastrar?\n"))
i = 0

for i in range(quantidade):
    aluno = input("Digite o nome do aluno\n")
    nota1 = float(input("Digite a primeira nota\n"))
    nota2 = float(input("Digite a segunda nota\n"))
    nota3 = float(input("Digite a terceira nota\n"))
    lista_de_alunos.append((aluno, nota1, nota2, nota3))

print(lista_de_alunos)





def cadastro_de_alunos():
    quantidade = int(input("Quantos alunos quer cadastrar?\n"))
    i = 0


    for i in range(quantidade):
        aluno = input("Digite o nome do aluno\n")
        notas = []
        for i in range(3):
            nota = float(input("Digite a nota do aluno\n"))
            notas.append(nota)
        notas_dos_alunos.append(notas)
        lista_de_alunos.append((aluno, notas))
    print(lista_de_alunos)



notas_dos_alunos = []
lista_de_alunos = []

cadastro_de_alunos()


