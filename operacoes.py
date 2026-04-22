import validacao
import database
import mysql.connector
import random
import string

def gerar_chave():
    caracteres = string.ascii_uppercase + string.digits
    return ''.join(random.choices(caracteres, k=7))


def cadastrar_eleitor():
    nome = input("Digite o nome completo do eleitor: ").strip()
    cpf = input("Digite o CPF do eleitor: ").strip()
    mesario = input("Você é mesário? (1 - Sim, 0 - Não): ").strip()
    titulo_de_eleitor = input("Digite o número do título de eleitor: ").strip()

    if not validacao.validacao(cpf):
        print("CPF inválido!")
        return
    if not validacao.validacao_titulo(titulo_de_eleitor):
        print("Título de eleitor inválido!")
        return

    chave_acesso = gerar_chave()

    try:
        conn = database.conectar()
        cursor = conn.cursor()

        sql = """INSERT INTO ELEITORES (nome_completo, titulo_eleitor, cpf, mesário, chave_acesso)
                 VALUES (%s, %s, %s, %s, %s)"""
        valores = (nome, titulo_de_eleitor, cpf, int(mesario), chave_acesso)

        cursor.execute(sql, valores)
        conn.commit()
        print("\n  Eleitor cadastrado com sucesso!")
        print(f"  Chave de acesso: {chave_acesso}")

    except mysql.connector.IntegrityError:
        print("\n  Erro: CPF ou título de eleitor já cadastrado.")
    except Exception as e:
        print(f"\n  Erro ao cadastrar: {e}")
    finally:
        cursor.close()
        conn.close()


def buscar_eleitor():
    cpf = input("Digite o CPF do eleitor a buscar: ").strip()

    try:
        conn = database.conectar()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM ELEITORES WHERE cpf = %s", (cpf,))
        eleitor = cursor.fetchone()

        if eleitor:
            print("\n  --- Eleitor encontrado ---")
            print(f"  Nome:    {eleitor['nome_completo']}")
            print(f"  CPF:     {eleitor['cpf']}")
            print(f"  Título:  {eleitor['titulo_eleitor']}")
            print(f"  Mesário: {'Sim' if eleitor['mesário'] else 'Não'}")
            print(f"  Votou:   {'Sim' if eleitor['votou'] else 'Não'}")
        else:
            print("\n  Eleitor não encontrado.")

    except Exception as e:
        print(f"\n  Erro ao buscar: {e}")
    finally:
        cursor.close()
        conn.close()


def editar_eleitor():
    print("\n  Em desenvolvimento.")

def remover_eleitor():
    print("\n  Em desenvolvimento.")

def listar_eleitores():
    conn = database.conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM eleitores")
    resultados = cursor.fetchall()

    for resultado in resultados:
        print(f"\nID: {resultado[0]}")
        print(f"Nome: {resultado[1]}")
        print(f"Título: {resultado[2]}")
        print(f"CPF: {resultado[3]}")
        print(f"Mesário: {'Sim' if resultado[4] else 'Não'}")
        print(f"Votou: {'Sim' if resultado[6] else 'Não'}")
        print("--------------------------------------------------")

    cursor.close()
    conn.close()

def cadastrar_candidato():
    print("\n  Em desenvolvimento.")

def editar_candidato():
    print("\n  Em desenvolvimento.")

def remover_candidato():
    print("\n  Em desenvolvimento.")

def buscar_candidato():
    print("\n  Em desenvolvimento.")

def listar_candidatos():
    print("\n  Em desenvolvimento.")

def autenticar_mesario():
    print("\n  Em desenvolvimento.")

def registrar_voto():
    print("\n  Em desenvolvimento.")

def encerrar_votacao():
    print("\n  Em desenvolvimento.")

def exibir_logs():
    print("\n  Em desenvolvimento.")

def exibir_protocolos():
    print("\n  Em desenvolvimento.")

def boletim_urna():
    print("\n  Em desenvolvimento.")

def estatistica_comparecimento():
    print("\n  Em desenvolvimento.")

def votos_por_partido():
    print("\n  Em desenvolvimento.")

def validacao_integridade():
    print("\n  Em desenvolvimento.")