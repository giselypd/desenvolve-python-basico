import re

with open(r"C:\Users\PDBD091\Curso de Python\frase.txt", "r") as arquivo:
    conteudo = arquivo.read()

palavras = re.sub(r'[^a-zA-Zá-úÁ-Ú]', ' ', conteudo).lower()  
lista_palavras = palavras.split()  

with open("palavras.txt", "w") as novo_arquivo:
    for palavra in lista_palavras:
        novo_arquivo.write(palavra + "\n")  

with open("palavras.txt", "r") as novo_arquivo:  
    print(novo_arquivo.read())
