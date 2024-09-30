#Escreva um programa que leia um inteiro N com a quantidade de respondentes e em seguida leia as N idades de cada respondente. Ao final, imprima a média das idades.
n = int(input("Digite a quantidade de respondentes: "))

soma = 0
cont = 0

while cont < n:
    idade = int(input(f"Digite a idade do respondente {cont + 1}: "))
    soma += idade
    cont += 1
print("Soma:", soma)
media = soma / n
print(f"A média das idades é {media:.0f} anos")