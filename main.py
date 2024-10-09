def somar(num1 , num2):
    soma = num1 + num2
    return soma

def subtrair(num1 , num2):
    subtraçao = num1 - num2
    return subtraçao

def multiplicar(num1 ,num2):
    multiplicaçao = num1 * num2
    return multiplicaçao

def dividir(num1 , num2):
    if num2 == 0 or num1 == 0:
        return "Erro: Divisao por zero"
    divisao = num1 / num2
    return round(divisao, 1)

operaçao = input("digite a operaçao soma, multiplicaçao, divisao ou subtraçao: ")
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))


if operaçao.lower() == "soma":
    soma = somar(num1 , num2)
    print(f"A soma de {num1} e {num2} é igual a {soma}")

elif operaçao.lower() == "subtraçao":
    subtraçao = subtrair(num1 , num2)
    print(f"A subtraçao de {num1} e {num2} é igual a {subtraçao}")

elif operaçao.lower() == "multiplicaçao":
    multiplicaçao = multiplicar(num1 , num2)
    print(f"A multiplicaçao de {num1} e {num2} é igual a {multiplicaçao}")

elif operaçao.lower() == "divisao":
    divisao = dividir(num1 , num2)
    print(f"A divisao de {num1} e {num2} é igual a {divisao}")
    
else:
    print("Digite uma operaçao valida")