def validacao(cpf):
    cpf_str = str(cpf).strip()
    if len(cpf_str) != 11 or not cpf_str.isdigit():
        print("CPF invalido.")
        return False

    if cpf_str == cpf_str[0] * 11:
        return False

    soma = 0
    for i in range(9):
        soma += int(cpf_str[i]) * (10 - i)
    dig1 = (soma * 10 % 11) % 10

    soma = 0
    for i in range(10):
        soma += int(cpf_str[i]) * (11 - i)
    dig2 = (soma * 10 % 11) % 10

    return dig1 == int(cpf_str[9]) and dig2 == int(cpf_str[10])
    
    
def validacao_titulo(titulo_de_eleitor):
    t_str = str(titulo_de_eleitor).strip()

    if not t_str.isdigit() or len(t_str) != 12:
        print("Erro.")
        return False

    soma1 = 0
    for i in range(8):
        soma1 += int(t_str[i]) * (i + 2)
    digito1 = soma1 % 11
    if digito1 == 0 or digito1 == 1:
        digito1 = 0

    soma2 = int(t_str[8]) * 7 + int(t_str[9]) * 8 + digito1 * 9
    digito2 = soma2 % 11
    if digito2 == 0 or digito2 == 1:
        digito2 = 0

    return int(t_str[10]) == digito1 and int(t_str[11]) == digito2