frase = input("Digite uma frase: ")

vogais = []
consoantes = []

for letra in frase:
    if letra.lower() in 'aeiou':
        vogais.append(letra.lower())
    elif letra.isalpha():
        consoantes.append(letra)

vogais.sort()

print("Vogais:", vogais)
print("Consoantes:", consoantes)
