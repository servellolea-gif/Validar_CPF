def validar_cpf(cpf):
    # Removendo caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf)) 

    # Verificando se o CPF possuí 11 dígitos
    if len(cpf) != 11:
        return False
    
    # Verificando se todos os digitos são iguais (caso raro, mas inválido)
    if cpf == cpf[0] * 11:
        return False
    
    # Calculando o primeiro dígito verificador
    soma = sum (int(cpf[i]) * (10 - i) for i in range(9)) # Multiplicando os primeiros 9 dígitos pelos seus pesos inversos, ou seja, o 1º dígito por 10 - 1, o 2º por 10 - 2, e assim por diante.
    resto = soma % 11 
    if resto < 2:
        digito_verificador_1 = 0
    else:
        digito_verificador_1 = 11 - resto # Exemplo: se o resto for 4, digito_verificador_1 será 11 - 4 = 7

    # Verificando o primeiro dígito verificador
    if int(cpf[9]) != digito_verificador_1:
        return False
    
    # Calculando o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 -i) for i in range(10)) # Multiplicando os primeiros 10 dígitos pelos seus pesos inversos, ou seja, o 1º dígito por 11 - 1, o 2º por 11 - 2, e assim por diante.
    resto = soma % 11
    if resto < 2:
        digito_verificador_2 = 0
    else:
        digito_verificador_2 = 11 - resto

    # Verificando o segundo dígito verificador
    if int(cpf[10]) != digito_verificador_2:
        return False
    
    # Se todas as verificações passaram, o CPF é válido
    return True

# Teste da função
cpf = input("Digite o CPF para validação (formato: xxx.xxx.xxx-xx ou xxxxxxxxxxx): ")
if validar_cpf(cpf):
    print(f'O CPF {cpf} é válido.')
else:
    print(f'O CPF {cpf} é inválido.')