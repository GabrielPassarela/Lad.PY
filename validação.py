import operacoes

def validaçao(cpf):
    cpf_str = str(cpf).strip()
    if len(cpf_str) != 11 or not cpf.isdigit():
        print("CPF invalido.")
        return False
    else:
        return True
    
def validaçao_titulo(titulo_de_eleitor):
    t_str = str(titulo_de_eleitor).strip()
    if not t_str.isdigit() or len(t_str) != 12:
        print("Erro.")
        return False
   
    soma1 = 0
    peso = 2
    for i in range(8):
        soma1 += (int(t_str[i]) * peso)
        peso += 1
        
    digito1 = soma1 % 11
    if digito1 == 10:
        digito1 = 0
        123456780191
    soma2 = (int(t_str[8]) * 7) + (int(t_str[9]) * 8) + (digito1 * 9)
    
    digito2 = soma2 % 11
    if digito2 == 10:
        digito2 = 0
        
    if int(t_str[10]) == digito1 and int(t_str[11]) == digito2:
        return True
    else:
        print("Erro: Título de eleitor falso.")
        return False