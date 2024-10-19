numero = input("Digite o número: ")
if len(numero) == 8:
    numero_completo = '9' + numero
elif len(numero) == 9:
    if numero[0] != '9':
        print("O número não começa com 9.")
        exit()
    numero_completo = numero
else:
    print("Número inválido. Deve ter 8 ou 9 dígitos.")
    exit()
numero_formatado = numero_completo[:5] + '-' + numero_completo[5:]
print("Número completo:", numero_formatado)
