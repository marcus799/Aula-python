
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


pessoas = []
i = 0
repetir = input("Voce quer cadastrar?\n(s/n)")
while repetir=='s' or repetir=='S' or repetir=='sim' or repetir=='SIM' or repetir=='Sim':
    peso = float(input("Qual o seu peso? "))
    altura = float(input("Qual a sua altura? "))
    IMC = peso/(altura*altura)
    pessoas.append(f"{IMC:.2f}")
    print(f"{IMC:.2f}")
    if IMC<=18.5:
        print("Voce esta abaixo do peso normal")
    elif IMC>18.5 and IMC<24.9:
        print("Peso normal")
    else:
        print("Acima do peso")
    repetir = input("Voce quer cadastrar?\n(s/n)")
print(pessoas)


pessoas = []
i = 0
repetir = input("Voce quer cadastrar?(s/n)\n")
while repetir.lower()=='s' or repetir.lower()=='sim':
    peso = float(input("Qual o seu peso? "))
    altura = float(input("Qual a sua altura? "))
    IMC = peso/(altura*altura)
    pessoas.append(f"{IMC:.2f}")
    print(f"{IMC:.2f}")
    if IMC<=18.5:
        print("Voce esta abaixo do peso normal")
    elif IMC>18.5 and IMC<24.9:
        print("Peso normal")
    else:
        print("Acima do peso")
    repetir = input("Voce quer cadastrar?\n(s/n)")
print(pessoas)