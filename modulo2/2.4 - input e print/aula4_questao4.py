#Escreva um programa que leia um valor inteiro referente a uma quantia em reais e calcule a menor quantidade possível de notas necessárias para pagar aquele valor
valor = int(input("Valor: "))

valor100 = valor // 100
valor = valor % 100
valor50 = valor // 50
valor = valor % 50
valor20 = valor // 20
valor = valor % 20
valor10 = valor // 10
valor = valor % 10
valor5 = valor // 5
valor = valor % 5
valor2 = valor // 2
valor = valor % 2
valor1 = valor // 1

print(f"{valor100} nota(s) de R$100,00")
print(f"{valor50} nota(s) de R$50,00")
print(f"{valor20} nota(s) de R$20,00")
print(f"{valor10} nota(s) de R$10,00")
print(f"{valor5} nota(s) de R$5,00")
print(f"{valor2} nota(s) de R$2,00")
print(f"{valor1} nota(s) de R$1,00")
