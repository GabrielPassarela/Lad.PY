def validacao(cpf):
    cpf_str = str(cpf).strip()
    cpf_str = cpf_str.replace(".", "").replace("-", "")
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
    t_str = t_str.replace(".", "").replace("-", "")

    if not t_str.isdigit() or len(t_str) != 12:
        print("Erro.")
        return False
    

    calculo1 = sum(int(t_str[i]) * (2 + i) for i in range(8))
    primeirodigito = calculo1 % 11
    if primeirodigito == 10:
        primeirodigito = 0
    
    if primeirodigito == 0 and int(t_str[8]) == 0 and int(t_str[9]) == 1 or int(t_str[8]) == 0 and int(t_str[9]) == 2:
        primeirodigito = 1

    calculo2 = (int(t_str[8]) * 7 ) + (int(t_str[9]) * 8) + (int(t_str[10]) * 9)
    segundodigito = calculo2 % 11
    if segundodigito == 10:
        segundodigito = 0
        
    if segundodigito == 0 and int(t_str[8]) == 0 and int(t_str[9]) == 1 or int(t_str[8]) == 0 and int(t_str[9]) == 2:
        segundodigito = 1

    if primeirodigito == int(t_str[10]) and segundodigito == int(t_str[11]):
        return True
    else:
        return False