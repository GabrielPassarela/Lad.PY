import hashlib

def gerar_hash(dado):
    dadosbyts = str(dado).encode('utf-8')
    hash_objeto = hashlib.sha256(dadosbyts)
    return hash_objeto.hexdigest()

if __name__ == "__main__":
    ex_cand = "Candidato_A"
    ex_cpf = "44303821829"
    
    print(f"Candidato Criptografado: {gerar_hash(ex_cand)}")
    print(f"CPF Criptografado:  {gerar_hash(ex_cpf)}")