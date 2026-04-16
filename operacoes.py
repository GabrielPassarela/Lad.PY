import validação

def cadastrar_eleitor():
    nome = input("Digite o nome completo do eleitor: ").strip()
    cpf = input("Digite o CPF do eleitor: ").strip()
    mesario = input("Você é mesário? (1 - Sim, 0 - Não): ").strip()
    titulo_de_eleitor = input("Digite o número do título de eleitor: ").strip()
        
    if not (validação.validaçao(cpf) and validação.validaçao_titulo(titulo_de_eleitor)):
        print("Documentos inválidos!")
        return

    print("\n  Eleitor cadastrado com sucesso!")
    return


def editar_eleitor():
    
    print("\n  Em desenvolvimento.")


def remover_eleitor():
    
    print("\n  Em desenvolvimento.")


def buscar_eleitor():
   
    print("\n  Em desenvolvimento.")


def listar_eleitores():
   
    print("\n  Em desenvolvimento.")


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