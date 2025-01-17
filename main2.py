operaçao = input("Digite a operaçao: ")

if operaçao.lower() == 'soma':
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))

    resultado = num1 + num2
    print("resultado da soma:", resultado)

elif operaçao.lower() == 'subtraçao':
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))

    resultado = num1 - num2
    print("O resultado da subtraçao é:", resultado)

elif operaçao.lower() == 'multiplicaçao':
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))

    resultado = num1 * num2
    print("O resultado da multiplicaçao é:", resultado)

elif operaçao.lower() == 'divisao':
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))

    resultado = num1 / num2
    print("O resultado da divisao é:", resultado)