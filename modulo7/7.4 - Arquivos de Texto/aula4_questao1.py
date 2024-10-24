import os

frase = input("Digite uma frase: ")
n_arquivo = "frase.txt"
with open(n_arquivo, "w") as arquivo:
    arquivo.write(frase)
caminho_completo = os.path.abspath(n_arquivo)
print(f"Frase salva em {caminho_completo}")