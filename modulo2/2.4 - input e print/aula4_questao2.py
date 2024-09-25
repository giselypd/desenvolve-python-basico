#Leia um valor inteiro correspondente a uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
F = int(input("Temperatura em graus Fahrenheit: "))

C = (F - 32) * (5/9)

print(f"{F} graus Fahrenheit são {int(C)} graus Celsius")

