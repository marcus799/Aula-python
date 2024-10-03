pessoas = []#lista de pessoas
i = 0
quantidade = int(input("Quantas pessoas voce quer cadastrar? "))
for i in range(quantidade):
    nome = input("Digite o seu nome: ")
    pessoas.append(nome)#adicionando o cadastro do nome na lista de pessoas com o comando append

print(pessoas)
for i in range(quantidade):
    print(f"pessoa:{pessoas[i]}")



idades = []
i = 0
quantidade = int(input("Quantas idades voce quer cadastrar? "))
for i in range(quantidade):
    idade = int(input("Qual a sua idade? "))
    idades.append(idade)
    if idade<18:
        print("Voce possui", idade, "anos e é menor de idade")
    else:
        print("Voce possui", idade, "anos e é ,maior de idade")
print(idades)



alturas = []
i = 0
quantidade = int(input("Quantas alturas voce vai digitar? "))
for i in range(quantidade):
    altura = float(input("Digite a sua altura "))
    alturas.append(altura)
    if altura>=1.80:
        print("sua altura e:", altura, "Voce e alto")
    else:
        print("sua altura e:", altura, "voce e baixo")
print(alturas)



pessoas = []
i = 0
quantidade = int(input("Quantas pessoas vao calcular o imc? "))
for i in range(quantidade):
    peso = float(input("Qual o seu peso? "))
    altura = float(input("Qual a sua altura? "))
    IMC = peso/(altura*altura)
    pessoas.append(f"{IMC:.2f}")
    print(f"{IMC:.2f}")
    if IMC<18.8:
        print("Voce esta abaixo do peso normal")
    elif IMC>18.5 and IMC<24.9:
        print("Peso normal")
    else:
        print("Acima do peso")
print(pessoas)



pessoas = []
while True:
    print("para encerrar este programa a qualquer momento digite 0")
    peso = float(input("Digite o seu peso: "))
    altura = float(input("Digite a altura: "))
    if peso==0 or altura==0:
        break
    else:
        IMC = peso/(altura*altura)
        pessoas.append(f"{IMC:.2f}")
        if IMC<=18.5:
            print("Voce esta abaixo do peso normal")
        elif IMC>18.5 and IMC<24.9:
            print("Peso normal")
        else:
            print("Acima do peso")
print(pessoas)