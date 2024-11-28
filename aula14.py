import mysql.connector # type: ignore

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "escola"
)
cursor = conn.cursor()



def cadastrar_aluno():
    nome = input("Digite o seu nome: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    insert_query = '''insert into aluno(nome,nota1,nota2,nota3)values(%s,%s,%s,%s)'''
    insert_values = (nome,nota1,nota2,nota3)
    cursor.execute(insert_query,insert_values)
    conn.commit()


def listar_alunos():

    select_query = "select*from aluno"
    cursor.execute(select_query)
    alunos = cursor.fetchall()
    for (nome,nota1,nota2,nota3) in alunos:
        #print(f"nome:{aluno['aluno']},nota1:{aluno['nota1']},nota2:{aluno['nota2']},nota3:{aluno['nota3']}")
        print(f"nome:{nome}, nota1 {nota1}, nota2 {nota2}, nota3 {nota3}")

def deletar_aluno():
    delete_query = "delete from aluno"
    cursor.execute(delete_query)
    conn.commit()
    print("Deletado com sucesso")

def atualizar_nome():
    nome = input("Digite o nome que voce quer atualizar: ")
    check_query = "select * from aluno where nome = %s"
    cursor.execute(check_query,(nome,))
    alunos = cursor.fetchone()
    if alunos:
        nome_atualizado = input("Digite o novo nome: ")
        update_query = "update aluno set nome = %s where aluno = %s "
        update_values = (nome_atualizado, nome)
        cursor.execute(update_query, update_values)
        conn.commit()
        print("Nome atualizado com sucesso!")

    else:
        print("Aluno nao encontrado")


cadastrar_aluno()
listar_alunos()
#deletar_aluno()
atualizar_nome()

conn.close()