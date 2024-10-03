def somar(num1 , num2):
    soma = num1 + num2
    return soma


operaçao = input("digite a operaçao soma, multiplicaçao, divisao ou subtraçao: ")
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))


if operaçao.lower() == "soma":
    #soma = num1 + num2
    soma = somar(num1 , num2)
    print("a soma é:", soma)

elif operaçao.lower() == "subtraçao":
    subtraçao = num1 - num2
    print("subtraçao é:",subtraçao)

elif operaçao.lower() == "divisao":
    divisao = num1 / num2
    print("a divisao é:",(divisao))
    
elif operaçao.lower() == "multiplicaçao":
    multiplicaçao = num1 * num2
    print("a multiplicaçao é:", multiplicaçao)

else:
    print("Digite uma operaçao valida")