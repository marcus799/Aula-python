
while True:
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))

    operaçao = input("Digite a operaçao: ")

    if operaçao.lower() == 'soma':
        print(f"o resultado da operaçao é {num1 + num2}")
        break

    elif operaçao.lower() == 'subtraçao':
        print(f"o resultado da operaçao é {num1 - num2}")
        break

    elif operaçao.lower() == 'multiplicaçao':
        print(f"o resultado da operaçao é {num1 * num2}")
        break

    elif operaçao.lower() == 'divisao':
        print(f"o resultado da operaçao é {num1 / num2}")
        break

    else:
        print("Digite uma operaçao valida")