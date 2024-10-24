import random
import os

def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def carregar_palavras():
    with open("C:\\Users\\PDBD091\\Curso de Python\\Módulo 7\\7.4 - Arquivos de Texto\\gabarito_forca.txt", "r") as file:  
        palavras = file.read().splitlines()  
    return palavras

def carregar_enforcado():
    with open("C:\\Users\\PDBD091\\Curso de Python\\Módulo 7\\7.4 - Arquivos de Texto\\gabarito_enforcado.txt", "r") as file:  
        enforcado_raw = file.read()
        enforcado = enforcado_raw.split("\n\n")  
    return enforcado

def imprime_enforcado(erros, enforcado):
    if erros < len(enforcado):  
        print(enforcado[erros])
    else:
        print(enforcado[-1])  

def jogar():
    palavras = carregar_palavras()
    enforcado = carregar_enforcado()
    palavra = random.choice(palavras).strip()  
    letras_adivinhadas = []
    erros = 0

    print("_ " * len(palavra))

    while erros < 6:
        letra = input("Adivinhe uma letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, insira apenas uma letra.")
            continue

        if letra in letras_adivinhadas:
            print("Você já tentou essa letra.")
            continue

        letras_adivinhadas.append(letra)

        if letra in palavra:
            print("Você acertou!")
        else:
            erros += 1
            print(f"Errado! Restam {6 - erros} tentativas.")
            imprime_enforcado(erros, enforcado)

        progresso = "".join([letra if letra in letras_adivinhadas else "_" for letra in palavra])
        print("Progresso:", progresso)

        if "_" not in progresso:
            print(f"Parabéns! Você acertou a palavra: {palavra}")
            break

    if erros == 6:
        imprime_enforcado(erros, enforcado) 
        print(f"Você perdeu! A palavra era: {palavra}")

jogar()
