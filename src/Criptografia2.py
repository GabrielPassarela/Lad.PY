import random
import string


CHAVE = [[3, 3],
         [2, 5]]

MOD = 26


def texto_para_numeros(texto):
    """Converte cada letra do texto em seu índice (A=0 … Z=25)."""
    texto = texto.upper().replace(" ", "")
    return [ord(c) - ord('A') for c in texto if c.isalpha()]


def numeros_para_texto(numeros):
    """Converte uma lista de índices de volta em texto."""
    return ''.join([chr(int(n) + ord('A')) for n in numeros])


def ajustar_texto(texto):
    """Garante que o texto tenha comprimento par (padding com 'X')."""
    texto = texto.upper().replace(" ", "")
    texto = ''.join(c for c in texto if c.isalpha())
    if len(texto) % 2 != 0:
        texto += 'X'
    return texto


def numero_para_letra(texto):
    """
    Converte cada dígito em uma letra: '0'→'A', '1'→'B' … '9'→'J'.
    Letras já presentes são mantidas em maiúsculas.
    """
    resultado = ""
    for c in str(texto):
        if c.isdigit():
            resultado += chr(int(c) + 65)
        elif c.isalpha():
            resultado += c.upper()
    return resultado


def letra_para_numero(texto):
    """
    Reverso de numero_para_letra:
    'A'→'0', 'B'→'1' … 'J'→'9'.
    Letras fora desse intervalo são mantidas.
    """
    resultado = ""
    for c in texto.upper():
        valor = ord(c) - 65          # A=0, B=1, …
        if 0 <= valor <= 9:          # só converte A-J (dígitos 0-9)
            resultado += str(valor)
        else:
            resultado += c
    return resultado



def multiplicar_matriz(matriz, bloco):
    """Multiplica uma matriz 2×2 por um vetor coluna [a, b] mod MOD."""
    resultado = []
    for i in range(2):
        valor = (matriz[i][0] * bloco[0] + matriz[i][1] * bloco[1]) % MOD
        resultado.append(valor)
    return resultado


def inversa_modular(numero):
    """Retorna o inverso modular de 'numero' em Z_26."""
    numero = numero % MOD
    for i in range(1, MOD):
        if (numero * i) % MOD == 1:
            return i
    return None


def inversa_modular_matriz(matriz):
    """Calcula a inversa modular de uma matriz 2×2 em Z_26."""
    a, b = matriz[0][0], matriz[0][1]
    c, d = matriz[1][0], matriz[1][1]

    det = (a * d - b * c) % MOD
    det_inv = inversa_modular(det)

    if det_inv is None:
        raise ValueError("A chave não é invertível em Z_26.")

    adjunta = [[d, -b],
               [-c,  a]]

    inversa = []
    for linha in adjunta:
        nova_linha = [(det_inv * v) % MOD for v in linha]
        inversa.append(nova_linha)
    return inversa


def criptografar_hill(texto):
    """
    Recebe uma string já composta apenas por letras (A-Z) e
    retorna o texto cifrado pela Cifra de Hill.
    A conversão de dígitos para letras deve ser feita ANTES de chamar esta função.
    """
    texto = ajustar_texto(texto)
    numeros = texto_para_numeros(texto)
    resultado = []

    for i in range(0, len(numeros), 2):
        bloco = [numeros[i], numeros[i + 1]]
        criptografado = multiplicar_matriz(CHAVE, bloco)
        resultado.extend(criptografado)

    return numeros_para_texto(resultado)


def descriptografar_hill(texto):
    """
    Recebe texto cifrado (letras A-Z) e retorna o texto descriptografado.
    A conversão de letras de volta para dígitos deve ser feita DEPOIS, se necessário.
    """
    numeros = texto_para_numeros(texto)
    chave_inv = inversa_modular_matriz(CHAVE)
    resultado = []

    for i in range(0, len(numeros), 2):
        bloco = [numeros[i], numeros[i + 1]]
        descriptografado = multiplicar_matriz(chave_inv, bloco)
        resultado.extend(descriptografado)

    return numeros_para_texto(resultado)



def criptografar_cpf(cpf):
    cpf_letras = numero_para_letra(cpf)
    return criptografar_hill(cpf_letras)


def descriptografar_cpf(cpf_criptografado):
    cpf_letras = descriptografar_hill(cpf_criptografado)
    return letra_para_numero(cpf_letras)



def gerar_chave_acesso(nome_completo):
    partes = nome_completo.strip().upper().split()
    letra1 = partes[0][0]
    letra2 = partes[0][1]
    letra3 = partes[1][0] if len(partes) > 1 else 'X'
    digitos = ''.join(random.choices(string.digits, k=4))
    return letra1 + letra2 + letra3 + digitos


def criptografar_chave_acesso(chave):
    parte_letras  = ''.join(c for c in chave if c.isalpha())
    parte_digitos = ''.join(c for c in chave if c.isdigit())
    texto = parte_letras + numero_para_letra(parte_digitos)
    return criptografar_hill(texto)


def descriptografar_chave_acesso(chave_criptografada):
    return descriptografar_hill(chave_criptografada)



def gerar_protocolo(numero_candidato):
    letras = ''.join(random.choices(string.ascii_uppercase, k=2))
    digitos = ''.join(random.choices(string.digits, k=5))
    return f"V{letras}26{numero_candidato:02d}{digitos}"


def criptografar_protocolo(protocolo):
    parte_letras  = ''.join(c for c in protocolo if c.isalpha())
    parte_digitos = ''.join(c for c in protocolo if c.isdigit())
    texto = parte_letras + numero_para_letra(parte_digitos)
    return criptografar_hill(texto)


def descriptografar_protocolo(protocolo_criptografado):
    return descriptografar_hill(protocolo_criptografado)



if __name__ == "__main__":
    print("\n==================================================")
    print("       LAD.Py - Sistema de Votacao Digital")
    print("       Demonstracao de Criptografia - Cifra de Hill")
    print("==================================================")

    # CPF
    cpf = "12345678901"
    cpf_cripto     = criptografar_cpf(cpf)
    cpf_recuperado = descriptografar_cpf(cpf_cripto)
    print(f"\n  CPF original     : {cpf}")
    print(f"  CPF criptografado: {cpf_cripto}")
    print(f"  CPF recuperado   : {cpf_recuperado[:11]}")

    # Chave de Acesso
    nome        = "Andre Silva"
    chave       = gerar_chave_acesso(nome)
    chave_cripto = criptografar_chave_acesso(chave)
    print(f"\n  Eleitor          : {nome}")
    print(f"  Chave original   : {chave}")
    print(f"  Chave criptograf.: {chave_cripto}")

    # Protocolo
    protocolo       = gerar_protocolo(99)
    protocolo_cripto = criptografar_protocolo(protocolo)
    print(f"\n  Protocolo original   : {protocolo}")
    print(f"  Protocolo criptograf.: {protocolo_cripto}")

    print("\n==================================================\n")