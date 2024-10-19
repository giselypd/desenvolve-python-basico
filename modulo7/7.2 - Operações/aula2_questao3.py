import string

def eh_palindromo(frase):
    frase_inversa = ""
    for char in frase:
        if char not in string.punctuation and not char.isspace():
            frase_inversa += char.lower()
    return frase_inversa == frase_inversa[::-1]

while True:
    frase = input('Digite uma frase (digite "Fim" para encerrar): ')
    if frase.lower() == "fim":
        break
    if eh_palindromo(frase):
        print(f'"{frase}" é palíndromo')
    else:
        print(f'"{frase}" não é palíndromo')
