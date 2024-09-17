
pessoas = ['marcus', 'anthony']
print(pessoas)

pessoas = []
nome = input("Digite o seu nome: ")
pessoas.append(nome)
print(nome)

pessoas = []
i = 0
quantidade = int(input("Quantas pessoas voce quer cadastrar? "))
for i in range(quantidade):
    nome = input("Digite o seu nome: ")
    pessoas.append(nome)

print(pessoas)
print(f"\npessoa:{pessoas[i]}")

pessoas = []
i = 0
quantidade = int(input("Quantas pessoas voce quer cadastrar? "))
for i in range(quantidade):
    nome = input("Digite o seu nome: ")
    pessoas.append(nome)
for i in range(quantidade):
    print(f"\npessoa:{pessoas[i]}")

alunos = []
notas = []
quantidade = int(input("Quantos alunos voce quer cadastrar? "))
for i in range(quantidade):
    cadastro = input("Digite o seu nome: ")
    nota1 = float(input("Digite a sua nota: "))
    alunos.append(cadastro)
    notas.append(nota1)

for i in range(quantidade):
    print(f"\nposiçao {i}: aluno: {alunos[i]}")
    print(f"\nposiçao {i}: notas: {notas[i]}")
#print(alunos)
#print(notas)