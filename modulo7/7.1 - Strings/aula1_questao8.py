def calcula_digito(cpf, peso):
    soma = 0
    for i in range(len(cpf)):
        soma += int(cpf[i]) * peso
        peso -= 1
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto

def valida_cpf(cpf):
    cpf = cpf.replace('.', '').replace('-', '')
    if len(cpf) != 11 or not cpf.isdigit():
        return "Inválido"
    primeiro_digito = calcula_digito(cpf[:9], 10)
    segundo_digito = calcula_digito(cpf[:9] + str(primeiro_digito), 11)
    if cpf[9] == str(primeiro_digito) and cpf[10] == str(segundo_digito):
        return "Válido"
    else:
        return "Inválido"

cpf_input = input("Digite o CPF (formato XXX.XXX.XXX-XX): ")
resultado = valida_cpf(cpf_input)
print(resultado)
