i = 0
vezes = int(input("Quantas vezes vai digitar o nome? "))
while i<vezes:
    nome = input("Digite o seu nome: ")
    print(nome)
    i = i+1

for i in range(5):
    nome = input("Digite o seu nome: ")
    print(nome)
    
vezes = int(input("Quantas vezes voce quer digitar o nome? "))
for i in range(vezes):
    nome = input("Digite o seu nome: ")
    print(nome)

resultado = ""
vezes = int(input("quantas vezes quer digitar o nome? "))
for i in range(vezes):
    nome = input("informe o seu nome: ")
    resultado = resultado+nome+"\n"
print(resultado)

vezes = int(input("Quantas vezes quer digitar o login? "))
for i in range(vezes):
    login = input("Digite o login: ")
    if login == "marcus@gmail.com":
        senha = int(input("Digite a senha: "))
        if senha == 123:
            print("Cadastro concluido")
        else:
            print("Senha invalida")
    else:
        print("Cadastro invalido")

produtos = int(input("Quantos produtos quer cadastrar? "))
for i in range(produtos):
    nome = input("Digite o nome do produto: ")
    preço = float(input("Digite o preço do produto: "))
    estoque = int(input("Digite a quantidade de produtos no estoque: "))
    quantidade = int(input("Quantos voce quer comprar? "))
    if estoque > quantidade:
        estoque = estoque-quantidade
        total_pagar = preço*quantidade
        print("Vendas realizadas com sucesso seu estoque agora e: ",estoque)
        print("o total a pagar e: ",total_pagar)
        pagamento = float(input("Quanto voce vai pagar? "))
        
    else:
        print("estoque insuficiente")