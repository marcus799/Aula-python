def gastos_dos_usuarios():
    #nome dos usuarios
    nome1 = input("Digite o seu nome: ")
    nome2 = input("\nDigite o seu nome: ")

    #gastos dos usuarios
    gastos_nome1 = int(input(f"\nDigite os seus gastos {nome1}: "))
    gastos_nome2 = int(input(f"\nDigite os seus gastos {nome2}: "))

    #verificaçao dos gastos
    if gastos_nome1 > gastos_nome2:
        print(f"\nOs gastos de {nome1} foram maiores que os de {nome2}")

    elif gastos_nome2 > gastos_nome1:
        print(f"\nOs gastos de {nome2} foram maiores que os de {nome1}")

    else:
        print(f"\nos gastos de {nome1} e os gastos de {nome2} foram iguais")


gastos_dos_usuarios()