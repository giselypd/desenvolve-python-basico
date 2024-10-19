import random

def encrypt(nomes):
    chave_aleatoria = random.randint(1, 10)
    nomes_cript = []
    for nome in nomes:
        nome_cript = ""
        for char in nome:
            novo_char = ord(char) + chave_aleatoria          
            if novo_char > 126:
                novo_char = 33 + (novo_char - 127)
            nome_cript += chr(novo_char)
        nomes_cript.append(nome_cript)
    return nomes_cript, chave_aleatoria

nomes = input("Digite os nomes separados por vírgula: ").split(",")
nomes = [nome.strip() for nome in nomes]
nomes_cript, chave = encrypt(nomes)
print("Nomes criptografados:", nomes_cript)
print("Chave de criptografia:", chave)
