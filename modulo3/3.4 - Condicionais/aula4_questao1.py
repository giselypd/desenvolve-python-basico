#Escreva um programa que lê dois números e informa se a sua soma é par ou ímpar.
n1, n2 = int(input("numero1: ")), int(input("numero2: "))
print("É par" if (n1+n2) % 2 == 0 else ("É ímpar"))