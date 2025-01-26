import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "game"
)
cursor = conn.cursor()

def cadastrar_jogador():
    nome = input("Digite o nome do jogador: ")
    pontuaçao = int(input("Digite a sua pontuaçao: "))
    vida = int(input("Digite o valor 3 para vida: "))

    insert_query = ''' insert into jogador(nome,pontuaçao,vida)values(%s,%s,%s)'''
    cursor.execute(insert_query,(nome,pontuaçao,vida))

    conn.commit()
    print("O jogador foi cadastrado com sucesso!")


def listar_jogador():
    select_query = "select * from jogador"
    cursor.execute(select_query)
    #print(f"id:{[0]}, nome:{[1]}, pontuaçao:{[2]}, vida:{[3]}")

    resultados = cursor.fetchall()

    for linha in resultados:
            id, nome, pontuacao, vida = linha
            print(f"ID: {id}, Nome: {nome}, Pontuação: {pontuacao}, Vida: {vida}")


def deletar_jogador():
    id_deletado = int(input("Digite o id que voce quer deletar: "))
    delete_query = "delete from jogador where id = %s"
    cursor.execute(delete_query,(id_deletado,))
    conn.commit()
    print("Jogador deletado com sucesso!")


def atualizar_jogador():
    id_jogador = int(input("Digite o id que voce quer atualizar: "))
    campo = int(input("Digite 1 se quer atualizar o nome e 2 para atualizar a pontuaçao: "))
    if campo == 1:
        novo_nome = input("Digite o novo nome: ")
        update_query = "update jogador set nome = %s where id = %s"
        cursor.execute(update_query,(novo_nome,id_jogador))
        conn.commit()
        print("nome atualizado com sucesso!")

    elif campo == 2:
        nova_pontuaçao = int(input("Digite a nova pontuaçao: "))
        update_query = "update jogador set pontuaçao = %s where id = %s"
        cursor.execute(update_query,(nova_pontuaçao,id_jogador))
        conn.commit()
        print("pontuaçao atualizada com sucesso!")
        
    else:
        print("Digite um numero valido")
        atualizar_jogador()

while True:
    print("Digite 1 para cadastrar 2 para listar 3 para deletar 4 para atualizar e 5 para encerrar o programa")
    opçao = int(input("Digite a opçao: "))

    if opçao == 1:
        cadastrar_jogador()
        print("Jogador cadastrado com sucesso!")

    elif opçao == 2:
        listar_jogador()
        
    elif opçao == 3:
        deletar_jogador()

    elif opçao == 4:    
        atualizar_jogador()

    elif opçao == 5:
        print("Programa encerrado!")
        break

    else:
        print("Digite uma opçao valida")
