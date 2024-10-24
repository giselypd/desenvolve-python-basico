with open('C:\\Users\\PDBD091\\Curso de Python\\Módulo 7\\7.4 - Arquivos de Texto\\estomago.txt', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()

print("As primeiras 25 linhas do arquivo são: ")
for linha in linhas[:25]:
    print(linha.strip())

num_linhas = len(linhas)
print(f"\nO número total de linhas no arquivo é: {num_linhas}")

linha_mais_longa = max(linhas, key=len)
print(f"\nA linha com o maior número de caracteres é:\n{linha_mais_longa.strip()}")
print(f"\nNúmero de caracteres nessa linha: {len(linha_mais_longa)}")

contador_nonato = sum(linha.lower().count('nonato') for linha in linhas)
contador_iria = sum(linha.lower().count(' íria ') for linha in linhas) 
print(f"\nO nome 'Nonato' aparece {contador_nonato} vezes no texto.")
print(f"O nome 'Íria' aparece {contador_iria} vezes no texto.")