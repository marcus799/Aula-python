
def soma():
    A = int(input("Digite o valor de A: "))
    B = int(input("Digite o valor de B: "))
    C = int(input("Digite o valor de C: "))

    soma = A + B
    print(f"A soma entre A e B é: {soma}")

    if soma < C:
        print("A soma é menor que C.")
    else:
        print("A soma é maior ou igual a C.")

print(soma())



def soma_iguais():
    A = int(input("\nDigite o valor de A: "))
    B = int(input("Digite o valor de B: "))

    if A == B:
        soma = A + B
        print(f"A soma dos valores iguais A e B é: {soma}")

    else:
        print(f"A soma so acontecerá se os valores de A e B forem iguais. A: {A}, B: {B}")

print(soma_iguais())