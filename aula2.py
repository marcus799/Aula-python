nota1 = float(input("Digite a primeira nota"))
nota2 = float(input("Digite a segunda nota"))
media = (nota1+nota2)/2
print(media)
if(media>=7.0):
    print("Aprovado")
elif(media>=4.1 and media<=6.9):
    print("recuperaçao")
else:
    print("Reprovado")

peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))
IMC = peso/(altura*altura)
if(IMC<=18.5):
    print("baixo peso")
elif (IMC>18.5 and IMC<=24.99):
    print("normal")
elif (IMC>25.0 and IMC<29.99):
    print("sobrepeso")
else:
    print("obesidade")
    
idade = int(input("Digite a idade: "))
if(idade<=12):
    print("criança")
elif (idade<18):
    print("adolescente")
    
elif (idade<59):
    print("adulto")
else:
    print("idoso")

salario = int(input("Digite a quantidade de salarios minimos que voce ganha: "))
if(salario>15):
    print("classe A")
elif (salario>=5 and salario<=15):
    print("classe B")
elif (salario>=3 and salario<=5):
    print("classe C")
elif (salario>1 and salario<3):
    print("classe D")
else:
    print("classe E")