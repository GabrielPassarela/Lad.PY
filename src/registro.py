import mysql.connector
import random

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="projeto_integrador"
)

cursor = conexao.cursor()

candidato_id = int(input("Digite o ID do candidato: "))

protocolo = f"PROT-{random.randint(100000,999999)}"

cursor.execute(
    "INSERT INTO VOTOS (candidato_id, data_hora, protocolo) VALUES (%s, NOW(), %s)",
    (candidato_id, protocolo)
)

conexao.commit()

print("Voto registrado com sucesso!")
print("Protocolo:", protocolo)

cursor.close()
conexao.close()