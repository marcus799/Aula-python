'''
def mostrar_nome():
    nome = input("Digite seu nome: ")
    print("Seu nome é:", nome)

mostrar_nome()

def somar():
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))        
    resultado = a + b
    print("O resultado da soma é:", resultado)

somar()
'''
numeros = [2, 4, 6, 8]

def contar_numeros(lista):
    contador = 0 
    for numero in lista:
       print("Número:", numero)
       contador = contador + 1
    return contador

print("Quantidade:", contar_numeros(numeros))