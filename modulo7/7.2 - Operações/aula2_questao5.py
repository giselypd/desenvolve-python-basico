import random

def embaralhar_palavras(frase):
    palavras = frase.split()
    palavras_embaralhadas = []

    for palavra in palavras:
        if len(palavra) > 3:
            primeira_letra = palavra[0]
            ultima_letra = palavra[-1]
            letras_internas = list(palavra[1:-1])  
            random.shuffle(letras_internas)  
            nova_palavra = primeira_letra + ''.join(letras_internas) + ultima_letra
            palavras_embaralhadas.append(nova_palavra)
        else:
            palavras_embaralhadas.append(palavra)

    frase_embaralhada = ' '.join(palavras_embaralhadas)
    return frase_embaralhada

frase_original = input("Digite uma frase: ")
frase_modificada = embaralhar_palavras(frase_original)
print(frase_modificada)
