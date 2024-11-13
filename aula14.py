import mysql.connector # type: ignore

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "escola"
)
cursor = conn.cursor()



def cadastrar_aluno():
    aluno = input("Digite o seu nome: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    insert_query = '''insert into aluno(aluno,nota1,nota2,nota3)values(%s,%s,%s,%s)'''
    insert_values = (aluno,nota1,nota2,nota3)
    cursor.execute(insert_query,insert_values)
    conn.commit()

cadastrar_aluno()
conn.close()