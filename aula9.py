
def cadastro_pessoa():
    print(f"Ola {nome} sua idade é {idade}")

def verificar_idade():
    if idade >= 18:
        print("Voce é maior de idade")
    else:
        print("Voce é menor de idade")



while True:
    escolha = int(input("Digite 1 para cadastrar e digite 2 para verificar a idade"))
    if escolha == 1:
        nome = input("Digite o seu nome\n")
        idade = int(input("Digite a sua idade\n"))
        cadastro_pessoa()

    elif escolha == 2:
        verificar_idade()

    else:
        print("Opçao invalida")


def verifica_par_impar():
    if num % 2 == 0:
        return("O numero é par")

    else:
        return("o numero é impar")





num = int(input("Digite um numero\n"))
resultado = verifica_par_impar()
print(resultado)


def verificar_placar():
    if timeA > timeB:
        return("O time A foi o vencedor")
    elif timeB > timeA:
        return("O time B foi o vencedor")
    else:
        return("Empate")




timeA = int(input("Digite o resultado do flamengo"))
timeB = int(input("Digite o resultado do vasco"))
resultado = verificar_placar()
print(resultado)









serieA = []

while True:
    cadastro = input("Deseja cadastrar? (S) ou (N)")
    if cadastro.lower() == 's' or cadastro.lower() == 'sim':
        time = input("Qual o nome do time?\n")
        serieA.append(time)




def cadastro_times():
    time = input("Qual o nome do time?\n")
    serieA.append(time)



serieA = []

cadastro = input("Deseja cadastrar? (S) ou (N)")
while cadastro.lower() == 's' or cadastro.lower() == 'sim':
    cadastro_times()
    cadastro = input("Deseja cadastrar? (S) ou (N)")
print(serieA)